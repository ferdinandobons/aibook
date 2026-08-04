# Esempio verificato. Capitolo 56

`snip_56_contract.py` esegue il caso minimo usato nel testo di **Vision encoder e Vision-Language Model**. `test_56_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_56_contract.py
python -m unittest -v test_56_contract.py
```
