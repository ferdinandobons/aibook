# Piano editoriale. Capitolo 97

## Obiettivo didattico

Seguire **Riprodurre e leggere un paper** da paper, codice, dati, seed, hardware e metriche a risultato replicato o differenza spiegata, osservando setup indipendente, run, confronto e analisi delle divergenze senza oltrepassare questo limite: una replica richiede stesso claim e confini dichiarati, non solo stesso codice.

## Prerequisiti reali

- Capitolo 4: Come valutare criticamente un risultato di AI
- Capitolo 83: Progettare una valutazione
- Capitolo 94: Percorso pratico dai fondamenti

## Percorso della lezione

1. **Domanda e claim.** Il paper viene scomposto in domanda, baseline, metodo, setup, risultati e limiti. Prova: SRC-97-001.
2. **Artefatti.** Codice, checkpoint, dati e configurazioni vengono versionati e confrontati con la descrizione. Prova: SRC-97-002.
3. **Replica.** Una riproduzione conferma lo stesso codice; una replica indipendente ricostruisce il metodo con scelte proprie. Prova: SRC-97-003.
4. **Divergenze.** Differenze di hardware, seed, preprocessing e versioni vengono registrate invece di essere nascoste. Prova: SRC-97-004.
5. **Conclusione sostenibile.** Il risultato viene limitato al setup eseguito e confrontato con l'incertezza del paper originale. Prova: SRC-97-001.

## Prove e artefatti

- riferimento minimo: `code/snip_97_contract.py`; test: `code/test_97_contract.py`; output: `code/outputs/SNIP-97-001.txt`.
- laboratorio esteso: `code/replication_protocol.py`; test: `code/test_replication_protocol.py`; output: `code/outputs/REPLICATION-PROTOCOL.txt`.
- visuali candidate: REPLICATIO-01, REPLICATIO-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
