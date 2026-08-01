# Codice del Capitolo 1

## Scopo

Lo snippet mostra una differenza osservabile tra training e inference senza introdurre un secondo percorso concettuale rispetto al capitolo.

## Ambiente eseguito

Vedere [`environments/python-pytorch.txt`](environments/python-pytorch.txt).

## Comandi

```bash
python snip_ai_001_training_inference.py
python -m unittest -v test_ai_snippets.py
```

## Mappa

| ID | File | Domanda |
|---|---|---|
| `SNIP-AI-001` | `snip_ai_001_training_inference.py` | Quando cambiano i parametri e quando vengono soltanto usati? |

## Contratto

- Input: quattro esempi illustrativi con due feature e due classi.
- Modello: `torch.nn.Linear(2, 2)`.
- Training: cross-entropy, SGD, 100 iterazioni, seed 7.
- Inference: un nuovo input di shape `[1,2]`, `model.eval()` e `torch.inference_mode()`.
- Output osservabili:
  - loss iniziale e finale;
  - modifica dei parametri durante il training;
  - assenza di modifica durante l'inference;
  - logit di shape `[1,2]`;
  - classe prevista.

## Provenienza

Il dataset è `Illustrativo`. L'output salvato è `Eseguito` nell'ambiente registrato. Non è una misura di generalizzazione o un benchmark.
