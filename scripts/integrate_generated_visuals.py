from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once_or_confirm(text: str, old: str, new: str, *, path: Path) -> str:
    old_count = text.count(old)
    new_count = text.count(new)
    if old_count == 1 and new_count == 0:
        return text.replace(old, new, 1)
    if old_count == 0 and new_count == 1:
        return text
    raise RuntimeError(
        f"Unexpected integration state in {path}: old={old_count}, new={new_count}, old_text={old!r}"
    )


def update_attention_chapter() -> Path:
    path = ROOT / "chapters/28_attention/CHAPTER.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once_or_confirm(
        text,
        "status: revisione di accessibilità per lettore non esperto completata, controllo visuale riaperto",
        "status: controllo visuale completato, revisione autoriale aperta",
        path=path,
    )
    text = replace_once_or_confirm(text, "version: 0.5.0-rc5", "version: 0.6.0-rc6", path=path)
    text = replace_once_or_confirm(
        text,
        "Nel pannello sinistro, `v1`, `v2` e `v3` confluiscono in un solo vettore `c`, riutilizzato da entrambe le posizioni, chiamate `consumer 1` e `consumer 2` nella figura.",
        "Nel pannello sinistro, `v1`, `v2` e `v3` confluiscono in un solo vettore `c`, riutilizzato da entrambe le posizioni, indicate nella figura come `Posizione 1` e `Posizione 2`.",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "../../assets/chapters/28_attention/ATT-01/candidate-v2.png",
        "../../assets/chapters/28_attention/ATT-01/candidate-v3.png",
        path=path,
    )
    path.write_text(text, encoding="utf-8")
    return path


def main() -> None:
    path = update_attention_chapter()
    print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
