# Registro dei claim. Capitolo 49

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `preference` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-49-01

- Affermazione esatta: DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-49-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Direct Preference Optimization: Your Language Model is Secretly a Reward Model; 4 Direct Preference Optimization; 5.1 Your Language Model Is Secretly a Reward Model (claim collegato alla sezione «Evitare un reward model esplicito» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-49-02

- Affermazione esatta: Ogni esempio richiede la stessa condizione e due risposte confrontabili. Errori o stili spurii possono diventare scorciatoie.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-49-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3.1.1 Learning the Reward Model; 3.1.2 Policy Optimisation with the Learned Reward; 3.2 Direct Preference Optimisation (claim collegato alla sezione «Coppie chosen e rejected» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-49-03

- Affermazione esatta: Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-49-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; KTO data need not come from preference datasets. (claim collegato alla sezione «Temperatura beta» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-49-04

- Affermazione esatta: Le varianti cambiano assunzioni, forma della loss o tipo di feedback. I nomi non rendono gli obiettivi intercambiabili.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-49-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; ORPO : Monolithic Preference Optimization without Reference Model; Alignment without Reward Model; 4 Odds Ratio Preference Optimization (claim collegato alla sezione «IPO, KTO, ORPO e varianti» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-49-05

- Affermazione esatta: L'ottimizzazione resta limitata alla copertura del dataset. Nuove policy possono visitare risposte non rappresentate nelle coppie.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-49-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Direct Preference Optimization: Your Language Model is Secretly a Reward Model; 4 Direct Preference Optimization; 5.1 Your Language Model Is Secretly a Reward Model (claim collegato alla sezione «Offline preference data» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-49-CODE

- Affermazione esatta: lo snippet snip_49_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_49_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
