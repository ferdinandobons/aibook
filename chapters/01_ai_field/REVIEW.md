# Guida alla revisione. Capitolo 1

## Stato

- `chapter_id`: `CH-P01-AI-FIELD`
- Versione: `0.4.0-rc3`
- Testo: review tecnica, didattica, editoriale, linguistica e di chiarezza per lettore non esperto superate
- Codice: audit tecnico superato, tre test registrati, nessuna modifica nelle riscritture
- Visuali: `AI-01` e `AI-02` validate tecnicamente
- Controllo incrociato: superato
- Review autoriale: aperta per la candidatura completa

## Percorso consigliato

1. `CHAPTER.md`, per chiarezza, voce, fluidità e progressione;
2. `assets/chapters/01_ai_field/AI-01/candidate-v1.png`;
3. `assets/chapters/01_ai_field/AI-02/candidate-v1.png`;
4. `TEXT_AUDIT.md`, per la cronologia delle review;
5. `CLAIMS.md`, per la mappa frase-prova;
6. `FONTI_PRIMARIE.md`, per fonti e limiti;
7. `code/`, per snippet, output e test;
8. `docs/02_STILE_E_QA_TESTO.md` e `docs/03_VISUALI.md`, per gli standard applicati.

## Modifiche principali della candidatura

- le tre domande guida compaiono nell'apertura;
- la definizione OECD viene tradotta subito in linguaggio comune;
- modello e sistema vengono distinti attraverso il caso della spedizione;
- machine learning viene spiegato prima come ciclo di esempi, errore e aggiornamento;
- parametri, iperparametri, checkpoint, training e inference vengono introdotti in ordine;
- `logit`, `loss`, `optimizer` e `shape` ricevono una spiegazione nel punto d'uso;
- la formula lineare e le formule probabilistiche aggiungono precisione senza reggere da sole la spiegazione;
- discriminativo e generativo vengono distinti con esempi prima della notazione;
- foundation model viene presentato come base adattabile;
- `AI-02` viene attraversata prima dello snippet PyTorch;
- `AI-01` rende visibili i tre aspetti senza disporli in una gerarchia;
- il riepilogo è in prosa e riprende le domande iniziali.

## Aspetti da valutare nel testo

- Un lettore senza formazione in AI comprende il problema già nelle prime righe?
- Le tre domande restano visibili lungo tutto il capitolo?
- Ogni termine tecnico è spiegato prima di essere riutilizzato?
- Il lettore può distinguere regola, machine learning e deep learning senza formule?
- Training e inference risultano diversi prima di arrivare al codice?
- Il codice conferma la spiegazione senza diventare una guida API?
- La distinzione discriminativo/generativo rimane chiara anche saltando la notazione probabilistica?
- Foundation model, modello generativo e sistema applicativo restano distinti?
- L'italiano sembra scritto direttamente, con un ritmo naturale?

## Prova di comprensione semplificata

Dopo la lettura, il revisore dovrebbe poter spiegare il capitolo senza usare inizialmente i termini tecnici:

1. alcuni sistemi seguono regole, altri modificano numeri interni usando esempi;
2. il training modifica quei numeri, l'inference li usa;
3. un sistema può scegliere una categoria oppure produrre un nuovo contenuto;
4. un modello di base adattabile non coincide con ogni applicazione costruita attorno a esso;
5. modello e sistema non sono la stessa cosa.

Se una di queste frasi non è ricostruibile, la review di chiarezza va riaperta.

## Controllo delle visuali

### `AI-01`

- [ ] I tre pannelli appaiono indipendenti e di pari importanza?
- [ ] Il caso guida collega la figura al testo?
- [ ] Nessuna disposizione suggerisce che un aspetto sia più avanzato degli altri?
- [ ] Tutto il testo è leggibile e contenuto nei box?

### `AI-02`

- [ ] È chiaro che il target entra nella loss?
- [ ] È chiaro che soltanto l'optimizer modifica i parametri?
- [ ] Il pannello inference è privo di loss, gradienti e optimizer?
- [ ] Il loop di training non sembra collegato all'inference?
- [ ] Tutto il testo è leggibile e contenuto nei box?

## Decisioni richieste all'autore

- [ ] Approvo il testo della versione `0.4.0-rc3`.
- [ ] Approvo `AI-01/candidate-v1.png`.
- [ ] Approvo `AI-02/candidate-v1.png`.
- [ ] Approvo il formato dello snippet e degli esercizi.
- [ ] Autorizzo la rinomina delle figure in `final.png`.
- [ ] Autorizzo il congelamento del Capitolo 1 e l'apertura del Capitolo 2.
