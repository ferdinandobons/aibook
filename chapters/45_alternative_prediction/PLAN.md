# Piano interno. Capitolo 45

- Domanda centrale: quale contratto costruisce Byte, predizione multi-token e language diffusion?
- Oggetto continuo: unità di predizione dal byte al token multiplo; input guida: byte, gerarchia, target e numero di passi.
- Prerequisito stabile: Capitolo 44, Mixture of Experts e calcolo condizionale.
- Gap: raggruppamento, multi-token prediction o diffusione discreta.
- Output consegnato: unità predette, loss e durata di decoding; consumer successivo: Capitolo 46, Supervised fine-tuning e instruction tuning.
- Invariante principale: granularità della rappresentazione e parallelismo sono assi distinti.
- Visuali: ALT-01 e ALT-02, con famiglie compositive variabili.
- Snippet: code/snip_45_contract.py; output: code/outputs/SNIP-45-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Byte e caratteri

- Ultima affermazione stabile: unità di predizione dal byte al token multiplo.
- Concetto nuovo: Modelli byte-level usano un vocabolario piccolo e sequenze più lunghe.
- Input e shape: byte, gerarchia, target e numero di passi.
- Operazione: raggruppamento, multi-token prediction o diffusione discreta.
- Output e shape: unità predette, loss e durata di decoding.
- Che cosa cambia: il passaggio specifico di «Byte e caratteri».
- Invariante: granularità della rappresentazione e parallelismo sono assi distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due byte raggruppati e due target predetti nello stesso passo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Gerarchie di byte.
- Prova: SRC-45-001 e sezione pubblica corrispondente.

## Transizione 2. Gerarchie di byte

- Ultima affermazione stabile: unità di predizione dal byte al token multiplo.
- Concetto nuovo: Patch fisse o dinamiche riducono la lunghezza vista dal modello globale.
- Input e shape: byte, gerarchia, target e numero di passi.
- Operazione: raggruppamento, multi-token prediction o diffusione discreta.
- Output e shape: unità predette, loss e durata di decoding.
- Che cosa cambia: il passaggio specifico di «Gerarchie di byte».
- Invariante: granularità della rappresentazione e parallelismo sono assi distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due byte raggruppati e due target predetti nello stesso passo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Predizione multi-token.
- Prova: SRC-45-002 e sezione pubblica corrispondente.

## Transizione 3. Predizione multi-token

- Ultima affermazione stabile: unità di predizione dal byte al token multiplo.
- Concetto nuovo: Head aggiuntive predicono più offset futuri e forniscono segnali oltre il token immediato.
- Input e shape: byte, gerarchia, target e numero di passi.
- Operazione: raggruppamento, multi-token prediction o diffusione discreta.
- Output e shape: unità predette, loss e durata di decoding.
- Che cosa cambia: il passaggio specifico di «Predizione multi-token».
- Invariante: granularità della rappresentazione e parallelismo sono assi distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due byte raggruppati e due target predetti nello stesso passo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Diffusione linguistica.
- Prova: SRC-45-003 e sezione pubblica corrispondente.

## Transizione 4. Diffusione linguistica

- Ultima affermazione stabile: unità di predizione dal byte al token multiplo.
- Concetto nuovo: Processi continui, discreti o masked denoisano più posizioni attraverso step iterativi.
- Input e shape: byte, gerarchia, target e numero di passi.
- Operazione: raggruppamento, multi-token prediction o diffusione discreta.
- Output e shape: unità predette, loss e durata di decoding.
- Che cosa cambia: il passaggio specifico di «Diffusione linguistica».
- Invariante: granularità della rappresentazione e parallelismo sono assi distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due byte raggruppati e due target predetti nello stesso passo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Assi separati.
- Prova: SRC-45-004 e sezione pubblica corrispondente.

## Transizione 5. Assi separati

- Ultima affermazione stabile: unità di predizione dal byte al token multiplo.
- Concetto nuovo: Unità del testo, architettura e obiettivo di predizione sono scelte distinte che interagiscono.
- Input e shape: byte, gerarchia, target e numero di passi.
- Operazione: raggruppamento, multi-token prediction o diffusione discreta.
- Output e shape: unità predette, loss e durata di decoding.
- Che cosa cambia: il passaggio specifico di «Assi separati».
- Invariante: granularità della rappresentazione e parallelismo sono assi distinti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due byte raggruppati e due target predetti nello stesso passo; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Supervised fine-tuning e instruction tuning.
- Prova: SRC-45-001 e sezione pubblica corrispondente.
