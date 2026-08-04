# Esempio verificato. Capitolo 46

`snip_46_contract.py` esegue il caso minimo usato nel testo di **Supervised fine-tuning e instruction tuning**. `test_46_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_46_contract.py
python -m unittest -v test_46_contract.py
```
