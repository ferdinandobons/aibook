# Specifica visuale `KNOW-02`

## Identità

- Capitolo: `CH-P03-KNOWLEDGE-LOGIC`
- Famiglia: rete probabilistica con calcolo numerico
- Orientamento: orizzontale
- File candidato: `candidate-v3.png`
- Canvas: `1800 × 1000`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Come fattorizza la congiunta la rete `H -> M`, `H -> T` e come produce il posterior `0,875`?

## Variabili e probabilità

```text
H = ritardo reale
M = segnale nel messaggio
T = tracking fermo

P(H=1) = 0,20
P(M=1|H=1) = 0,80
P(M=1|H=0) = 0,10
P(T=1|H=1) = 0,70
P(T=1|H=0) = 0,20
```

## Fattorizzazione

```text
P(H,M,T) = P(H) P(M|H) P(T|H)
```

## Evidenza

```text
M=1, T=1
numeratore H=1: 0,112
numeratore H=0: 0,016
posterior: 0,875
```

## Layout

- rete e tabelle condizionali a sinistra;
- calcolo a destra;
- prior come annotazione laterale di `H`, non come nodo intermedio;
- frecce dirette da `H` a `M` e `T`;
- footer che dichiara l'indipendenza condizionata come assunzione del modello;
- nessun simbolo non supportato dal font.

## Confine

La figura non attribuisce causalità automatica agli archi e non presenta le probabilità come stime di produzione.

## Provenienza

Valori da `SNIP-KNOW-001`. PNG raster prodotto da `scripts/generate_knowledge_visuals.py`; nessun SVG.
