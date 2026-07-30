# Pacchetto di review. Capitolo 28

Il branch di produzione contiene la candidatura editoriale `0.4.0-rc4` del Capitolo 28.

## Percorso consigliato

1. `chapters/28_attention/REVIEW.md`;
2. `chapters/28_attention/CHAPTER.md`;
3. `chapters/28_attention/TEXT_AUDIT.md`;
4. `docs/20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`;
5. `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`;
6. `assets/chapters/28_attention/ATT-01/candidate-v2.png`;
7. `assets/chapters/28_attention/ATT-02/candidate-v2.png`;
8. `chapters/28_attention/code/`;
9. `chapters/28_attention/CLAIMS.md` e fonti.

## Novità della candidatura

La versione `0.4.0-rc4` affronta un problema diverso dal precedente gate anti-template. Il testo non mostrava più lo scaffold, ma conservava ancora un ritmo schematico e una voce vicina alla documentazione tecnica.

La nuova stesura:

- separa metadati e manuale;
- riduce le sezioni principali a otto;
- riunisce score, scaling, softmax e somma pesata in un solo percorso;
- chiarisce la distinzione tra key e value;
- alleggerisce dettagli API e riproducibilità;
- usa un italiano più naturale;
- ricompone il problema iniziale nel riepilogo;
- registra una review linguistica e una lettura ad alta voce.

## Stato delle immagini

- `ATT-01/candidate-v2.png`: tecnicamente validata nella versione precedente, controllo incrociato riaperto;
- `ATT-02/candidate-v2.png`: tecnicamente validata nella versione precedente, controllo incrociato riaperto.

`ATT-01` usa ancora le label `consumer 1` e `consumer 2`. Il testo le localizza una sola volta; l'autore può confermarle oppure richiedere una revisione con `posizione 1` e `posizione 2`.

## Stato del codice

I tre snippet e i test non sono stati modificati. La nuova prosa descrive gli stessi input, lo stesso ordine delle operazioni e gli stessi output registrati.

## Confine

Il pacchetto non contiene render di pagine o mockup editoriali. Contiene Markdown, figure tecniche, codice, test, output, fonti e audit.

## Regole canoniche pertinenti

- `docs/18_PROTOCOLLO_QA_DIDATTICO.md`;
- `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`;
- `docs/20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`;
- `docs/16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`;
- `docs/17_STANDARD_VISIVO_CANONICO.md`.
