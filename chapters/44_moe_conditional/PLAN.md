# Piano editoriale. Capitolo 44

## Obiettivo didattico

Seguire **Mixture of Experts e calcolo condizionale** da logits del router, top-k e capacità per esperto a carico, token restituiti e costo attivo, osservando routing, dispatch, expert compute e combine senza oltrepassare questo limite: parametri totali e parametri attivi non sono la stessa quantità.

## Prerequisiti reali

- Capitolo 16: Addestrare reti profonde
- Capitolo 29: Il Transformer da zero
- Capitolo 36: Training distribuito e continued pretraining

## Percorso della lezione

1. **Router top-k.** Un router assegna probabilità agli esperti e attiva un sottoinsieme per token. Prova: SRC-44-001.
2. **Capacità.** Ogni esperto riceve un limite di token. Overflow, rerouting o dropping devono essere dichiarati. Prova: SRC-44-002.
3. **Load balancing.** Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione. Prova: SRC-44-003.
4. **Expert parallelism.** Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti. Prova: SRC-44-004.
5. **Parametri totali e attivi.** Un MoE può avere molti parametri totali e pochi parametri attivi per token. FLOP, memoria e comunicazione vanno riportati separatamente. Prova: SRC-44-001.

## Prove e artefatti

- riferimento minimo: `code/snip_44_contract.py`; test: `code/test_44_contract.py`; output: `code/outputs/SNIP-44-001.txt`.
- visuali candidate: MOE-01, MOE-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
