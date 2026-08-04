# Registro dei claim. Capitolo 7

| ID | Claim sostenibile | Prova | Stato |
|---|---|---|---|
| `CLM-PROB-001` | Una misura di probabilità assegna valori non negativi agli eventi, assegna probabilità uno allo spazio campionario e soddisfa additività numerabile per eventi disgiunti. | `SRC-PROB-007`, `SRC-PROB-001` | verificata |
| `CLM-PROB-002` | La probabilità condizionata è `P(A|B)=P(A∩B)/P(B)` quando `P(B)>0`. | `SRC-PROB-001` | verificata |
| `CLM-PROB-003` | La legge della probabilità totale marginalizza su una partizione degli stati possibili. | `SRC-PROB-001` | verificata |
| `CLM-PROB-004` | Il teorema di Bayes riordina una probabilità congiunta e normalizza attraverso la probabilità dell'evidenza. | `SRC-PROB-001`, `SRC-PROB-002` | verificata |
| `CLM-PROB-005` | Due eventi sono indipendenti quando la loro probabilità congiunta fattorizza nel prodotto delle marginali. | `SRC-PROB-001` | verificata |
| `CLM-PROB-006` | L'indipendenza condizionata dipende dalla variabile su cui si condiziona e non implica necessariamente indipendenza marginale. | `SRC-PROB-001`, `SRC-PROB-002` | verificata |
| `CLM-PROB-007` | Una variabile aleatoria è una funzione che associa un valore numerico agli esiti dello spazio campionario. | `SRC-PROB-001`, `SRC-PROB-002` | verificata |
| `CLM-PROB-008` | Una distribuzione discreta assegna masse agli esiti; una densità continua deve essere integrata su un intervallo per ottenere una probabilità. | `SRC-PROB-001`, `SRC-PROB-006` | verificata |
| `CLM-PROB-009` | Il valore atteso è una media pesata rispetto alla distribuzione, quando la somma o l'integrale esiste. | `SRC-PROB-001`, `SRC-PROB-002` | verificata |
| `CLM-PROB-010` | La varianza è l'attesa dello scarto quadratico dalla media e misura dispersione nella scala quadratica della variabile. | `SRC-PROB-001` | verificata |
| `CLM-PROB-011` | La covarianza descrive associazione lineare centrata; covarianza zero non implica indipendenza in generale. | `SRC-PROB-001`, `SRC-PROB-002` | verificata |
| `CLM-PROB-012` | Una popolazione o distribuzione generatrice è distinta dal campione osservato. | `SRC-PROB-003`, `SRC-PROB-005` | verificata |
| `CLM-PROB-013` | Una statistica è una funzione dei dati osservati; uno stimatore è una regola usata per stimare un parametro. | `SRC-PROB-003`, `SRC-PROB-004` | verificata |
| `CLM-PROB-014` | A dati fissati, la likelihood è una funzione del parametro e non è automaticamente una distribuzione di probabilità normalizzata sul parametro. | `SRC-PROB-002`, `SRC-PROB-004`, `SRC-PROB-010` | verificata |
| `CLM-PROB-015` | Per osservazioni Bernoulli indipendenti e non tutte uguali, la MLE del parametro `p` è la media campionaria. | derivazione; `SRC-PROB-002`, `SRC-PROB-004` | verificata |
| `CLM-PROB-016` | Un posterior bayesiano è proporzionale al prodotto tra likelihood e prior, con costante di normalizzazione pari alla probabilità marginale dei dati. | `SRC-PROB-002` | verificata |
| `CLM-PROB-017` | Un intervallo di confidenza frequentista ha una interpretazione di copertura del procedimento, non una probabilità posteriore del parametro fisso. | `SRC-PROB-003`, `SRC-PROB-005` | verificata |
| `CLM-PROB-018` | Un intervallo credibile bayesiano è calcolato dalla distribuzione posteriore e dipende da prior e likelihood. | `SRC-PROB-002` | verificata |
| `CLM-PROB-019` | Sotto condizioni appropriate, la legge dei grandi numeri collega la media campionaria al valore atteso al crescere del campione. | `SRC-PROB-001`, `SRC-PROB-003` | verificato con condizioni |
| `CLM-PROB-020` | Sotto ipotesi iid e varianza finita, il teorema centrale del limite descrive la convergenza in distribuzione della media standardizzata verso una normale. | `SRC-PROB-001`, `SRC-PROB-003` | verificato con condizioni |
| `CLM-PROB-021` | `torch.distributions.Bernoulli` rappresenta variabili binarie con probabilità `p` di valore uno e accetta `probs` oppure `logits`. | `SRC-PROB-008` | verificata |
| `CLM-PROB-022` | Nel caso eseguito, `P(H|E1)=0,666667` e il secondo aggiornamento produce `0,875000`. | `SNIP-PROB-001` | verificata |
| `CLM-PROB-023` | Nel campione Bernoulli eseguito, sette successi su venti producono MLE `0,35`. | `SNIP-PROB-001` | verificata |
| `CLM-PROB-024` | Per una Bernoulli con `p=0,30`, media teorica e varianza sono `0,30` e `0,21`. | `SRC-PROB-008`, `SNIP-PROB-001` | verificato ed eseguito |
| `CLM-PROB-025` | Nel run registrato, le medie campionarie per `n=10`, `100` e `10 000` sono `0,60`, `0,32` e `0,3042`. | `SNIP-PROB-001` | verificata |

## Claim esclusi

- una frequenza osservata non è automaticamente la probabilità vera;
- un posterior alto non dimostra che il modello di likelihood sia corretto;
- indipendenza condizionata non viene assunta senza dichiarazione;
- correlazione non implica causalità;
- una densità continua non è una probabilità puntuale;
- la likelihood non è un posterior senza prior e normalizzazione;
- la legge dei grandi numeri non garantisce una deviazione piccola per ogni campione finito;
- il teorema centrale del limite non rende normale la distribuzione originale;
- un intervallo di confidenza al 95% non significa che il parametro fisso abbia probabilità 95% di trovarsi nell'intervallo osservato;
- una simulazione con seed fissato non sostituisce una dimostrazione matematica.
