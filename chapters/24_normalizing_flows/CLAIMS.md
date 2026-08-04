# Registro dei claim. Capitolo 24

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `flows` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-24-01

- Affermazione esatta: Una trasformazione invertibile collega una distribuzione semplice ai dati. La densità usa il determinante Jacobiano.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-24-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Density estimation using Real NVP; 1 Introduction; 2 Related work (claim collegato alla sezione «Cambio di variabile» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-24-02

- Affermazione esatta: RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-24-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 5.1 Log-likelihood and generation (claim collegato alla sezione «Coupling layer» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-24-03

- Affermazione esatta: L'invertibilità limita operazioni e dimensioni. Squeeze, split e permutazioni riorganizzano l'informazione senza perderla.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-24-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 2.2 Continuous Normalizing Flows (claim collegato alla sezione «Invertibilità e architettura» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-24-04

- Affermazione esatta: Una ODE definisce una trasformazione continua. La likelihood usa la variazione del log-density lungo il flusso.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-24-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Normalizing Flows for Probabilistic Modeling and Inference; 2 Normalizing Flows; 2.3.1 Forward KL Divergence and Maximum Likelihood Estimation (claim collegato alla sezione «Continuous normalizing flow» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-24-05

- Affermazione esatta: I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-24-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Density estimation using Real NVP; 1 Introduction; 2 Related work (claim collegato alla sezione «Sampling e costo» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-24-CODE

- Affermazione esatta: lo snippet snip_24_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_24_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
