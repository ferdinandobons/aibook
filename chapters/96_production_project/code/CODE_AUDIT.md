# Audit del codice

- ambiente minimo: Python 3.13.12, CPU
- comando snippet: `python snip_96_contract.py`
- comando test: `python -m unittest -v test_96_contract.py`
- test del riferimento: 4 superati
- controlli: output atteso, determinismo, serializzazione, valori finiti, limite interpretativo
- laboratorio esteso: `python production_pipeline.py`
- test laboratorio: `python -m unittest -v test_production_pipeline.py` (5 superati)
- output laboratorio: `outputs/PRODUCTION-PIPELINE.txt`
- ambiente laboratorio: `environments/lab.txt`
- risultato: esempio didattico delimitato, non benchmark di produzione
- stato: verificato localmente; review autoriale aperta
