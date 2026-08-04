# Piano interno. Capitolo 56

- Domanda centrale: quale contratto costruisce Vision encoder e Vision-Language Model?
- Oggetto continuo: patch visivi e token linguistici in un VLM; input guida: immagine, patch, testo e query.
- Prerequisito stabile: Capitolo 55, Fondamenti della multimodalità.
- Gap: vision encoder, projector e cross-attention.
- Output consegnato: token visivi, risposta e grounding; consumer successivo: Capitolo 57, Generazione e modifica delle immagini.
- Invariante principale: una risposta linguistica non certifica che il dettaglio sia nell'immagine.
- Visuali: VLM-01 e VLM-02, con famiglie compositive variabili.
- Snippet: code/snip_56_contract.py; output: code/outputs/SNIP-56-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Patch e vision encoder

- Ultima affermazione stabile: patch visivi e token linguistici in un VLM.
- Concetto nuovo: Una immagine viene trasformata in patch o feature. Risoluzione, positional encoding e pooling definiscono la sequenza visiva.
- Input e shape: immagine, patch, testo e query.
- Operazione: vision encoder, projector e cross-attention.
- Output e shape: token visivi, risposta e grounding.
- Che cosa cambia: il passaggio specifico di «Patch e vision encoder».
- Invariante: una risposta linguistica non certifica che il dettaglio sia nell'immagine.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due patch aggregate e una domanda con riferimento locale; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Dual encoder.
- Prova: SRC-56-001 e sezione pubblica corrispondente.

## Transizione 2. Dual encoder

- Ultima affermazione stabile: patch visivi e token linguistici in un VLM.
- Concetto nuovo: CLIP allinea immagine e testo con una loss contrastiva. I due encoder supportano retrieval efficiente ma interagiscono tardi.
- Input e shape: immagine, patch, testo e query.
- Operazione: vision encoder, projector e cross-attention.
- Output e shape: token visivi, risposta e grounding.
- Che cosa cambia: il passaggio specifico di «Dual encoder».
- Invariante: una risposta linguistica non certifica che il dettaglio sia nell'immagine.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due patch aggregate e una domanda con riferimento locale; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Projector.
- Prova: SRC-56-002 e sezione pubblica corrispondente.

## Transizione 3. Projector

- Ultima affermazione stabile: patch visivi e token linguistici in un VLM.
- Concetto nuovo: Architetture modulari proiettano feature visive nella dimensione del language model. Il projector stabilisce capacità e numero di visual token.
- Input e shape: immagine, patch, testo e query.
- Operazione: vision encoder, projector e cross-attention.
- Output e shape: token visivi, risposta e grounding.
- Che cosa cambia: il passaggio specifico di «Projector».
- Invariante: una risposta linguistica non certifica che il dettaglio sia nell'immagine.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due patch aggregate e una domanda con riferimento locale; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Q-Former e cross-attention.
- Prova: SRC-56-003 e sezione pubblica corrispondente.

## Transizione 4. Q-Former e cross-attention

- Ultima affermazione stabile: patch visivi e token linguistici in un VLM.
- Concetto nuovo: Query apprese possono estrarre un insieme compatto di feature. Altre architetture inseriscono cross-attention dedicata.
- Input e shape: immagine, patch, testo e query.
- Operazione: vision encoder, projector e cross-attention.
- Output e shape: token visivi, risposta e grounding.
- Che cosa cambia: il passaggio specifico di «Q-Former e cross-attention».
- Invariante: una risposta linguistica non certifica che il dettaglio sia nell'immagine.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due patch aggregate e una domanda con riferimento locale; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Grounding e hallucination.
- Prova: SRC-56-004 e sezione pubblica corrispondente.

## Transizione 5. Grounding e hallucination

- Ultima affermazione stabile: patch visivi e token linguistici in un VLM.
- Concetto nuovo: Descrivere una immagine non garantisce localizzare oggetti o relazioni. Grounding, OCR e affidabilità richiedono test specifici.
- Input e shape: immagine, patch, testo e query.
- Operazione: vision encoder, projector e cross-attention.
- Output e shape: token visivi, risposta e grounding.
- Che cosa cambia: il passaggio specifico di «Grounding e hallucination».
- Invariante: una risposta linguistica non certifica che il dettaglio sia nell'immagine.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due patch aggregate e una domanda con riferimento locale; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Generazione e modifica delle immagini.
- Prova: SRC-56-001 e sezione pubblica corrispondente.
