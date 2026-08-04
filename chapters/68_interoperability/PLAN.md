# Piano editoriale. Capitolo 68

## Obiettivo didattico

Seguire **Protocolli e interoperabilità** da capability, schema, token e policy a messaggio accettato o errore di protocollo, osservando negoziazione, encoding, autorizzazione e compatibilità senza oltrepassare questo limite: compatibilità sintattica non garantisce semantica o autorizzazione.

## Prerequisiti reali

- Capitolo 67: Output strutturato e uso degli strumenti

## Percorso della lezione

1. **Contratti tra componenti.** Un protocollo definisce messaggi, capability, versioni ed errori tra modello, client, server e tool. Prova: SRC-68-001.
2. **Model Context Protocol.** MCP organizza risorse, prompt e tool esposti da server. La versione della specifica e il trasporto devono essere dichiarati. Prova: SRC-68-001.
3. **Agent-to-agent.** Protocolli A2A e famiglie affini descrivono discovery, task, messaggi e artefatti tra agenti. Prova: SRC-68-002.
4. **Identità e autorizzazione.** Interoperabilità non implica fiducia. Token, scope, provenance e policy devono attraversare ogni hop. Prova: SRC-68-003.
5. **Compatibilità ed evoluzione.** Version e capability negotiation rendono esplicita l'incompatibilità. Una versione non supportata non deve proseguire silenziosamente. Prova: SRC-68-001.

## Prove e artefatti

- riferimento minimo: `code/snip_68_contract.py`; test: `code/test_68_contract.py`; output: `code/outputs/SNIP-68-001.txt`.
- visuali candidate: INTEROPERA-01, INTEROPERA-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
