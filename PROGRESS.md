# Avanzamento del libro

## Stato corrente

- Repository operativo: `ferdinandobons/aibook`
- Branch canonico: `main`
- Branch di review: `review/chapter-28-pilot`
- Pull request: `#1`
- Modalità: produzione seriale controllata
- Capitolo pilota: `CH-P06-ATTENTION`, numero di lavoro 28
- Versione candidata: `0.3.0-rc3`
- Stato: **revisione autoriale aperta**
- Ultima ricerca approfondita globale: 30 luglio 2026
- Ultima verifica delle fonti del capitolo: 30 luglio 2026
- Standard visivo canonico adottato: 30 luglio 2026
- Struttura logica in prosa adottata: 30 luglio 2026

## Pacchetto disponibile

Il branch di review contiene:

- capitolo Markdown completo, riscritto come prosa tecnica naturale;
- fonti primarie e documentazione ufficiale;
- registro delle affermazioni;
- audit fattuale, matematico, algoritmico e temporale;
- quattro review didattiche registrate;
- tre snippet Python/PyTorch;
- tre test pertinenti superati;
- ambiente e output registrati;
- due immagini tecniche candidate con specifiche, alt text e audit;
- checklist per la revisione dell'autore.

Non contiene render delle pagine, mockup editoriali o screenshot di impaginazioni.

## Review didattica

La prima candidatura è stata corretta in due cicli distinti:

1. revisione della sequenza didattica, dei gate e dei confini;
2. revisione della superficie editoriale e rimozione delle intestazioni metacognitive ripetute.

La versione `0.3.0-rc3` mantiene internamente stato, problema, trasformazione, output, invariante e confine, ma li integra in paragrafi e titoli semantici.

Documenti pertinenti:

- `docs/EXPLANATION_STYLE_AND_VISUALS.md`;
- `docs/18_PROTOCOLLO_QA_DIDATTICO.md`;
- `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`;
- `docs/01_TEMPLATE_CAPITOLO.md`.

## Stato delle visuali

- `ATT-01/candidate-v2.png`: `validata tecnicamente`; approvazione autoriale aperta.
- `ATT-02/candidate-v2.png`: `validata tecnicamente`; approvazione autoriale aperta.
- Le versioni `candidate-v1.png` sono state rimosse perché corrotte e non revisionabili.
- Nessuna immagine è denominata `final.png` prima dell'approvazione.

## Standard visivo adottato

Tutte le immagini future seguono `docs/17_STANDARD_VISIVO_CANONICO.md`:

- sfondo bianco puro `#FFFFFF`;
- orientamento orizzontale o verticale scelto in base al contenuto;
- palette semantica stabile;
- box, frecce e gerarchia tipografica comuni;
- una domanda didattica principale per figura;
- nessuna renderizzazione completa della pagina usata come figura tecnica;
- prima generazione sempre trattata come bozza.

Il contenimento del testo è un gate obbligatorio. Overflow, clipping, sovrapposizioni e padding insufficiente bloccano l'approvazione.

## Prossimo gate

1. review del capitolo `0.3.0-rc3` e degli artefatti nella pull request;
2. commenti e correzioni;
3. riapertura degli audit interessati quando necessario;
4. approvazione della prosa, del formato pilota e delle due visuali;
5. rinomina delle figure approvate in `final.png`;
6. congelamento del capitolo e merge;
7. avvio seriale dei capitoli successivi.