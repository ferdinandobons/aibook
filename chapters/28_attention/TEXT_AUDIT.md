# Audit del testo. Capitolo 28

## Stato

- Versione: `0.1.0-rc1`
- Data: 30 luglio 2026
- Esito tecnico: **superato con review autoriale aperta**

## Audit fattuale

- [x] Ogni affermazione portante è registrata in `CLAIMS.md`.
- [x] Le citazioni sono state controllate nelle fonti primarie o ufficiali.
- [x] Il testo distingue Transformer originale, API PyTorch e implementazioni hardware-aware.
- [x] Non sono riportati benchmark propri.
- [x] Non sono presenti inferenze fattuali non dichiarate.

## Audit matematico

- [x] Shape di `Q`, `K`, `V`, score, pesi e output ricontrollate.
- [x] Esempio numerico ricalcolato con PyTorch `float64`.
- [x] Somma dei pesi verificata.
- [x] Output della singola query verificato.
- [x] Equivalenza tra formula diretta e API verificata.
- [x] Ipotesi della derivazione sulla varianza esplicitate.

## Audit algoritmico

- [x] Ordine: score, scaling, mask, softmax, prodotto con `V`.
- [x] La mask non è descritta come operazione sulle value.
- [x] Il dropout è separato dal caso base.
- [x] Multi-head: head separate, concatenazione, `W^O`.

## Audit temporale

- [x] PyTorch stable risolve a `2.13` alla data della ricerca.
- [x] Ambiente locale `2.10.0+cpu` dichiarato separatamente.
- [x] Nessuna dichiarazione di esecuzione sotto `2.13`.

## Audit didattico

- [x] Oggetto continuo unico.
- [x] Un'operazione principale per passaggio.
- [x] Formula introdotta dopo il calcolo concreto.
- [x] Codice introdotto dopo il meccanismo.
- [x] Varianti hardware differite.
- [x] Cambiamento, invariante e confine espliciti.

## Elementi aperti alla review autoriale

1. Tono e lunghezza complessiva.
2. Quantità di matematica nel capitolo base.
3. Collocazione della sezione multi-head.
4. Approvazione o rigenerazione delle figure candidate.
5. Conferma dell'uso di `attention` in inglese nel titolo e nel corpo.
