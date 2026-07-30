# Governance e architettura editoriale

## Stato

- Stato: `vincolante`
- Repository: `ferdinandobons/aibook`
- Branch canonico: `main`
- Lingua: italiano
- Formato: Markdown
- Opera: unica e continua
- Produzione: seriale e controllata
- Capitolo pilota: `CH-P06-ATTENTION`
- Ultima ricerca approfondita globale: **30 luglio 2026**
- Entry point: `../GUIDELINE.md`
- Indice: `01_INDICE_EDITORIALE.md`
- Catalogo: `14_CATALOGO_STATO_ARTE.md`
- Ricerca globale: `15_REGISTRO_RICERCHE_APPROFONDITE.md`
- Workflow: `05_WORKFLOW_E_REPOSITORY.md`

## 1. Scopo

Il repository contiene il manuale tecnico **Intelligenza artificiale generativa**, dai fondamenti matematici e computazionali ai modelli generativi, alle architetture, al post-training, alla multimodalità, agli agenti, ai sistemi, alla valutazione e alla sicurezza.

Il libro segue problemi, meccanismi e contratti tecnici. I prodotti vengono usati come studi di caso, non come struttura dell'opera.

Ogni capitolo tecnico integra, quando pertinente:

1. testo verificato e scritto come manuale;
2. formule, tabelle ed esempi controllati;
3. immagini tecniche sottoposte ad audit;
4. codice eseguito e testato;
5. fonti, claim e review.

## 2. Forma dell'opera

Esiste una sola sorgente canonica. Può essere esportata come volume unico, più tomi, sito, knowledge base o corso. L'export non modifica identità e ordine concettuale.

## 3. Lettore e profondità

Il livello principale è intermedio tecnico. Gli approfondimenti avanzati entrano quando servono per matematica, shape, stabilità, complessità, memoria, implementazione, training distribuito, serving, hardware, compiler, kernel e trade-off di sistema.

Il caso base precede le varianti. La semplificazione non può modificare il meccanismo.

## 4. Parti stabili

| ID | Parte canonica | Domanda stabile |
|---|---|---|
| `P01` | Campo, metodo e storia dell'AI | Che cosa viene chiamato AI, come si è sviluppato il campo e come si valuta la conoscenza tecnica? |
| `P02` | Matematica, informazione e calcolo | Quali quantità, strutture e vincoli computazionali descrivono i modelli? |
| `P03` | Apprendimento, ottimizzazione e decisione | Come si definiscono obiettivi, segnali, update e decisioni? |
| `P04` | Reti neurali e rappresentazioni | Come vengono costruite rappresentazioni neurali riutilizzabili? |
| `P05` | Modellazione generativa | Come si modellano e si campionano distribuzioni di dati? |
| `P06` | Sequenze, linguaggio e contesto | Come vengono rappresentate e trasformate sequenze e dipendenze contestuali? |
| `P07` | Dati, pretraining e scaling | Come vengono costruiti dati, ricette e sistemi di pretraining? |
| `P08` | Progettazione delle architetture | Quali operatori, blocchi, memorie e pattern definiscono l'architettura interna? |
| `P09` | Adattamento, allineamento e ragionamento | Come si modificano capacità e comportamento dopo il pretraining? |
| `P10` | Multimodalità e modelli del mondo | Come si rappresentano e generano modalità diverse e dinamiche ambientali? |
| `P11` | Conoscenza esterna, memoria e azione | Come un modello recupera conoscenza, conserva stato, usa strumenti e agisce? |
| `P12` | Efficienza, inference e sistemi | Come si riducono costo, memoria e latenza e come si servono i modelli? |
| `P13` | Valutazione, interpretabilità, sicurezza e governance | Come si misurano, comprendono, proteggono e governano i sistemi? |
| `P14` | Laboratori, integrazione e osservatorio | Come si integrano sistemi, si replicano risultati e si monitora la frontiera? |

### Immutabilità

ID, nome e ordine delle parti cambiano soltanto quando:

1. una classe rilevante non è più collocabile;
2. almeno due revisioni approfondite documentano il problema;
3. esiste una mappa di migrazione;
4. la decisione viene registrata;
5. il committente approva.

Un nuovo modello o paper non basta.

## 5. Routing funzionale

Ogni tecnica ha una collocazione primaria.

1. descrivere il problema risolto;
2. identificare il punto del ciclo di vita;
3. individuare l'oggetto modificato;
4. scegliere la parte proprietaria dell'oggetto;
5. registrare collegamenti secondari.

| Oggetto modificato | Parte |
|---|---|
| definizioni, storia, metodo | `P01` |
| matematica, informazione, numerica, hardware di base | `P02` |
| obiettivi, ottimizzazione, RL, decisione | `P03` |
| layer neurali e rappresentazioni | `P04` |
| fattorizzazione generativa, latent, diffusion, flow, sampling | `P05` |
| token, embedding, sequence modeling, attention base | `P06` |
| dati, curriculum, scaling, pretraining | `P07` |
| blocchi, attention variant, SSM, MoE, routing, memoria interna | `P08` |
| fine-tuning, preferenze, post-training, reasoning | `P09` |
| visione, audio, video, 3D, world model, embodied | `P10` |
| retrieval, RAG, memoria esterna, tool, agenti | `P11` |
| quantizzazione, pruning, decoding, cache, compiler, serving | `P12` |
| valutazione, interpretabilità, sicurezza, privacy, diritto | `P13` |
| laboratori, repliche e osservatorio | `P14` |

## 6. Modelli e studi di caso

Un modello non riceve automaticamente un capitolo. Può essere studio di caso, fonte di una tecnica o capitolo autonomo soltanto quando esiste una domanda didattica durevole con fonti e contratto propri.

## 7. Maturità

- `CORE`: concetto durevole, trasversale e necessario.
- `ESTABLISHED`: verificato e rilevante, ma non universale o ancora in evoluzione.
- `FRONTIER`: recente, sperimentale, con evidenza o terminologia limitata.

Percorso ordinario:

```text
FRONTIER -> ESTABLISHED -> CORE
```

La promozione richiede nuove prove, adozioni o repliche, terminologia sufficientemente stabile, trade-off e failure mode documentati. La maturità non cambia automaticamente parte, ID o ordine.

Le voci frontier restano nella parte funzionale. `P14` conserva osservatorio, repliche, domande aperte e cronologia delle maturità.

## 8. Identità dei capitoli

Ogni capitolo possiede:

```text
chapter_id
part_id
order_key
titolo
slug
maturità
stato editoriale
prerequisiti
successori
alias
```

Il numero stampato è specifico dell'edizione. `chapter_id` resta stabile.

L'ordine dipende da prerequisiti, caso base, livello di astrazione, rapporto tra meccanismo e implementazione e maturità dell'evidenza.

Split e merge richiedono nuovi ID quando necessario, alias, redirect, migrazione di claim, fonti, visuali e codice.

## 9. Accuratezza

La versione approvata non contiene fatti basati su inferenze editoriali.

Sono prove ammesse:

- paper originale;
- report ufficiale;
- documentazione ufficiale;
- repository ufficiale;
- standard o documento istituzionale;
- derivazione verificata;
- risultato riprodotto.

Ogni capitolo contiene `FONTI_PRIMARIE.md`, `CLAIMS.md` e `TEXT_AUDIT.md`.

## 10. Produzione seriale

Non si apre il capitolo successivo finché quello corrente non è approvato e congelato oppure sospeso con problemi documentati. Il ciclo completo è in `05_WORKFLOW_E_REPOSITORY.md`.

## 11. Operazioni di aggiornamento

Le procedure operative sono in `05_WORKFLOW_E_REPOSITORY.md`:

- U1 nuova tecnica;
- U2 nuova evidenza;
- U3 API o implementazione;
- U4 maturità;
- U5 nuovo capitolo;
- U6 split o merge;
- U7 correzione tecnica;
- U8 nuova edizione.

## 12. Registro delle decisioni

### Editoriale e metodo

| ID | Stato | Decisione |
|---|---|---|
| `DEC-001` | vincolante | Repository operativo `ferdinandobons/aibook`; branch canonico `main`. |
| `DEC-002` | vincolante | Formato sorgente Markdown. |
| `DEC-003` | vincolante | Italiano; termini tecnici inglesi quando appropriati. |
| `DEC-004` | sostituita | Due volumi sostituiti dall'opera unica. |
| `DEC-005` | vincolante | Produzione seriale controllata. |
| `DEC-006` | pilota approvato | `CH-P06-ATTENTION` è il capitolo pilota. |
| `DEC-007` | vincolante | Livello intermedio con approfondimenti avanzati necessari. |
| `DEC-008` | vincolante | Didactic-first, fonti primarie, nessuna semplificazione falsa. |
| `DEC-009` | vincolante | Oggetto continuo in ogni capitolo. |
| `DEC-010` | vincolante | Nessuna dipendenza da `LEARN_GOVERNANCE.md`. |

### Accuratezza

| ID | Stato | Decisione |
|---|---|---|
| `DEC-011` | vincolante | Ogni informazione portante richiede prova. |
| `DEC-012` | vincolante | Inferenze fattuali escluse. |
| `DEC-013` | vincolante | Contenuti recenti ricontrollati e datati. |
| `DEC-014` | vincolante | Priorità a fonti primarie e ufficiali. |
| `DEC-015` | vincolante | Citazione vicina al claim e dossier completo. |
| `DEC-016` | vincolante | Audit tecnico, didattico, editoriale e linguistico. |
| `DEC-017` | vincolante | `CLAIMS.md` con ID stabili. |

### Visuali

| ID | Stato | Decisione |
|---|---|---|
| `DEC-018` | vincolante | Immagini con strumento immagini; SVG non principale. |
| `DEC-019` | vincolante | Prima generazione non finale. |
| `DEC-020` | vincolante | Review e rigenerazione iterative. |
| `DEC-021` | vincolante | Ogni figura risponde a una domanda. |
| `DEC-022` | vincolante | Stile pulito, leggibile, significato non affidato al colore. |
| `DEC-023` | vincolante | Nessun numero rigido di figure. |
| `DEC-024` | vincolante | PNG, alt text, equivalente testuale e audit. |
| `DEC-045` | vincolante | Overflow, clipping e padding insufficiente sono bloccanti. |

### Codice e workflow

| ID | Stato | Decisione |
|---|---|---|
| `DEC-025` | vincolante | Almeno uno snippet per capitolo tecnico, salvo eccezione. |
| `DEC-026` | vincolante | Python e PyTorch principali; NumPy per controlli. |
| `DEC-027` | vincolante | Snippet brevi; script lunghi soltanto quando necessari. |
| `DEC-028` | vincolante | Codice verificato, eseguito e testato. |
| `DEC-029` | vincolante | `Eseguito` soltanto con ambiente e log o test. |
| `DEC-030` | vincolante | Coerenza tra testo, formule, immagini e codice. |
| `DEC-031` | vincolante | Revisione del committente prima del freeze. |
| `DEC-032` | vincolante | Freeze associato a data e commit. |
| `DEC-033` | vincolante | Nessuna produzione senza documentazione coerente. |
| `DEC-046` | vincolante | Difetto didattico seguito da nuova review integrale. |
| `DEC-047` | vincolante | Scaffold interno, prosa naturale e gate anti-template. |
| `DEC-048` | vincolante | Review editoriale, linguistica, lettura ad alta voce e tre lettori. |

### Architettura evolutiva

| ID | Stato | Decisione |
|---|---|---|
| `DEC-034` | vincolante | Opera unica; tomi, sito e corso sono export. |
| `DEC-035` | vincolante | Parti `P01`-`P14` stabili. |
| `DEC-036` | vincolante | Routing per problema e oggetto modificato. |
| `DEC-037` | vincolante | Maturità separata dalla collocazione. |
| `DEC-038` | vincolante | ID semantici separati dalla numerazione. |
| `DEC-039` | vincolante | Frontiera distribuita nelle parti funzionali. |
| `DEC-040` | vincolante | Catalogo delle principali famiglie, senza completezza assoluta. |
| `DEC-041` | vincolante | `GUIDELINE.md` è l'entry point. |
| `DEC-042` | vincolante | Aggiornamenti U1-U8. |
| `DEC-043` | vincolante | Ricerca globale registrata; frontier ricontrollata. |
| `DEC-044` | pianificazione | 98 capitoli con ID semantici. |

### Decisioni sostituite

| ID | Sostituita da | Nota |
|---|---|---|
| `DEC-S01` | `DEC-018` | Uso prioritario di SVG rimosso. |
| `DEC-S02` | `DEC-010` | Dipendenza esterna rimossa. |
| `DEC-S03` | `DEC-012` | Inferenze fattuali non ammesse. |
| `DEC-S04` | `DEC-034` | Due volumi non canonici. |
| `DEC-S05` | `DEC-047` | Blocco atomico non pubblicato come telaio. |
| `DEC-S06` | `DEC-048` | Correttezza didattica non sufficiente senza qualità linguistica. |

## 13. Propagazione

Quando una decisione cambia:

1. aggiornare questo documento;
2. aggiornare i documenti specialistici;
3. aggiornare indice e catalogo quando necessario;
4. controllare i riferimenti;
5. aggiornare `docs/README.md`, root `GUIDELINE.md` e `PROGRESS.md` quando coinvolti;
6. registrare il commit.

Un conflitto non risolto blocca il lavoro interessato.

## 14. Gate documentale

La documentazione è coerente quando un sistema senza contesto può:

- comprendere scopo e struttura;
- collocare e aggiornare una tecnica;
- applicare fonti, claim, codice e visuali;
- scrivere prosa da manuale senza esporre lo scaffold;
- ripetere le review;
- ricostruire una versione approvata dal commit.
