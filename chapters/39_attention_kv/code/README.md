# Esempio verificato. Capitolo 39

`snip_39_contract.py` esegue il caso minimo usato nel testo di **Varianti dell'attention e gestione KV**. `test_39_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_39_contract.py
python -m unittest -v test_39_contract.py
```
