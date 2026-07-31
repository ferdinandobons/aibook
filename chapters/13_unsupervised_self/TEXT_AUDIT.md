# Audit del testo. Capitolo 13

## Stato

- Versione: `0.2.0-rc1`
- Data: 31 luglio 2026
- Esito fattuale: **superato**
- Esito matematico: **superato**
- Esito algoritmico: **superato**
- Esito didattico: **superato dopo seconda lettura**
- Gate anti-template: **superato**
- Esito editoriale e linguistico: **superato**
- Chiarezza per lettore non esperto: **superata**
- Continuità tra capitoli: **superata**
- Codice: nove test registrati
- Visuali: validate tecnicamente
- Revisione autoriale: aperta

## Audit di continuità

### Ingresso dal Capitolo 12

Il capitolo precedente ha costruito un predittore da coppie input-target. L'apertura rimuove esplicitamente la label esterna e chiede quale segnale resti disponibile. Non presume conoscenza di k-means, autoencoder o contrastive learning.

### Prerequisiti richiamati

- distanza e media, Capitolo 5;
- gradienti e optimizer, Capitolo 6;
- campione e distribuzione, Capitolo 7;
- loss e logits, Capitolo 8;
- precisione numerica, Capitolo 9;
- train, validation e test, Capitolo 12.

Le formule necessarie vengono riscritte localmente.

### Uscita verso il Capitolo 14

Il riepilogo separa dataset statico e target auto-generato dal caso in cui un agente sceglie azioni e riceve reward ritardati. Il meccanismo del reinforcement learning non viene anticipato.

## Prima lettura critica

Difetti trovati e corretti:

1. `senza label` rischiava di essere letto come `senza supervisione operativa`;
2. non supervisionato e self-supervised potevano sembrare categorie con confine universale;
3. k-means poteva apparire come scoperta automatica di classi reali;
4. il numero del cluster poteva essere interpretato semanticamente;
5. PCA e autoencoder richiedevano un ponte con il Capitolo 5;
6. reconstruction loss rischiava di sostituire la valutazione downstream;
7. masked modeling richiedeva un percorso esplicito dal dato originale alla loss;
8. la formula contrastiva richiedeva prima la definizione di positiva e alternative;
9. collapse non poteva essere spiegato con un solo rimedio universale;
10. pseudo-label dovevano essere distinte da label umane;
11. linear probe e fine-tuning dovevano essere separati;
12. le label usate nella valutazione potevano essere confuse con quelle assenti dal pretraining;
13. la baseline zero del primo snippet non generalizzava bene; è stata sostituita con una baseline media più pertinente;
14. il masked autoencoder iniziale riceveva soltanto zeri nelle posizioni mascherate; è stata aggiunta la mask esplicita;
15. una maschera fissa nel training produceva un risultato test peggiore della baseline; le maschere ora cambiano durante il training e restano fisse soltanto nel test.

## Seconda lettura integrale

### Lettore non esperto

- [x] parte dalla rimozione di una label già conosciuta;
- [x] chiarisce che resta una funzione obiettivo;
- [x] costruisce k-means prima della sua interpretazione;
- [x] spiega encoder, decoder e bottleneck;
- [x] mostra da dove nasce il target mascherato;
- [x] descrive coppie positive prima della formula contrastiva;
- [x] distingue pretraining e valutazione;
- [x] codice dopo i meccanismi.

### Lettore tecnico

- [x] obiettivo k-means corretto;
- [x] assegnamento e media coerenti;
- [x] limite del minimo locale dichiarato;
- [x] masked MSE calcolata soltanto sulle coordinate nascoste;
- [x] mask fornita al modello;
- [x] formula contrastiva con temperatura e set del denominatore;
- [x] setup dei paper non mescolati;
- [x] API PyTorch separate dall'ambiente eseguito.

### Lettore che riprende il capitolo

- [x] tre famiglie localizzabili in `UNSUP-01`;
- [x] pipeline mascherata localizzabile in `UNSUP-02`;
- [x] riepilogo distingue obiettivo, rappresentazione e evaluation;
- [x] ponte al reinforcement learning esplicito.

## Audit numerico

- [x] shape train `[120,4]`;
- [x] shape test `[60,4]`;
- [x] cluster counts `[40,40,40]`;
- [x] obiettivo k-means `203,144502 -> 60,284823`;
- [x] masked train loss `2,218895 -> 0,359401`;
- [x] masked test loss `0,391415`;
- [x] baseline media `1,900604`;
- [x] embedding shape `[60,2]`;
- [x] nove test superati.

## Audit linguistico

- [x] italiano scritto direttamente;
- [x] nessun em dash;
- [x] termini introdotti dopo il referente;
- [x] paragrafi causali;
- [x] nessuna rassegna enciclopedica;
- [x] cautele collocate nel punto necessario;
- [x] lettura ad alta voce superata internamente.

## Verdetto

Il capitolo supera i gate fattuali, matematici, algoritmici, didattici, anti-template, editoriali, linguistici, visuali e di continuità. Può essere sottoposto alla revisione autoriale.
