# Specifica visuale `EVAL-02`

## Identità

- Capitolo: `CH-P01-CRITICAL-EVALUATION`
- Sezione: media, slice, costo e variabilità
- Famiglia: confronto quantitativo
- Orientamento: orizzontale
- File candidato: `candidate-v1.png`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Perché il modello con accuratezza media maggiore non è automaticamente quello preferibile nel caso d'uso?

## Pannello sinistro

Confronto A/B su:

- accuratezza complessiva: `0,792` e `0,833`;
- slice standard: `0,750` e `0,938`;
- slice urgente: `0,875` e `0,625`;
- somma pesata degli errori: `8,0` e `13,0`.

## Pannello destro

- asse della differenza `accuracy(B) - accuracy(A)`;
- differenza osservata `+0,042`;
- intervallo bootstrap percentile 95% `[-0,208, +0,292]`;
- linea verticale in zero;
- nota: l'intervallo include zero, non dimostra equivalenza e non cancella il risultato sulla slice urgente.

## Invariante e confine

I due modelli vengono confrontati sugli stessi 24 casi illustrativi. Pesi, dati e intervallo non rappresentano un prodotto reale e non vanno generalizzati fuori dall'esempio.

## Contenimento

- barre e valori allineati;
- zero visibile e distinto dal punto osservato;
- nessuna cifra fuori dal pannello;
- footer separato dai grafici;
- colore affiancato dalle label A/B e dai valori.
- domanda principale: Quale confronto o limite chiarisce «La domanda viene prima della metrica»?

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
