# Piano editoriale. Capitolo 41

## Obiettivo didattico

Seguire **Linear attention, fast weights e delta rule** da sequenza x_t, kernel fattorizzabile e stato a h_t e predizione con costo dichiarato, osservando recurrence, normalizzazione e fast weights senza oltrepassare questo limite: la fattorizzazione cambia memoria e capacità di interazione.

## Prerequisiti reali

- Capitolo 28: Il meccanismo di attention
- Capitolo 37: Anatomia del blocco moderno

## Percorso della lezione

1. **Kernel fattorizzabile.** Una feature map permette di riassociare i prodotti senza una matrice completa di score. Prova: SRC-41-001.
2. **Recurrence causale.** Statistiche S e z vengono aggiornate per token e hanno dimensione indipendente dalla lunghezza. Prova: SRC-41-002.
3. **Normalizzazione.** Il denominatore controlla la scala e richiede feature e stabilizzazione coerenti. Prova: SRC-41-003.
4. **Fast weights.** Lo stato può essere letto come memoria associativa che accumula coppie key-value. Prova: SRC-41-004.
5. **Delta rule.** L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascrittura cieca. Prova: SRC-41-001.

## Prove e artefatti

- riferimento minimo: `code/snip_41_contract.py`; test: `code/test_41_contract.py`; output: `code/outputs/SNIP-41-001.txt`.
- visuali candidate: LINATT-01, LINATT-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
