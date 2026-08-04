# Piano interno. Capitolo 59

- Domanda centrale: quale contratto costruisce Audio, parlato e musica?
- Oggetto continuo: un segnale audio e la sua rappresentazione discreta; input guida: waveform, sample rate, spettrogramma o codec.
- Prerequisito stabile: Capitolo 58, Modelli multimodali nativi e any-to-any.
- Gap: ASR, TTS, codec e generazione.
- Output consegnato: testo, waveform o token audio; consumer successivo: Capitolo 60, Generazione video.
- Invariante principale: sample rate e durata fanno parte del contratto.
- Visuali: AUDIO-01 e AUDIO-02, con famiglie compositive variabili.
- Snippet: code/snip_59_contract.py; output: code/outputs/SNIP-59-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Waveform e spettrogramma

- Ultima affermazione stabile: un segnale audio e la sua rappresentazione discreta.
- Concetto nuovo: Il segnale audio è campionato nel tempo. STFT e mel filterbank producono rappresentazioni tempo-frequenza con parametri espliciti.
- Input e shape: waveform, sample rate, spettrogramma o codec.
- Operazione: ASR, TTS, codec e generazione.
- Output e shape: testo, waveform o token audio.
- Che cosa cambia: il passaggio specifico di «Waveform e spettrogramma».
- Invariante: sample rate e durata fanno parte del contratto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una breve waveform convertita in frame e token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: ASR.
- Prova: SRC-59-001 e sezione pubblica corrispondente.

## Transizione 2. ASR

- Ultima affermazione stabile: un segnale audio e la sua rappresentazione discreta.
- Concetto nuovo: Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer. Streaming e offline hanno vincoli diversi.
- Input e shape: waveform, sample rate, spettrogramma o codec.
- Operazione: ASR, TTS, codec e generazione.
- Output e shape: testo, waveform o token audio.
- Che cosa cambia: il passaggio specifico di «ASR».
- Invariante: sample rate e durata fanno parte del contratto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una breve waveform convertita in frame e token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: TTS.
- Prova: SRC-59-002 e sezione pubblica corrispondente.

## Transizione 3. TTS

- Ultima affermazione stabile: un segnale audio e la sua rappresentazione discreta.
- Concetto nuovo: Sintesi vocale trasforma testo in acoustic representation e waveform. Durata, prosodia e vocoder sono componenti distinti.
- Input e shape: waveform, sample rate, spettrogramma o codec.
- Operazione: ASR, TTS, codec e generazione.
- Output e shape: testo, waveform o token audio.
- Che cosa cambia: il passaggio specifico di «TTS».
- Invariante: sample rate e durata fanno parte del contratto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una breve waveform convertita in frame e token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Neural codec.
- Prova: SRC-59-003 e sezione pubblica corrispondente.

## Transizione 4. Neural codec

- Ultima affermazione stabile: un segnale audio e la sua rappresentazione discreta.
- Concetto nuovo: Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model.
- Input e shape: waveform, sample rate, spettrogramma o codec.
- Operazione: ASR, TTS, codec e generazione.
- Output e shape: testo, waveform o token audio.
- Che cosa cambia: il passaggio specifico di «Neural codec».
- Invariante: sample rate e durata fanno parte del contratto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una breve waveform convertita in frame e token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Musica e dialogo.
- Prova: SRC-59-004 e sezione pubblica corrispondente.

## Transizione 5. Musica e dialogo

- Ultima affermazione stabile: un segnale audio e la sua rappresentazione discreta.
- Concetto nuovo: Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche.
- Input e shape: waveform, sample rate, spettrogramma o codec.
- Operazione: ASR, TTS, codec e generazione.
- Output e shape: testo, waveform o token audio.
- Che cosa cambia: il passaggio specifico di «Musica e dialogo».
- Invariante: sample rate e durata fanno parte del contratto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: una breve waveform convertita in frame e token; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Generazione video.
- Prova: SRC-59-001 e sezione pubblica corrispondente.
