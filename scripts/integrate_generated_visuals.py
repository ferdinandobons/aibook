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


def update_history_chapter() -> Path:
    path = ROOT / "chapters/02_history/CHAPTER.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once_or_confirm(
        text,
        "status: prima stesura completa, visuali e codice in revisione",
        "status: candidatura completa in revisione autoriale",
        path=path,
    )
    text = replace_once_or_confirm(text, "version: 0.1.0-draft1", "version: 0.2.0-rc1", path=path)
    text = replace_once_or_confirm(
        text,
        "Il seguente snippet mostra una ricerca in ampiezza su un piccolo workflow. Non riproduce un programma storico specifico; rende osservabile il contratto di base: stati espliciti, azioni esplicite e ricerca di un percorso.",
        "Il seguente snippet mostra una ricerca in ampiezza su un piccolo workflow. L'algoritmo mantiene una coda ed esplora prima i percorsi con meno transizioni. Non riproduce un programma storico specifico; rende osservabile il contratto di base: stati espliciti, azioni esplicite e ricerca di un percorso.",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "Le support vector network del 1995, per esempio, costruiscono una superficie decisionale in uno spazio di feature e rappresentano una delle famiglie importanti dell'apprendimento statistico [Cortes e Vapnik, 1995].",
        "Il lavoro del 1995 sulle support-vector network costruisce una superficie decisionale in uno spazio di feature e rappresenta uno degli esempi importanti dell'apprendimento statistico [Cortes e Vapnik, 1995].",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "Nel 2012, Krizhevsky, Sutskever e Hinton addestrarono una rete convoluzionale profonda sul dataset ImageNet usando una implementazione GPU e riportarono un risultato nettamente migliore rispetto agli altri sistemi della competizione descritta nel paper [Krizhevsky et al., 2012].",
        "Nel 2012, Krizhevsky, Sutskever e Hinton addestrarono una rete convoluzionale profonda su ImageNet, un grande benchmark di immagini etichettate, usando unità di calcolo parallelo GPU. Nel paper riportarono un risultato nettamente migliore rispetto agli altri sistemi della competizione [Krizhevsky et al., 2012].",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "BERT usa il pretraining bidirezionale di un Transformer e il fine-tuning per diversi compiti linguistici [Devlin et al., 2019].",
        "BERT usa il pretraining bidirezionale di un Transformer e un ulteriore addestramento, chiamato fine-tuning, per diversi compiti linguistici [Devlin et al., 2019].",
        path=path,
    )
    text = replace_once_or_confirm(
        text,
        "Nel 2020, Kaplan e colleghi studiarono relazioni empiriche tra loss, dimensione del modello, quantità di dati e compute per la famiglia di language model analizzata [Kaplan et al., 2020].",
        "Nel 2020, Kaplan e colleghi studiarono relazioni empiriche tra loss, dimensione del modello, quantità di dati e risorse di calcolo per la famiglia di language model analizzata [Kaplan et al., 2020].",
        path=path,
    )
    path.write_text(text, encoding="utf-8")
    return path


def update_lifecycle_chapter() -> Path:
    path = ROOT / "chapters/03_lifecycle/CHAPTER.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once_or_confirm(
        text,
        "status: prima stesura completa, visuali e codice in revisione",
        "status: candidatura completa in revisione autoriale",
        path=path,
    )
    text = replace_once_or_confirm(text, "version: 0.1.0-draft1", "version: 0.2.0-rc1", path=path)
    path.write_text(text, encoding="utf-8")
    return path


def main() -> None:
    for path in [update_attention_chapter(), update_history_chapter(), update_lifecycle_chapter()]:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
