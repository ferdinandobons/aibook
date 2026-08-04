# Esempio verificato. Capitolo 95

`snip_95_contract.py` esegue il caso minimo usato nel testo di **Costruire un piccolo language model**. `test_95_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_95_contract.py
python -m unittest -v test_95_contract.py
```

## Decoder causale addestrato e campionato

Codice: `tiny_transformer_lm.py`; test: `test_tiny_transformer_lm.py`; output: `outputs/TINY-TRANSFORMER-LM.txt`; ambiente: `environments/lab.txt`.
