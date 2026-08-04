# Registro dei claim. Capitolo 15

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `mlp` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-15-01

- Affermazione esatta: Il percettrone combina feature con pesi e bias. Il confine risultante è lineare nello spazio delle feature.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-15-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: original article record; abstract and bibliographic record (claim collegato alla sezione «Una decisione lineare» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: publisher/index record opened via web research; title, author and original publication checked; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-15-02

- Affermazione esatta: Una MLP alterna trasformazioni affini e funzioni non lineari. Senza non linearità, più layer affini collassano in una sola trasformazione affine.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-15-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Inferring neural activity before plasticity as a foundation for learning beyond backpropagation (claim collegato alla sezione «Strati nascosti» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-15-03

- Affermazione esatta: ReLU, tanh, sigmoid e GELU modificano propagazione, saturazione e regolarità. La scelta deve essere letta insieme a inizializzazione e normalizzazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-15-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Deep Learning; An MIT Press book; Ian Goodfellow and Yoshua Bengio and Aaron Courville (claim collegato alla sezione «Attivazioni» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-15-04

- Affermazione esatta: Una rete più ampia può rappresentare funzioni più complesse, ma parametri aggiuntivi non garantiscono generalizzazione o ottimizzazione stabile.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-15-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification; 1 Introduction; 2 Approach (claim collegato alla sezione «Capacità ed espressività» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-15-05

- Affermazione esatta: Il forward produce logits e loss. Backpropagation e optimizer trasformano il segnale in aggiornamenti, secondo i contratti costruiti nei capitoli matematici.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-15-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: original article record; abstract and bibliographic record (claim collegato alla sezione «Dal forward al training» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: publisher/index record opened via web research; title, author and original publication checked; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-15-CODE

- Affermazione esatta: lo snippet snip_15_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_15_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
