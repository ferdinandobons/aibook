# Audit del testo. Capitolo 7

## Stato

- Versione: `0.2.0-rc1`
- Data: 31 luglio 2026
- Esito fattuale e matematico: **superato**
- Esito didattico: **superato dopo seconda lettura**
- Gate anti-template: **superato**
- Esito editoriale e linguistico: **superato**
- Chiarezza per lettore non esperto: **superata**
- Codice: sei test registrati, esito positivo
- Visuali: validate tecnicamente
- Revisione autoriale: aperta

## Prima lettura critica

Difetti corretti:

1. prior, likelihood e posterior comparivano troppo vicini;
2. congiunta, marginale e condizionata richiedevano una tabella comune;
3. l'indipendenza condizionata del secondo aggiornamento doveva essere marcata come assunzione;
4. massa discreta e densità continua andavano separate;
5. la likelihood poteva sembrare una distribuzione normalizzata sul parametro;
6. parametro, stimatore e stima non erano ancora distinti;
7. LLN e CLT richiedevano condizioni esplicite;
8. confidenza frequentista e credibilità bayesiana dovevano restare separate;
9. `PROB-01` aveva contrasto insufficiente in alcune intestazioni;
10. `PROB-02` usava l'abbreviazione `SE` prima di spiegarla.

Correzioni applicate:

- costruita la tabella congiunta prima del posterior;
- mantenuto lo stesso caso numerico lungo Bayes;
- dichiarata l'indipendenza condizionata come parte del modello;
- distinte PMF, PDF e CDF;
- definita la likelihood a dati fissati;
- separati popolazione, campione, parametro, statistica, stimatore e stima;
- aggiunte condizioni a LLN e CLT;
- separate le due interpretazioni degli intervalli;
- corretto il contrasto di `PROB-01`;
- sostituito `SE` con `deviazione della media`.

## Seconda lettura integrale

### Lettore non esperto

- [x] problema concreto prima della notazione;
- [x] esiti ed eventi prima degli assiomi;
- [x] prior spiegato in parole;
- [x] condizionata letta come domanda;
- [x] Bayes ricostruito sulla tabella;
- [x] Bernoulli introdotta dopo il caso binario;
- [x] campione e parametro distinti prima della MLE;
- [x] codice dopo il meccanismo.

### Lettore tecnico

- [x] tabella congiunta normalizzata;
- [x] legge totale e Bayes corretti;
- [x] indipendenza marginale e condizionata distinte;
- [x] PMF, densità e CDF distinte;
- [x] aspettativa, varianza e covarianza definite;
- [x] MLE Bernoulli derivata con casi di bordo;
- [x] LLN e CLT formulate con ipotesi;
- [x] intervalli frequentisti e bayesiani separati;
- [x] API PyTorch verificate sulla stable 2.13.

## Audit numerico

- [x] `P(H,E1)=0,16`;
- [x] `P(not H,E1)=0,08`;
- [x] `P(E1)=0,24`;
- [x] `P(H|E1)=2/3`;
- [x] secondo posterior `0,875`;
- [x] MLE Bernoulli `7/20=0,35`;
- [x] media teorica `0,30`;
- [x] varianza teorica `0,21`;
- [x] medie eseguite `0,60`, `0,32` e `0,3042`;
- [x] valori delle due visuali ricontrollati.

## Audit fattuale e linguistico

- [x] fonti accademiche e istituzionali;
- [x] PyTorch stable ricontrollata il 31 luglio 2026;
- [x] ambiente eseguito distinto dalla documentazione;
- [x] italiano scritto direttamente;
- [x] nessun em dash;
- [x] termini tecnici definiti;
- [x] nessun ritmo da checklist nel testo pubblico;
- [x] lettura ad alta voce superata internamente.

## Verdetto

Il testo `0.2.0-rc1` supera i gate fattuali, matematici, didattici, anti-template, editoriali, linguistici e di accessibilità. Può essere sottoposto alla revisione autoriale insieme alle visuali e al codice.
