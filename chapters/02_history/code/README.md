# Codice del Capitolo 2

## `SNIP-HIST-001`. Ricerca simbolica su stati espliciti

Domanda: che cosa significa rappresentare un problema come stati, azioni e goal e cercare un percorso?

File:

- `snip_hist_001_symbolic_search.py`;
- `test_history_snippet.py`;
- `outputs/SNIP-HIST-001.txt`;
- `outputs/TESTS.txt`;
- `environments/python.txt`.

Il grafo è illustrativo. La breadth-first search restituisce un percorso con il minor numero di transizioni nel grafo dichiarato. Lo snippet non riproduce Logic Theorist, General Problem Solver, MYCIN o un altro sistema storico specifico.

## Esecuzione

```bash
python snip_hist_001_symbolic_search.py
python -m unittest -v
```

## Risultati registrati

- percorso trovato: `request_received -> order_identified -> ticket_opened`;
- lunghezza: 2 transizioni;
- tre test superati;
- dipendenze esterne: nessuna.
