# Registro dei claim. Capitolo 35

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `pretraining_recipe` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-35-01

- Affermazione esatta: Packing, padding e mask determinano quanti token validi contribuiscono alla loss.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-35-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Language Models are Few-Shot Learners; 3.1 Language Modeling, Cloze, and Completion Tasks; 3.1.1 Language Modeling (claim collegato alla sezione «Batch di token» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-35-02

- Affermazione esatta: Scala dei pesi e residual deve restare coerente con profondità, norm e dtype.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-35-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 4.1 Evaluating Decoupled Weight Decay With Different Learning Rate Schedules; 4.2 Decoupling the Weight Decay and Initial Learning Rate Parameters (claim collegato alla sezione «Inizializzazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-35-03

- Affermazione esatta: Learning rate, beta, epsilon e weight decay descrivono insieme l'optimizer.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-35-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour; 2.1 Learning Rates for Large Minibatches; Training error. (claim collegato alla sezione «AdamW» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-35-04

- Affermazione esatta: Il learning rate dipende da step o token e deve riprendere dal contatore corretto.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-35-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Saving & Loading a General Checkpoint for Inference and/or Resuming Training # (claim collegato alla sezione «Warmup e schedule» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-35-05

- Affermazione esatta: Modello, optimizer, scheduler, scaler, RNG e posizione nei dati servono per un resume fedele.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-35-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Language Models are Few-Shot Learners; 3.1 Language Modeling, Cloze, and Completion Tasks; 3.1.1 Language Modeling (claim collegato alla sezione «Checkpoint e recovery» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-35-CODE

- Affermazione esatta: lo snippet snip_35_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_35_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
