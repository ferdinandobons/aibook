# Registro dei claim. Capitolo 73

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `distillation` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-73-01

- Affermazione esatta: La distillazione usa logits, distribuzioni o sequenze del teacher come target aggiuntivi per uno student.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-73-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Distilling the Knowledge in a Neural Network; 2 Distillation; 2.1 Matching logits is a special case of distillation (claim collegato alla sezione «Teacher e student» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-73-02

- Affermazione esatta: Una temperatura più alta rivela relazioni tra classi o token. Hard target e soft target vengono pesati separatamente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-73-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter; 2 Knowledge distillation; 3 DistilBERT: a distilled version of BERT (claim collegato alla sezione «Temperature e loss» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-73-03

- Affermazione esatta: Per modelli generativi, risposte del teacher diventano un nuovo dataset. Filtri e diversità determinano ciò che lo student vede.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-73-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Post-Training Pruning; Layer-Wise Pruning.; 3 The SparseGPT Algorithm (claim collegato alla sezione «Sequence distillation» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-73-04

- Affermazione esatta: Pesi, canali, head o layer possono essere rimossi. Sparsità nominale e accelerazione reale dipendono da kernel e hardware.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-73-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; A Simple and Effective Pruning Approach for Large Language Models; 3 Wanda: Pruning by Weights and Activations (claim collegato alla sezione «Pruning» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-73-05

- Affermazione esatta: Fine-tuning o calibration recuperano qualità dopo compressione. Il confronto deve includere memoria, latency e regressioni per slice.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-73-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Distilling the Knowledge in a Neural Network; 2 Distillation; 2.1 Matching logits is a special case of distillation (claim collegato alla sezione «Recovery» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-73-CODE

- Affermazione esatta: lo snippet snip_73_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_73_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
