# Codice. Capitolo 9

## Snippet

`snip_num_001_precision_contracts.py` rende osservabili sette contratti numerici:

1. proprietà dei dtype tramite `torch.finfo`;
2. incremento rappresentabile vicino a uno;
3. non associatività dell'addizione floating point;
4. overflow della formula ingenua e stabilità di `logsumexp`;
5. range differente di fp16 e bfloat16;
6. autocast CPU in bfloat16 per una matmul;
7. byte teorici di storage per elemento.

## Esecuzione

```bash
python snip_num_001_precision_contracts.py
python -m unittest -v test_numerics_hardware.py
```

## Artefatti

- output: `outputs/SNIP-NUM-001.txt`;
- test: `outputs/TESTS.txt`;
- ambiente: `environments/python-pytorch.txt`;
- audit: `CODE_AUDIT.md`.

## Confini

- il run è CPU e non misura throughput;
- l'esempio autocast non rappresenta una GPU;
- l'errore della matmul dipende da seed, shape, valori e backend;
- i byte calcolati escludono metadati, allocator, copie, gradienti e stati dell'optimizer;
- i valori `inf` sono intenzionali negli esempi di overflow.
