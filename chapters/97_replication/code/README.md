# Esempio verificato. Capitolo 97

`snip_97_contract.py` esegue il caso minimo usato nel testo di **Riprodurre e leggere un paper**. `test_97_contract.py` conserva l'output atteso, controlla determinismo, serializzazione, valori finiti, forma del contratto e rifiuto dei casi non documentati.

```bash
python snip_97_contract.py
python -m unittest -v test_97_contract.py
```

## Replica indipendente con incertezza

Codice: `replication_protocol.py`; test: `test_replication_protocol.py`; output: `outputs/REPLICATION-PROTOCOL.txt`; ambiente: `environments/lab.txt`.
