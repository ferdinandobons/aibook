# Piano editoriale. Capitolo 33

## Obiettivo didattico

Seguire **Dataset mixture, curriculum e dati sintetici** da pesi, temperatura, curriculum e conteggio dei token a probabilità effettive e mix osservato, osservando campionamento, ripesatura e generazione controllata senza oltrepassare questo limite: peso nominale e esposizione effettiva non sono la stessa misura.

## Prerequisiti reali

- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 26: Il testo come dato
- Capitolo 32: Il ciclo di vita dei dati

## Percorso della lezione

1. **Peso effettivo delle sorgenti.** Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni. Prova: SRC-33-001.
2. **Temperature sampling.** Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli. Prova: SRC-33-002.
3. **Mixture ottimizzata.** Pesi appresi con proxy model dipendono da domini, validation e budget. Prova: SRC-33-003.
4. **Curriculum.** Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione. Prova: SRC-33-004.
5. **Dati sintetici.** Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato. Prova: SRC-33-001.

## Prove e artefatti

- riferimento minimo: `code/snip_33_contract.py`; test: `code/test_33_contract.py`; output: `code/outputs/SNIP-33-001.txt`.
- visuali candidate: MIX-01, MIX-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
