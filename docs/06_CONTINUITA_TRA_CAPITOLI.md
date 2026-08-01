# Continuità tra capitoli e controllo dei prerequisiti

## Stato

- Stato: `vincolante`
- Ambito: ordine didattico, ponti tra lezioni, prerequisiti, forward reference e concetti differiti
- Registro operativo: `BOOK_PRODUCTION.md` e `PROGRESS.md`
- Ultimo audit: 31 luglio 2026

## 1. Obiettivo

Il libro deve poter essere letto in ordine senza richiedere concetti non ancora costruiti. Un termine può comparire prima del capitolo che lo formalizza soltanto quando il testo ne fornisce una spiegazione locale sufficiente e lo usa come orientamento, non come prerequisito nascosto.

La continuità non richiede che ogni capitolo riassuma il precedente. Richiede che il lettore sappia:

1. quale risultato già acquisito viene riutilizzato;
2. quale capacità manca ancora;
3. perché il nuovo capitolo è il passo successivo;
4. quale oggetto verrà consegnato al capitolo seguente.

## 2. Contratto di ingresso e uscita

Ogni `PLAN.md` registra:

```text
Prerequisiti stabili:
Concetti richiamati ma rispiegati localmente:
Forward reference non necessarie alla comprensione:
Gap che apre il capitolo:
Output consegnato al capitolo successivo:
```

L'apertura del capitolo richiama soltanto i prerequisiti necessari. Il riepilogo dichiara la capacità ottenuta e, quando utile, la domanda rimasta aperta.

## 3. Quattro modi ammessi per introdurre un concetto

### Concetto già stabilizzato

Il capitolo precedente o un prerequisito esplicito lo ha spiegato e verificato. Può essere usato direttamente, con un breve richiamo.

### Spiegazione locale

Il concetto non è ancora formalizzato altrove, ma la lezione fornisce tutto ciò che serve per l'uso corrente. Le proprietà avanzate restano differite.

### Forward reference

Il termine serve a orientare il lettore o a raccontare la storia, ma il ragionamento non dipende dal suo meccanismo. Il testo dichiara che verrà studiato più avanti.

### Concetto nuovo del capitolo

Il capitolo ne costruisce referente, esempio, formula, implementazione e confini. Non può essere presupposto in una sezione precedente dello stesso capitolo.

Un uso che non appartiene a nessuna delle quattro classi è un buco di spiegazione.

## 4. Gate di continuità

Prima di promuovere una candidatura si controlla:

- l'apertura parte da una capacità realmente disponibile;
- nessuna formula richiede simboli mai introdotti;
- nessuna API sostituisce una spiegazione mancante;
- i rimandi storici non vengono usati come dimostrazioni;
- i concetti differiti non diventano prerequisiti impliciti;
- le stesse parole mantengono lo stesso significato tra capitoli;
- esempi, shape e convenzioni che cambiano vengono dichiarati;
- il riepilogo non apre un nuovo meccanismo;
- il ponte al capitolo successivo non anticipa dettagli non necessari;
- gli esercizi non richiedono contenuti futuri senza segnalarlo.

## 5. Matrice di continuità, Capitoli 1-12

| Passaggio | Risultato consegnato | Nuova domanda | Esito |
|---|---|---|---|
| 1 -> 2 | tassonomia di meccanismo, obiettivo e ampiezza | come si sono formati i paradigmi | continuo ed esplicito |
| 2 -> 3 | componenti simbolici, appresi e ibridi | come si costruisce e mantiene un sistema | continuo ed esplicito |
| 3 -> 4 | protocollo, split, deployment e monitoraggio | quando un risultato sostiene un claim | continuo; il caso di valutazione riusa gli stessi split e costi |
| 4 -> 5 | metriche e risultati espressi con numeri | quali strutture matematiche rappresentano dati e modelli | continuo, cambio di parte; il Capitolo 5 riparte da una rappresentazione concreta |
| 5 -> 6 | vettori, matrici, layer e shape | come attribuire la loss ai parametri | continuo ed esplicito |
| 6 -> 7 | sensibilità locale e gradienti | come rappresentare incertezza, campioni e quantità non osservate | continuo; il Capitolo 7 riparte da un caso binario concreto |
| 7 -> 8 | distribuzioni, likelihood e stima | come trasformare previsione e target in una loss | continuo ed esplicito |
| 8 -> 9 | logits, softmax e funzioni obiettivo | come vengono eseguite con precisione finita | continuo ed esplicito |
| 9 -> 10 | contratto matematico, numerico e hardware | come scegliere sequenze di azioni | continuo, nuova parte funzionale e nuovo oggetto concreto |
| 10 -> 11 | stati, transizioni, goal e ricerca | come rappresentare fatti, conseguenze e incertezza | continuo ed esplicito |
| 11 -> 12 | regole e probabilità specificate direttamente | come apprendere una funzione da esempi etichettati | continuo ed esplicito |
| 12 -> 13 | predittore appreso da target esterni | che cosa si può apprendere senza una label esterna per ogni esempio | ponte predisposto |

### Esito dell'audit

Non sono emersi buchi di spiegazione bloccanti nei passaggi 1-12. I cambi di parte 4->5 e 9->10 non richiedono il meccanismo del capitolo precedente per comprendere la nuova apertura, ma devono continuare a partire da oggetti concreti e a dichiarare il nuovo livello di analisi.

## 6. Forward reference controllate

Le seguenti anticipazioni non sono prerequisiti nascosti:

- il Capitolo 1 nomina logits, loss e gradienti con una spiegazione locale; la formalizzazione arriva nei Capitoli 5-8;
- il Capitolo 2 nomina backpropagation, Transformer, scaling e foundation model in funzione storica; i meccanismi vengono trattati nelle parti successive;
- il Capitolo 4 usa il bootstrap come procedura operativa su 24 coppie di predizioni; probabilità, campionamento e intervalli vengono formalizzati nel Capitolo 7;
- il Capitolo 10 nomina policy network e value network come componenti di AlphaGo; reinforcement learning viene costruito nel Capitolo 14.

In ciascun caso il capitolo rimane comprensibile senza conoscere in anticipo la teoria completa del termine.

## 7. Correzioni da riaprire

Una modifica a un capitolo riapre la continuità quando:

- introduce un nuovo prerequisito;
- cambia il significato di un termine condiviso;
- sposta una formula prima del suo referente;
- modifica l'oggetto consegnato al capitolo successivo;
- elimina un ponte necessario;
- aggiunge una variante che presuppone un caso base non ancora trattato.

La review deve allora rileggere almeno il capitolo modificato, quello precedente e quello successivo.
