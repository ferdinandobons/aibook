# Registro dei claim. Capitolo 34

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `scaling` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-34-01

- Affermazione esatta: Una power law approssima loss rispetto a parametri, dati o compute in un intervallo misurato.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-34-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Scaling Laws for Neural Language Models; 1.2 Summary of Scaling Laws; 2.1 Parameter and Compute Scaling of Transformers (claim collegato alla sezione «Fit empirico» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-34-02

- Affermazione esatta: A budget fissato, modello e token competono. Il risultato dipende da ricetta e qualità dei dati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-34-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Training Compute-Optimal Large Language Models; Appendix A Training dataset; Appendix C Consistency of scaling results across datasets (claim collegato alla sezione «Allocazione compute-optimal» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-34-03

- Affermazione esatta: Configurazioni con compute simile rendono osservabile la loss minima per budget.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-34-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism; 2.3 Data and Model Parallelism in Deep Learning; 4.1 Training Dataset (claim collegato alla sezione «Esperimenti isoFLOP» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-34-04

- Affermazione esatta: Residui, intervalli e ipotesi su loss irriducibile limitano la previsione fuori scala.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-34-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; ZeRO: Memory Optimizations Toward Training Trillion Parameter Models; 2.1 Data, Model and Pipeline Parallelism; 3.1 Model States: Optimizer States, Gradients and Parameters (claim collegato alla sezione «Extrapolation» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-34-05

- Affermazione esatta: Una scelta compute-optimal per il training può non minimizzare costo e latenza del servizio.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-34-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Scaling Laws for Neural Language Models; 1.2 Summary of Scaling Laws; 2.1 Parameter and Compute Scaling of Transformers (claim collegato alla sezione «Training e inference cost» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-34-CODE

- Affermazione esatta: lo snippet snip_34_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_34_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
