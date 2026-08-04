# Piano editoriale. Capitolo 66

## Obiettivo didattico

Seguire **Contesto lungo, retrieval e memoria** da segmento, query, budget e durata a contesto scelto, memoria aggiornata e costo, osservando routing, scrittura episodica e recupero senza oltrepassare questo limite: memoria persistente e contesto temporaneo hanno politiche diverse.

## Prerequisiti reali

- Capitolo 38: Posizione e contesto lungo
- Capitolo 63: Information retrieval
- Capitolo 64: Retrieval-Augmented Generation

## Percorso della lezione

1. **Tre risorse differenti.** Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiornabilità differenti. Prova: SRC-66-001.
2. **Quando usare il contesto.** Inserire tutti i documenti evita un indice separato ma aumenta prefill, distrattori e costo per richiesta. Prova: SRC-66-002.
3. **Quando recuperare.** Retrieval seleziona un sottoinsieme aggiornabile e attribuibile. Può fallire per query, indice o ranking. Prova: SRC-66-003.
4. **Memoria episodica.** Un sistema può salvare fatti o riassunti tra sessioni. Provenienza, consenso, scadenza e correzione diventano parte del contratto. Prova: SRC-66-004.
5. **Routing ibrido.** Una policy può scegliere cache, contesto, retrieval o memoria. La decisione deve essere misurata rispetto a qualità, latenza e privacy. Prova: SRC-66-001.

## Prove e artefatti

- riferimento minimo: `code/snip_66_contract.py`; test: `code/test_66_contract.py`; output: `code/outputs/SNIP-66-001.txt`.
- visuali candidate: MEMORY-01, MEMORY-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
