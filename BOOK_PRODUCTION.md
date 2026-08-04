# Piano operativo per la produzione completa del libro

## Stato

- Branch canonico: `main`
- Opera materializzata: 98 capitoli e 12 appendici
- Modalità: audit seriale controllato e revisione autoriale
- Stato corrente: 98 candidature tecniche con testo, fonti e visuali; 94 con codice testato e 4 con eccezione motivata
- Verifica corrente: 464 test in 115 file, 267/267 file Python analizzati sintatticamente, 98/98 capitoli senza problemi automatici
- Data di apertura del branch: 30 luglio 2026
- Ultimo aggiornamento: 4 agosto 2026

La produzione automatizzata ha raggiunto l'intero indice. Non è ancora un via libera editoriale: restano lettura ad alta voce, revisione per lettore non esperto, ricontrollo fattuale delle fonti sensibili, approvazione autoriale delle immagini e congelamento dei candidati in `final.png`.

## Documenti operativi

- governance: `docs/00_GOVERNANCE_E_ARCHITETTURA.md`;
- indice: `docs/01_INDICE_EDITORIALE.md`;
- stile e QA del testo: `docs/02_STILE_E_QA_TESTO.md`;
- visuali: `docs/03_VISUALI.md`;
- fonti, codice e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`;
- workflow e repository: `docs/05_WORKFLOW_E_REPOSITORY.md`;
- catalogo: `docs/14_CATALOGO_STATO_ARTE.md`;
- ricerca globale: `docs/15_REGISTRO_RICERCHE_APPROFONDITE.md`.

## Sequenza di produzione

```text
ricerca
-> claim
-> piano interno
-> stesura
-> formule e derivazioni
-> codice e test
-> visuali e audit
-> audit fattuale, matematico e algoritmico
-> controllo incrociato e temporale
-> review didattica
-> gate anti-template
-> review editoriale e linguistica
-> review per lettore non esperto
-> seconda lettura completa
-> revisione autoriale
-> congelamento
```

Una candidatura può lasciare l'unità corrente quando claim, testo, policy del codice e visuali hanno superato i gate interni ed è disponibile per la revisione autoriale. `final.png` e congelamento richiedono approvazione.

## Quadro dell'opera

| Parte | Intervallo | Stato |
|---|---:|---|
| `P01` Campo, metodo e storia dell'AI | 1-4 | candidature tecniche complete |
| `P02` Matematica, informazione e calcolo | 5-9 | candidature tecniche complete |
| `P03` Apprendimento, ottimizzazione e decisione | 10-14 | candidature tecniche complete |
| `P04` Reti neurali e rappresentazioni | 15-19 | candidature tecniche complete |
| `P05` Modellazione generativa | 20-25 | candidature tecniche complete |
| `P06` Sequenze, linguaggio e contesto | 26-31 | candidature tecniche complete |
| `P07` Dati, pretraining e scaling | 32-36 | candidature tecniche complete |
| `P08` Progettazione delle architetture | 37-45 | candidature tecniche complete |
| `P09` Adattamento, allineamento e ragionamento | 46-54 | candidature tecniche complete |
| `P10` Multimodalità e modelli del mondo | 55-62 | candidature tecniche complete |
| `P11` Conoscenza esterna, memoria e azione | 63-72 | candidature tecniche complete |
| `P12` Efficienza, inference e sistemi | 73-82 | candidature tecniche complete |
| `P13` Valutazione, interpretabilità, sicurezza e governance | 83-93 | candidature tecniche complete |
| `P14` Laboratori, integrazione e osservatorio | 94-98 | candidature tecniche complete |

## Evidenza dell'ultimo audit

- `98/98` capitoli hanno una coppia di immagini PNG attive, per `196` riferimenti risolti; le 12 appendici portano il totale attivo a `208` immagini;
- l'audit semantico e quello strutturale non rilevano capitoli problematici;
- i test locali sono `464` superati in `115` file e i file Python analizzati sintatticamente sono `267/267`;
- la verifica delle fonti registra `419` fonti uniche e `502` collegamenti fonte-claim: `332` con contesto aperto, `127` con contesto parziale e `43` confermati tramite accesso web ufficiale;
- le immagini storiche non referenziate sono state spostate fuori dal repository in una cartella temporanea recuperabile;
- la revisione della prosa ha eliminato i paragrafi pubblici identici tra tre o più capitoli; l'audit editoriale misura `863-3.402` parole pubbliche, mentre l'audit generale misura `938-3.670` parole secondo i rispettivi perimetri di conteggio;
- le 196 visuali dei capitoli usano 84 coppie distinte e 165 modelli semantici ricondotti a dieci primitive controllabili. Processi, stack, tree, grid, boundary, grafi, evidenza, confronti, cicli e tile vengono scelti in base alla relazione da spiegare; non vengono usati grafici quantitativi senza misure;
- `94/98` capitoli includono codice testato. I capitoli 20, 30, 93 e 98 conservano un'eccezione documentata e non contengono vecchi script generici;

Questi risultati dimostrano una candidatura tecnica completa, non l'approvazione finale. Il prossimo ciclo è editoriale: lettura integrale, lettura ad alta voce, controllo per un lettore non esperto e revisione autoriale delle figure.

## Tooling visuale

Il workflow include generatori raster per l'intero indice. Le visuali candidate sono PNG con sfondo bianco, controllo del contenimento e artefatti `SPEC.md`, `AUDIT.md` e `ALT_TEXT.md`.

Quando image-gen ignora la specifica o inventa informazioni sul progetto, la candidata viene respinta e il difetto viene registrato. Per grafi, formule e connessioni che richiedono precisione viene usato il renderer raster deterministico, mai SVG come artefatto principale.

## Aggiornamento del piano

Dopo ogni passata si aggiornano questo file, `PROGRESS.md`, lo stato del capitolo e gli eventuali riferimenti in indice e catalogo. Tag e release restano esclusi finché i gate editoriali e tecnici non sono chiusi.
