# Esempio verificato. Capitolo 41

`snip_41_contract.py` esegue il caso minimo usato nel testo di **Linear attention, fast weights e delta rule**. `test_41_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_41_contract.py
python -m unittest -v test_41_contract.py
```
