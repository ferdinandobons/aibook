# Template canonico di un capitolo

## Stato

- Stato: `vincolante`
- Metodo: `EXPLANATION_STYLE_AND_VISUALS.md`
- Regola di superficie: `19_STRUTTURA_LOGICA_IN_PROSA.md`
- Review didattica: `18_PROTOCOLLO_QA_DIDATTICO.md`

## 1. Principio del template

Il template distingue due artefatti:

1. lo scaffold interno usato per pianificare e revisionare;
2. il capitolo destinato al lettore.

Lo scaffold interno è regolare e analitico. Il capitolo pubblicato è una spiegazione in prosa con titoli semantici adatti al contenuto.

Non si copiano nel testo, come struttura ripetitiva, le etichette `Dove siamo`, `Problema`, `Trasformazione`, `Cosa è cambiato`, `Cosa è rimasto invariato`, `Cosa non fa` o `Frase di continuità`.

## 2. File obbligatori

```text
chapters/<slug>/
  PLAN.md
  CHAPTER.md
  FONTI_PRIMARIE.md
  CLAIMS.md
  TEXT_AUDIT.md
  CHANGELOG.md
  REVIEW.md
  code/
  assets/
```

## 3. Metadati del capitolo

`CHAPTER.md` o il front matter associato registra:

```text
chapter_id:
part_id:
order_key:
titolo:
slug:
maturità:
stato editoriale:
data di apertura:
data ultima ricerca web:
data ultima verifica fonti:
data di congelamento:
versione Python:
versione delle librerie:
device e dtype:
prerequisiti:
concetti differiti:
capitolo o consumer successivo:
```

I dettagli operativi non devono interrompere la lettura della lezione nella versione editoriale finale.

## 4. Scaffold interno in `PLAN.md`

Prima della stesura si registra:

```text
Domanda centrale:
Oggetto continuo:
Stato iniziale:
Gap:
Output finale:
Invarianti principali:
Confini:
Concetti differiti:
Consumer successivo:
Visuali previste:
Snippet previsti:
```

Per ogni transizione portante si compila internamente:

```text
Ultima affermazione stabile:
Oggetto corrente:
Un concetto nuovo:
Input e shape:
Operazione:
Output e shape:
Cosa cambia:
Cosa resta invariato:
Cosa non fa:
Cosa userà l'output:
Esempio o prova:
Errore comune:
Giunzione con il passaggio successivo:
```

Questa scheda non determina i titoli visibili del capitolo.

## 5. Struttura destinata al lettore

Il capitolo usa soltanto le sezioni necessarie al proprio profilo. Un possibile percorso è:

```text
Titolo
Orientamento iniziale in prosa
Problema concreto
Meccanismo costruito per passaggi
Esempio continuo
Pseudocodice, quando utile
Formalizzazione
Implementazione
Varianti o confini pertinenti
Ricostruzione
Controlli ed esercizi
Fonti e artefatti
```

I titoli sono semantici. Devono nominare il contenuto reale, per esempio:

```text
Perché una combinazione fissa non basta
Dal confronto ai coefficienti
Escludere le posizioni future
Dalla formula all'implementazione
```

Non esiste una sequenza obbligatoria di trenta intestazioni uguale per ogni capitolo.

## 6. Orientamento iniziale

L'apertura deve rendere chiari, in uno o più paragrafi naturali:

- il punto da cui si parte;
- la capacità mancante;
- ciò che il lettore saprà ricostruire alla fine;
- il confine del capitolo.

Una bussola schematica può essere conservata in `PLAN.md`. Nel testo pubblico viene usata soltanto quando migliora davvero la comprensione.

## 7. Transizioni nella prosa

Ogni passaggio deve contenere le funzioni del blocco atomico, ma le integra in frasi e paragrafi.

Esempio:

```text
I tre prodotti scalari forniscono uno score per ogni key. Il vettore risultante ha shape [S], mentre V non è ancora coinvolta. Gli score non sono coefficienti normalizzati: possono essere negativi e non sommano a 1. Prima della softmax, il passaggio successivo ne controlla la scala.
```

Il reviewer deve poter ricostruire stato, output, invariante, confine e continuità. Il lettore non deve vedere un modulo compilato.

## 8. Ordine di introduzione

Quando pertinente, l'ordine è:

```text
domanda concreta
-> oggetto o esempio osservabile
-> valori e shape
-> algoritmo o pseudocodice
-> formula generale
-> derivazione necessaria
-> implementazione verificata
-> varianti e ottimizzazioni
```

Il pseudocodice può essere omesso quando non esiste un algoritmo sequenziale utile da esplicitare. L'omissione deve essere motivata nel piano.

## 9. Visuali

Ogni visuale inclusa possiede:

```text
FIG-ID
SPEC.md
AUDIT.md
ALT_TEXT.md
candidate-vN.png o final.png
```

Nel capitolo la prosa:

1. introduce la domanda della figura;
2. attraversa gli elementi nell'ordine di lettura;
3. esplicita il risultato e il passaggio successivo.

Le etichette `Domanda della figura` e `Conclusione della figura` non sono obbligatorie nella superficie pubblicata.

## 10. Codice

Prima di ogni snippet, la prosa identifica naturalmente:

- l'input già noto;
- le righe che implementano l'operazione centrale;
- l'output o l'invariante da controllare.

Il contratto completo dello snippet resta in `code/README.md` e `code/CODE_AUDIT.md`. Nel corpo non è obbligatorio pubblicare una sezione intitolata `Contratto dello snippet`.

Ogni snippet registra:

```text
ID
file
ambiente
versioni
device
dtype
seed
comando
output
test
stato audit
```

## 11. Matematica, shape e invarianti

Le formule entrano dopo i referenti concreti. Shape, condizioni e invarianti vengono dichiarati nel punto in cui servono, in prosa, tabella o box tecnico.

La forma editoriale può variare. Non può variare la precisione.

## 12. Varianti e confini

Una variante entra dopo il caso base e dichiara:

- collo di bottiglia;
- modifica;
- comportamento invariato;
- costo nuovo;
- trade-off;
- fonte e versione.

Un concetto rinviato viene mantenuto come ponte breve o riferimento incrociato. Non viene spiegato a metà per riempire una sezione standard.

## 13. Ricostruzione e controlli

La conclusione permette al lettore di:

- ricostruire il flusso;
- localizzare il meccanismo;
- indicarne il confine;
- trasferirlo a un nuovo input;
- prevedere una variazione.

I titoli di questi controlli possono essere mantenuti perché descrivono azioni distinte richieste al lettore.

## 14. Fonti e artefatti

Il capitolo chiude con le sezioni pertinenti tra:

- fonti primarie;
- documentazione ufficiale;
- repository e standard;
- artefatti di riproduzione;
- letture complementari separate.

## 15. Audit

`TEXT_AUDIT.md` registra almeno:

- audit fattuale;
- audit matematico;
- audit algoritmico;
- audit temporale;
- audit incrociato;
- una o più review didattiche complete;
- controllo anti-template secondo `19_STRUTTURA_LOGICA_IN_PROSA.md`;
- esito autoriale.

Un capitolo non passa a revisione autoriale soltanto perché contiene tutte le etichette del vecchio template. Deve mostrare una prosa naturale e permettere al reviewer di ricostruire la logica sottostante.

## 16. Registro finale

```text
Review fattuale:
Review matematica:
Review architetturale e algoritmica:
Review temporale:
Review codice:
Review visuale:
Review incrociata:
Review didattica:
Review anti-template:
Review autoriale:
Data di congelamento:
Commit congelato:
Problemi non bloccanti:
Sezioni rinviate:
```