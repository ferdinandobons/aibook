# Protocollo di conformità didattica ed editoriale

## Stato

- Stato: `vincolante`
- Ambito: ogni capitolo, lezione, appendice tecnica e revisione sostanziale
- Metodo: `EXPLANATION_STYLE_AND_VISUALS.md`
- Superficie in prosa: `19_STRUTTURA_LOGICA_IN_PROSA.md`
- Voce editoriale: `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`
- Registro: `chapters/<capitolo>/TEXT_AUDIT.md`

## 1. Scopo

Un capitolo deve essere corretto nei fatti, nella sequenza didattica e nella forma editoriale.

La logica di stato, problema, trasformazione, output, invariante e confine è obbligatoria. Le relative etichette non sono obbligatorie nel testo pubblicato. Il reviewer controlla ciò che il lettore può capire, non il numero di campi nominalmente presenti.

Un capitolo viene respinto quando:

- introduce termini prima dei referenti;
- salta passaggi necessari;
- accumula concetti diversi nella stessa transizione;
- anticipa formule, codice o varianti;
- rende impliciti shape o confini necessari;
- espone lo scaffold come struttura ripetitiva;
- frammenta il testo in microsezioni;
- suona come una specifica o una reference;
- non permette ricostruzione e trasferimento.

## 2. Review iterative

Ogni capitolo riceve almeno tre letture distinte:

1. **Review strutturale e didattica**, dedicata a oggetto continuo, gate e sequenza.
2. **Review anti-template e ricostruibilità**, dedicata alla superficie editoriale e alla coerenza globale.
3. **Review editoriale e linguistica**, dedicata a fluidità, italiano idiomatico e leggibilità da manuale.

Quando emerge un difetto bloccante:

1. il capitolo torna allo stato `revisione didattica` o `revisione editoriale`;
2. il difetto viene registrato;
3. vengono corretti tutti gli artefatti coinvolti;
4. si ripete l'intera review interessata;
5. si esegue comunque una nuova lettura completa.

Una modifica successiva a ordine, terminologia, esempio, formula, visuale, codice, confine, titoli o voce riapre i gate pertinenti.

## 3. Indipendenza del reviewer

La review viene svolta come se il reviewer non conoscesse il piano dell'autore.

Il capitolo deve funzionare usando soltanto:

- prerequisiti dichiarati;
- contenuto già stabilizzato;
- testo, figure e codice richiamato.

`PLAN.md` non può compensare una giunzione mancante nella prosa.

## 4. Scaffold interno

In `PLAN.md` e `TEXT_AUDIT.md` devono essere ricostruibili:

```text
Ultima affermazione stabile
Oggetto corrente
Un concetto nuovo
Input e shape
Operazione
Output e shape
Cosa cambia
Cosa resta invariato
Cosa non fa
Consumer successivo
Esempio o prova
Errore comune
Giunzione
```

`CHAPTER.md` integra queste funzioni senza ripetere le etichette.

## 5. Review 1. Struttura e gate

### Oggetto continuo

Registrare:

```text
Oggetto iniziale:
Stato dopo ogni sezione:
Output finale:
Passaggio successivo:
```

Lo stesso oggetto deve attraversare il capitolo. Un cambio di esempio o notazione richiede una ragione didattica.

### Catena causale

Verificare:

1. stato iniziale;
2. problema;
3. motivo della nuova operazione;
4. trasformazione concreta;
5. risultato;
6. invariante;
7. elemento differito.

### Gate di comparsa

Controllare:

- termine tecnico dopo il referente;
- astrazione accompagnata da oggetto e operazione;
- frecce dopo la spiegazione dei nodi;
- esempio e shape prima della formula;
- pseudocodice prima della formula quando chiarisce un algoritmo;
- codice dopo il meccanismo;
- varianti dopo il caso base.

### Trasformazione dominante

Ogni paragrafo deve avere una trasformazione o una relazione principale. Più passaggi brevi possono stare nella stessa sezione se formano un unico movimento concettuale.

La sezione viene divisa quando combina:

- meccanismo matematico e dettagli API;
- caso base e ottimizzazione hardware;
- formula e benchmark;
- variante e failure mode indipendente;
- più oggetti che richiedono prerequisiti diversi.

### Visuali e codice

Ogni figura viene introdotta, attraversata e conclusa nella prosa.

Prima di uno snippet devono risultare chiari:

- input;
- operazione centrale;
- output o invariante.

### Confini

Un concetto differito può essere nominato per localizzare ciò che segue, ma non viene spiegato a metà.

## 6. Review 2. Superficie editoriale e ricostruibilità

Il reviewer rilegge il capitolo senza consultare il piano.

Controlla:

- titoli semantici;
- sezioni abbastanza ampie;
- assenza di intestazioni metacognitive ripetute;
- continuità tra paragrafi;
- shape e invarianti ancora visibili;
- esempio continuo presente durante le astrazioni;
- riepilogo che ricompone il problema;
- esercizi coerenti con ciò che è stato costruito;
- coerenza tra prosa, formule, visuali e codice.

Sono difetti bloccanti:

- capitolo che appare come una checklist;
- molte microsezioni di uno o due paragrafi;
- un titolo per ogni operazione elementare;
- metadati operativi nel flusso di lettura;
- spiegazione dominata da box e liste;
- codice o note API che cambiano il capitolo in una reference.

## 7. Review 3. Voce e lingua italiana

Si applica `20_VOCE_EDITORIALE_E_REVISIONE_LINGUISTICA.md`.

Il reviewer controlla:

- italiano naturale;
- sintassi non tradotta dall'inglese;
- uso necessario e coerente dei termini tecnici;
- assenza di calchi e ibridi evitabili;
- ritmo variato;
- frasi non troppo uniformi;
- periodi non sovraccarichi;
- soggetti e referenti chiari;
- cautele non ripetute;
- citazioni che non spezzano il ragionamento;
- separazione tra testo pubblico e materiali di progetto.

Il capitolo viene letto ad alta voce. Vengono segnati i punti in cui:

- il periodo è difficile da pronunciare;
- il referente si perde;
- il registro cambia bruscamente;
- la frase suona burocratica;
- il lettore deve tornare indietro per capire l'operazione.

La review simula almeno un lettore nuovo, un lettore tecnico e un lettore che riprende il capitolo dopo tempo.

## 8. Controlli finali

Il capitolo deve permettere:

- **ricostruzione**, ripetere il flusso;
- **localizzazione**, indicare dove avviene un'operazione;
- **confine**, dire cosa non viene concluso;
- **trasferimento**, applicare il meccanismo a un nuovo caso;
- **variazione**, prevedere l'effetto di una modifica.

## 9. Registro in `TEXT_AUDIT.md`

Ogni review registra:

```text
Review ID:
Versione esaminata:
Data:
Profilo del lettore:
Ambito:
Difetti bloccanti:
Difetti non bloccanti:
Correzioni applicate:
Artefatti riaperti:
Esito:
Reviewer:
```

Stati ammessi:

- `non eseguita`;
- `in corso`;
- `respinta`;
- `corretta, nuova review richiesta`;
- `superata`.

## 10. Difetti bloccanti

Il capitolo viene respinto in presenza di:

- oggetto continuo interrotto;
- dipendenza da un concetto non stabilizzato;
- termine o formula anticipati;
- codice prima del meccanismo;
- variante prima del caso base;
- invariante necessario implicito;
- visuale non integrata;
- contraddizione tra artefatti;
- semplificazione falsa;
- scaffold pubblicato come telaio;
- frammentazione eccessiva;
- metadati di progetto esposti;
- italiano non fluido in più passaggi;
- calchi non necessari;
- ritmo meccanico;
- ripetizione eccessiva di negazioni e cautele;
- riepilogo ridotto a checklist;
- lettura ad alta voce non superata.

## 11. Gate di approvazione

Un capitolo passa alla revisione autoriale soltanto quando:

- i claim portanti sono verificati;
- la review strutturale è superata;
- il gate anti-template è superato;
- la review editoriale e linguistica è superata;
- ogni difetto bloccante è stato corretto;
- dopo le correzioni è stata eseguita una nuova lettura integrale;
- testo, figure e codice seguono lo stesso percorso;
- i materiali operativi non interrompono la lezione.

Ogni modifica strutturale o linguistica successiva riapre il gate.

## 12. Applicazione retroattiva

Il protocollo si applica:

- a tutti i capitoli futuri;
- ai capitoli modificati in modo sostanziale;
- ai capitoli esistenti prima di una nuova edizione;
- alle sezioni aggiunte per nuove tecniche.

La conformità non deriva dal rispetto nominale del template. Deriva dalla qualità del testo che il lettore incontra.
