# Politica delle fonti, delle citazioni e della verifica temporale

## Scopo

Il libro deve permettere di risalire da ogni affermazione portante alla prova che la sostiene. Una frase plausibile, diffusa o coerente con la letteratura non è considerata verificata finché non viene controllata nel contenuto originale di una fonte ammessa.

La ricerca web serve a individuare e consultare fonti primarie e documentazione ufficiale. Non sostituisce il controllo della fonte originale.

## Principio di non inferenza

La versione approvata non contiene affermazioni fattuali ottenute per inferenza editoriale.

Sono esclusi, salvo che vengano attribuiti esplicitamente a una fonte che li formula:

- interpretazioni causali non dimostrate;
- generalizzazioni da un singolo modello a una famiglia;
- attribuzioni di intenzione agli autori;
- conclusioni architetturali ricavate da indizi incompleti;
- stime di prestazioni o costi non misurate;
- descrizioni di implementazione non documentate;
- previsioni sullo sviluppo futuro presentate come fatti.

Quando una fonte non stabilisce un punto, il testo usa soltanto ciò che è verificabile oppure omette l'affermazione.

Le derivazioni matematiche non sono considerate inferenze editoriali quando partono da definizioni verificate, esplicitano tutti i passaggi necessari e vengono ricontrollate.

## Gerarchia delle fonti

### Livello 1. Fonte primaria pubblicata

- atti ufficiali di conferenze;
- riviste scientifiche;
- standard pubblicati;
- documenti istituzionali e normativi.

È la fonte preferita per metodi, risultati, definizioni e norme.

### Livello 2. Fonte ufficiale degli autori

- versione ufficiale su arXiv;
- technical report dell'organizzazione responsabile;
- model card, system card o data card ufficiale;
- supplemento tecnico degli autori.

Si registra la versione o revisione esatta.

### Livello 3. Documentazione ufficiale

- documentazione PyTorch, JAX, CUDA o di altre librerie;
- specifiche delle API;
- note di rilascio;
- guide ufficiali del framework.

È la fonte preferita per firme API, comportamento documentato, versioni supportate e semantica corrente.

### Livello 4. Repository ufficiale

- repository degli autori;
- repository dell'organizzazione;
- codice di riferimento;
- test ufficiali;
- file di configurazione e commit.

Il repository viene usato per verificare implementazioni concrete. Un comportamento del codice non viene automaticamente attribuito al paper se il paper non lo descrive.

### Livello 5. Fonti secondarie

Blog, articoli divulgativi, post, video e discussioni possono aiutare a individuare una fonte primaria o a comprendere l'esistenza di un dibattito. Non sostengono da soli:

- una spiegazione portante;
- una formula;
- un dato quantitativo;
- una descrizione architetturale;
- una firma API;
- un'affermazione normativa.

## Fonte adeguata al tipo di affermazione

| Affermazione | Fonte preferita |
|---|---|
| Definizione di un metodo | Paper originale o standard |
| Risultato sperimentale | Tabella o sezione del paper, con setup |
| Architettura di un modello | Technical report, model card o repository ufficiale |
| Comportamento di un'API | Documentazione ufficiale della versione dichiarata |
| Dettaglio di implementazione | Repository ufficiale e commit |
| Requisito legale o normativo | Testo ufficiale dell'ente competente |
| Valore ottenuto nel libro | Script eseguito, log, ambiente e test |
| Esempio didattico | Etichetta `Illustrativo` e verifica interna |

## Dossier delle fonti

Ogni capitolo contiene `FONTI_PRIMARIE.md` con, per ogni voce:

```text
ID fonte:
Titolo:
Autori o organizzazione:
Tipo:
Data:
Versione, revisione o commit:
Identificatore o URL:
Data di consultazione:
Sezioni rilevanti:
Affermazioni sostenibili:
Limiti:
Divergenze note:
```

Una fonte non viene citata genericamente per sostenere un'intera sezione quando soltanto una sua parte è pertinente.

## Registro delle affermazioni

Ogni affermazione portante viene collegata a una o più fonti in `CLAIMS.md`.

Il controllo deve rispondere a queste domande:

1. La fonte formula davvero l'affermazione?
2. La formulazione del libro è più forte della fonte?
3. Sono state mantenute condizioni e limitazioni?
4. La fonte descrive un metodo, un'implementazione o un singolo esperimento?
5. Esistono versioni successive o errata?
6. La data e la versione sono ancora pertinenti?
7. Un'altra fonte primaria affidabile contraddice o qualifica il punto?

## Citazioni nel testo

La forma predefinita è una citazione breve, collocata vicino all'affermazione:

```text
[Vaswani et al., 2017, §3.2.1]
[PyTorch Docs, scaled_dot_product_attention, versione X.Y, consultato il GG-MM-AAAA]
[Nome del report, revisione o data, sezione N]
```

Quando il documento ha pagine stabili, si usa la pagina. Quando ha sezioni stabili, si usa la sezione. Per codice e repository si registra il commit quando il dettaglio dipende dall'implementazione.

## Bibliografia del capitolo

La bibliografia finale viene separata in:

1. fonti primarie;
2. documentazione ufficiale;
3. repository e artefatti di riproduzione;
4. standard o documenti istituzionali;
5. letture complementari, esplicitamente non usate come prova portante.

## Dati quantitativi

Un numero misurato deve indicare, in misura adeguata al contesto:

- modello e checkpoint;
- dataset o benchmark;
- split;
- metrica;
- harness o implementazione;
- prompt o protocollo;
- hardware;
- dtype;
- batch size o altri parametri rilevanti;
- data;
- fonte o comando di riproduzione.

Un numero privo di setup non viene presentato come confronto conclusivo.

## Risultati riprodotti

Un risultato del progetto può essere etichettato `Eseguito` soltanto quando sono disponibili:

- codice;
- ambiente;
- versioni;
- comando;
- input;
- output;
- test o controllo indipendente;
- data di esecuzione.

Un risultato illustrativo non viene descritto come misurato.

## Verifica temporale

Ogni capitolo registra:

- data dell'ultima ricerca;
- data dell'ultima verifica delle fonti;
- data di congelamento editoriale;
- versioni delle documentazioni consultate;
- revisioni dei paper;
- release o commit rilevanti.

Le informazioni recenti vengono ricontrollate immediatamente prima dell'approvazione. Il capitolo non pretende aggiornamento oltre la data di congelamento.

## Ricerca di contenuti nuovi

Per modelli, librerie, benchmark, leggi, standard e prodotti recenti:

1. si esegue una nuova ricerca web;
2. si identifica la fonte ufficiale corrente;
3. si controlla l'eventuale cronologia delle revisioni;
4. si registra la data;
5. si aggiorna il dossier;
6. si ricontrollano le frasi già scritte.

La memoria del modello non viene usata come fonte per dettagli suscettibili di cambiamento.

## Divergenze tra fonti

Quando fonti primarie affidabili differiscono:

- la divergenza viene registrata;
- non si forza una sintesi non sostenuta;
- si distingue il livello della differenza, per esempio definizione, setup, implementazione o versione;
- il testo presenta separatamente le posizioni verificabili;
- si evita una conclusione se le fonti non la permettono.

## Paper, documentazione e implementazione

Questi livelli non sono intercambiabili:

- il paper descrive il metodo e il setup pubblicato;
- il technical report può descrivere una versione specifica del sistema;
- la documentazione descrive un contratto supportato;
- il repository descrive un'implementazione concreta;
- il prodotto può aggiungere comportamento non documentato nel paper.

Il capitolo deve indicare quale livello sta descrivendo.

## Citazioni di codice e API

Per ogni API si registra:

- nome completo;
- firma verificata;
- versione della libreria;
- pagina ufficiale;
- note di versione rilevanti;
- eventuali differenze tra CPU, CUDA o backend.

Nessuna firma API viene scritta sulla base della memoria.

## Contenuto non verificabile

Quando un'informazione non può essere verificata direttamente:

- non viene presentata come fatto;
- non viene resa plausibile tramite formulazioni vaghe;
- non viene sostenuta da una fonte secondaria debole;
- viene omessa oppure registrata come problema aperto fuori dal testo approvato.

## Gate di approvazione delle fonti

Un capitolo non può essere approvato finché:

- tutte le affermazioni portanti hanno una prova;
- tutte le citazioni sono state aperte e controllate nel contesto originale;
- i dettagli recenti sono stati ricontrollati;
- i dati quantitativi hanno una provenienza completa;
- le divergenze sono registrate;
- non rimangono inferenze fattuali presentate come contenuto del libro;
- bibliografia e registro delle affermazioni coincidono con il testo finale.