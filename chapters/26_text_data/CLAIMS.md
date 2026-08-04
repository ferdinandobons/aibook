# Registro dei claim. Capitolo 26

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `text_data` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-26-01

- Affermazione esatta: Il testo è una sequenza di code point codificata in byte. Normalizzazione Unicode e decoding devono essere dichiarati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-26-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Unicode® 17.0.0; New Data Files for Unicode 17.0; Unicode Standard Annexes (claim collegato alla sezione «Unicode e byte» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-26-02

- Affermazione esatta: BPE, WordPiece e Unigram costruiscono vocabolari subword con algoritmi differenti. Il tokenizer fa parte dell'interfaccia del checkpoint.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-26-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale (claim collegato alla sezione «Tokenizzazione» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: corretta
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-26-03

- Affermazione esatta: BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi. ID uguali richiedono la stessa convenzione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-26-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; ByT5: Towards a Token-Free Future with Pre-trained Byte-to-Byte Models (claim collegato alla sezione «Token speciali» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-26-04

- Affermazione esatta: Più documenti possono condividere una sequenza. Attention mask e loss mask devono impedire dipendenze non desiderate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-26-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer; B Converting WNLI to Our Text-to-Text Format (claim collegato alla sezione «Packing e confini» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-26-05

- Affermazione esatta: Token per carattere variano tra lingue e formati. La lunghezza in token influenza contesto, costo e valutazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-26-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Unicode® 17.0.0; New Data Files for Unicode 17.0; Unicode Standard Annexes (claim collegato alla sezione «Lunghezza, lingua e costi» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-26-CODE

- Affermazione esatta: lo snippet snip_26_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_26_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
