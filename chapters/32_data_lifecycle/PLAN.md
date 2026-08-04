# Piano editoriale. Capitolo 32

## Obiettivo didattico

Seguire **Il ciclo di vita dei dati** da testo grezzo, metadati, split e digest a record ammesso, conteggi e manifest, osservando parsing, filtro, deduplicazione e tokenizzazione senza oltrepassare questo limite: ogni trasformazione deve restare ricostruibile e ordinata.

## Prerequisiti reali

- Capitolo 26: Il testo come dato
- Capitolo 31: Dalla rappresentazione linguistica agli LLM

## Percorso della lezione

1. **Sorgenti e provenienza.** Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shard. Prova: SRC-32-001.
2. **Parsing e normalizzazione.** Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e devono essere versionate. Prova: SRC-32-002.
3. **Filtri.** Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono statistiche prima e dopo. Prova: SRC-32-003.
4. **Deduplicazione e contaminazione.** Hash esatti e similarità approssimata rilevano forme differenti di duplicazione. I benchmark richiedono controlli separati. Prova: SRC-32-004.
5. **Split, tokenizzazione e manifest.** Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training. Prova: SRC-32-001.

## Prove e artefatti

- riferimento minimo: `code/snip_32_contract.py`; test: `code/test_32_contract.py`; output: `code/outputs/SNIP-32-001.txt`.
- visuali candidate: DATA-01, DATA-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
