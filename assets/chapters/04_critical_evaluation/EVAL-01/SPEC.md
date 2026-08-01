# Specifica visuale `EVAL-01`

## Identità

- Capitolo: `CH-P01-CRITICAL-EVALUATION`
- Sezione: apertura e protocollo di valutazione
- Famiglia: processo di controllo
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Quali controlli collegano un punteggio osservato a un claim che il risultato può realmente sostenere?

## Ordine

```text
Domanda
-> Protocollo
-> Baseline
-> Metrica
-> Slice e costi
-> Variabilità
-> Controlli
-> Claim
```

## Contenuto

- domanda: decisione da sostenere;
- protocollo: dati, split e condizioni;
- baseline: soluzione di riferimento;
- metrica: proprietà misurata e proprietà omesse;
- slice e costi: errori importanti nei gruppi rilevanti;
- variabilità: campione e run;
- controlli: leakage, ablation e contaminazione;
- claim: conclusione limitata alle prove raccolte.

## Invariante e confine

La figura mostra una sequenza di domande di audit, non una garanzia che ogni esperimento che le nomina sia corretto. Nessun singolo box può sostenere da solo il claim finale.

## Contenimento

- massimo tre righe per box;
- frecce esterne ai contenitori;
- ordine a serpentina leggibile;
- nessuna sovrapposizione tra titolo, box e footer;
- colore associato anche a numero e titolo, non unico segnale.
