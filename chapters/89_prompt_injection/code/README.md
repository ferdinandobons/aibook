# Esempio verificato. Capitolo 89

`snip_89_contract.py` esegue il caso minimo usato nel testo di **Prompt injection e sicurezza dei tool**. `test_89_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_89_contract.py
python -m unittest -v test_89_contract.py
```
