# Registro dei claim. Capitolo 71

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `agent_eval` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-71-01

- Affermazione esatta: Osservazioni, azioni, tool result e reward formano esempi sequenziali. Logging incompleto rende impossibile ricostruire il fallimento.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-71-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; AgentBench : Evaluating LLMs as Agents; 2 LLM-as-Agent: Definition and Preliminary; 3 Composition of AgentBench : A Brief Look (claim collegato alla sezione «Traiettorie come dati» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-71-02

- Affermazione esatta: Traiettorie riuscite possono essere imitate. Il dataset deve includere recovery, errori e decisioni di non agire.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-71-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; WebArena : A Realistic Web Environment for Building Autonomous Agents; 2 WebArena : Websites as an Environment for Autonomous Agents; 2.1 Controlling Agents through High-level Natural Language (claim collegato alla sezione «Imitation e SFT» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-71-03

- Affermazione esatta: Reward verificabili o simulati aggiornano policy multi-step. Il modello può sfruttare bug dell'ambiente o del checker.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-71-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2.1 Benchmark Construction; Appendix A Benchmark Details; A.4 Evaluation Procedure (claim collegato alla sezione «RL in ambienti» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-71-04

- Affermazione esatta: Success rate, step, costo e side effect devono essere misurati. Task statici rischiano contaminazione e overfitting.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-71-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Benchmark agentici» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-71-05

- Affermazione esatta: Reset, seed, timeout, credenziali e versioni dei servizi sono parte del protocollo sperimentale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-71-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; AgentBench : Evaluating LLMs as Agents; 2 LLM-as-Agent: Definition and Preliminary; 3 Composition of AgentBench : A Brief Look (claim collegato alla sezione «Evaluation harness» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-71-CODE

- Affermazione esatta: lo snippet snip_71_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_71_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
