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


def update_numerics_chapter() -> Path:
    path = ROOT / "chapters/09_numerics_hardware/CHAPTER.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once_or_confirm(
        text,
        "status: testo e codice completi, visuali in revisione",
        "status: candidatura completa in revisione autoriale",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "version: 0.1.0-draft1",
        "version: 0.2.0-rc1",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "<!-- Inserire NUM-01 dopo la materializzazione e l'audit del PNG. -->",
        "![Range e precisione dei dtype floating point](../../assets/chapters/09_numerics_hardware/NUM-01/candidate-v1.png)\n\nLa figura confronta range e precisione senza trasformare la larghezza del dtype in una graduatoria universale. Float16 e bfloat16 occupano entrambi due byte, ma distribuiscono diversamente i bit tra esponente e significando.",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "<!-- Inserire NUM-02 dopo la materializzazione e l'audit del PNG. -->",
        "![Contratto tipico della mixed precision](../../assets/chapters/09_numerics_hardware/NUM-02/candidate-v1.png)\n\nLa figura separa storage, autocast, accumulo, gradienti e aggiornamento dei pesi. L'optimizer modifica i parametri, non l'input, e il dtype visibile del tensore non descrive da solo l'intero percorso numerico.",
        path=path,
    )
    path.write_text(text, encoding="utf-8")
    return path


def update_search_chapter() -> Path:
    path = ROOT / "chapters/10_search_planning/CHAPTER.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once_or_confirm(
        text,
        "status: testo e codice completi, visuali in revisione",
        "status: candidatura completa in revisione autoriale",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "version: 0.1.0-draft1",
        "version: 0.2.0-rc1",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "<!-- Inserire SEARCH-01 dopo la materializzazione e l'audit del PNG. -->",
        "![Uniform-cost e A* sullo stesso grafo](../../assets/chapters/10_search_planning/SEARCH-01/candidate-v2.png)\n\nLa figura mantiene fisso il grafo e confronta soltanto l'ordine di espansione. Nel caso illustrativo, uniform-cost e A* restituiscono lo stesso piano di costo 6; l'euristica consistente evita l'espansione dei tre stati del ramo di pagamento e dell'intervento dell'agente.",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "<!-- Inserire SEARCH-02 dopo la materializzazione e l'audit del PNG. -->",
        "![Minimax e potatura alpha-beta](../../assets/chapters/10_search_planning/SEARCH-02/candidate-v2.png)\n\nLa figura mostra l'albero minimax completo e marca il ramo che alpha-beta non deve valutare. La foglia 9 resta visibile per ricostruire il valore minimax, ma il collegamento tratteggiato indica che non viene visitata nell'ordine usato dal codice.",
        path=path,
    )
    path.write_text(text, encoding="utf-8")
    return path


def update_knowledge_chapter() -> Path:
    path = ROOT / "chapters/11_knowledge_logic/CHAPTER.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once_or_confirm(
        text,
        "status: testo e codice completi, visuali in revisione",
        "status: candidatura completa in revisione autoriale",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "version: 0.1.0-draft1",
        "version: 0.2.0-rc1",
        path=path,
    )
    path.write_text(text, encoding="utf-8")
    return path


def main() -> None:
    for path in [
        update_numerics_chapter(),
        update_search_chapter(),
        update_knowledge_chapter(),
    ]:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
