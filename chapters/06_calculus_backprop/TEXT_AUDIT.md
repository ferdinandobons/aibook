# Audit del testo. Capitolo 6

## Stato

- Versione: `0.2.0-rc1`
- Data: 31 luglio 2026
- Protocollo: `docs/02_STILE_E_QA_TESTO.md`
- Esito fattuale e matematico: **superato**
- Esito didattico: **superato dopo seconda lettura**
- Gate anti-template: **superato**
- Esito editoriale e linguistico: **superato**
- Chiarezza per lettore non esperto: **superata**
- Codice: cinque test registrati, esito positivo
- Visuali: validate tecnicamente, revisione autoriale aperta

## `DID-CALC-01`. Prima lettura completa

### Difetti rilevati

1. La distinzione tra derivata locale e variazione finita richiedeva un esempio numerico prima della rete.
2. Il gradiente rischiava di essere interpretato come aggiornamento dei parametri.
3. La transizione dalla chain rule scalare alla Jacobiana era troppo rapida.
4. Il termine VJP compariva senza un contratto esplicito tra gradiente in arrivo e gradiente in uscita.
5. La prima candidata di `CALC-02` aveva il footer sovrapposto ai box inferiori.
6. Tre tentativi con lo strumento immagini rappresentavano lo stato del libro anziché il grafo matematico.
7. La parte PyTorch rischiava di diventare una reference API.
8. Accumulo, `gradcheck`, modalità dei gradienti e operazioni in-place erano presenti ma non ancora legati agli errori che possono produrre.

### Correzioni

- aggiunto l'esempio di `f(x)=x^2` e della perturbazione `0,001`;
- separati gradiente, backpropagation e optimizer step;
- introdotte Jacobiana e derivata direzionale dopo il caso scalare;
- definito il reverse mode come composizione di prodotti con derivate locali;
- rigenerata `CALC-02` con zona di sicurezza sufficiente;
- respinte le visuali non pertinenti senza pubblicarle;
- mantenuto un solo snippet principale nel corpo;
- collegati accumulo, grafo liberato, `no_grad`, `inference_mode` e in-place ai relativi confini operativi.

## `DID-CALC-02`. Seconda lettura integrale

### Lettore non esperto

- [x] il problema viene presentato prima del gergo;
- [x] la derivata è spiegata come sensibilità locale;
- [x] il lettore vede un esempio finito prima della definizione multivariata;
- [x] derivate parziali e gradiente vengono distinti;
- [x] la chain rule viene applicata prima del termine backpropagation;
- [x] il forward numerico precede il backward;
- [x] i valori della rete rimangono gli stessi lungo tutto il capitolo;
- [x] le formule avanzate possono essere saltate senza perdere il meccanismo di base.

### Lettore tecnico

- [x] formula del gradiente coerente con la convenzione a vettori colonna;
- [x] Jacobiana con shape `[m,n]`;
- [x] reverse mode espresso come `J^T` moltiplicato per il gradiente in arrivo;
- [x] forward mode e reverse mode distinti senza assoluti sulla complessità;
- [x] backpropagation separata dall'optimizer;
- [x] differenze finite distinte da automatic differentiation;
- [x] contratti PyTorch controllati sulla documentazione stable 2.13;
- [x] output eseguiti distinti dalle definizioni generali.

### Lettore che riprende il capitolo

- [x] sezioni semantiche e localizzabili;
- [x] esempio numerico unico;
- [x] due visuali con funzioni diverse;
- [x] riepilogo in tre paragrafi;
- [x] esercizi collegati a variazioni controllate del caso base.

## Audit matematico

- [x] `z=2,5`;
- [x] `h=0,9866142981514303`;
- [x] `y_hat=-0,4906300087060012`;
- [x] `L=0,39661090620382594`;
- [x] `dL/dy_hat=-0,8906300087060013`;
- [x] `dL/dh=0,6234410060942008`;
- [x] `dh/dz=0,026592226683160525`;
- [x] `dL/dz=0,01657868455763465`;
- [x] `dL/dw1=0,0331573691152693`;
- [x] `dL/db1=0,01657868455763465`;
- [x] `dL/dw2=-0,8787083009520738`;
- [x] `dL/db2=-0,8906300087060013`;
- [x] valori arrotondati coerenti tra testo, visuali e output.

## Audit fattuale e temporale

- [x] chain rule, gradienti e grafi collegati a fonti consolidate;
- [x] ruolo storico di Rumelhart, Hinton e Williams descritto senza attribuire una origine unica all'AD inversa;
- [x] distinzione AD, differenze finite e simbolico verificata su Baydin et al.;
- [x] PyTorch stable ricontrollata il 31 luglio 2026;
- [x] `backward()` e accumulo verificati sulla documentazione ufficiale;
- [x] output non scalare e gradiente esterno verificati;
- [x] `torch.autograd.grad` verificato come API che restituisce gradienti rispetto agli input;
- [x] `gradcheck` e doppia precisione verificati;
- [x] `no_grad`, `inference_mode` ed `eval()` non trattati come sinonimi.

## Audit linguistico

- [x] italiano scritto direttamente;
- [x] nessun em dash;
- [x] termini inglesi usati soltanto quando standard;
- [x] nessuna sequenza ripetitiva di microsezioni;
- [x] paragrafi matematici collegati da frasi causali;
- [x] caveat avanzati collocati dopo il percorso principale;
- [x] lettura ad alta voce superata internamente.

## Confini aperti

- ottimizzatori e dinamica del training sono differiti;
- Hessiane e derivate di ordine superiore sono differite;
- il codice usa un esempio scalare e non misura prestazioni di una rete reale;
- le visuali restano candidate fino all'approvazione autoriale.

## Verdetto

Il testo `0.2.0-rc1` supera i gate fattuali, matematici, didattici, anti-template, editoriali, linguistici e di accessibilità. Il capitolo può passare alla revisione autoriale dopo la materializzazione dei due PNG nel feature branch.
