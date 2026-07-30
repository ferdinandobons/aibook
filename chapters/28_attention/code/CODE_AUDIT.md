# Audit del codice. Capitolo 28

- Data: 30 luglio 2026
- Versione del capitolo: `0.2.0-rc2`
- Python eseguito: `3.13.5`
- PyTorch eseguito: `2.10.0+cpu`
- Documentazione API ricontrollata: stable `2.13`
- Esito: **approvato tecnicamente per review autoriale**

## Controlli

- [x] Import completi.
- [x] Nessuna dipendenza da stato di notebook.
- [x] Esecuzione da processi nuovi.
- [x] Shape dichiarate e testate.
- [x] Somme delle righe testate.
- [x] Equivalenza formula/API testata in `float64`.
- [x] Causal mask confrontata con implementazione additiva diretta.
- [x] Output salvati.
- [x] Tre test superati dopo la riscrittura didattica.
- [x] Nessuno snippet introduce multi-head attention prima del capitolo dedicato.

## Limiti

- Nessuna GPU disponibile nel run registrato.
- Nessun benchmark di kernel.
- Nessuna esecuzione locale sotto PyTorch `2.13`.
- Il comportamento dei backend fused non è misurato.
