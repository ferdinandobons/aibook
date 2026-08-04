# Esempio verificato. Capitolo 31

`snip_31_contract.py` esegue il caso minimo usato nel testo di **Dalla rappresentazione linguistica agli LLM**. `test_31_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_31_contract.py
python -m unittest -v test_31_contract.py
```
