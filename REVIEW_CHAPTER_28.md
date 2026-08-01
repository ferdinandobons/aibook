# Pacchetto di review. Capitolo 28

Il branch di produzione contiene la candidatura `0.6.0-rc6` del Capitolo 28.

## Percorso consigliato

1. `chapters/28_attention/REVIEW.md`;
2. `chapters/28_attention/CHAPTER.md`;
3. `chapters/28_attention/TEXT_AUDIT.md`;
4. `assets/chapters/28_attention/ATT-01/candidate-v3.png`;
5. `assets/chapters/28_attention/ATT-02/candidate-v2.png`;
6. `chapters/28_attention/code/`;
7. `chapters/28_attention/CLAIMS.md` e fonti;
8. `docs/02_STILE_E_QA_TESTO.md` e `docs/03_VISUALI.md`.

## Novità della candidatura

- testo riscritto per un lettore non esperto;
- token, vettore, shape e prodotto scalare spiegati nel punto d'uso;
- formula compatta dopo il calcolo completo;
- un solo snippet completo nel corpo;
- `ATT-01` rigenerata come `candidate-v3.png`;
- `consumer 1/2` sostituito con `Posizione 1/2`;
- alt text di `ATT-01` corretto con i coefficienti `0,05`, `0,15`, `0,80` della seconda query;
- `ATT-02` ricontrollata nel nuovo flusso;
- controllo incrociato testo, visuali e codice superato.

## Stato

- Testo: validato internamente.
- Codice: tre snippet e tre test invariati.
- Visuali: validate tecnicamente.
- Review autoriale: aperta.
- `final.png`: nessun file prima dell'approvazione.

Il pacchetto contiene Markdown, figure tecniche, codice, test, output, fonti e audit. Non contiene pagine rasterizzate o mockup editoriali.
