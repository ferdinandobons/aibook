# Registro dei claim. Capitolo 17

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `conv` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-17-01

- Affermazione esatta: Una convoluzione applica lo stesso kernel in posizioni differenti. Questa condivisione incorpora una ipotesi di regolarità locale.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-17-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Condivisione locale dei pesi» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-17-02

- Affermazione esatta: Stride e padding determinano la griglia dell'output. Il receptive field cresce con layer, kernel e dilatazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-17-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Deep Residual Learning for Image Recognition; 3 Deep Residual Learning; 3.1 Residual Learning (claim collegato alla sezione «Stride, padding e receptive field» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-17-03

- Affermazione esatta: La convoluzione è equivariant a traslazioni entro le condizioni del bordo. Pooling e aggregazione possono costruire una maggiore invariance.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-17-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (claim collegato alla sezione «Equivarianza e invariance» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-17-04

- Affermazione esatta: Patch embedding e attention offrono una geometria diversa. CNN e Transformer possono essere combinati, ma il confronto richiede stesso budget e dati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-17-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Neural Message Passing for Quantum Chemistry; 1 Introduction; 2 Message Passing Neural Networks (claim collegato alla sezione «Vision Transformer e ibridi» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-17-05

- Affermazione esatta: Su un grafo, i vicini non sono disposti in una griglia regolare. Le GNN aggregano messaggi rispettando la struttura degli archi e le simmetrie dichiarate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-17-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Grafi e message passing» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-17-CODE

- Affermazione esatta: lo snippet snip_17_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_17_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
