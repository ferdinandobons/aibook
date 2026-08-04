# Piano interno. Capitolo 38

- Domanda centrale: quale contratto costruisce Posizione e contesto lungo?
- Oggetto continuo: la relazione tra posizione e rappresentazione del token; input guida: query, key e indice di posizione.
- Prerequisito stabile: Capitolo 37, Anatomia del blocco moderno.
- Gap: posizione assoluta, relativa, RoPE o bias.
- Output consegnato: score dipendente dalla posizione; consumer successivo: Capitolo 39, Varianti dell'attention e gestione KV.
- Invariante principale: estendere il contesto richiede una misura fuori dalla lunghezza addestrata.
- Visuali: POS-01 e POS-02, con famiglie compositive variabili.
- Snippet: code/snip_38_contract.py; output: code/outputs/SNIP-38-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Posizione assoluta

- Ultima affermazione stabile: la relazione tra posizione e rappresentazione del token.
- Concetto nuovo: Embedding appresi o sinusoidali aggiungono un segnale legato all'indice.
- Input e shape: query, key e indice di posizione.
- Operazione: posizione assoluta, relativa, RoPE o bias.
- Output e shape: score dipendente dalla posizione.
- Che cosa cambia: il passaggio specifico di «Posizione assoluta».
- Invariante: estendere il contesto richiede una misura fuori dalla lunghezza addestrata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso vettore ruotato a due posizioni diverse; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Posizione relativa.
- Prova: SRC-38-001 e sezione pubblica corrispondente.

## Transizione 2. Posizione relativa

- Ultima affermazione stabile: la relazione tra posizione e rappresentazione del token.
- Concetto nuovo: Bias o rappresentazioni relative modificano i confronti in funzione della distanza.
- Input e shape: query, key e indice di posizione.
- Operazione: posizione assoluta, relativa, RoPE o bias.
- Output e shape: score dipendente dalla posizione.
- Che cosa cambia: il passaggio specifico di «Posizione relativa».
- Invariante: estendere il contesto richiede una misura fuori dalla lunghezza addestrata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso vettore ruotato a due posizioni diverse; provare anche una condizione incoerente e osservare il controllo.
- Consumer: RoPE.
- Prova: SRC-38-002 e sezione pubblica corrispondente.

## Transizione 3. RoPE

- Ultima affermazione stabile: la relazione tra posizione e rappresentazione del token.
- Concetto nuovo: Rotazioni di query e key rendono il prodotto scalare dipendente dall'offset relativo.
- Input e shape: query, key e indice di posizione.
- Operazione: posizione assoluta, relativa, RoPE o bias.
- Output e shape: score dipendente dalla posizione.
- Che cosa cambia: il passaggio specifico di «RoPE».
- Invariante: estendere il contesto richiede una misura fuori dalla lunghezza addestrata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso vettore ruotato a due posizioni diverse; provare anche una condizione incoerente e osservare il controllo.
- Consumer: ALiBi.
- Prova: SRC-38-003 e sezione pubblica corrispondente.

## Transizione 4. ALiBi

- Ultima affermazione stabile: la relazione tra posizione e rappresentazione del token.
- Concetto nuovo: Bias lineari penalizzano distanze maggiori con slope per head.
- Input e shape: query, key e indice di posizione.
- Operazione: posizione assoluta, relativa, RoPE o bias.
- Output e shape: score dipendente dalla posizione.
- Che cosa cambia: il passaggio specifico di «ALiBi».
- Invariante: estendere il contesto richiede una misura fuori dalla lunghezza addestrata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso vettore ruotato a due posizioni diverse; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Estensione e valutazione.
- Prova: SRC-38-004 e sezione pubblica corrispondente.

## Transizione 5. Estensione e valutazione

- Ultima affermazione stabile: la relazione tra posizione e rappresentazione del token.
- Concetto nuovo: Positional interpolation e metodi affini estendono gli indici, ma l'uso effettivo del contesto deve essere misurato.
- Input e shape: query, key e indice di posizione.
- Operazione: posizione assoluta, relativa, RoPE o bias.
- Output e shape: score dipendente dalla posizione.
- Che cosa cambia: il passaggio specifico di «Estensione e valutazione».
- Invariante: estendere il contesto richiede una misura fuori dalla lunghezza addestrata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lo stesso vettore ruotato a due posizioni diverse; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Varianti dell'attention e gestione KV.
- Prova: SRC-38-001 e sezione pubblica corrispondente.
