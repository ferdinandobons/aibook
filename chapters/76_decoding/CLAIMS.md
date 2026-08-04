# Registro dei claim. Capitolo 76

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `decoding` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-76-01

- Affermazione esatta: Greedy sceglie il massimo locale; beam mantiene più prefissi secondo score accumulati e criteri di lunghezza.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-76-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3 Language Model Decoding; 4.3 Natural Language Does Not Maximize Probability (claim collegato alla sezione «Greedy e beam search» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-76-02

- Affermazione esatta: Temperature, top-k e top-p modificano la distribuzione prima dell'estrazione. Seed e backend influenzano la riproducibilità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-76-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Diverse beam Search: Decoding Diverse Solutions from Neural Sequence Models (claim collegato alla sezione «Sampling» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-76-03

- Affermazione esatta: Repetition penalty, stop sequence e minimum length intervengono in punti differenti e possono interagire.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-76-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Locally Typical Sampling; 5 Sampling from a Language Process; 5.2 Locally Typical Sampling (claim collegato alla sezione «Penalità e stop» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-76-04

- Affermazione esatta: Grammar, automi e schema limitano i token ammessi. Validità strutturale non garantisce argomenti corretti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-76-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning; 2.2 Grammar-constrained decoding (GCD); Appendix F Decoding Settings (claim collegato alla sezione «Constrained decoding» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-76-05

- Affermazione esatta: Qualità, diversità, latency, token per secondo e probabilità della sequenza devono essere letti insieme.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-76-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3 Language Model Decoding; 4.3 Natural Language Does Not Maximize Probability (claim collegato alla sezione «Metriche» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-76-CODE

- Affermazione esatta: lo snippet snip_76_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_76_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
