# Piano editoriale. Capitolo 19

## Obiettivo didattico

Seguire **Representation learning** da u = [1, 2, 0] e v = [2, 1, 0] a un vettore, una similarità o una predizione downstream, osservando una proiezione, una ricostruzione o una metrica tra rappresentazioni senza oltrepassare questo limite: la geometria dipende da dati, obiettivo e normalizzazione.

## Prerequisiti reali

- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 13: Apprendimento non supervisionato e auto-supervisionato
- Capitolo 15: Dal percettrone alle reti multilayer

## Percorso della lezione

1. **Che cosa rappresenta un vettore.** Una rappresentazione è un insieme di quantità prodotte dal modello e usate da un calcolo successivo. Il significato dipende da obiettivo e dati. Prova: SRC-19-001.
2. **Bottleneck e autoencoder.** Un autoencoder comprime e ricostruisce. Un bottleneck limita la capacità, ma non garantisce che le coordinate corrispondano a fattori interpretabili. Prova: SRC-19-002.
3. **Metric e contrastive learning.** Obiettivi contrastivi avvicinano coppie positive e separano alternative. La definizione delle coppie e delle augmentazioni stabilisce le invarianti apprese. Prova: SRC-19-003.
4. **Disentanglement e identifiability.** Separare fattori latenti richiede ipotesi. Senza supervision o bias aggiuntivi, molte rappresentazioni equivalenti possono spiegare gli stessi dati. Prova: SRC-19-004.
5. **Valutare una rappresentazione.** Linear probe, retrieval e fine-tuning misurano proprietà diverse. Una buona metrica downstream non dimostra interpretabilità globale. Prova: SRC-19-001.

## Prove e artefatti

- riferimento minimo: `code/snip_19_contract.py`; test: `code/test_19_contract.py`; output: `code/outputs/SNIP-19-001.txt`.
- visuali candidate: REPRESEN-01, REPRESEN-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
