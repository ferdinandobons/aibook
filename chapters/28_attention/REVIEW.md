# Guida alla revisione. Capitolo 28

## Versione da revisionare

- Capitolo: `CH-P06-ATTENTION`
- Versione: `0.4.0-rc4`
- Testo: review fattuale, didattica, editoriale e linguistica superate internamente
- Codice: tre snippet invariati, test registrati superati
- Visuali: validate tecnicamente nella versione precedente, controllo incrociato riaperto
- Review autoriale: riaperta

## Percorso consigliato

1. `CHAPTER.md`, per voce, fluidità, progressione e profondità matematica;
2. `TEXT_AUDIT.md`, per le review `EDIT-ATT-01` e `EDIT-ATT-02`;
3. `assets/.../ATT-01/candidate-v2.png`, per il confronto iniziale;
4. `assets/.../ATT-02/candidate-v2.png`, per il calcolo numerico;
5. `code/`, per i tre snippet e i test;
6. `CLAIMS.md` e `FONTI_PRIMARIE.md`, per la tracciabilità;
7. `docs/02_STILE_E_QA_TESTO.md`, per voce e review del manuale;
8. `docs/03_VISUALI.md`, per lo standard delle figure.

## Modifiche principali della versione `0.4.0-rc4`

- metadati e registri non interrompono più il capitolo;
- le sezioni principali sono state ridotte a otto;
- score, scaling, softmax e somma pesata formano un unico percorso discorsivo;
- l'esempio viene introdotto come astrazione numerica di un problema sequenziale;
- i ruoli di query, key e value sono spiegati con maggiore naturalezza;
- l'identità numerica di `K` e `V` viene dichiarata come scelta illustrativa;
- i dettagli PyTorch sono stati alleggeriti e raccolti in una nota;
- complessità, limiti e multi-head attention sono riuniti in una sezione finale;
- il riepilogo torna al problema del contesto fisso;
- fonti e artefatti sono condensati.

## Aspetti da valutare nel testo

- La lezione si legge come un capitolo di manuale?
- Il passaggio dal problema intuitivo ai vettori è naturale?
- Il calcolo completo resta localizzabile senza essere frammentato?
- La distinzione tra key e value è chiara anche se i numeri coincidono?
- Le formule sostengono il ritmo?
- La sezione PyTorch è utile senza diventare una reference?
- Il riepilogo rende evidente che cosa l'attention permette di fare?

## Stato delle visuali

- `ATT-01`: candidata tecnicamente validata nella versione precedente;
- `ATT-02`: candidata tecnicamente validata nella versione precedente.

La nuova prosa usa entrambe le figure, ma il controllo incrociato deve essere ripetuto. `ATT-01` conserva le label `consumer 1` e `consumer 2`; il testo le localizza una sola volta. Una futura revisione può sostituirle con `posizione 1` e `posizione 2`.

## Decisioni richieste all'autore

- [ ] Approvo la nuova voce editoriale.
- [ ] Approvo la riduzione delle sezioni.
- [ ] Approvo il ritmo della spiegazione matematica.
- [ ] Approvo la profondità tecnica.
- [ ] Approvo il formato dei tre snippet.
- [ ] Confermo `ATT-01` nel nuovo contesto oppure richiedo l'aggiornamento delle label.
- [ ] Confermo `ATT-02` nel nuovo contesto.
- [ ] Autorizzo l'applicazione di questa voce ai capitoli successivi.
