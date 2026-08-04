# Piano editoriale. Capitolo 34

## Obiettivo didattico

Seguire **Scaling law e progettazione del modello** da punti con parametri, token, FLOP e loss a stima con intervallo osservato e costo, osservando fit, confronto isoFLOP ed estrapolazione senza oltrepassare questo limite: un fit fuori dominio non è una legge garantita.

## Prerequisiti reali

- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 16: Addestrare reti profonde
- Capitolo 32: Il ciclo di vita dei dati

## Percorso della lezione

1. **Fit empirico.** Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato. Prova: SRC-34-001.
2. **Allocazione compute-optimal.** A budget fissato, modello e token competono. Il risultato dipende da ricetta e qualità dei dati. Prova: SRC-34-002.
3. **Esperimenti isoFLOP.** Configurazioni con compute simile rendono osservabile la loss minima per budget. Prova: SRC-34-003.
4. **Extrapolation.** Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala. Prova: SRC-34-004.
5. **Training e inference cost.** Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio. Prova: SRC-34-001.

## Prove e artefatti

- riferimento minimo: `code/snip_34_contract.py`; test: `code/test_34_contract.py`; output: `code/outputs/SNIP-34-001.txt`.
- visuali candidate: SCALE-01, SCALE-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
