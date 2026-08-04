# Esempio verificato. Capitolo 88

`snip_88_contract.py` esegue il caso minimo usato nel testo di **Robustezza, jailbreak e attacchi adversarial**. `test_88_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_88_contract.py
python -m unittest -v test_88_contract.py
```
