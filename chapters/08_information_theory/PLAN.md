# Piano interno. Capitolo 8

## Identità

- `chapter_id`: `CH-P02-INFORMATION-THEORY`
- Parte: `P02`, Matematica, informazione e calcolo
- Titolo: Teoria dell'informazione e funzioni obiettivo
- Profilo: fondamento informativo e probabilistico delle loss
- Domanda centrale: come trasformiamo una distribuzione prevista e un risultato osservato in una quantità scalare che distingua previsioni migliori, peggiori e numericamente instabili?
- Oggetto continuo: classificatore a tre classi per la richiesta `Il pacco non è arrivato`

## Oggetto numerico

```text
classi:
0 = problema di consegna
1 = modifica ordine
2 = problema di pagamento

logits corretti: [2,0; 0,5; -1,0]
target: classe 0
probabilità: [0,785597; 0,175290; 0,039113]
NLL / cross-entropy: 0,241311
entropia predittiva: 0,621585 nat

target morbido q: [0,90; 0,05; 0,05]
H(q): 0,394398
H(q,p): 0,466311
KL(q||p): 0,071914

logits confidentemente errati: [-1,0; 0,5; 2,0]
loss target classe 0: 3,241311
```

## Stato finale del lettore

Il lettore sa:

1. interpretare self-information ed entropia;
2. distinguere entropia, cross-entropy e KL divergence;
3. comprendere unità in bit o nat;
4. collegare negative log-likelihood e massima verosimiglianza;
5. distinguere logits, probabilità e log-probabilità;
6. ricostruire softmax e log-softmax;
7. leggere la cross-entropy con target hard o soft;
8. spiegare perché una previsione confidentemente errata riceve loss elevata;
9. derivare il gradiente `p - q` rispetto ai logits;
10. distinguere loss per classificazione, regressione e regolarizzazione;
11. collegare MSE a una likelihood gaussiana a varianza fissata e L1 a una likelihood laplaciana a scala fissata;
12. usare `CrossEntropyLoss`, `NLLLoss`, `log_softmax` e `KLDivLoss` senza violarne i contratti.

## Progressione

1. Informazione di un evento.
2. Entropia come informazione media.
3. Entropia congiunta, condizionata e mutua informazione.
4. Cross-entropy e KL.
5. Likelihood e negative log-likelihood.
6. Logits e softmax.
7. Esempio numerico a tre classi.
8. Gradiente della cross-entropy.
9. Target soft e label smoothing.
10. Stabilità numerica di log-softmax.
11. Empirical risk e riduzioni sul batch.
12. MSE, L1 e scelta dell'obiettivo.
13. PyTorch e controlli API.

## Visuali

### `INFO-01`. Dai logits alla cross-entropy

Due righe parallele, previsione corretta e previsione confidentemente errata, con logits, probabilità target e loss.

### `INFO-02`. Entropia, cross-entropy e KL

Confronto tra target `q` e predizione `p`; mostra `H(q,p)=H(q)+KL(q||p)` con valori del caso morbido e il caso one-hot come confine.

## Codice

### `SNIP-INFO-001`

- softmax e log-softmax;
- NLL manuale e `F.cross_entropy`;
- entropia della predizione;
- decomposizione cross-entropy;
- gradiente rispetto ai logits;
- caso confidentemente errato;
- overflow della formula ingenua e stabilità di `log_softmax`;
- sette test.

## Gate specifici

- entropia informativa non viene presentata come significato semantico;
- KL non viene chiamata distanza metrica;
- base del logaritmo e unità vengono dichiarate;
- cross-entropy e accuratezza non vengono confuse;
- `CrossEntropyLoss` riceve logits, non probabilità già normalizzate nel caso standard;
- target probabilistici devono essere distribuzioni valide;
- `KLDivLoss` riceve log-probabilità nell'input;
- `reduction='batchmean'` viene distinta da `'mean'` per la KL matematica;
- l'equivalenza MSE-Gaussiana richiede varianza fissata;
- l'obiettivo non viene presentato come garanzia di calibrazione o qualità del sistema.
