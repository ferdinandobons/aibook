# Struttura logica implicita nella prosa

## Stato

- Stato: `vincolante`
- Data di adozione: 30 luglio 2026
- Ambito: tutti i capitoli, le lezioni e le appendici destinate al lettore
- Documenti collegati: `EXPLANATION_STYLE_AND_VISUALS.md`, `01_TEMPLATE_CAPITOLO.md`, `18_PROTOCOLLO_QA_DIDATTICO.md`

## 1. Principio

La struttura logica del metodo è obbligatoria. Le sue etichette non devono però diventare la struttura visibile e ripetitiva di ogni lezione.

Campi come:

```text
Dove siamo
Problema
Input e shape
Trasformazione
Output e shape
Cosa è cambiato
Cosa è rimasto invariato
Cosa non fa
Cosa usa l'output dopo
Errore comune
Frase di continuità
```

sono uno strumento di progettazione e di review. Per impostazione predefinita non diventano titoli o sottotitoli pubblicati nel capitolo.

Il lettore deve percepire una spiegazione naturale, non il modulo usato dall'autore per controllarla.

## 2. Due livelli distinti

### Livello interno

`PLAN.md`, `TEXT_AUDIT.md` e le schede di progettazione rendono espliciti:

- stato del lettore;
- problema locale;
- input e output;
- trasformazione;
- cambiamento;
- invariante;
- confine;
- consumer successivo;
- concetti differiti.

Questi campi devono poter essere controllati uno per uno.

### Livello destinato al lettore

`CHAPTER.md` usa:

- titoli semantici legati al contenuto;
- paragrafi causali;
- formule e tabelle nel punto in cui servono;
- transizioni naturali;
- box soltanto quando aggiungono valore reale.

Il testo integra le funzioni del blocco atomico senza annunciarle con etichette standard ripetute.

## 3. Titoli ammessi

I titoli devono dire quale oggetto o meccanismo viene esaminato.

Esempi corretti:

```text
Perché una combinazione fissa non basta
Dal confronto ai coefficienti
Combinare i vettori sorgente
Escludere le posizioni future
Dalla formula all'implementazione PyTorch
```

Esempi da evitare come struttura ricorrente del testo pubblicato:

```text
Dove siamo
Problema locale
Trasformazione
Cosa è cambiato
Cosa è rimasto invariato
Cosa non fa
Frase di continuità
Stato del lettore
Contratto dello snippet
```

Una di queste etichette può comparire eccezionalmente in un box o in una tabella quando è davvero la forma più chiara. Non può diventare il telaio standard di tutte le sezioni.

## 4. Come incorporare il blocco atomico nella prosa

Una transizione completa può essere scritta in uno o più paragrafi naturali.

Esempio:

```text
Abbiamo ora tre score, uno per ogni key. I valori hanno la shape corretta, ma non sono ancora coefficienti confrontabili: possono essere negativi e non sommano a 1. Applichiamo quindi la softmax lungo le tre posizioni sorgente. Otteniamo tre coefficienti non negativi, associati alle stesse righe di K e V, la cui somma è 1. Le value non sono ancora state combinate; il passaggio successivo userà questi coefficienti per costruire l'output.
```

In questo paragrafo sono presenti, senza etichette visibili:

- stato corrente;
- problema;
- trasformazione;
- output;
- invariante;
- ciò che resta da fare;
- continuità con il passaggio successivo.

## 5. Variabilità editoriale

I capitoli non devono sembrare prodotti da un unico stampo.

La struttura visibile può cambiare in funzione del profilo:

- un componente può seguire il flusso dei dati;
- un processo può seguire gli stati;
- un'architettura può seguire moduli e interfacce;
- un metodo di training può seguire segnale, loss, gradiente e update;
- un confronto può seguire una differenza controllata;
- un paper può seguire domanda, proposta, setup, risultati e limiti.

La logica interna resta verificabile, ma il ritmo, i titoli e la disposizione della prosa si adattano al soggetto.

## 6. Shape, invarianti e confini

Shape, invarianti e confini non devono essere nascosti al punto da diventare ambigui. Devono essere espliciti nel significato, non necessariamente nel titolo.

Forme consigliate:

```text
Il vettore mantiene shape [S]: cambia la magnitudine degli score, non il numero di posizioni.
```

```text
La mask interviene sugli score prima della softmax. Le righe di V restano invariate.
```

```text
Questa operazione combina le value disponibili; non introduce informazione esterna.
```

## 7. Transizioni naturali

La frase di continuità resta obbligatoria come funzione logica, ma non richiede l'intestazione `Frase di continuità` né la formula identica `Ora che...` in ogni sezione.

Sono ammesse formulazioni diverse, purché nominino l'oggetto ottenuto e il passo successivo:

```text
I tre score sono ora disponibili. Prima di normalizzarli dobbiamo controllarne la scala.
```

```text
I coefficienti risultanti sono associati alle stesse tre value. Possiamo quindi usarli per costruire il vettore di output.
```

```text
Il caso numerico è completo; la stessa sequenza di operazioni può ora essere espressa in forma matriciale.
```

## 8. Codice e visuali

Prima di uno snippet, input, operazione centrale e controllo atteso possono essere spiegati in prosa. Non è obbligatorio pubblicare un box denominato `Contratto dello snippet`.

Una figura viene inquadrata, ispezionata e conclusa nel testo vicino. Anche in questo caso non sono obbligatorie le etichette `Domanda della figura` o `Conclusione della figura`, purché le tre funzioni siano chiaramente presenti.

## 9. Gate anti-template

La review didattica respinge un capitolo quando:

- ripete sistematicamente le stesse intestazioni metacognitive;
- espone il foglio di progettazione al posto di una spiegazione fluida;
- spezza un meccanismo semplice in troppe microsezioni;
- usa elenchi e box dove una sequenza di paragrafi sarebbe più leggibile;
- rende ogni capitolo formalmente identico anche quando il profilo è diverso;
- nasconde invece informazioni necessarie come shape, invarianti o confini.

La correzione non consiste nel rimuovere la logica. Consiste nel trasferire la logica dalla superficie editoriale alla costruzione della prosa.

## 10. Regola di approvazione

Un capitolo può essere approvato soltanto quando entrambe le condizioni sono vere:

1. il reviewer può ricostruire tutti i campi del blocco atomico leggendo il testo;
2. il lettore non è costretto a vedere gli stessi campi come una sequenza rigida di titoli ripetuti.

La conformità viene registrata in `TEXT_AUDIT.md`.