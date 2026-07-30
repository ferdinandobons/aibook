# Template canonico di un capitolo

## Stato

- Stato: `vincolante`
- Metodo: `EXPLANATION_STYLE_AND_VISUALS.md`
- Struttura in prosa: `19_STRUTTURA_LOGICA_IN_PROSA.md`
- Voce editoriale: `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`
- Review: `18_PROTOCOLLO_QA_DIDATTICO.md`

## 1. Principio

Il template distingue:

1. scaffold interno per pianificazione e review;
2. testo destinato al lettore;
3. artefatti di prova e riproduzione.

Lo scaffold è regolare e analitico. Il capitolo pubblicato è una spiegazione in prosa, con titoli e ritmo adatti al contenuto.

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

## 3. Metadati

I metadati vengono conservati in un commento HTML all'inizio di `CHAPTER.md`, in front matter non renderizzato oppure in un file separato.

Formato consigliato:

```text
<!--
chapter_id:
part_id:
order_key:
title:
slug:
maturity:
status:
version:
opened:
last_web_research:
last_source_check:
freeze_date:
environment:
prerequisites:
deferred:
next_chapter:
-->
```

La versione editoriale non mostra:

- stato della candidatura;
- branch e commit;
- esito degli audit;
- immagini respinte;
- note sulla pull request;
- dettagli operativi non necessari alla comprensione.

## 4. Scaffold interno in `PLAN.md`

Prima della stesura si registra:

```text
Domanda centrale:
Oggetto continuo:
Stato iniziale:
Gap:
Output finale:
Invarianti:
Confini:
Concetti differiti:
Passaggio successivo:
Visuali:
Snippet:
```

Per ogni transizione portante:

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
Consumer successivo:
Esempio o prova:
Errore comune:
Giunzione:
```

Lo scaffold non determina i titoli visibili.

## 5. Struttura destinata al lettore

Il capitolo usa soltanto le sezioni necessarie al proprio profilo.

Un possibile percorso è:

```text
Titolo
Apertura concreta
Problema
Meccanismo o argomento costruito per passaggi
Esempio continuo
Formalizzazione
Codice o esperimento
Varianti e confini pertinenti
Riepilogo
Controlli ed esercizi
Riferimenti e materiali verificabili
```

Non esiste una sequenza obbligatoria identica per tutti i capitoli.

Come riferimento editoriale, un capitolo tecnico ordinario usa spesso da cinque a dieci sezioni principali. Il numero può cambiare, ma ogni titolo deve corrispondere a una domanda o a un movimento concettuale reale.

## 6. Apertura

L'apertura rende chiari, in prosa:

- il punto da cui si parte;
- il problema concreto;
- perché il problema conta;
- ciò che il lettore saprà fare;
- il confine del capitolo.

Una bussola schematica può restare in `PLAN.md`. Nel corpo compare soltanto se migliora la lettura.

## 7. Titoli e gerarchia

Il titolo del capitolo usa `#`.

Le sezioni principali usano `##`.

Le sottosezioni usano `###` soltanto quando la gerarchia è reale. Non si usa `#` per ogni sezione interna.

Titoli adatti:

```text
Una stessa richiesta, sistemi diversi
Quando il comportamento viene appreso
Il calcolo completo su una query
Escludere le posizioni future
Dalla formula a PyTorch
```

Titoli da non usare come telaio ricorrente:

```text
Dove siamo
Problema locale
Trasformazione
Cosa è cambiato
Cosa non fa
Frase di continuità
Contratto dello snippet
```

## 8. Paragrafi

Ogni paragrafo ha una relazione dominante, ma può collegare stato, problema, passaggio, conseguenza e limite.

Il reviewer deve poter ricostruire lo scaffold; il lettore deve incontrare un ragionamento.

Le sezioni non vengono spezzate per ogni operazione elementare. Più passaggi brevi possono vivere nella stessa sezione quando appartengono allo stesso movimento.

## 9. Ordine di introduzione

Quando pertinente:

```text
domanda concreta
-> esempio osservabile
-> valori e shape
-> algoritmo o pseudocodice
-> formula generale
-> derivazione
-> implementazione
-> varianti
```

Il pseudocodice può essere omesso quando non chiarisce un processo sequenziale. La decisione viene registrata in `PLAN.md`.

## 10. Visuali

Ogni visuale possiede:

```text
FIG-ID
SPEC.md
AUDIT.md
ALT_TEXT.md
candidate-vN.png o final.png
```

Nel capitolo la prosa:

1. introduce la domanda;
2. attraversa gli elementi;
3. esplicita il risultato.

Le etichette editoriali non sono obbligatorie.

Una visuale mancante o respinta viene registrata negli audit. Il capitolo destinato al lettore non descrive i fallimenti del processo di generazione.

## 11. Codice

Prima di uno snippet, la prosa chiarisce input, operazione centrale e controllo atteso.

Il corpo mostra soltanto il frammento utile alla spiegazione. Il contratto completo resta in `code/README.md` e `code/CODE_AUDIT.md`.

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

I dettagli di ambiente e tolleranza non interrompono il discorso, salvo che siano essenziali per interpretare il risultato.

## 12. Matematica, shape e invarianti

Le formule entrano dopo i referenti concreti.

Shape, condizioni e invarianti vengono dichiarati nel punto in cui servono, in prosa, tabella o box tecnico. La forma editoriale può variare; la precisione no.

## 13. Varianti e confini

Una variante entra dopo il caso base e dichiara:

- collo di bottiglia;
- modifica;
- comportamento invariato;
- nuovo costo;
- trade-off;
- fonte e versione.

Un concetto rinviato viene mantenuto come ponte breve o riferimento incrociato.

## 14. Riepilogo

La conclusione riprende il problema iniziale e ricompone il percorso. Non si limita a elencare i nomi delle operazioni.

Il lettore deve poter:

- ricostruire;
- localizzare;
- delimitare;
- trasferire;
- prevedere una variazione.

## 15. Controlli ed esercizi

I controlli di comprensione possono mantenere titoli come:

- Ricostruzione;
- Localizzazione;
- Confine;
- Trasferimento;
- Variazione.

Gli esercizi richiedono soltanto conoscenze costruite nel capitolo o dichiarate come prerequisiti.

## 16. Riferimenti e materiali

Il capitolo chiude con una sezione breve che rinvia a:

- fonti primarie;
- documentazione ufficiale;
- codice e test;
- output e ambiente;
- letture complementari separate.

Registri di approvazione, audit completi e storia delle versioni non fanno parte del testo destinato al lettore.

## 17. Audit

`TEXT_AUDIT.md` registra:

- audit fattuale;
- audit matematico;
- audit algoritmico;
- audit temporale;
- audit incrociato;
- review strutturale;
- gate anti-template;
- review editoriale e linguistica;
- lettura ad alta voce;
- revisione autoriale.

## 18. Gate finale

Un capitolo non passa a revisione autoriale soltanto perché contiene tutti gli artefatti. Deve:

- essere corretto;
- risultare continuo;
- usare un italiano naturale;
- mantenere l'esempio;
- separare manuale e materiali operativi;
- superare una nuova lettura completa dopo le correzioni.
