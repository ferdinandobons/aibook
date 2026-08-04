# Registro dei claim. Capitolo 21

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `autoregressive` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-21-01

- Affermazione esatta: La chain rule scompone la probabilità con un ordine. Ogni fattore condiziona sugli elementi precedenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-21-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Generating Sequences With Recurrent Neural Networks; 2 Prediction Network; 3 Text Prediction (claim collegato alla sezione «Fattorizzare una sequenza» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-21-02

- Affermazione esatta: Durante il training il modello riceve il prefisso reale e predice il passo successivo. Durante la generazione riceve anche i propri output.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-21-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Teacher forcing» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-21-03

- Affermazione esatta: La causal mask impedisce a una posizione di usare target futuri. Un errore nella maschera produce leakage pur con loss numericamente valida.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-21-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3 Language Model Decoding; 4.3 Natural Language Does Not Maximize Probability (claim collegato alla sezione «Maschera causale» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-21-04

- Affermazione esatta: Ogni scelta modifica il contesto successivo. Errori iniziali possono spostare la traiettoria verso regioni poco viste nel training.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-21-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Attention Is All You Need; 1 Introduction; 2 Background (claim collegato alla sezione «Sampling e accumulo degli errori» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-21-05

- Affermazione esatta: L'autoregressione non è limitata al testo. Una sequenza può rappresentare pixel, code audio o latent discreti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-21-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Generating Sequences With Recurrent Neural Networks; 2 Prediction Network; 3 Text Prediction (claim collegato alla sezione «Immagini, audio e token discreti» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-21-CODE

- Affermazione esatta: lo snippet snip_21_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_21_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
