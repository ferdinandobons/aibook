# Esempio verificato. Capitolo 29

`snip_29_contract.py` esegue il caso minimo usato nel testo di **Il Transformer da zero**. `test_29_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_29_contract.py
python -m unittest -v test_29_contract.py
```
