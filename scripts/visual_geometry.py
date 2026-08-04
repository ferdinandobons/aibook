"""Geometry contracts shared by the deterministic visual generators.

The raster audit is deliberately independent from the visual renderer.  The
renderer records the intended boxes and text areas, while this module checks
the saved PNG for canvas containment and checks the recorded layout for
intersections, touching siblings, and visible connectors over text.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

from PIL import Image, ImageChops


CANVAS = (1800, 1000)
SAFE_MARGIN = 20
MIN_GAP = 8


def _box(value: Iterable[float]) -> tuple[float, float, float, float]:
    x0, y0, x1, y1 = (float(item) for item in value)
    if x1 < x0 or y1 < y0:
        raise ValueError(f"invalid geometry box: {value}")
    return x0, y0, x1, y1


def _overlap(a: tuple[float, float, float, float], b: tuple[float, float, float, float], gap: float = 0) -> bool:
    return not (
        a[2] + gap <= b[0]
        or b[2] + gap <= a[0]
        or a[3] + gap <= b[1]
        or b[3] + gap <= a[1]
    )


def _contains(parent: tuple[float, float, float, float], child: tuple[float, float, float, float], gap: float = 0) -> bool:
    return (
        parent[0] + gap < child[0]
        and parent[1] + gap < child[1]
        and child[2] < parent[2] - gap
        and child[3] < parent[3] - gap
    )


def _segment_intersects_rect(
    start: tuple[float, float],
    end: tuple[float, float],
    rect: tuple[float, float, float, float],
) -> bool:
    """Return whether the open body of a segment intersects a rectangle."""

    x0, y0, x1, y1 = rect
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, start[0] - x0), (dx, x1 - start[0]), (-dy, start[1] - y0), (dy, y1 - start[1])):
        if p == 0:
            if q < 0:
                return False
            continue
        ratio = q / p
        if p < 0:
            if ratio > t1:
                return False
            t0 = max(t0, ratio)
        else:
            if ratio < t0:
                return False
            t1 = min(t1, ratio)
    return t1 - t0 > 1e-6 and t1 > 1e-5 and t0 < 1 - 1e-5


@dataclass
class GeometryObject:
    id: str
    kind: str
    box: tuple[float, float, float, float]
    label: str = ""
    order: int = 0


@dataclass
class GeometryConnector:
    id: str
    start: tuple[float, float]
    end: tuple[float, float]
    order: int = 0


class GeometryRecorder:
    """Record semantic drawing primitives and validate their relationships."""

    def __init__(self, figure_id: str, canvas: tuple[int, int] = CANVAS) -> None:
        self.figure_id = figure_id
        self.canvas = canvas
        self.objects: list[GeometryObject] = []
        self.connectors: list[GeometryConnector] = []
        self._order = 0

    def _next(self) -> int:
        self._order += 1
        return self._order

    def shape(self, kind: str, box: Iterable[float], label: str = "") -> None:
        self.objects.append(GeometryObject(f"{kind}-{len(self.objects) + 1:03d}", kind, _box(box), label, self._next()))

    def text(self, box: Iterable[float], text: str) -> None:
        self.objects.append(
            GeometryObject(
                f"text-{len(self.objects) + 1:03d}",
                "text",
                _box(box),
                " ".join(str(text).split())[:180],
                self._next(),
            )
        )

    def connector(self, start: Iterable[float], end: Iterable[float]) -> None:
        a = tuple(float(value) for value in start)
        b = tuple(float(value) for value in end)
        if len(a) != 2 or len(b) != 2:
            raise ValueError("connectors need two-dimensional endpoints")
        self.connectors.append(GeometryConnector(f"connector-{len(self.connectors) + 1:03d}", a, b, self._next()))

    def errors(self, minimum_gap: float = MIN_GAP, safe_margin: float = SAFE_MARGIN) -> list[str]:
        width, height = self.canvas
        errors: list[str] = []
        for item in self.objects:
            x0, y0, x1, y1 = item.box
            if x0 < safe_margin or y0 < safe_margin or x1 > width - safe_margin or y1 > height - safe_margin:
                errors.append(f"{item.id} leaves the safe canvas area: {item.box}")
            if x1 <= x0 or y1 <= y0:
                errors.append(f"{item.id} has no positive area: {item.box}")

        for index, left in enumerate(self.objects):
            for right in self.objects[index + 1 :]:
                if left.kind == "text" and right.kind == "text":
                    if _overlap(left.box, right.box):
                        errors.append(f"text areas {left.id} and {right.id} overlap or touch")
                    continue
                if left.kind == "text" or right.kind == "text":
                    text = left if left.kind == "text" else right
                    shape = right if left.kind == "text" else left
                    if _overlap(text.box, shape.box) and not _contains(shape.box, text.box, min(4, minimum_gap)):
                        errors.append(f"{text.id} intersects {shape.id} without safe padding")
                    continue
                if _overlap(left.box, right.box, minimum_gap):
                    nested = _contains(left.box, right.box, minimum_gap) or _contains(right.box, left.box, minimum_gap)
                    if not nested:
                        errors.append(f"shapes {left.id} and {right.id} overlap or touch")

        for connector in self.connectors:
            for item in self.objects:
                # A connector drawn before a node is intentionally hidden by
                # that node.  A connector drawn afterwards must never cross
                # the visible text area.
                if connector.order <= item.order or item.kind != "text":
                    continue
                if _segment_intersects_rect(connector.start, connector.end, item.box):
                    errors.append(f"{connector.id} is drawn over {item.id}")
        return errors

    def manifest(self, errors: list[str] | None = None) -> dict[str, Any]:
        return {
            "schema": 1,
            "figure": self.figure_id,
            "canvas": list(self.canvas),
            "safe_margin": SAFE_MARGIN,
            "minimum_gap": MIN_GAP,
            "objects": [asdict(item) | {"box": list(item.box)} for item in self.objects],
            "connectors": [asdict(item) | {"start": list(item.start), "end": list(item.end)} for item in self.connectors],
            "errors": errors or [],
        }

    def validate(self) -> None:
        errors = self.errors()
        if errors:
            raise ValueError(f"{self.figure_id}: visual geometry contract failed: " + "; ".join(errors[:8]))


class TrackingDraw:
    """Proxy around ImageDraw that records boxes without changing rendering."""

    def __init__(self, image: Image.Image, recorder: GeometryRecorder) -> None:
        from PIL import ImageDraw

        self._draw = ImageDraw.Draw(image)
        self.geometry = recorder

    def rounded_rectangle(self, xy, *args, **kwargs):
        self.geometry.shape("rounded_rectangle", xy)
        return self._draw.rounded_rectangle(xy, *args, **kwargs)

    def rectangle(self, xy, *args, **kwargs):
        self.geometry.shape("rectangle", xy)
        return self._draw.rectangle(xy, *args, **kwargs)

    def ellipse(self, xy, *args, **kwargs):
        self.geometry.shape("ellipse", xy)
        return self._draw.ellipse(xy, *args, **kwargs)

    def __getattr__(self, name: str):
        return getattr(self._draw, name)


def raster_metrics(path: Path, safe_margin: int = SAFE_MARGIN) -> dict[str, Any]:
    with Image.open(path) as image:
        image.load()
        rgb = image.convert("RGB")
        width, height = rgb.size
        background = Image.new("RGB", rgb.size, (255, 255, 255))
        difference = ImageChops.difference(rgb, background).convert("L")
        content = difference.point(lambda value: 255 if value > 7 else 0)
        bbox = content.getbbox()
        border_pixels = []
        for crop in ((0, 0, width, safe_margin), (0, height - safe_margin, width, height), (0, 0, safe_margin, height), (width - safe_margin, 0, width, height)):
            border_pixels.append(content.crop(crop).getbbox() is not None)
        margins = None
        if bbox:
            margins = [bbox[0], bbox[1], width - bbox[2], height - bbox[3]]
        return {
            "mode": image.mode,
            "size": [width, height],
            "content_bbox": list(bbox) if bbox else None,
            "content_margins": margins,
            "border_has_content": any(border_pixels),
            "problems": [
                *(["dimension"] if (width, height) != CANVAS else []),
                *(["content reaches the safe canvas margin"] if margins and min(margins) < safe_margin else []),
                *(["non-white pixels in the safe border"] if any(border_pixels) else []),
            ],
        }


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    recorder = GeometryRecorder(str(manifest.get("figure", "unknown")), tuple(manifest.get("canvas", CANVAS)))
    for item in manifest.get("objects", []):
        recorder.objects.append(
            GeometryObject(
                str(item["id"]), str(item["kind"]), _box(item["box"]), str(item.get("label", "")), int(item.get("order", 0))
            )
        )
    for item in manifest.get("connectors", []):
        recorder.connectors.append(
            GeometryConnector(
                str(item["id"]), tuple(float(value) for value in item["start"]), tuple(float(value) for value in item["end"]), int(item.get("order", 0))
            )
        )
    return recorder.errors(float(manifest.get("minimum_gap", MIN_GAP)), int(manifest.get("safe_margin", SAFE_MARGIN)))


def load_manifest(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_manifest(path: Path, manifest: dict[str, Any]) -> None:
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
