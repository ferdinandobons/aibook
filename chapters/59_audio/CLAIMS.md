# Registro dei claim. Capitolo 59

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `audio` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-59-01

- Affermazione esatta: Il segnale audio è campionato nel tempo. STFT e mel filterbank producono rappresentazioni tempo-frequenza con parametri espliciti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-59-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations; 5.2 High-Resource Labeled Data Evaluation on Librispeech; Appendix C Full results for Libri-light and Librispeech (claim collegato alla sezione «Waveform e spettrogramma» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-59-02

- Affermazione esatta: Il riconoscimento vocale mappa audio a testo con obiettivi CTC, encoder-decoder o transducer. Streaming e offline hanno vincoli diversi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-59-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Robust Speech Recognition via Large-Scale Weak Supervision; 3.3 English Speech Recognition; 3.4 Multi-lingual Speech Recognition (claim collegato alla sezione «ASR» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-59-03

- Affermazione esatta: Sintesi vocale trasforma testo in acoustic representation e waveform. Durata, prosodia e vocoder sono componenti distinti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-59-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; AudioLM: a Language Modeling Approach to Audio Generation; III-B Trade-offs of discrete audio representations; IV-E Probing the linguistic knowledge of AudioLM (claim collegato alla sezione «TTS» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-59-04

- Affermazione esatta: Codec neurali quantizzano il suono in code discreti multi-rate, usabili da audio language model.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-59-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; SoundStream: An End-to-End Neural Audio Codec (claim collegato alla sezione «Neural codec» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-59-05

- Affermazione esatta: Struttura musicale, speaker identity, turn-taking e latenza richiedono dati e metriche specifiche.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-59-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations; 5.2 High-Resource Labeled Data Evaluation on Librispeech; Appendix C Full results for Libri-light and Librispeech (claim collegato alla sezione «Musica e dialogo» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-59-CODE

- Affermazione esatta: lo snippet snip_59_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_59_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
