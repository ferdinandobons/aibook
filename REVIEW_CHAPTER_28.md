# Pacchetto di review. Capitolo 28

Il branch di produzione contiene la candidatura `0.5.0-rc5` del Capitolo 28, riscritta per rendere il meccanismo accessibile anche a un lettore che non padroneggia ancora algebra lineare e API PyTorch.

## Percorso consigliato

1. `chapters/28_attention/REVIEW.md`;
2. `chapters/28_attention/CHAPTER.md`;
3. `chapters/28_attention/TEXT_AUDIT.md`;
4. `docs/02_STILE_E_QA_TESTO.md`;
5. `docs/03_VISUALI.md`;
6. `assets/chapters/28_attention/ATT-01/candidate-v2.png`;
7. `assets/chapters/28_attention/ATT-02/candidate-v2.png`;
8. `chapters/28_attention/code/`;
9. `chapters/28_attention/CLAIMS.md` e fonti.

## Novità della candidatura

La versione `0.4.0-rc4` aveva già eliminato la frammentazione e la voce da documentazione, ma richiedeva ancora una familiarità implicita con token, vettori, shape, prodotto scalare, softmax e PyTorch.

La versione `0.5.0-rc5`:

- parte dalla frase `Il pacco non è arrivato`;
- spiega token e vettore prima di usarli;
- traduce le shape in righe e valori per riga;
- presenta query, key e value come ruoli matematici;
- spiega il prodotto scalare come moltiplicazione e somma;
- spiega score e softmax in parole prima delle formule;
- separa la derivazione sulla varianza come approfondimento;
- presenta la formula come riassunto di passaggi già eseguiti;
- spiega la causal mask come divieto di leggere il futuro;
- mostra un solo snippet completo nel corpo;
- rinvia gli altri controlli agli artefatti del codice;
- introduce il costo quadratico attraverso il numero di coppie da confrontare;
- registra una review specifica per il lettore non esperto.

## Stato delle immagini

- `ATT-01/candidate-v2.png`: validata tecnicamente nella versione precedente, controllo incrociato riaperto;
- `ATT-02/candidate-v2.png`: validata tecnicamente nella versione precedente, controllo incrociato riaperto.

`ATT-01` usa ancora le label `consumer 1` e `consumer 2`. La nuova prosa le localizza una sola volta, ma `posizione 1` e `posizione 2` sarebbero più coerenti con il lessico accessibile della candidatura.

## Stato del codice

I tre snippet e i test non sono stati modificati. La lezione mostra integralmente soltanto `SNIP-ATT-001`; `SNIP-ATT-002` e `SNIP-ATT-003` restano richiamati come controlli verificabili nel repository.

Non viene dichiarata una nuova esecuzione per la sola riscrittura editoriale. Restano validi gli output e i test già registrati.

## Domande principali per la review

- Il problema dell'attention è comprensibile prima dei vettori?
- Query, key e value possono essere spiegate senza formula?
- Il percorso score, scaling, softmax e somma pesata resta continuo?
- L'approfondimento matematico è utile senza diventare un prerequisito?
- La causal mask è chiara prima della notazione?
- Il passaggio a PyTorch conferma il meccanismo anziché sostituirlo?
- Il testo suona come prosa tecnica italiana naturale?

## Confine

Il pacchetto non contiene render di pagine o mockup editoriali. Contiene Markdown, figure tecniche, codice, test, output, fonti e audit.

## Regole canoniche pertinenti

- `docs/02_STILE_E_QA_TESTO.md`;
- `docs/03_VISUALI.md`;
- `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`.
