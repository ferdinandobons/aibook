# Piano interno. Capitolo 52

- Domanda centrale: quale contratto costruisce Addestrare e distillare il reasoning?
- Oggetto continuo: una traccia di reasoning e la risposta che la segue; input guida: prompt, trace del teacher, answer e costo in token.
- Prerequisito stabile: Capitolo 51, Reinforcement learning con reward verificabili.
- Gap: distillazione, self-consistency e rejection sampling.
- Output consegnato: traccia selezionata, risposta e misura di costo; consumer successivo: Capitolo 53, Test-time compute, ricerca e controllo del budget.
- Invariante principale: una traccia leggibile non prova faithfulness causale.
- Visuali: TRAINING-01 e TRAINING-02, con famiglie compositive variabili.
- Snippet: code/snip_52_contract.py; output: code/outputs/SNIP-52-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Tracce e risposte

- Ultima affermazione stabile: una traccia di reasoning e la risposta che la segue.
- Concetto nuovo: Una traccia di ragionamento è testo prodotto dal modello. Può aiutare il training senza costituire una prova fedele del processo interno.
- Input e shape: prompt, trace del teacher, answer e costo in token.
- Operazione: distillazione, self-consistency e rejection sampling.
- Output e shape: traccia selezionata, risposta e misura di costo.
- Che cosa cambia: il passaggio specifico di «Tracce e risposte».
- Invariante: una traccia leggibile non prova faithfulness causale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre tracce, due concordanti, con selezione majority vote; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Distillazione.
- Prova: SRC-52-001 e sezione pubblica corrispondente.

## Transizione 2. Distillazione

- Ultima affermazione stabile: una traccia di reasoning e la risposta che la segue.
- Concetto nuovo: Un teacher produce soluzioni o distribuzioni che diventano target per uno student. Filtraggio e copertura stabiliscono cosa viene trasferito.
- Input e shape: prompt, trace del teacher, answer e costo in token.
- Operazione: distillazione, self-consistency e rejection sampling.
- Output e shape: traccia selezionata, risposta e misura di costo.
- Che cosa cambia: il passaggio specifico di «Distillazione».
- Invariante: una traccia leggibile non prova faithfulness causale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre tracce, due concordanti, con selezione majority vote; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Self-consistency e rejection sampling.
- Prova: SRC-52-004 e sezione pubblica corrispondente.

## Transizione 3. Self-consistency e rejection sampling

- Ultima affermazione stabile: una traccia di reasoning e la risposta che la segue.
- Concetto nuovo: Più candidate vengono generate e selezionate con voto o verifier. Il dataset risultante dipende dalla procedura di selezione.
- Input e shape: prompt, trace del teacher, answer e costo in token.
- Operazione: distillazione, self-consistency e rejection sampling.
- Output e shape: traccia selezionata, risposta e misura di costo.
- Che cosa cambia: il passaggio specifico di «Self-consistency e rejection sampling».
- Invariante: una traccia leggibile non prova faithfulness causale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre tracce, due concordanti, con selezione majority vote; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Faithfulness.
- Prova: SRC-52-002 e sezione pubblica corrispondente.

## Transizione 4. Faithfulness

- Ultima affermazione stabile: una traccia di reasoning e la risposta che la segue.
- Concetto nuovo: Una spiegazione corretta può essere post-hoc. Valutare risposta e fedeltà richiede esperimenti differenti.
- Input e shape: prompt, trace del teacher, answer e costo in token.
- Operazione: distillazione, self-consistency e rejection sampling.
- Output e shape: traccia selezionata, risposta e misura di costo.
- Che cosa cambia: il passaggio specifico di «Faithfulness».
- Invariante: una traccia leggibile non prova faithfulness causale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre tracce, due concordanti, con selezione majority vote; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Costo e lunghezza.
- Prova: SRC-52-003 e sezione pubblica corrispondente.

## Transizione 5. Costo e lunghezza

- Ultima affermazione stabile: una traccia di reasoning e la risposta che la segue.
- Concetto nuovo: Tracce più lunghe aumentano token e latenza. Il training deve distinguere utilità della risposta e budget del processo.
- Input e shape: prompt, trace del teacher, answer e costo in token.
- Operazione: distillazione, self-consistency e rejection sampling.
- Output e shape: traccia selezionata, risposta e misura di costo.
- Che cosa cambia: il passaggio specifico di «Costo e lunghezza».
- Invariante: una traccia leggibile non prova faithfulness causale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre tracce, due concordanti, con selezione majority vote; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Test-time compute, ricerca e controllo del budget.
- Prova: SRC-52-001 e sezione pubblica corrispondente.
