# Registro dei claim. Capitolo 16

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `deep` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-16-01

- Affermazione esatta: Attivazioni e gradienti possono crescere o ridursi lungo la profondità. Inizializzazione, attivazioni e residual determinano la scala osservata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-16-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Deep Residual Learning for Image Recognition; 3 Deep Residual Learning; 3.1 Residual Learning (claim collegato alla sezione «Segnali che attraversano molti layer» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-16-02

- Affermazione esatta: Xavier e He initialization collegano la varianza dei pesi al fan-in o fan-out. Le formule presuppongono attivazioni e indipendenze approssimate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-16-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Understanding the difficulty of training deep feedforward neural networks (claim collegato alla sezione «Inizializzazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-16-03

- Affermazione esatta: BatchNorm, LayerNorm e RMSNorm normalizzano assi e statistiche differenti. Non sono sostituibili senza considerare batch, sequenza e architettura.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-16-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift; 3 Normalization via Mini-Batch Statistics; 3.3 Batch Normalization enables higher learning rates (claim collegato alla sezione «Normalizzazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-16-04

- Affermazione esatta: Un residual path conserva un percorso identità e facilita il trasporto di informazione. La somma richiede shape compatibili e una scala controllata.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-16-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Dropout: A Simple Way to Prevent Neural Networks from Overfitting; Abstract (claim collegato alla sezione «Residual e profondità» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-16-05

- Affermazione esatta: Dropout, weight decay, data augmentation ed early stopping agiscono in punti diversi. Curve, norme e slice aiutano a distinguere underfitting, overfitting e instabilità.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-16-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Deep Residual Learning for Image Recognition; 3 Deep Residual Learning; 3.1 Residual Learning (claim collegato alla sezione «Regolarizzazione e diagnostica» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-16-CODE

- Affermazione esatta: lo snippet snip_16_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_16_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
