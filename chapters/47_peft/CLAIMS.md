# Registro dei claim. Capitolo 47

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `peft` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-47-01

- Affermazione esatta: PEFT modifica un sottoinsieme di parametri o introduce moduli piccoli, lasciando invariata la maggior parte del checkpoint.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-47-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Parameter-Efficient Transfer Learning for NLP; Supplementary Material for Parameter-Efficient Transfer Learning for NLP; 2 Adapter tuning for NLP (claim collegato alla sezione «Parametri congelati e adattamento» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-47-02

- Affermazione esatta: Blocchi bottleneck vengono inseriti nel percorso residuale. Posizione, dimensione e inizializzazione determinano l'interfaccia con il modello base.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-47-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; LoRA: Low-Rank Adaptation of Large Language Models; Adapter Layers Introduce Inference Latency; 4.1 Low-Rank-Parametrized Update Matrices (claim collegato alla sezione «Adapter» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-47-03

- Affermazione esatta: Un aggiornamento di rango ridotto fattorizza la variazione di una matrice come BA e può essere fuso nei pesi per l'inference.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-47-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning; 2.2 Parameter-efficient fine-tuning; 3.3 Parameter-efficient fine-tuning with (IA) 3 (claim collegato alla sezione «LoRA» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-47-04

- Affermazione esatta: Soft prompt, prefix key-value e vettori di scaling modificano punti diversi del calcolo e non sono equivalenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-47-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; QLoRA : Efficient Finetuning of Quantized LLMs; Low-rank Adapters; Memory Requirement of Parameter-Efficient Finetuning (claim collegato alla sezione «Prompt, prefix e IA3» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-47-05

- Affermazione esatta: Il modello base quantizzato riduce memoria, mentre gli adapter restano addestrabili. Formato, tokenizer e architettura devono corrispondere.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-47-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Parameter-Efficient Transfer Learning for NLP; Supplementary Material for Parameter-Efficient Transfer Learning for NLP; 2 Adapter tuning for NLP (claim collegato alla sezione «QLoRA e compatibilità» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-47-CODE

- Affermazione esatta: lo snippet snip_47_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_47_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
