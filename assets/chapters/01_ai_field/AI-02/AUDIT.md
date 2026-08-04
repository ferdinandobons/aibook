# Audit visuale `AI-02`

## Stato

- Esito: **validata tecnicamente**
- Approvazione tecnica: sì
- Approvazione autoriale: no
- File candidato: `candidate-v1.png`
- Generatore: `scripts/generate_book_visuals.py`
- Data: 30 luglio 2026

## Iterazioni respinte

| Tentativo | Difetto bloccante | Decisione |
|---|---|---|
| 1 | pagina doppia con tassonomia e training, troppo densa e non conforme alla domanda unica | respinta |
| 2 | testo sovrapposto, output compresso e note fuori dai contenitori | respinta |

## Controlli della candidata `candidate-v1.png`

### Contratto del training

- [x] dati e target distinti;
- [x] target collegato alla loss e non direttamente al modello;
- [x] output prodotto dal modello prima della loss;
- [x] gradienti successivi alla loss;
- [x] optimizer step successivo ai gradienti;
- [x] `optimizer step` unico nodo che modifica `θ` in `θ'`;
- [x] percorso di aggiornamento separato dal flusso dei dati;
- [x] checkpoint aggiornato riportato al modello.

### Contratto dell'inference

- [x] nuovo input collegato al checkpoint fissato;
- [x] output prodotto senza target;
- [x] nessuna loss;
- [x] nessun gradiente;
- [x] nessun optimizer step;
- [x] parametri dichiarati invariati;
- [x] nessuna affermazione di generalizzazione.

### Geometria e stile

- [x] sfondo globale `#FFFFFF`;
- [x] orientamento orizzontale adeguato;
- [x] testo integralmente contenuto;
- [x] `θ` e `θ'` leggibili;
- [x] nessuna freccia attraversa una label;
- [x] loop di training non collegato al pannello inference;
- [x] palette canonica;
- [x] nessun watermark o branding;
- [x] PNG decodificato e verificato dal generatore.

### Coerenza col capitolo

- [x] ordine allineato alla prosa;
- [x] `optimizer.step()` localizzato come aggiornamento;
- [x] `eval()` e `inference_mode()` dichiarati distinti nel footer;
- [x] alt text verificato;
- [x] figura coerente con `SNIP-AI-001` senza inventare valori quantitativi.

## Difetti residui

Nessun difetto tecnico bloccante noto. La figura resta una candidata fino all'approvazione autoriale.

## Decisione

Il gate visuale tecnico del Capitolo 1 è superato. Il capitolo può passare alla revisione autoriale completa.

## Gate geometrico raster

- [x] PNG decodificato e dimensione standard verificata;
- [x] contenuto distante almeno 20 px dal bordo;
- [x] checklist storica di padding e contenimento mantenuta;
- [x] nessuna sovrapposizione o elemento attaccato dichiarato nell'audit della candidata;
- [x] manifest `GEOMETRY.json` scritto per il controllo indipendente del raster.
