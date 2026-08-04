# Esempio verificato. Capitolo 96

`snip_96_contract.py` esegue il caso minimo usato nel testo di **Progetto di produzione completo**. `test_96_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti e presenza del limite interpretativo.

```bash
python snip_96_contract.py
python -m unittest -v test_96_contract.py
```

## Gate offline, canary e rollback

Codice: `production_pipeline.py`; test: `test_production_pipeline.py`; output: `outputs/PRODUCTION-PIPELINE.txt`; ambiente: `environments/lab.txt`.
