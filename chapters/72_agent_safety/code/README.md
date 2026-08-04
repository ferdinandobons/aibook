# Esempio verificato. Capitolo 72

`snip_72_contract.py` esegue il caso minimo usato nel testo di **Sicurezza operativa degli agenti**. `test_72_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_72_contract.py
python -m unittest -v test_72_contract.py
```
