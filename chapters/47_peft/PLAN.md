# Piano editoriale. Capitolo 47

## Obiettivo didattico

Seguire **Fine-tuning efficiente** da peso W, matrice A e B, rank e quantizzazione a delta W e checkpoint adattatore, osservando adapter, LoRA, prefix o QLoRA senza oltrepassare questo limite: il delta non è il modello completo e va valutato sullo stesso base model.

## Prerequisiti reali

- Capitolo 5: Algebra lineare, vettori e tensori
- Capitolo 46: Supervised fine-tuning e instruction tuning

## Percorso della lezione

1. **Parametri congelati e adattamento.** PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint. Prova: SRC-47-001.
2. **Adapter.** Blocchi bottleneck vengono inseriti nel percorso residuale. Posizione, dimensione e inizializzazione determinano l'interfaccia con il modello base. Prova: SRC-47-002.
3. **LoRA.** Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può essere fuso nei pesi per l'inference. Prova: SRC-47-003.
4. **Prompt, prefix e IA3.** Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti. Prova: SRC-47-004.
5. **QLoRA e compatibilità.** Il modello base quantizzato riduce memoria, mentre gli adapter restano addestrabili. Formato, tokenizer e architettura devono corrispondere. Prova: SRC-47-001.

## Prove e artefatti

- riferimento minimo: `code/snip_47_contract.py`; test: `code/test_47_contract.py`; output: `code/outputs/SNIP-47-001.txt`.
- visuali candidate: PEFT-01, PEFT-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
