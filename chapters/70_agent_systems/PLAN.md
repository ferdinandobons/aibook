# Piano editoriale. Capitolo 70

## Obiettivo didattico

Seguire **Multi-agent, browser, computer e code agents** da task, ruoli, browser, codice e handoff a risultato con responsabilità e log per componente, osservando delega, comunicazione, esecuzione e aggregazione senza oltrepassare questo limite: più agenti ampliano anche superficie e costo dell'errore.

## Prerequisiti reali

- Capitolo 67: Output strutturato e uso degli strumenti
- Capitolo 69: Ciclo agentico, pianificazione e verifica

## Percorso della lezione

1. **Browser agent.** L'agente interpreta pagine, link e form e deve distinguere contenuto della pagina da istruzioni autorizzate. Prova: SRC-70-001.
2. **Computer use.** Screenshot, coordinate e azioni di input formano un loop percettivo. Risoluzione, focus e stato dell'interfaccia possono cambiare. Prova: SRC-70-002.
3. **Code agent.** Repository, test, shell e diff definiscono l'ambiente. Modifiche devono essere limitate, testate e revisionabili. Prova: SRC-70-003.
4. **Multi-agent.** Ruoli distinti possono parallelizzare o criticare, ma introducono comunicazione, ridondanza e propagazione degli errori. Prova: SRC-70-004.
5. **Confronto con un singolo workflow.** Il beneficio deve essere misurato rispetto a una baseline con stesso modello, tool e budget. Prova: SRC-70-001.

## Prove e artefatti

- riferimento minimo: `code/snip_70_contract.py`; test: `code/test_70_contract.py`; output: `code/outputs/SNIP-70-001.txt`.
- visuali candidate: SYSTEMS-01, SYSTEMS-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
