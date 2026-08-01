# Audit del codice. Capitolo 9

## Stato

- Snippet: `SNIP-NUM-001`
- Ambiente: Python 3.13.5, PyTorch 2.10.0+cpu, CPU
- Test: 7 superati
- Data: 31 luglio 2026
- Esito: **superato**

## Controlli

- [x] `torch.finfo` interrogato per fp16, bfloat16, fp32 e fp64;
- [x] `1 + eps/2` arrotonda a `1` nel run per tutti i dtype esaminati;
- [x] `1 + eps` produce il successivo valore maggiore di `1`;
- [x] esempio di non associatività riproducibile in float32;
- [x] formula ingenua di logsumexp produce intenzionalmente `inf`;
- [x] `torch.logsumexp` produce un valore finito;
- [x] conversione di `70000` in fp16 produce `inf`;
- [x] conversione in bfloat16 produce `70144`;
- [x] autocast CPU restituisce output bfloat16 per la matmul usata;
- [x] errore rispetto al riferimento fp32 misurato senza interpretarlo come benchmark;
- [x] byte di storage calcolati da shape ed `element_size`;
- [x] seed registrato;
- [x] output letterale salvato;
- [x] test rieseguiti in processo separato.

## Test registrati

```text
test_cpu_autocast_uses_bfloat16_for_matmul
test_dtype_range_and_precision_contracts
test_eps_is_observable_near_one
test_float32_addition_is_not_associative_for_constructed_case
test_fp16_and_bfloat16_have_different_range
test_stable_logsumexp_remains_finite
test_storage_bytes_follow_element_size
```

## Limiti

- nessuna GPU era disponibile nel run;
- non sono stati misurati tempo, throughput, consumo energetico o bandwidth;
- autocast e kernel possono cambiare tra versioni e device;
- il confronto della matmul usa una sola shape e un solo seed;
- l'assenza di errore nei test non dimostra stabilità di un modello completo;
- l'uso di `inf` è intenzionale e confinato agli esempi di range e formula ingenua.

## Verdetto

Il codice sostiene i claim osservabili del capitolo e non estende i risultati oltre l'ambiente dichiarato.
