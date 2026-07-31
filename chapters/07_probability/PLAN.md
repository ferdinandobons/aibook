# Piano interno. Capitolo 7

## Identità

- `chapter_id`: `CH-P02-PROBABILITY`
- Parte: `P02`, Matematica, informazione e calcolo
- Titolo: Probabilità, statistica e inferenza
- Profilo: fondamento probabilistico per modelli, dati e valutazione
- Domanda centrale: come rappresentiamo l'incertezza, aggiorniamo una credenza con nuove osservazioni e distinguiamo una distribuzione da una stima ottenuta su un campione?
- Oggetto continuo: una richiesta `Il pacco non è arrivato`, uno stato non osservato `problema di consegna reale` e due evidenze osservabili

## Prerequisiti

- algebra elementare;
- somme e prodotti;
- vettori e media;
- Python e PyTorch soltanto per lo snippet.

## Oggetto numerico

```text
H: esiste un problema di consegna reale
P(H) = 0,20

E1: il testo contiene una formulazione compatibile con mancata consegna
P(E1|H) = 0,80
P(E1|not H) = 0,10
P(H|E1) = 2/3

E2: il tracking è fermo
P(E2|H) = 0,70
P(E2|not H) = 0,20
P(H|E1,E2) = 0,875
```

Il secondo aggiornamento assume indipendenza condizionata di `E1` ed `E2` dato lo stato. L'assunzione viene dichiarata come parte del modello, non come fatto sul mondo reale.

## Stato finale del lettore

Il lettore sa:

1. distinguere esito, evento, variabile aleatoria e distribuzione;
2. leggere probabilità congiunte, marginali e condizionate;
3. applicare legge della probabilità totale e teorema di Bayes;
4. distinguere indipendenza marginale e condizionata;
5. interpretare valore atteso, varianza e covarianza;
6. distinguere massa di probabilità e densità;
7. separare popolazione, campione, parametro, statistica e stimatore;
8. interpretare la likelihood come funzione del parametro a dati fissati;
9. ricavare la MLE Bernoulli come media campionaria;
10. comprendere il ruolo di legge dei grandi numeri e teorema centrale del limite con condizioni esplicite;
11. distinguere in modo operativo inferenza frequentista e bayesiana;
12. usare `torch.distributions.Bernoulli` per momenti, log-probabilità e campionamento.

## Progressione

1. Incertezza su uno stato non osservato.
2. Spazio degli esiti ed eventi.
3. Distribuzione congiunta e marginalizzazione.
4. Probabilità condizionata.
5. Legge totale e Bayes.
6. Indipendenza e assunzioni del modello.
7. Variabili aleatorie e distribuzioni discrete o continue.
8. Valore atteso, varianza e covarianza.
9. Popolazione, campione e statistiche.
10. Likelihood e massima verosimiglianza.
11. Campionamento, legge dei grandi numeri e CLT.
12. Inferenza frequentista e bayesiana.
13. PyTorch e controlli numerici.

## Visuali

### `PROB-01`. Dal prior al posterior

Tabella congiunta per `H` ed `E1`, marginalizzazione dell'evidenza e normalizzazione della colonna osservata. Il flusso deve mostrare numeratore `0,16`, evidenza `0,24` e posterior `0,6667`.

### `PROB-02`. Distribuzione, campione e stimatore

Mostra una Bernoulli con `p=0,30`, tre campioni di dimensione `10`, `100` e `10 000`, le rispettive medie osservate e la distinzione tra parametro fisso e statistica variabile.

## Codice

### `SNIP-PROB-001`

- aggiornamento di Bayes esatto;
- secondo aggiornamento sequenziale;
- MLE Bernoulli come media di venti osservazioni;
- log-likelihood con `torch.distributions.Bernoulli`;
- momenti teorici della Bernoulli;
- simulazioni con campioni di dimensione `10`, `100` e `10 000`;
- sei test.

## Gate specifici

- probabilità e frequenza osservata non vengono trattate come sinonimi;
- una probabilità condizionata dichiara sempre la condizione;
- la likelihood non viene normalizzata sui parametri come se fosse un posterior;
- densità e probabilità puntuale non vengono confuse nel caso continuo;
- indipendenza condizionata viene dichiarata come assunzione;
- correlazione non viene presentata come causalità;
- LLN e CLT includono condizioni e non diventano garanzie su un singolo campione;
- un intervallo di confidenza non viene interpretato come probabilità posteriore del parametro;
- il posterior dipende dal prior e dal modello di likelihood;
- i risultati Monte Carlo sono marcati come eseguiti nell'ambiente registrato.
