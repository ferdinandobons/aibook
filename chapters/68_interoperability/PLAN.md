# Piano interno. Capitolo 68

- Domanda centrale: quale contratto costruisce Protocolli e interoperabilità?
- Oggetto continuo: un messaggio tra componenti con identità e versione; input guida: capability, schema, token e policy.
- Prerequisito stabile: Capitolo 67, Output strutturato e uso degli strumenti.
- Gap: negoziazione, encoding, autorizzazione e compatibilità.
- Output consegnato: messaggio accettato o errore di protocollo; consumer successivo: Capitolo 69, Ciclo agentico, pianificazione e verifica.
- Invariante principale: compatibilità sintattica non garantisce semantica o autorizzazione.
- Visuali: INTEROPERA-01 e INTEROPERA-02, con famiglie compositive variabili.
- Snippet: code/snip_68_contract.py; output: code/outputs/SNIP-68-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Contratti tra componenti

- Ultima affermazione stabile: un messaggio tra componenti con identità e versione.
- Concetto nuovo: Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool.
- Input e shape: capability, schema, token e policy.
- Operazione: negoziazione, encoding, autorizzazione e compatibilità.
- Output e shape: messaggio accettato o errore di protocollo.
- Che cosa cambia: il passaggio specifico di «Contratti tra componenti».
- Invariante: compatibilità sintattica non garantisce semantica o autorizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due versioni dello schema con campo obbligatorio mancante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Model Context Protocol.
- Prova: SRC-68-001 e sezione pubblica corrispondente.

## Transizione 2. Model Context Protocol

- Ultima affermazione stabile: un messaggio tra componenti con identità e versione.
- Concetto nuovo: MCP organizza risorse, prompt e tool esposti da server. La versione della specifica e il trasporto devono essere dichiarati.
- Input e shape: capability, schema, token e policy.
- Operazione: negoziazione, encoding, autorizzazione e compatibilità.
- Output e shape: messaggio accettato o errore di protocollo.
- Che cosa cambia: il passaggio specifico di «Model Context Protocol».
- Invariante: compatibilità sintattica non garantisce semantica o autorizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due versioni dello schema con campo obbligatorio mancante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Agent-to-agent.
- Prova: SRC-68-001 e sezione pubblica corrispondente.

## Transizione 3. Agent-to-agent

- Ultima affermazione stabile: un messaggio tra componenti con identità e versione.
- Concetto nuovo: Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti.
- Input e shape: capability, schema, token e policy.
- Operazione: negoziazione, encoding, autorizzazione e compatibilità.
- Output e shape: messaggio accettato o errore di protocollo.
- Che cosa cambia: il passaggio specifico di «Agent-to-agent».
- Invariante: compatibilità sintattica non garantisce semantica o autorizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due versioni dello schema con campo obbligatorio mancante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Identità e autorizzazione.
- Prova: SRC-68-002 e sezione pubblica corrispondente.

## Transizione 4. Identità e autorizzazione

- Ultima affermazione stabile: un messaggio tra componenti con identità e versione.
- Concetto nuovo: Interoperabilità non implica fiducia. Token, scope, provenance e policy devono attraversare ogni hop.
- Input e shape: capability, schema, token e policy.
- Operazione: negoziazione, encoding, autorizzazione e compatibilità.
- Output e shape: messaggio accettato o errore di protocollo.
- Che cosa cambia: il passaggio specifico di «Identità e autorizzazione».
- Invariante: compatibilità sintattica non garantisce semantica o autorizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due versioni dello schema con campo obbligatorio mancante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Compatibilità ed evoluzione.
- Prova: SRC-68-003 e sezione pubblica corrispondente.

## Transizione 5. Compatibilità ed evoluzione

- Ultima affermazione stabile: un messaggio tra componenti con identità e versione.
- Concetto nuovo: Versioning, feature negotiation e fallback impediscono che un nuovo campo cambi silenziosamente il significato del workflow.
- Input e shape: capability, schema, token e policy.
- Operazione: negoziazione, encoding, autorizzazione e compatibilità.
- Output e shape: messaggio accettato o errore di protocollo.
- Che cosa cambia: il passaggio specifico di «Compatibilità ed evoluzione».
- Invariante: compatibilità sintattica non garantisce semantica o autorizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due versioni dello schema con campo obbligatorio mancante; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Ciclo agentico, pianificazione e verifica.
- Prova: SRC-68-004 e sezione pubblica corrispondente.
