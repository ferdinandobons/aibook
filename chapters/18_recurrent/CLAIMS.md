# Registro dei claim. Capitolo 18

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `rnn` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-18-01

- Affermazione esatta: Una RNN aggiorna uno stato nascosto con input e stato precedente. Lo stesso insieme di parametri viene riutilizzato a ogni passo.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-18-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Neural Computation 9(8), pp. 1735-1780; abstract and original article record (claim collegato alla sezione «Uno stato che attraversa la sequenza» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: MIT Press article record and author publication index opened via web research; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-18-02

- Affermazione esatta: Il grafo ricorrente viene srotolato nel tempo. Gradienti molto lunghi possono svanire o esplodere.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-18-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2.1 Preliminary: Recurrent Neural Networks (claim collegato alla sezione «Backpropagation through time» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-18-03

- Affermazione esatta: Gate di input, forget e output controllano il flusso della memoria. GRU usa una parametrizzazione più compatta, con un contratto differente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-18-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Sequence to Sequence Learning with Neural Networks (claim collegato alla sezione «LSTM e GRU» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-18-04

- Affermazione esatta: Una rete bidirezionale usa anche il futuro ed è adatta a encoding offline. Non può essere usata direttamente per generazione causale streaming.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-18-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; On the difficulty of training Recurrent Neural Networks; 1.1 Training recurrent networks (claim collegato alla sezione «Bidirezionalità e causalità» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-18-05

- Affermazione esatta: La recurrence mantiene memoria compatta; l'attention accede a rappresentazioni esplicite. I due meccanismi possono essere complementari.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-18-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Neural Computation 9(8), pp. 1735-1780; abstract and original article record (claim collegato alla sezione «RNN, attention e stato» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: MIT Press article record and author publication index opened via web research; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-18-CODE

- Affermazione esatta: lo snippet snip_18_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_18_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
