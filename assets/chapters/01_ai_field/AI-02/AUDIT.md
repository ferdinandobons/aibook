# Audit visuale `AI-02`

## Stato

- Esito: **da generare**
- Approvazione tecnica: no
- Approvazione autoriale: no
- File candidato nel repository: nessuno
- Data: 30 luglio 2026

## Generazioni disponibili

Nessuna candidata ha rappresentato il confronto training/inference. I tentativi eseguiti durante la lavorazione di `AI-01` hanno mostrato che il contesto dello strumento immagini era dominato da schermate GitHub e riepiloghi del progetto. Per evitare di accumulare immagini irrilevanti, `AI-02` non è stata ulteriormente generata nella stessa sequenza.

## Condizione di ripresa

La generazione deve avvenire con `AI-02/SPEC.md` come referente dominante e deve essere seguita da un audit indipendente del raster effettivo.

## Controlli obbligatori sulla futura candidata

- [ ] target collegato alla loss e non al modello;
- [ ] gradienti prodotti dopo la loss;
- [ ] optimizer collegato al cambiamento `θ -> θ'`;
- [ ] inference priva di loss, gradienti e optimizer;
- [ ] checkpoint fissato usato per il nuovo input;
- [ ] `eval()` e `inference_mode()` non presentati come sinonimi;
- [ ] nessuna affermazione di generalizzazione;
- [ ] frecce e feedback loop inequivocabili;
- [ ] sfondo bianco puro;
- [ ] testo integralmente contenuto;
- [ ] coerenza con prosa, snippet e fonti.

## Gate di approvazione

La visuale resta bloccante per il passaggio del capitolo alla revisione autoriale.
