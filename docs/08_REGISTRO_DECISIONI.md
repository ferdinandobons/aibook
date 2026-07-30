# Registro consolidato delle decisioni

## Funzione

Questo documento registra le decisioni esplicite che governano il progetto. Ogni nuova decisione deve essere propagata ai documenti specialistici interessati.

Stati:

- `vincolante`: applicata a tutto il progetto;
- `pilota`: applicata al capitolo pilota e da confermare dopo la revisione autoriale;
- `sostituita`: conservata per tracciare una modifica;
- `aperta`: richiede una decisione.

Non risultano decisioni aperte che impediscano la review del Capitolo 28.

# Decisioni editoriali

## DEC-001. Repository operativo

- Stato: `vincolante`
- Tutti i progressi vengono registrati in `ferdinandobons/aibook`.
- Branch predefinito: `main`.

## DEC-002. Formato sorgente

- Stato: `vincolante`
- Il formato sorgente è Markdown.

## DEC-003. Lingua

- Stato: `vincolante`
- Il libro è scritto in italiano.
- I termini tecnici standard restano in inglese quando appropriato.

## DEC-004. Struttura in due volumi

- Stato: `sostituita`
- Sostituita da `DEC-034`.

## DEC-005. Modalità di produzione

- Stato: `vincolante`
- Produzione seriale controllata, un capitolo completo alla volta.

## DEC-006. Capitolo pilota

- Stato: `pilota`
- Il primo capitolo è `CH-P06-ATTENTION`, visualizzato come Capitolo 28 nell'edizione di lavoro.

## DEC-007. Livello tecnico

- Stato: `vincolante`
- Livello principale intermedio tecnico, con approfondimenti avanzati quando necessari.

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
- `LEARN_GOVERNANCE.md` non è una dipendenza.
- Tutte le regole devono essere presenti nel repository.

# Accuratezza e fonti

## DEC-011. Verifica di tutte le informazioni

- Stato: `vincolante`
- Ogni informazione portante richiede fonte primaria, documentazione ufficiale, standard, derivazione verificata o prova riproducibile.

## DEC-012. Esclusione delle inferenze fattuali

- Stato: `vincolante`
- La versione approvata non contiene fatti basati su inferenze editoriali.

## DEC-013. Ricerca web aggiornata

- Stato: `vincolante`
- Contenuti recenti vengono ricontrollati al momento della lavorazione.
- Ogni capitolo registra date di verifica e congelamento.

## DEC-014. Gerarchia delle fonti

- Stato: `vincolante`
- Priorità a paper originali, atti, report, documentazione, repository ufficiali e standard.

## DEC-015. Sistema di citazione

- Stato: `vincolante`
- Citazione breve vicino all'affermazione e bibliografia completa alla fine.

## DEC-016. Review del testo

- Stato: `vincolante`
- Ogni capitolo attraversa audit fattuale, matematico, architetturale, algoritmico, temporale, incrociato e didattico.
- Dopo le correzioni viene eseguita una nuova lettura completa.

## DEC-017. Registro delle affermazioni

- Stato: `vincolante`
- Ogni capitolo contiene `CLAIMS.md` con ID stabili e prova delle affermazioni portanti.

# Immagini

## DEC-018. Strumento di produzione

- Stato: `vincolante`
- Le immagini tecniche vengono create con lo strumento immagini.
- Gli SVG non sono l'artefatto editoriale principale.

## DEC-019. Prima generazione non finale

- Stato: `vincolante`
- Ogni prima generazione è una bozza.

## DEC-020. Review iterativa delle immagini

- Stato: `vincolante`
- Ogni visuale viene revisionata e rigenerata finché non restano difetti bloccanti.

## DEC-021. Funzione delle visuali

- Stato: `vincolante`
- Ogni figura risponde a una domanda didattica ed è parte della spiegazione.

## DEC-022. Stile visuale

- Stato: `vincolante`
- Diagrammi originali, puliti e leggibili, con significato non affidato al solo colore.

## DEC-023. Quantità delle immagini

- Stato: `vincolante`
- Non esiste un numero rigido di immagini per capitolo.

## DEC-024. Formato e accessibilità

- Stato: `vincolante`
- Asset finali PNG ad alta risoluzione, con alt text, equivalente testuale e audit.

# Codice

## DEC-025. Presenza del codice

- Stato: `vincolante`
- Ogni capitolo tecnico include almeno uno snippet eseguibile, salvo eccezione motivata.

## DEC-026. Linguaggi e librerie

- Stato: `vincolante`
- Python e PyTorch sono la scelta principale; NumPy è ammesso per controlli indipendenti.

## DEC-027. Dimensione degli snippet

- Stato: `vincolante`
- Snippet brevi e autosufficienti; script lunghi soltanto quando necessari.

## DEC-028. Correttezza del codice

- Stato: `vincolante`
- Ogni snippet viene verificato, eseguito in un processo pulito e testato.

## DEC-029. Provenienza degli output

- Stato: `vincolante`
- Un output è `Eseguito` soltanto quando deriva dall'ambiente e dal comando registrati.

# Workflow

## DEC-030. Controllo incrociato

- Stato: `vincolante`
- Testo, formule, immagini e codice condividono label, shape, numeri, ordine, invarianti e confini.

## DEC-031. Revisione autoriale

- Stato: `vincolante`
- Dopo i gate tecnici, ogni capitolo viene sottoposto alla revisione del committente.

## DEC-032. Congelamento del capitolo

- Stato: `vincolante`
- La versione approvata è associata a data e commit SHA.

## DEC-033. Avvio del lavoro

- Stato: `vincolante`
- Un capitolo non entra in produzione finché documentazione e autorizzazione non sono coerenti.

# Architettura evolutiva

## DEC-034. Una sola opera canonica

- Stato: `vincolante`
- Il repository contiene una sola opera continua; volume, tomi, sito e corso sono export.

## DEC-035. Parti stabili `P01`-`P14`

- Stato: `vincolante`
- ID, nomi e ordine delle quattordici parti sono stabili.

## DEC-036. Routing funzionale

- Stato: `vincolante`
- Una tecnica viene collocata in base al problema risolto e all'oggetto modificato.

## DEC-037. Maturità `CORE`, `ESTABLISHED`, `FRONTIER`

- Stato: `vincolante`
- La maturità è separata dalla collocazione e cambia soltanto con nuove prove.

## DEC-038. Identità semantica dei capitoli

- Stato: `vincolante`
- Ogni capitolo ha `chapter_id`, `part_id`, `order_key`, slug, prerequisiti, successori e alias.

## DEC-039. Frontiera distribuita

- Stato: `vincolante`
- Le tecniche `FRONTIER` restano nella parte funzionale pertinente.

## DEC-040. Catalogo dello stato dell'arte

- Stato: `vincolante`
- `14_CATALOGO_STATO_ARTE.md` registra le principali famiglie censite senza dichiarare completezza assoluta.

## DEC-041. Entry point per sistemi senza contesto

- Stato: `vincolante`
- `GUIDELINE.md` è il primo file operativo.

## DEC-042. Protocollo degli aggiornamenti

- Stato: `vincolante`
- Gli aggiornamenti seguono le procedure U1-U8 di `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`.

## DEC-043. Ricerca approfondita globale

- Stato: `vincolante`
- L'ultima ricerca globale è registrata al 30 luglio 2026.
- Le voci `FRONTIER` vengono ricontrollate periodicamente.

## DEC-044. Indice dell'edizione di lavoro

- Stato: `vincolante` per la pianificazione corrente.
- `10_INDICE_EDITORIALE.md` contiene 98 capitoli pianificati con ID semantici.

# Decisioni visuali e didattiche aggiuntive

## DEC-045. Contenimento del testo nelle visuali

- Stato: `vincolante`
- Testo, pedici, apici e simboli devono rimanere integralmente nei propri contenitori.
- Overflow, clipping, sovrapposizioni e padding insufficiente sono difetti bloccanti.
- Riferimento: `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`.

## DEC-046. Review didattica iterativa

- Stato: `vincolante`
- Ogni capitolo riceve almeno una review didattica completa.
- Se emerge un difetto bloccante, il capitolo viene corretto e sottoposto a una nuova review integrale.
- Il ciclo continua finché `TEXT_AUDIT.md` non registra un esito positivo.
- Riferimento: `18_PROTOCOLLO_QA_DIDATTICO.md`.

## DEC-047. Struttura logica implicita nella prosa

- Stato: `vincolante`
- Stato, problema, input, trasformazione, output, invariante, confine e continuità restano obbligatori come funzioni logiche.
- Per impostazione predefinita non vengono pubblicati come sequenza ripetitiva di intestazioni metacognitive.
- Lo scaffold esplicito appartiene a `PLAN.md` e `TEXT_AUDIT.md`; `CHAPTER.md` usa titoli semantici e prosa naturale.
- La review include un gate anti-template.
- Riferimento: `19_STRUTTURA_LOGICA_IN_PROSA.md`.

# Decisioni sostituite

## DEC-S01. Uso prioritario di SVG

- Stato: `sostituita`
- Sostituita da `DEC-018`.

## DEC-S02. Dipendenza da `LEARN_GOVERNANCE.md`

- Stato: `sostituita`
- Sostituita da `DEC-010`.

## DEC-S03. Inferenze editoriali ammesse se etichettate

- Stato: `sostituita`
- Sostituita da `DEC-012`.

## DEC-S04. Due volumi come struttura canonica

- Stato: `sostituita`
- Sostituita da `DEC-034`.

## DEC-S05. Blocco atomico pubblicato come struttura standard

- Stato: `sostituita`
- Interpretazione precedente: le etichette del blocco atomico potevano diventare il telaio visibile ricorrente dei capitoli.
- Sostituita da `DEC-047`.
- Il blocco resta obbligatorio per progettazione e review, ma viene incorporato nella prosa.

# Regola di propagazione

Quando una decisione cambia:

1. aggiornare questo registro;
2. aggiornare contratto e protocolli coinvolti;
3. aggiornare template, catalogo e indice quando necessario;
4. controllare i riferimenti incrociati;
5. aggiornare `11_AUDIT_DOCUMENTAZIONE.md`;
6. registrare il commit.