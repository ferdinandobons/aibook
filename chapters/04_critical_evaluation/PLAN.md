# Piano interno. Capitolo 4

## Identità

- `chapter_id`: `CH-P01-CRITICAL-EVALUATION`
- Parte: `P01`, Campo, metodo e storia dell'AI
- Titolo: Come valutare criticamente un risultato di AI
- Profilo: metodo scientifico e lettura degli esperimenti
- Versione candidata prevista: `0.1.0-rc1`
- Oggetto continuo: due classificatori, `A` e `B`, valutati sulle stesse 24 richieste di assistenza
- Domanda centrale: quando una differenza di benchmark giustifica davvero la conclusione che un sistema sia migliore?

## Prerequisiti

- distinzione tra modello e sistema;
- training, validation e test;
- accuratezza come frazione di predizioni corrette;
- Python di base soltanto per eseguire lo snippet.

## Concetti differiti

- teoria statistica completa dei test d'ipotesi;
- causal inference formale;
- fairness e safety evaluation avanzate;
- benchmark multimodali e agentici;
- valutazione economica dei sistemi in produzione.

## Stato finale del lettore

Il lettore sa:

1. ricostruire la domanda sperimentale;
2. controllare baseline, dati e protocollo;
3. distinguere metrica media, slice e costo degli errori;
4. leggere una differenza insieme alla sua variabilità;
5. riconoscere leakage, contaminazione e riuso eccessivo del test set;
6. usare ablation e controlli per restringere un claim causale;
7. verificare se il risultato è riproducibile e rilevante per il sistema reale.

## Progressione didattica

1. Un numero non è ancora una conclusione.
2. La domanda e il protocollo precedono la metrica.
3. La baseline rende interpretabile il miglioramento.
4. La media può nascondere slice critiche e costi asimmetrici.
5. Seed, campionamento e tuning introducono variabilità.
6. Il test set può perdere indipendenza attraverso leakage, adattamento e contaminazione.
7. Ablation e controlli restringono ciò che si può attribuire alla modifica.
8. Riproducibilità e documentazione rendono il claim verificabile.
9. Ricostruzione sul confronto tra i modelli `A` e `B`.

## Codice

### `SNIP-EVAL-001`

- Input: 24 casi con label, predizioni di due modelli, slice e costo dell'errore.
- Output:
  - accuratezza complessiva;
  - accuratezza per slice;
  - costo pesato degli errori;
  - intervallo bootstrap appaiato della differenza di accuratezza.
- Invarianti:
  - i due modelli vengono confrontati sugli stessi esempi;
  - il resampling conserva l'accoppiamento;
  - il modello con accuratezza media maggiore può avere costo peggiore e risultati inferiori sulla slice urgente.

## Visuali previste

### `EVAL-01`. Dal risultato al claim sostenibile

Pipeline di controllo: domanda, protocollo, dati, baseline, metriche, variabilità, slice, riproducibilità e confine del claim.

### `EVAL-02`. La media non basta

Confronto tra `A` e `B` su accuratezza complessiva, slice standard, slice urgente, costo pesato e intervallo della differenza.

## Gate specifici

- non confondere significatività statistica e rilevanza pratica;
- non presentare l'intervallo bootstrap come garanzia universale;
- non inferire causalità da una sola ablation;
- non trattare un benchmark come misura completa della qualità;
- non trasformare una performance media in proprietà di tutte le slice;
- dichiarare quando dati, predizioni e costi sono illustrativi;
- spiegare ogni termine statistico prima della formula o del codice;
- mantenere il testo accessibile anche saltando lo snippet.
