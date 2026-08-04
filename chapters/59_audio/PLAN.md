# Piano editoriale. Capitolo 59

## Obiettivo didattico

Seguire **Audio, parlato e musica** da waveform, sample rate, spettrogramma o codec a testo, waveform o token audio, osservando ASR, TTS, codec e generazione senza oltrepassare questo limite: sample rate e durata fanno parte del contratto.

## Prerequisiti reali

- Capitolo 26: Il testo come dato
- Capitolo 55: Fondamenti della multimodalità

## Percorso della lezione

1. **Waveform e spettrogramma.** Il segnale audio è campionato nel tempo. STFT e mel filterbank producono rappresentazioni tempo-frequenza con parametri espliciti. Prova: SRC-59-001.
2. **ASR.** Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer. Streaming e offline hanno vincoli diversi. Prova: SRC-59-002.
3. **TTS.** Sintesi vocale trasforma testo in acoustic representation e waveform. Durata, prosodia e vocoder sono componenti distinti. Prova: SRC-59-003.
4. **Neural codec.** Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model. Prova: SRC-59-004.
5. **Musica e dialogo.** Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche. Prova: SRC-59-001.

## Prove e artefatti

- riferimento minimo: `code/snip_59_contract.py`; test: `code/test_59_contract.py`; output: `code/outputs/SNIP-59-001.txt`.
- visuali candidate: AUDIO-01, AUDIO-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
