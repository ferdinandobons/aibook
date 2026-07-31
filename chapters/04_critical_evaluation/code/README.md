# Codice. Capitolo 4

Il file `snip_eval_001_paired_comparison.py` confronta due modelli sugli stessi 24 esempi illustrativi.

Produce quattro letture dello stesso confronto:

- accuratezza complessiva;
- accuratezza nei gruppi `standard` e `urgent`;
- somma pesata degli errori;
- intervallo bootstrap appaiato della differenza tra le accuratezze.

Il modello B ha una accuratezza complessiva leggermente maggiore. Il modello A ottiene però un risultato migliore nel gruppo urgente e una somma pesata degli errori inferiore. L'intervallo illustrativo include zero.

Dati e pesi sono costruiti soltanto per la spiegazione. Non rappresentano un prodotto o un benchmark pubblico.

## Esecuzione

```bash
python snip_eval_001_paired_comparison.py
python -m unittest -v
```

Ambiente, output e test sono registrati nelle rispettive cartelle.
