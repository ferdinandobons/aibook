# Esempio verificato. Capitolo 53

`snip_53_contract.py` esegue il caso minimo usato nel testo di **Test-time compute, ricerca e controllo del budget**. `test_53_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_53_contract.py
python -m unittest -v test_53_contract.py
```
