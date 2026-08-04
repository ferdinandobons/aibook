# Registro dei claim. Capitolo 58

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `native_multimodal` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-58-01

- Affermazione esatta: Sequenze possono alternare testo, immagini, audio e marker. Il tokenizer multimodale definisce unità e ordine.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-58-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 5.2 Image-To-Text (claim collegato alla sezione «Token interleaved» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-58-02

- Affermazione esatta: Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e adapter specifici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-58-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Backbone condiviso» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-58-03

- Affermazione esatta: La generazione di testo e media richiede head o decoder differenti, anche quando il backbone è comune.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-58-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Autoregressive multimodal modeling; Autoregressive MultiModal Models with Time-Aligned and Non-Aligned Representations; Autoregressive video representation learning (claim collegato alla sezione «Output multimodale» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-58-04

- Affermazione esatta: Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state realmente addestrate e valutate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-58-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; NExT-GPT: Any-to-Any Multimodal LLM; Multimodal Large Language Models; Multimodal Encoding Stage (claim collegato alla sezione «Any-to-any» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-58-05

- Affermazione esatta: Audio, video e testo possiedono frequenze differenti. Allineamento temporale e turn-taking diventano parte dell'architettura.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-58-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 5.2 Image-To-Text (claim collegato alla sezione «Sincronizzazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-58-CODE

- Affermazione esatta: lo snippet snip_58_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_58_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
