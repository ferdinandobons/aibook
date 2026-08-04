# Piano editoriale. Capitolo 49

## Obiettivo didattico

Seguire **Ottimizzazione diretta delle preferenze** da prompt, log-probability della policy e riferimento a loss di preferenza e policy aggiornata, osservando margine DPO, beta e variante offline senza oltrepassare questo limite: la preferenza osservata non è una verità assoluta.

## Prerequisiti reali

- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 48: Preferenze, reward model e RLHF

## Percorso della lezione

1. **Evitare un reward model esplicito.** DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata. Prova: SRC-49-001.
2. **Coppie chosen e rejected.** Ogni esempio richiede la stessa condizione e due risposte confrontabili. Errori o stili spurii possono diventare scorciatoie. Prova: SRC-49-002.
3. **Temperatura beta.** Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie. Prova: SRC-49-003.
4. **IPO, KTO, ORPO e varianti.** Le varianti cambiano assunzioni, forma della loss o tipo di feedback. I nomi non rendono gli obiettivi intercambiabili. Prova: SRC-49-004.
5. **Offline preference data.** L'ottimizzazione resta limitata alla copertura del dataset. Nuove policy possono visitare risposte non rappresentate nelle coppie. Prova: SRC-49-001.

## Prove e artefatti

- riferimento minimo: `code/snip_49_contract.py`; test: `code/test_49_contract.py`; output: `code/outputs/SNIP-49-001.txt`.
- visuali candidate: OPT-01, OPT-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
