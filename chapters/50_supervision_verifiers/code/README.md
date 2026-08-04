# Esempio verificato. Capitolo 50

`snip_50_contract.py` esegue il caso minimo usato nel testo di **Process supervision, outcome supervision e verifier**. `test_50_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_50_contract.py
python -m unittest -v test_50_contract.py
```
