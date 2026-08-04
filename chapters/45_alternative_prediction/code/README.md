# Esempio verificato. Capitolo 45

`snip_45_contract.py` esegue il caso minimo usato nel testo di **Byte, predizione multi-token e language diffusion**. `test_45_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti e presenza del limite interpretativo.

```bash
python snip_45_contract.py
python -m unittest -v test_45_contract.py
```
