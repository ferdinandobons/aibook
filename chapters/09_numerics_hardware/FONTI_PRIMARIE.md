# Fonti primarie e autorevoli. Capitolo 9

## Stato

- Ultima verifica web: 31 luglio 2026
- Ambito: aritmetica floating point, dtype, stabilità numerica, mixed precision, hardware e riproducibilità

## SRC-NUM-001. IEEE 754-2019

IEEE Standards Association, *IEEE Standard for Floating-Point Arithmetic*, IEEE 754-2019.

URL ufficiale: https://standards.ieee.org/ieee/754/6210/

Uso: formati e operazioni floating point, arrotondamento, valori speciali ed eccezioni.

## SRC-NUM-002. Goldberg 1991

David Goldberg, *What Every Computer Scientist Should Know About Floating-Point Arithmetic*, ACM Computing Surveys, 1991.

Uso: errore di arrotondamento, cancellazione, guard digits e non associatività.

## SRC-NUM-003. Higham

Nicholas J. Higham, *Accuracy and Stability of Numerical Algorithms*, seconda edizione, SIAM, 2002.

Uso: errore forward e backward, condizionamento e stabilità degli algoritmi.

## SRC-NUM-004. PyTorch numerical accuracy

Documentazione ufficiale PyTorch stable, `Numerical accuracy`.

URL: https://docs.pytorch.org/docs/stable/notes/numerical_accuracy.html

Uso: accuratezza finita, non associatività, differenze CPU/GPU, operazioni batched, valori estremi, TF32 e riduzioni in precisione ridotta.

Data di controllo: 31 luglio 2026. La pagina risultava aggiornata il 29 gennaio 2026.

## SRC-NUM-005. PyTorch dtype e type info

Documentazione ufficiale PyTorch stable:

- https://docs.pytorch.org/docs/stable/tensor_attributes.html
- https://docs.pytorch.org/docs/stable/type_info.html

Uso: `torch.dtype`, strutture `float16`, `bfloat16`, `float32`, `float64`, proprietà `torch.finfo`, `eps`, `tiny`, `max` e numero di bit.

## SRC-NUM-006. PyTorch AMP

Documentazione ufficiale PyTorch stable, `torch.amp`.

URL: https://docs.pytorch.org/docs/stable/amp.html

Uso: mixed precision, autocast, scelta degli operatori, CPU bfloat16, CUDA float16 e `GradScaler`.

## SRC-NUM-007. PyTorch logsumexp

Documentazione ufficiale PyTorch stable, `torch.logsumexp`.

URL: https://docs.pytorch.org/docs/stable/generated/torch.logsumexp.html

Uso: calcolo stabilizzato del logaritmo della somma di esponenziali.

## SRC-NUM-008. PyTorch riproducibilità

Documentazione ufficiale PyTorch stable, `Reproducibility`.

URL: https://docs.pytorch.org/docs/stable/notes/randomness.html

Uso: limiti della riproducibilità tra release, piattaforme, CPU e GPU; algoritmi deterministici e costo potenziale.

## SRC-NUM-009. Precisione delle matmul float32

Documentazione ufficiale PyTorch, `torch.set_float32_matmul_precision`.

URL: https://docs.pytorch.org/docs/stable/generated/torch.set_float32_matmul_precision.html

Uso: distinzione tra dtype esterno e precisione interna delle moltiplicazioni matriciali float32.

## SRC-NUM-010. Mixed Precision Training

Paulius Micikevicius et al., *Mixed Precision Training*, arXiv:1710.03740, 2017.

URL: https://arxiv.org/abs/1710.03740

Uso: master weights in precisione singola e loss scaling per gestire il range limitato dei gradienti fp16.

## SRC-NUM-011. BFLOAT16

Dhiraj Kalamkar et al., *A Study of BFLOAT16 for Deep Learning Training*, arXiv:1905.12322, 2019.

URL: https://arxiv.org/abs/1905.12322

Uso: struttura bfloat16, range simile a fp32 e precisione ridotta; risultati empirici nel perimetro del paper.

## SRC-NUM-012. NVIDIA CUDA Programming Guide

NVIDIA, *CUDA Programming Guide*, sezioni sui tipi floating point e sui formati alternativi.

URL: https://docs.nvidia.com/cuda/cuda-programming-guide/

Uso: fp16, bfloat16, TF32, Tensor Core e tipi di accumulatore supportati.

## SRC-NUM-013. cuBLAS

NVIDIA, documentazione ufficiale cuBLAS.

URL: https://docs.nvidia.com/cuda/cublas/

Uso: modalità di calcolo, precisione degli input e degli accumulatori, Tensor Core e opzioni rapide.

## SRC-NUM-014. Roofline

Samuel Williams, Andrew Waterman e David Patterson, *Roofline: An Insightful Visual Performance Model for Multicore Architectures*, Communications of the ACM, 2009.

DOI: https://doi.org/10.1145/1498765.1498785

Uso: rapporto tra picco di calcolo, bandwidth e intensità aritmetica.

## Regola d'uso

- Le proprietà dei formati derivano da IEEE, PyTorch e documentazione hardware ufficiale.
- Le osservazioni eseguite derivano da `SNIP-NUM-001` nell'ambiente registrato.
- Nessuna accelerazione viene dichiarata senza misurazione sul dispositivo, kernel, shape e versione pertinenti.
- Le differenze osservate tra dtype non vengono interpretate automaticamente come perdita di qualità del modello.
