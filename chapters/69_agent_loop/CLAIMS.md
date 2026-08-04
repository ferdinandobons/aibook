# Registro dei claim. Capitolo 69

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `agent_loop` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-69-01

- Affermazione esatta: Un agente riceve input, risultato dei tool e memoria. Lo stato operativo deve essere separato dal testo libero del modello.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-69-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; D.2.3 ReAct-IM trajectory (claim collegato alla sezione «Osservare e aggiornare lo stato» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-69-02

- Affermazione esatta: Un piano scompone il compito in passi e dipendenze. Il piano iniziale può essere rivisto dopo nuove osservazioni.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-69-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Toolformer: Language Models Can Teach Themselves to Use Tools; 3 Tools; Appendix A API Details (claim collegato alla sezione «Pianificare» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-69-03

- Affermazione esatta: Ogni azione usa un tool o modifica un ambiente. Parametri, autorizzazioni e costo devono essere validati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-69-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; WebArena : A Realistic Web Environment for Building Autonomous Agents; 2 WebArena : Websites as an Environment for Autonomous Agents; 2.1 Controlling Agents through High-level Natural Language (claim collegato alla sezione «Agire» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-69-04

- Affermazione esatta: Test, controlli di stato o giudici indipendenti valutano il risultato. Una autocritica del modello non equivale a verifica esterna.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-69-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Verificare» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-69-05

- Affermazione esatta: Budget, goal raggiunto, errore irreversibile o richiesta di approvazione definiscono condizioni di stop.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-69-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; D.2.3 ReAct-IM trajectory (claim collegato alla sezione «Terminare» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-69-CODE

- Affermazione esatta: lo snippet snip_69_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_69_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
