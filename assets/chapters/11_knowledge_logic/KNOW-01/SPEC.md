# Specifica visuale `KNOW-01`

## Identità

- Capitolo: `CH-P03-KNOWLEDGE-LOGIC`
- Famiglia: flusso deduttivo a tre colonne
- Orientamento: orizzontale
- File candidato: `candidate-v2.png`
- Canvas: `1800 × 1000`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Come producono nuove conclusioni tre regole positive applicate agli stessi fatti?

## Contenuto

### Fatti iniziali

```text
message_mentions_missing_delivery(order_42)
tracking_stalled(order_42)
delivery_date_passed(order_42)
```

### Regole

```text
R1 -> possible_delay(?ordine)
R2 -> needs_review(?ordine)
R3 -> eligible_for_delay_workflow(?ordine)
```

### Fatti derivati

```text
possible_delay(order_42)
needs_review(order_42)
eligible_for_delay_workflow(order_42)
```

## Layout

- fatti iniziali in blu;
- regole in viola;
- fatti derivati in verde;
- tre passaggi numerati;
- predicati lunghi spezzati intenzionalmente dentro i box;
- footer ambra su assenza e negazione;
- nessuna freccia attraversa un contenitore.

## Confine

La figura mostra un forward chaining positivo. Non rappresenta negation-as-failure, contraddizioni, probabilità o causalità.

## Provenienza

Dati da `SNIP-KNOW-001`. PNG raster prodotto da `scripts/generate_knowledge_visuals.py`; nessun SVG.
