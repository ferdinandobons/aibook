# Piano interno. Capitolo 76

- Domanda centrale: quale contratto costruisce Decoding e generazione vincolata?
- Oggetto continuo: logits e spazio delle sequenze ammissibili; input guida: logits, prefisso, temperatura e vincolo.
- Prerequisito stabile: Capitolo 75, Modelli low-bit nativi e co-design numerico.
- Gap: greedy, beam, sampling, penalty e stop.
- Output consegnato: token scelto, sequenza e metrica di costo; consumer successivo: Capitolo 77, Speculative e parallel decoding.
- Invariante principale: il decoding modifica la traiettoria, non corregge il modello a monte.
- Visuali: DECODING-01 e DECODING-02, con famiglie compositive variabili.
- Snippet: code/snip_76_contract.py; output: code/outputs/SNIP-76-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Greedy e beam search

- Ultima affermazione stabile: logits e spazio delle sequenze ammissibili.
- Concetto nuovo: Greedy sceglie il massimo locale; beam mantiene più prefissi secondo score accumulati e criteri di lunghezza.
- Input e shape: logits, prefisso, temperatura e vincolo.
- Operazione: greedy, beam, sampling, penalty e stop.
- Output e shape: token scelto, sequenza e metrica di costo.
- Che cosa cambia: il passaggio specifico di «Greedy e beam search».
- Invariante: il decoding modifica la traiettoria, non corregge il modello a monte.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: greedy e top-p sullo stesso vettore di logits; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sampling.
- Prova: SRC-76-001 e sezione pubblica corrispondente.

## Transizione 2. Sampling

- Ultima affermazione stabile: logits e spazio delle sequenze ammissibili.
- Concetto nuovo: Temperature, top-k e top-p modificano la distribuzione prima dell'estrazione. Seed e backend influenzano la riproducibilità.
- Input e shape: logits, prefisso, temperatura e vincolo.
- Operazione: greedy, beam, sampling, penalty e stop.
- Output e shape: token scelto, sequenza e metrica di costo.
- Che cosa cambia: il passaggio specifico di «Sampling».
- Invariante: il decoding modifica la traiettoria, non corregge il modello a monte.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: greedy e top-p sullo stesso vettore di logits; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Penalità e stop.
- Prova: SRC-76-002 e sezione pubblica corrispondente.

## Transizione 3. Penalità e stop

- Ultima affermazione stabile: logits e spazio delle sequenze ammissibili.
- Concetto nuovo: Repetition penalty, stop sequence e minimum length intervengono in punti differenti e possono interagire.
- Input e shape: logits, prefisso, temperatura e vincolo.
- Operazione: greedy, beam, sampling, penalty e stop.
- Output e shape: token scelto, sequenza e metrica di costo.
- Che cosa cambia: il passaggio specifico di «Penalità e stop».
- Invariante: il decoding modifica la traiettoria, non corregge il modello a monte.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: greedy e top-p sullo stesso vettore di logits; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Constrained decoding.
- Prova: SRC-76-003 e sezione pubblica corrispondente.

## Transizione 4. Constrained decoding

- Ultima affermazione stabile: logits e spazio delle sequenze ammissibili.
- Concetto nuovo: Grammar, automi e schema limitano i token ammessi. Validità strutturale non garantisce argomenti corretti.
- Input e shape: logits, prefisso, temperatura e vincolo.
- Operazione: greedy, beam, sampling, penalty e stop.
- Output e shape: token scelto, sequenza e metrica di costo.
- Che cosa cambia: il passaggio specifico di «Constrained decoding».
- Invariante: il decoding modifica la traiettoria, non corregge il modello a monte.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: greedy e top-p sullo stesso vettore di logits; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Metriche.
- Prova: SRC-76-004 e sezione pubblica corrispondente.

## Transizione 5. Metriche

- Ultima affermazione stabile: logits e spazio delle sequenze ammissibili.
- Concetto nuovo: Qualità, diversità, latency, token per secondo e probabilità della sequenza devono essere letti insieme.
- Input e shape: logits, prefisso, temperatura e vincolo.
- Operazione: greedy, beam, sampling, penalty e stop.
- Output e shape: token scelto, sequenza e metrica di costo.
- Che cosa cambia: il passaggio specifico di «Metriche».
- Invariante: il decoding modifica la traiettoria, non corregge il modello a monte.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: greedy e top-p sullo stesso vettore di logits; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Speculative e parallel decoding.
- Prova: SRC-76-001 e sezione pubblica corrispondente.
