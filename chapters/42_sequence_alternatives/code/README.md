# Esempio verificato. Capitolo 42

`snip_42_contract.py` esegue il caso minimo usato nel testo di **State-space model, recurrence e long convolution**. `test_42_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_42_contract.py
python -m unittest -v test_42_contract.py
```
