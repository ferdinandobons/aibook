La sezione successiva può dipendere solo da concetti stabili o stabilizzati. I
concetti differiti possono essere nominati solo come confini.

## Struttura portante universale

Ogni articolo segue questi movimenti. Non sono saggi indipendenti; sono fasi di
una sola esecuzione cumulativa.

1. **Ancora.** Parti dall'ultimo oggetto che il lettore target può ricostruire.
2. **Mostra il gap.** Dimostra una capacità mancante, un fallimento o un vincolo.
3. **Esegui la transizione minima.** Fai una operazione reale su un oggetto.
4. **Nomina e contratta.** Introduci il termine tecnico solo dopo il meccanismo.
5. **Ripeti e scala.** Generalizza un oggetto alla volta.
6. **Formalizza e collega.** Aggiungi shape, formule, codice e varianti solo
   dopo la stabilizzazione del meccanismo concreto.
7. **Ricostruisci e trasferisci.** Ricostruisci il percorso completo e applicalo
   a un caso modificato.

Ogni sezione di meccanismo segue:

```text
ORIENTA -> INTRODUCI -> ESEGUI -> REINTEGRA -> CONTROLLA
```

## Blocco atomico di spiegazione

Usa questo blocco per ogni transizione importante:

```text
Dove siamo:
Problema:
Input e shape:
Trasformazione:
Output e shape:
Cosa è cambiato:
Cosa è rimasto invariato:
Cosa non fa:
Cosa usa l'output dopo:
Esempio minimo:
Errore comune:
Frase di continuità:
```

La frase di continuità deve essere concreta:

```text
Ora che abbiamo ottenuto X, il componente successivo può usare X per fare Y.
```

Se X o Y sono vaghi, la sezione non è pronta.

## Gate di comparsa

Ogni elemento nuovo entra solo dopo che il suo referente concreto è stabile.

### Gate del termine

Un termine tecnico può comparire quando:

1. il lettore ha visto l'oggetto o l'operazione;
2. il testo assegna al termine un significato stabile;
3. le sezioni successive usano lo stesso termine in modo coerente.

Descrivi prima di nominare.

### Gate dell'astrazione

Parole come `rappresentazione`, `contesto`, `significato`, `feature`,
`memoria` ed `efficienza` richiedono un referente concreto:

```text
quali valori
in quale oggetto
prodotti da quale operazione
usati da quale calcolo successivo
```

Non usare un'astrazione come se spiegasse se stessa.

### Gate delle frecce

Le catene con frecce sono riassunti, non prime spiegazioni. Prima di mostrare
`A -> B -> C`, il lettore deve sapere cosa sono A, B e C, cosa significa ogni
freccia e cosa cambia a ogni transizione.

### Gate di simboli e formule

Introduci matematica in questo ordine:

```text
domanda in linguaggio naturale
-> esempio numerico
-> tabella o shape
-> pseudocodice
-> formula
-> derivazione solo se serve
```

Ogni simbolo deve avere prima una quantità concreta visibile. Una formula entra