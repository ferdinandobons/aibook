# Piano interno. Capitolo 67

- Domanda centrale: quale contratto costruisce Output strutturato e uso degli strumenti?
- Oggetto continuo: una chiamata a tool con schema e autorizzazione; input guida: nome, argomenti, scope e stato.
- Prerequisito stabile: Capitolo 66, Contesto lungo, retrieval e memoria.
- Gap: parsing, selezione, esecuzione e osservazione.
- Output consegnato: risultato del tool o rifiuto tracciato; consumer successivo: Capitolo 68, Protocolli e interoperabilità.
- Invariante principale: schema valido non significa permesso di eseguire il side effect.
- Visuali: TOOLS-01 e TOOLS-02, con famiglie compositive variabili.
- Snippet: code/snip_67_contract.py; output: code/outputs/SNIP-67-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Schema dell'output

- Ultima affermazione stabile: una chiamata a tool con schema e autorizzazione.
- Concetto nuovo: JSON Schema, grammar o tipi stabiliscono campi e vincoli. Validità sintattica non garantisce correttezza semantica.
- Input e shape: nome, argomenti, scope e stato.
- Operazione: parsing, selezione, esecuzione e osservazione.
- Output e shape: risultato del tool o rifiuto tracciato.
- Che cosa cambia: il passaggio specifico di «Schema dell'output».
- Invariante: schema valido non significa permesso di eseguire il side effect.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lookup consentito e refund rifiutato da allowlist; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Selezione del tool.
- Prova: SRC-67-001 e sezione pubblica corrispondente.

## Transizione 2. Selezione del tool

- Ultima affermazione stabile: una chiamata a tool con schema e autorizzazione.
- Concetto nuovo: Il modello sceglie una funzione tra opzioni descritte. Nomi, descrizioni e autorizzazioni influenzano la decisione.
- Input e shape: nome, argomenti, scope e stato.
- Operazione: parsing, selezione, esecuzione e osservazione.
- Output e shape: risultato del tool o rifiuto tracciato.
- Che cosa cambia: il passaggio specifico di «Selezione del tool».
- Invariante: schema valido non significa permesso di eseguire il side effect.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lookup consentito e refund rifiutato da allowlist; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Argomenti.
- Prova: SRC-67-002 e sezione pubblica corrispondente.

## Transizione 3. Argomenti

- Ultima affermazione stabile: una chiamata a tool con schema e autorizzazione.
- Concetto nuovo: Gli argomenti vengono estratti dal contesto e validati prima dell'esecuzione. Campi mancanti richiedono chiarimento o fallback.
- Input e shape: nome, argomenti, scope e stato.
- Operazione: parsing, selezione, esecuzione e osservazione.
- Output e shape: risultato del tool o rifiuto tracciato.
- Che cosa cambia: il passaggio specifico di «Argomenti».
- Invariante: schema valido non significa permesso di eseguire il side effect.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lookup consentito e refund rifiutato da allowlist; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Esecuzione e osservazione.
- Prova: SRC-67-003 e sezione pubblica corrispondente.

## Transizione 4. Esecuzione e osservazione

- Ultima affermazione stabile: una chiamata a tool con schema e autorizzazione.
- Concetto nuovo: Il sistema esegue il tool fuori dal modello e restituisce un risultato strutturato. Timeout ed errori devono essere rappresentati.
- Input e shape: nome, argomenti, scope e stato.
- Operazione: parsing, selezione, esecuzione e osservazione.
- Output e shape: risultato del tool o rifiuto tracciato.
- Che cosa cambia: il passaggio specifico di «Esecuzione e osservazione».
- Invariante: schema valido non significa permesso di eseguire il side effect.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lookup consentito e refund rifiutato da allowlist; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Idempotenza e side effect.
- Prova: SRC-67-004 e sezione pubblica corrispondente.

## Transizione 5. Idempotenza e side effect

- Ultima affermazione stabile: una chiamata a tool con schema e autorizzazione.
- Concetto nuovo: Operazioni di lettura e scrittura hanno rischi differenti. Conferma, deduplicazione e transaction ID impediscono ripetizioni non desiderate.
- Input e shape: nome, argomenti, scope e stato.
- Operazione: parsing, selezione, esecuzione e osservazione.
- Output e shape: risultato del tool o rifiuto tracciato.
- Che cosa cambia: il passaggio specifico di «Idempotenza e side effect».
- Invariante: schema valido non significa permesso di eseguire il side effect.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: lookup consentito e refund rifiutato da allowlist; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Protocolli e interoperabilità.
- Prova: SRC-67-001 e sezione pubblica corrispondente.
