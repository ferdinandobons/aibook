# Esempio verificato. Capitolo 90

`snip_90_contract.py` esegue il caso minimo usato nel testo di **Poisoning, backdoor, extraction e supply chain**. `test_90_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_90_contract.py
python -m unittest -v test_90_contract.py
```
