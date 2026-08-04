# Esempio verificato. Capitolo 80

`snip_80_contract.py` esegue il caso minimo usato nel testo di **Serving disaggregato e inference distribuita**. `test_80_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_80_contract.py
python -m unittest -v test_80_contract.py
```
