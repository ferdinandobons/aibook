# Piano interno. Capitolo 77

- Domanda centrale: quale contratto costruisce Speculative e parallel decoding?
- Oggetto continuo: draft e target durante il decoding speculativo; input guida: token proposti, logits draft e logits target.
- Prerequisito stabile: Capitolo 76, Decoding e generazione vincolata.
- Gap: proposta, verifica, accettazione e fallback.
- Output consegnato: token accettati, velocità e distribuzione preservata; consumer successivo: Capitolo 78, KV cache e riuso del contesto.
- Invariante principale: lo speedup richiede verifica senza cambiare il contratto di output.
- Visuali: DECODING-01 e DECODING-02, con famiglie compositive variabili.
- Snippet: code/snip_77_contract.py; output: code/outputs/SNIP-77-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Draft e target

- Ultima affermazione stabile: draft e target durante il decoding speculativo.
- Concetto nuovo: Un modello economico propone più token; il modello target li verifica in parallelo.
- Input e shape: token proposti, logits draft e logits target.
- Operazione: proposta, verifica, accettazione e fallback.
- Output e shape: token accettati, velocità e distribuzione preservata.
- Che cosa cambia: il passaggio specifico di «Draft e target».
- Invariante: lo speedup richiede verifica senza cambiare il contratto di output.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre token proposti, due accettati e uno ricalcolato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Acceptance.
- Prova: SRC-77-001 e sezione pubblica corrispondente.

## Transizione 2. Acceptance

- Ultima affermazione stabile: draft e target durante il decoding speculativo.
- Concetto nuovo: La regola di accettazione conserva esattamente la distribuzione target nel metodo speculativo standard.
- Input e shape: token proposti, logits draft e logits target.
- Operazione: proposta, verifica, accettazione e fallback.
- Output e shape: token accettati, velocità e distribuzione preservata.
- Che cosa cambia: il passaggio specifico di «Acceptance».
- Invariante: lo speedup richiede verifica senza cambiare il contratto di output.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre token proposti, due accettati e uno ricalcolato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Speedup.
- Prova: SRC-77-002 e sezione pubblica corrispondente.

## Transizione 3. Speedup

- Ultima affermazione stabile: draft e target durante il decoding speculativo.
- Concetto nuovo: Il guadagno dipende da acceptance rate, costo del draft, lunghezza proposta e hardware.
- Input e shape: token proposti, logits draft e logits target.
- Operazione: proposta, verifica, accettazione e fallback.
- Output e shape: token accettati, velocità e distribuzione preservata.
- Che cosa cambia: il passaggio specifico di «Speedup».
- Invariante: lo speedup richiede verifica senza cambiare il contratto di output.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre token proposti, due accettati e uno ricalcolato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Medusa, EAGLE e ReDrafter.
- Prova: SRC-77-003 e sezione pubblica corrispondente.

## Transizione 4. Medusa, EAGLE e ReDrafter

- Ultima affermazione stabile: draft e target durante il decoding speculativo.
- Concetto nuovo: Head multiple, feature prediction e recurrent drafter producono candidate con strutture differenti.
- Input e shape: token proposti, logits draft e logits target.
- Operazione: proposta, verifica, accettazione e fallback.
- Output e shape: token accettati, velocità e distribuzione preservata.
- Che cosa cambia: il passaggio specifico di «Medusa, EAGLE e ReDrafter».
- Invariante: lo speedup richiede verifica senza cambiare il contratto di output.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre token proposti, due accettati e uno ricalcolato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Parallel decoding.
- Prova: SRC-77-004 e sezione pubblica corrispondente.

## Transizione 5. Parallel decoding

- Ultima affermazione stabile: draft e target durante il decoding speculativo.
- Concetto nuovo: Metodi lookahead o Jacobi aggiornano più posizioni ma devono dichiarare se preservano esattamente la distribuzione originale.
- Input e shape: token proposti, logits draft e logits target.
- Operazione: proposta, verifica, accettazione e fallback.
- Output e shape: token accettati, velocità e distribuzione preservata.
- Che cosa cambia: il passaggio specifico di «Parallel decoding».
- Invariante: lo speedup richiede verifica senza cambiare il contratto di output.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre token proposti, due accettati e uno ricalcolato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: KV cache e riuso del contesto.
- Prova: SRC-77-001 e sezione pubblica corrispondente.
