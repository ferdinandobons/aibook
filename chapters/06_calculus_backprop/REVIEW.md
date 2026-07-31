# Guida alla revisione. Capitolo 6

## Versione

- `chapter_id`: `CH-P02-CALCULUS-BACKPROP`
- Versione: `0.2.0-rc1`
- Testo: review fattuale, matematica, didattica, editoriale e linguistica superate internamente
- Codice: eseguito, cinque test registrati
- Visuali: validate tecnicamente
- Stato: revisione autoriale aperta

## Percorso consigliato

1. `CHAPTER.md`, per progressione, matematica e voce;
2. `CALC-01/candidate-v1.png`, per forward e backward;
3. `CALC-02/candidate-v2.png`, per reverse mode e VJP;
4. `code/snip_calc_001_manual_autograd.py`, per il confronto tra calcolo manuale, autograd e differenze finite;
5. `code/outputs/SNIP-CALC-001.txt` e `TESTS.txt`;
6. `CLAIMS.md` e `FONTI_PRIMARIE.md`;
7. `TEXT_AUDIT.md`;
8. `docs/02_STILE_E_QA_TESTO.md`, `docs/03_VISUALI.md` e `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`.

## Aspetti da valutare

- La derivata è comprensibile come sensibilità locale prima della definizione multivariata?
- La differenza tra gradiente e aggiornamento dei parametri è netta?
- La regola della catena si ricostruisce senza saltare passaggi?
- Il lettore comprende perché i gradienti procedono in senso inverso rispetto ai valori?
- Jacobiana, VJP, forward mode e reverse mode arrivano al momento giusto?
- Il livello tecnico è sufficiente senza trasformare il capitolo in una reference di autograd?
- I confini su differenze finite, `gradcheck`, accumulo e in-place sono chiari?
- L'italiano rimane fluido nei passaggi matematici?

## Prova di comprensione semplificata

Dopo la lettura, il revisore dovrebbe poter spiegare senza formule:

1. il forward calcola una previsione e una loss;
2. ogni operazione conosce come il proprio output cambia rispetto agli input;
3. il backward combina queste sensibilità dalla loss verso i parametri;
4. la backpropagation calcola gradienti, non aggiorna i parametri;
5. autograd esegue automaticamente questa composizione sul grafo registrato;
6. differenze finite e `gradcheck` controllano localmente il risultato.

## Decisioni richieste

- [ ] Approvo l'apertura e l'esempio scalare.
- [ ] Approvo la profondità su gradiente, Jacobiana e VJP.
- [ ] Approvo la distinzione tra backpropagation e optimizer.
- [ ] Approvo il livello dei dettagli PyTorch.
- [ ] Approvo `CALC-01`.
- [ ] Approvo `CALC-02`.
- [ ] Approvo esercizi e rinvii.
- [ ] Autorizzo il congelamento del capitolo dopo le eventuali correzioni.
