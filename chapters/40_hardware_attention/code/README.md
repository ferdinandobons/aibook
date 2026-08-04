# Esempio verificato. Capitolo 40

`snip_40_contract.py` esegue il caso minimo usato nel testo di **Attention hardware-aware**. `test_40_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_40_contract.py
python -m unittest -v test_40_contract.py
```
