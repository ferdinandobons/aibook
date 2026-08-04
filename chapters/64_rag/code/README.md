# Esempio verificato. Capitolo 64

`snip_64_contract.py` esegue il caso minimo usato nel testo di **Retrieval-Augmented Generation**. `test_64_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_64_contract.py
python -m unittest -v test_64_contract.py
```
