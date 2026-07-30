# Registro consolidato delle decisioni

## Funzione

Questo documento registra le decisioni esplicite che governano il progetto. Ogni nuova decisione deve essere aggiunta qui e propagata ai documenti specialistici interessati.

Stati:

- `vincolante`: applicata a tutto il progetto;
- `pilota`: applicata al capitolo pilota e da confermare dopo la revisione autoriale;
- `sostituita`: conservata per tracciare una modifica;
- `aperta`: richiede una decisione prima del lavoro interessato.

Alla data di questo aggiornamento non risultano decisioni aperte che impediscano il lavoro previsto.

# Decisioni editoriali

## DEC-001. Repository operativo

- Stato: `vincolante`
- Tutti i progressi vengono registrati in `ferdinandobons/aibook`.
- Branch predefinito: `main`.
- Documenti, capitoli, audit, codice e asset approvati devono essere ricostruibili dai commit.

## DEC-002. Formato sorgente

- Stato: `vincolante`
- Il formato sorgente del libro è Markdown.

## DEC-003. Lingua

- Stato: `vincolante`
- Il libro è scritto in italiano.
- I termini tecnici standard restano in inglese quando questa è la forma corrente nel settore.

## DEC-004. Struttura in due volumi

- Stato: `sostituita`
- Decisione precedente: opera canonica organizzata in due volumi.
- Sostituita da: `DEC-034`.
- Motivo: separare la struttura concettuale canonica dalla scelta tipografica di export.

## DEC-005. Modalità di produzione

- Stato: `vincolante`
- Produzione seriale controllata, un capitolo completo alla volta.
- Ogni capitolo supera i gate prima di procedere al successivo.

## DEC-006. Capitolo pilota

- Stato: `pilota`
- Il primo capitolo prodotto è `CH-P06-ATTENTION`, visualizzato come Capitolo 28 nell'edizione di lavoro.
- Il pilota valida tono, profondità, matematica, codice, visuali e processo di review.

## DEC-007. Livello tecnico

- Stato: `vincolante`
- Livello principale intermedio tecnico.
- Gli approfondimenti avanzati entrano ogni volta che sono necessari per una spiegazione corretta.

## DEC-008. Impostazione didattica

- Stato: `vincolante`
- Approccio didactic-first ancorato a fonti primarie.
- La semplificazione non può modificare il meccanismo.

## DEC-009. Metodo di spiegazione

- Stato: `vincolante`
- Si applica `EXPLANATION_STYLE_AND_VISUALS.md`.
- Ogni capitolo porta un oggetto concreto dall'apertura alla ricostruzione finale.

## DEC-010. Dipendenze metodologiche

- Stato: `vincolante`
- `LEARN_GOVERNANCE.md` non è una dipendenza del libro.
- Tutte le informazioni necessarie devono essere presenti nel repository.

# Decisioni su accuratezza e fonti

## DEC-011. Verifica di tutte le informazioni

- Stato: `vincolante`
- Ogni informazione portante richiede fonte primaria, documentazione ufficiale, standard, derivazione verificata o prova riproducibile.

## DEC-012. Esclusione delle inferenze fattuali

- Stato: `vincolante`
- La versione approvata non contiene affermazioni fattuali basate su inferenze editoriali.
- Quando una fonte non stabilisce un punto, il punto viene ristretto, omesso o mantenuto fuori dal testo approvato.

## DEC-013. Ricerca web aggiornata

- Stato: `vincolante`
- Paper, report, documentazione, API, modelli, benchmark, standard e normative recenti vengono ricontrollati al momento della lavorazione.
- Ogni capitolo registra data di verifica e data di congelamento.

## DEC-014. Gerarchia delle fonti

- Stato: `vincolante`
- Priorità a paper originali, atti ufficiali, report ufficiali, documentazione ufficiale, repository ufficiali e standard.
- Le fonti secondarie non sostengono da sole le affermazioni portanti.

## DEC-015. Sistema di citazione

- Stato: `vincolante`
- Citazione breve vicino all'affermazione e bibliografia completa alla fine del capitolo.
- Sezione, pagina, versione, revisione o commit vengono indicati quando necessari.

## DEC-016. Review del testo

- Stato: `vincolante`
- Ogni capitolo attraversa audit fattuale, matematico, architetturale, algoritmico, temporale, incrociato e didattico.
- Dopo le correzioni viene eseguita una seconda lettura completa.

## DEC-017. Registro delle affermazioni

- Stato: `vincolante`
- Ogni capitolo contiene `CLAIMS.md` con ID stabili e prova di ogni affermazione portante.

# Decisioni sulle immagini

## DEC-018. Strumento di produzione

- Stato: `vincolante`
- Le immagini tecniche vengono create con lo strumento immagini.
- Gli SVG non sono l'artefatto editoriale principale.

## DEC-019. Prima generazione non finale

- Stato: `vincolante`
- Ogni prima generazione è una bozza.

## DEC-020. Review iterativa delle immagini

- Stato: `vincolante`
- Ogni visuale viene revisionata e rigenerata o modificata finché non restano difetti bloccanti.
- Una singola linea ambigua, una shape errata o un valore incoerente bloccano l'approvazione.

## DEC-021. Funzione delle visuali

- Stato: `vincolante`
- Ogni figura risponde a una sola domanda didattica.
- Le visuali sono parte della spiegazione, non decorazione.

## DEC-022. Stile visuale

- Stato: `vincolante`
- Diagrammi originali, puliti e leggibili, ispirati al linguaggio delle immagini di riferimento senza copiarne layout o branding.
- Il colore non è l'unico portatore di significato.

## DEC-023. Quantità delle immagini

- Stato: `vincolante`
- Non esiste un numero rigido di immagini per capitolo.
- Ogni capitolo tecnico include almeno una visuale portante approvata.

## DEC-024. Formato e accessibilità

- Stato: `vincolante`
- Asset finali in PNG ad alta risoluzione, con alt text, equivalente testuale e audit.

# Decisioni sul codice

## DEC-025. Presenza del codice

- Stato: `vincolante`
- Testo, immagini e codice sono integrati.
- Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata.

## DEC-026. Linguaggi e librerie

- Stato: `vincolante`
- Python e PyTorch sono la scelta principale.
- NumPy è ammesso per esempi e verifiche indipendenti.
- Pseudocodice e codice eseguibile restano distinti.

## DEC-027. Dimensione degli snippet

- Stato: `vincolante`
- Snippet brevi e autosufficienti, normalmente tra circa 8 e 40 righe significative.
- Script più lunghi restano nel repository quando necessari.

## DEC-028. Correttezza del codice

- Stato: `vincolante`
- Ogni snippet viene verificato sulla documentazione ufficiale, eseguito in un processo pulito e testato.
- Output e shape coincidono con testo, formule e immagini.

## DEC-029. Provenienza degli output

- Stato: `vincolante`
- Un output è `Eseguito` soltanto quando deriva dall'ambiente e dal comando registrati.
- Gli output costruiti per spiegare il formato sono `Illustrativo`.

# Decisioni sul workflow

## DEC-030. Controllo incrociato

- Stato: `vincolante`
- Testo, formule, immagini e codice condividono label, shape, numeri, ordine, invarianti e confini.
- Una contraddizione blocca il capitolo.

## DEC-031. Revisione autoriale

- Stato: `vincolante`
- Dopo i gate tecnici, ogni capitolo viene sottoposto alla revisione del committente.
- Modifiche tecniche riaprono gli audit pertinenti.

## DEC-032. Congelamento del capitolo

- Stato: `vincolante`
- La versione approvata è associata a data e commit SHA.
- Non si dichiara aggiornamento oltre la data registrata.

## DEC-033. Avvio del lavoro

- Stato: `vincolante`
- Un capitolo non entra in produzione finché la documentazione pertinente non è coerente e il lavoro non è autorizzato.

# Decisioni sull'architettura evolutiva

## DEC-034. Una sola opera canonica

- Stato: `vincolante`
- Il repository contiene una sola opera continua.
- Volume unico, tomi, sito e corso sono export della stessa sorgente.
- La divisione tipografica non modifica l'architettura concettuale.

## DEC-035. Parti stabili `P01`-`P14`

- Stato: `vincolante`
- Le quattordici parti, i relativi ID, nomi e ordine sono definiti in `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`.
- Una nuova architettura o ottimizzazione non rinomina e non riordina automaticamente le parti.
- Una modifica richiede ricerca indipendente, mappa di migrazione e approvazione esplicita del committente.

## DEC-036. Routing funzionale

- Stato: `vincolante`
- Una tecnica viene collocata in base al problema risolto e all'oggetto modificato.
- Il nome del modello, la data o la popolarità non determinano la collocazione.
- Ogni tecnica ha una collocazione primaria e può avere riferimenti secondari.

## DEC-037. Maturità `CORE`, `ESTABLISHED`, `FRONTIER`

- Stato: `vincolante`
- La maturità è un attributo editoriale separato dalla collocazione.
- La promozione ordinaria è `FRONTIER -> ESTABLISHED -> CORE` e richiede nuove prove.
- Una modifica di maturità non cambia automaticamente parte, ID o ordine.

## DEC-038. Identità semantica dei capitoli

- Stato: `vincolante`
- Ogni capitolo ha `chapter_id` stabile, `part_id`, `order_key`, slug, prerequisiti, successori e alias.
- Il numero visualizzato è specifico dell'edizione.
- Split e merge conservano alias e mappa di migrazione.

## DEC-039. Frontiera distribuita

- Stato: `vincolante`
- Le tecniche `FRONTIER` restano nella parte funzionale pertinente.
- `P14` contiene osservatorio, repliche, cronologia e domande aperte, non è un contenitore generico per tutto ciò che è nuovo.

## DEC-040. Catalogo dello stato dell'arte

- Stato: `vincolante`
- `14_CATALOGO_STATO_ARTE.md` è il registro delle principali famiglie e tecniche censite.
- Non è ammesso dichiarare completezza assoluta.
- Ogni voce ha ID, parte, maturità, destinazione e data di verifica.

## DEC-041. Entry point per sistemi senza contesto

- Stato: `vincolante`
- `GUIDELINE.md` nella root è il primo file operativo.
- Deve permettere a una persona o a un sistema AI privo del contesto originario di aggiornare il progetto correttamente.
- `README.md` e `docs/README.md` devono rinviarlo esplicitamente.

## DEC-042. Protocollo degli aggiornamenti

- Stato: `vincolante`
- Nuove tecniche, nuove evidenze, API, cambi di maturità, nuovi capitoli, split, merge, correzioni e nuove edizioni seguono le procedure U1-U8 di `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`.

## DEC-043. Ricerca approfondita globale

- Stato: `vincolante`
- L'ultima ricerca globale è registrata con data **30 luglio 2026** in `15_REGISTRO_RICERCHE_APPROFONDITE.md`.
- Le voci `FRONTIER` vengono ricontrollate almeno ogni 90 giorni durante la produzione attiva.
- Una ricerca globale viene ripetuta prima di ogni nuova edizione e quando emerge una famiglia non collocabile.

## DEC-044. Indice dell'edizione di lavoro

- Stato: `vincolante` per la pianificazione corrente, non ancora congelato come edizione pubblicata.
- `10_INDICE_EDITORIALE.md` contiene 98 capitoli pianificati con ID semantici.
- Il Capitolo 28 conserva il ruolo di pilota.
- La numerazione può cambiare prima del congelamento, gli ID semantici no.

# Decisioni sostituite

## DEC-S01. Uso prioritario di SVG

- Stato: `sostituita`
- Sostituita da: `DEC-018`.

## DEC-S02. Dipendenza da una frase in `LEARN_GOVERNANCE.md`

- Stato: `sostituita`
- Sostituita da: `DEC-010`.

## DEC-S03. Inferenze editoriali ammesse se etichettate

- Stato: `sostituita`
- Sostituita da: `DEC-012`.

## DEC-S04. Due volumi come struttura canonica

- Stato: `sostituita`
- Sostituita da: `DEC-034`.
- La divisione in tomi resta disponibile soltanto come export.

# Regola di propagazione

Quando una decisione cambia:

1. aggiornare questo registro;
2. aggiornare contratto, architettura e protocolli coinvolti;
3. aggiornare template, catalogo e indice quando necessario;
4. controllare i riferimenti incrociati;
5. aggiornare `11_AUDIT_DOCUMENTAZIONE.md`;
6. registrare il commit.