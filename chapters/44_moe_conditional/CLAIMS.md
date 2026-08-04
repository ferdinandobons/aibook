# Registro dei claim. Capitolo 44

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `moe` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-44-01

- Affermazione esatta: Un router assegna probabilità agli esperti e attiva un sottoinsieme per token.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-44-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer; 1.2 Our Approach: The Sparsely-Gated Mixture-of-Experts Layer; 1.3 Related work on Mixtures of Experts (claim collegato alla sezione «Router top-k» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-44-02

- Affermazione esatta: Ogni esperto riceve un limite di token. Overflow, rerouting o dropping devono essere dichiarati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-44-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2.1 Simplifying Sparse Routing; 2.2 Efficient Sparse Routing; 5 Designing Models with Data, Model, and Expert-Parallelism (claim collegato alla sezione «Capacità» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-44-03

- Affermazione esatta: Loss ausiliarie contrastano router collapse, ma possono competere con la specializzazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-44-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models; 2 Preliminaries: Mixture-of-Experts for Transformers; 3.1 Fine-Grained Expert Segmentation (claim collegato alla sezione «Load balancing» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-44-04

- Affermazione esatta: Token ed output attraversano collective all-to-all tra dispositivi che ospitano esperti differenti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-44-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Appendix C Expert Specialization Patterns of the 16B Aux-Loss-Based and Aux-Loss-Free Models (claim collegato alla sezione «Expert parallelism» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-44-05

- Affermazione esatta: Un MoE può avere molti parametri totali e pochi parametri attivi per token. FLOP, memoria e comunicazione vanno riportati separatamente.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-44-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer; 1.2 Our Approach: The Sparsely-Gated Mixture-of-Experts Layer; 1.3 Related work on Mixtures of Experts (claim collegato alla sezione «Parametri totali e attivi» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-44-CODE

- Affermazione esatta: lo snippet snip_44_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_44_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
