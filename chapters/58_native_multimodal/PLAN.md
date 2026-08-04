# Piano editoriale. Capitolo 58

## Obiettivo didattico

Seguire **Modelli multimodali nativi e any-to-any** da sequenza testo-immagine-audio con mask a token o artefatto nella modalità richiesta, osservando backbone condiviso, routing e sincronizzazione senza oltrepassare questo limite: ordine, durata e maschera della modalità devono essere espliciti.

## Prerequisiti reali

- Capitolo 55: Fondamenti della multimodalità
- Capitolo 56: Vision encoder e Vision-Language Model

## Percorso della lezione

1. **Token interleaved.** Sequenze possono alternare testo, immagini, audio e marker. Il tokenizer multimodale definisce unità e ordine. Prova: SRC-58-001.
2. **Backbone condiviso.** Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e adapter specifici. Prova: SRC-58-002.
3. **Output multimodale.** La generazione di testo e media richiede head o decoder differenti, anche quando il backbone è comune. Prova: SRC-58-003.
4. **Any-to-any.** Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state realmente addestrate e valutate. Prova: SRC-58-004.
5. **Sincronizzazione.** Audio, video e testo possiedono frequenze differenti. Allineamento temporale e turn-taking diventano parte dell'architettura. Prova: SRC-58-001.

## Prove e artefatti

- riferimento minimo: `code/snip_58_contract.py`; test: `code/test_58_contract.py`; output: `code/outputs/SNIP-58-001.txt`.
- visuali candidate: MULTIMODAL-01, MULTIMODAL-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
