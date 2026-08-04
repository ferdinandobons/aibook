# Esempio verificato. Capitolo 44

`snip_44_contract.py` esegue il caso minimo usato nel testo di **Mixture of Experts e calcolo condizionale**. `test_44_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_44_contract.py
python -m unittest -v test_44_contract.py
```
