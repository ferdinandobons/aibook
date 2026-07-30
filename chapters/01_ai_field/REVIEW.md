# Guida alla revisione. Capitolo 1

## Stato

- `chapter_id`: `CH-P01-AI-FIELD`
- Versione: `0.3.0-rc2`
- Testo: review tecnica, didattica, editoriale, linguistica e di chiarezza per lettore non esperto superate
- Codice: audit tecnico superato, tre test registrati, nessuna modifica nella riscrittura
- Visuali: aperte
- Review autoriale: non ancora aperta per il capitolo completo

## Percorso consigliato

1. `CHAPTER.md`, per chiarezza, voce, fluidità e progressione;
2. `TEXT_AUDIT.md`, per le review da `EDIT-AI-01` a `EDIT-AI-04`;
3. `CLAIMS.md`, per la mappa frase-prova;
4. `FONTI_PRIMARIE.md`, per fonti e limiti;
5. `code/`, per snippet, output e test;
6. `assets/chapters/01_ai_field/`, per specifiche e stato delle visuali;
7. `docs/02_STILE_E_QA_TESTO.md`, per voce e review del manuale;
8. `docs/03_VISUALI.md`, per lo standard delle figure.

## Modifiche principali della versione `0.3.0-rc2`

- le tre domande guida compaiono nell'apertura;
- la definizione OECD viene tradotta subito in linguaggio comune;
- modello e sistema vengono distinti attraverso il caso della spedizione;
- machine learning viene spiegato prima come ciclo di esempi, errore e aggiornamento;
- parametri, iperparametri, checkpoint, training e inference vengono introdotti in ordine;
- `feature`, `logit`, `loss`, `optimizer` e `shape` ricevono una spiegazione nel punto d'uso;
- la formula lineare e le formule probabilistiche aggiungono precisione senza reggere da sole la spiegazione;
- discriminativo e generativo vengono distinti con esempi prima della notazione;
- foundation model viene presentato come base adattabile, senza anticipare una lista di tecniche;
- il riepilogo è in prosa e riprende le tre domande iniziali.

## Aspetti da valutare nel testo

- Un lettore senza formazione in AI comprende il problema già nelle prime righe?
- Le tre domande restano visibili lungo tutto il capitolo?
- Ogni termine tecnico è spiegato prima di essere riutilizzato come abbreviazione?
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

## Stato delle visuali

- `AI-01`: da rigenerare;
- `AI-02`: da generare;
- PNG pubblicati: nessuno.

Le visuali restano bloccanti per la candidatura completa. La versione testuale può essere revisionata come standard di voce per lettori non specialisti.

## Controlli visuali futuri

- `AI-01` deve mostrare i tre aspetti senza falsa gerarchia e con le stesse parole semplici del testo;
- `AI-02` deve separare training e inference senza introdurre gergo non spiegato;
- entrambe devono usare sfondo bianco e lo standard canonico;
- testo, figure e snippet devono descrivere lo stesso contratto;
- dopo l'inserimento si ripetono review incrociata, linguistica e lettura completa.
