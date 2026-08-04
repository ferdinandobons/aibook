# Esempio verificato. Capitolo 36

`snip_36_contract.py` esegue il caso minimo usato nel testo di **Training distribuito e continued pretraining**. `test_36_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti e presenza del limite interpretativo.

```bash
python snip_36_contract.py
python -m unittest -v test_36_contract.py
```
