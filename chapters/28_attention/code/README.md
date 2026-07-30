# Codice del Capitolo 28

## Ambiente eseguito

Vedere `environments/python-pytorch.txt`.

## Comandi

```bash
python snip_att_001_single_query.py
python snip_att_002_matrix_api.py
python snip_att_003_causal_mask.py
python snip_att_004_multihead_shapes.py
python -m unittest -v test_attention_snippets.py
```

## Mappa

| ID | File | Scopo |
|---|---|---|
| `SNIP-ATT-001` | `snip_att_001_single_query.py` | esempio numerico per una query |
| `SNIP-ATT-002` | `snip_att_002_matrix_api.py` | formula matriciale e confronto API |
| `SNIP-ATT-003` | `snip_att_003_causal_mask.py` | causal mask e pesi futuri nulli |
| `SNIP-ATT-004` | `snip_att_004_multihead_shapes.py` | shape di output e pesi per due head |
