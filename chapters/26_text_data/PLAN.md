# Piano editoriale. Capitolo 26

## Obiettivo didattico

Seguire **Il testo come dato** da una stringa Unicode con byte e token speciali a ID, confini, mask e costo in token, osservando normalizzazione, segmentazione e packing senza oltrepassare questo limite: stringa, encoding e tokenizer devono restare dichiarati.

## Prerequisiti reali

- Capitolo 2: Dai simboli ai foundation model
- Capitolo 7: Probabilità, statistica e inferenza
- Capitolo 8: Teoria dell'informazione e funzioni obiettivo

## Percorso della lezione

1. **Unicode e byte.** Il testo è una sequenza di code point codificata in byte. Normalizzazione Unicode e decoding devono essere dichiarati. Prova: SRC-26-001.
2. **Tokenizzazione.** BPE, WordPiece e Unigram costruiscono vocabolari subword con algoritmi differenti. Il tokenizer fa parte dell'interfaccia del checkpoint. Prova: SRC-26-002.
3. **Token speciali.** BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi. ID uguali richiedono la stessa convenzione. Prova: SRC-26-003.
4. **Packing e confini.** Più documenti possono condividere una sequenza. Attention mask e loss mask devono impedire dipendenze non desiderate. Prova: SRC-26-004.
5. **Lunghezza, lingua e costi.** Token per carattere variano tra lingue e formati. La lunghezza in token influenza contesto, costo e valutazione. Prova: SRC-26-001.

## Prove e artefatti

- riferimento minimo: `code/snip_26_contract.py`; test: `code/test_26_contract.py`; output: `code/outputs/SNIP-26-001.txt`.
- visuali candidate: DATA-01, DATA-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
