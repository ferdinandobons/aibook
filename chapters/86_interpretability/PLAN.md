# Piano editoriale. Capitolo 86

## Obiettivo didattico

Seguire **Interpretabilità delle rappresentazioni e dei circuiti** da attivazioni, probe, attribution e baseline a effetto osservato con controllo e confondenti, osservando probing, attribution, causal intervention e circuit tracing senza oltrepassare questo limite: correlazione di una feature non prova causalità.

## Prerequisiti reali

- Capitolo 6: Calcolo differenziale e backpropagation
- Capitolo 19: Representation learning
- Capitolo 31: Dalla rappresentazione linguistica agli LLM

## Percorso della lezione

1. **Oggetto dell'interpretazione.** Pesi, attivazioni, feature, head e comportamento sono livelli differenti. Il metodo deve dichiarare quale livello analizza. Prova: SRC-86-001.
2. **Probing.** Un probe misura informazione decodificabile da una rappresentazione. Non prova che il modello usi quella informazione causalmente. Prova: SRC-86-002.
3. **Attribution.** Gradienti, integrated gradients e perturbazioni assegnano importanza secondo definizioni differenti e possono essere instabili. Prova: SRC-86-003.
4. **Causal intervention.** Ablation, activation patching e path patching modificano componenti e misurano effetti sul comportamento. Prova: SRC-86-004.
5. **Circuiti.** Un circuito è un insieme di componenti e connessioni sufficienti per un comportamento nel setup studiato. Sufficienza e necessità richiedono test separati. Prova: SRC-86-001.

## Prove e artefatti

- riferimento minimo: `code/snip_86_contract.py`; test: `code/test_86_contract.py`; output: `code/outputs/SNIP-86-001.txt`.
- visuali candidate: INTERPRETA-01, INTERPRETA-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
