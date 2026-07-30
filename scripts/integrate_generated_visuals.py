from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_exact(text: str, old: str, new: str, *, path: Path) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one occurrence in {path}: {old!r}; found {count}")
    return text.replace(old, new, 1)


def update_attention_chapter() -> Path:
    path = ROOT / "chapters/28_attention/CHAPTER.md"
    text = path.read_text(encoding="utf-8")
    text = replace_exact(
        text,
        "status: revisione di accessibilità per lettore non esperto completata, controllo visuale riaperto",
        "status: controllo visuale completato, revisione autoriale aperta",
        path=path,
    )
    text = replace_exact(text, "version: 0.5.0-rc5", "version: 0.6.0-rc6", path=path)
    text = replace_exact(
        text,
        "Nel pannello sinistro, `v1`, `v2` e `v3` confluiscono in un solo vettore `c`, riutilizzato da entrambe le posizioni, chiamate `consumer 1` e `consumer 2` nella figura.",
        "Nel pannello sinistro, `v1`, `v2` e `v3` confluiscono in un solo vettore `c`, riutilizzato da entrambe le posizioni, indicate nella figura come `Posizione 1` e `Posizione 2`.",
        path=path,
    )
    text = replace_exact(
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
