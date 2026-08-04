# Esempio verificato. Capitolo 78

`snip_78_contract.py` esegue il caso minimo usato nel testo di **KV cache e riuso del contesto**. `test_78_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_78_contract.py
python -m unittest -v test_78_contract.py
```
