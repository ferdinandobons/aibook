# Specifica visuale `AI-02`

## Identità

- Capitolo: `CH-P01-AI-FIELD`
- Sezione: Parametri, training e inference
- Famiglia: process / comparison
- Orientamento: orizzontale
- Stato: `candidate-v1, validata tecnicamente`
- File: `candidate-v1.png`
- Standard: `docs/03_VISUALI.md`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Quando cambiano i parametri del modello e quando vengono soltanto usati per produrre un output?

## Pannello sinistro. Training

Ordine:

```text
Dati di training
-> Modello con parametri θ
-> Output
-> Loss rispetto ai target
-> Gradienti
-> Optimizer step
-> Parametri aggiornati θ'
```

Requisiti:

- il percorso di aggiornamento torna al box del modello;
- `optimizer step` è l'unico nodo che modifica `θ` in `θ'`;
- badge: `i parametri cambiano`;
- il target entra nella loss, non direttamente nel modello.

## Pannello destro. Inference

Ordine:

```text
Nuovo input
-> Modello con checkpoint fissato θ'
-> Output
```

Requisiti:

- nessuna loss;
- nessun gradiente;
- nessun optimizer;
- badge: `parametri invariati`;
- nota: `caso base del capitolo`.

## Titolo e footer

- titolo: `AI-02 · Training e inference usano il modello in fasi diverse`;
- sottotitolo: `L'optimizer aggiorna i parametri nel training; l'inference usa il checkpoint disponibile`;
- footer: `eval() e inference_mode() hanno ruoli distinti in PyTorch`.

## Layout

- due pannelli paralleli;
- training a sinistra, inference a destra;
- frecce da sinistra a destra;
- feedback di aggiornamento separato dal flusso dei dati;
- output dei pannelli non collegati;
- ordine di lettura evidente.

## Palette

- blu: dati e input;
- viola: modello e parametri;
- ambra: loss e gradienti;
- verde: output e checkpoint pronto;
- rosso tenue per gli elementi assenti nell'inference.

## Contenimento

- testo interamente nei box;
- massimo tre righe per box;
- `θ` e `θ'` completamente visibili;
- padding sufficiente;
- nessuna freccia attraversa una label;
- il loop di aggiornamento non sembra collegato all'inference.

## Elementi vietati

- repository, branch, pull request o stato del progetto;
- grafici di accuratezza o loss non derivati dal codice;
- GPU o hardware non discussi;
- affermazioni di generalizzazione;
- `eval()` presentato come sinonimo della disabilitazione dei gradienti;
- watermark, loghi o branding.

## Provenienza

- training: documentazione PyTorch e `SNIP-AI-001`;
- inference: `SNIP-AI-001` e documentazione `Module` / `inference_mode`;
- nessun valore quantitativo necessario;
- generazione raster riproducibile: `scripts/generate_book_visuals.py`.
- domanda principale: Quale trasformazione centrale rende osservabile «Una stessa richiesta, sistemi diversi» nel capitolo 1?
