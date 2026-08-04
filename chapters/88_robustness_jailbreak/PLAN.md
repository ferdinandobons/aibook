# Piano editoriale. Capitolo 88

## Obiettivo didattico

Seguire **Robustezza, jailbreak e attacchi adversarial** da threat model, prompt, budget e risposta a success rate, failure mode e costo della difesa, osservando jailbreak, perturbazione, difesa e adaptive evaluation senza oltrepassare questo limite: un test superato non copre minacce non incluse nel protocollo.

## Prerequisiti reali

- Capitolo 4: Come valutare criticamente un risultato di AI
- Capitolo 31: Dalla rappresentazione linguistica agli LLM
- Capitolo 72: Sicurezza operativa degli agenti

## Percorso della lezione

1. **Threat model.** Attaccante, accesso, obiettivo, budget e superficie definiscono il test. Un jailbreak testuale e un attacco ai pesi hanno contratti diversi. Prova: SRC-88-001.
2. **Perturbazioni.** Typo, parafrasi, encoding e contenuti multimodali possono aggirare filtri superficiali. Prova: SRC-88-002.
3. **Ottimizzazione adversarial.** Suffix e prompt vengono cercati per aumentare una loss di attacco. Trasferibilità e query budget devono essere riportati. Prova: SRC-88-003.
4. **Difese.** Training, filtri, classificatori e refusal possono ridurre alcuni attacchi e introdurre falsi positivi o nuove bypass. Prova: SRC-88-004.
5. **Valutazione adattiva.** Una difesa deve essere testata da attaccanti che conoscono il metodo, entro un protocollo sicuro e autorizzato. Prova: SRC-88-001.

## Prove e artefatti

- riferimento minimo: `code/snip_88_contract.py`; test: `code/test_88_contract.py`; output: `code/outputs/SNIP-88-001.txt`.
- visuali candidate: JAILBREAK-01, JAILBREAK-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
