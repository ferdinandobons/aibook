# Piano editoriale. Capitolo 84

## Obiettivo didattico

Seguire **Fattualità, incertezza e affidabilità** da claim, predizione, fonti e score di confidenza a risposta supportata o astensione motivata, osservando verifica, calibrazione, astensione e retrieval senza oltrepassare questo limite: confidenza alta non certifica la verità fattuale.

## Prerequisiti reali

- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 83: Progettare una valutazione

## Percorso della lezione

1. **Correttezza e supporto.** Una frase può essere vera senza essere sostenuta dal contesto fornito, oppure fedele al contesto ma riferita a una fonte errata. Prova: SRC-84-001.
2. **Hallucination.** Il termine copre errori diversi: entità inventate, attribuzioni scorrette, contraddizioni e citazioni inesistenti. La tassonomia deve precedere la metrica. Prova: SRC-84-002.
3. **Calibrazione.** Probabilità del token, score di un verifier e frequenza empirica devono essere collegati con un protocollo di calibrazione. Prova: SRC-84-003.
4. **Astensione.** Un sistema può rifiutare o chiedere chiarimenti quando il rischio è alto. Coverage e accuracy conditional vanno riportate insieme. Prova: SRC-84-004.
5. **Verifica e retrieval.** Fonti esterne possono aumentare supporto, ma retrieval e generazione hanno failure mode separati. La provenienza deve restare tracciabile. Prova: SRC-84-001.

## Prove e artefatti

- riferimento minimo: `code/snip_84_contract.py`; test: `code/test_84_contract.py`; output: `code/outputs/SNIP-84-001.txt`.
- visuali candidate: FACTUALITY-01, FACTUALITY-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
