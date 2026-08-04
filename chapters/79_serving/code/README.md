# Esempio verificato. Capitolo 79

`snip_79_contract.py` esegue il caso minimo usato nel testo di **Serving, batching e scheduling**. `test_79_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_79_contract.py
python -m unittest -v test_79_contract.py
```
