# Audit del codice. Capitolo 2

## Stato

- Snippet: `SNIP-HIST-001`
- Linguaggio: Python 3.13.5
- Dipendenze: standard library
- Esito: **superato**
- Data: 30 luglio 2026

## Contratto

- Input: grafo esplicito, stato iniziale e goal.
- Operazione: breadth-first search con coda FIFO e insieme degli stati visitati.
- Output: lista ordinata di coppie `(azione, nuovo_stato)`.
- Invariante: ogni stato viene inserito nella coda al massimo una volta.
- Confine: il percorso è minimo per numero di transizioni soltanto quando ogni arco ha lo stesso costo.

## Controlli

- [x] lo stato iniziale e il goal devono esistere nel grafo;
- [x] una transizione verso uno stato sconosciuto produce errore;
- [x] il caso noto restituisce il percorso di due transizioni;
- [x] l'ultimo stato è `ticket_opened`;
- [x] il percorso non ripete stati;
- [x] un goal irraggiungibile produce `ValueError`;
- [x] output registrato in processo pulito;
- [x] tre test superati.

## Limiti didattici

- il grafo è costruito a mano;
- le azioni non hanno costi differenti;
- non vengono modellate incertezza, probabilità o conoscenza incompleta;
- lo snippet illustra una struttura simbolica generale e non viene attribuito a un programma storico specifico.

## Esito

Il codice è coerente con la sezione su stati, azioni e ricerca. Non apre un percorso concettuale diverso dal capitolo e non sostiene claim storici attraverso la sola esecuzione.
