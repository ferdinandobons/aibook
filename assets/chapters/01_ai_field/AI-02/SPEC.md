# Specifica visuale `AI-02`

## Identità

- Capitolo: `CH-P01-AI-FIELD`
- Sezione: Training e inference sono due fasi diverse
- Famiglia: process / comparison
- Orientamento: orizzontale
- Stato: `storyboard, generazione bloccata`
- Standard: `docs/17_STANDARD_VISIVO_CANONICO.md`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Quando cambiano i parametri del modello e quando vengono soltanto usati per produrre un output?

## Pannello sinistro. Training

Ordine obbligatorio:

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

- il percorso di aggiornamento deve tornare esplicitamente al box dei parametri;
- `optimizer step` deve essere l'unico nodo che modifica `θ` in `θ'`;
- badge: `i parametri cambiano`;
- il target entra nella loss, non direttamente nel modello.

## Pannello destro. Inference

Ordine obbligatorio:

```text
Nuovo input
-> Modello con checkpoint fissato θ'
-> Output
```

Requisiti:

- nessuna loss;
- nessun gradiente;
- nessun optimizer;
- badge: `i parametri restano invariati`;
- nota: `caso base del capitolo`.

## Titolo e footer

- titolo: `AI-02 · Training e inference usano il modello in fasi diverse`;
- sottotitolo: `L'optimizer aggiorna i parametri nel training; l'inference usa il checkpoint disponibile`;
- footer: `eval() e inference_mode() hanno ruoli distinti in PyTorch`.

## Layout

- due pannelli paralleli con larghezza simile;
- training a sinistra, inference a destra;
- frecce da sinistra a destra;
- feedback di aggiornamento separato visivamente dal flusso dei dati;
- output dei due pannelli non collegati tra loro;
- ordine di lettura evidente.

## Palette

- blu: dati e input;
- viola: modello e parametri;
- ambra: loss e gradienti;
- verde: output e checkpoint pronto;
- rosso tenue solo per indicare un percorso vietato, se necessario.

## Contenimento

- testo completamente dentro i box;
- massimo tre righe per box;
- pedice o apice di `θ` e `θ'` interamente visibili;
- padding sufficiente;
- nessuna freccia attraversa una label;
- il loop di aggiornamento non deve sembrare collegato all'inference.

## Elementi vietati

- repository, branch, pull request o stato del progetto;
- grafici di accuratezza o loss non derivati dal codice;
- GPU o hardware non discussi;
- affermazioni di generalizzazione;
- `eval()` presentato come sinonimo di disabilitazione dei gradienti;
- watermark, loghi o branding.

## Provenienza

- sequenza del training: documentazione PyTorch e `SNIP-AI-001`;
- sequenza inference: `SNIP-AI-001` e documentazione `Module` / `inference_mode`;
- nessun valore quantitativo necessario.
