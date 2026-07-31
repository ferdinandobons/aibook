# Registro dei claim. Capitolo 9

## Stato

- Data: 31 luglio 2026
- Claim aperti: 0
- Risultati eseguiti: associati a `SNIP-NUM-001`

| ID | Claim | Prova | Condizioni e limiti |
|---|---|---|---|
| `CLM-NUM-001` | Un formato floating point rappresenta soltanto un insieme finito di valori. | IEEE 754-2019; Goldberg 1991 | Non descrive numeri reali con precisione arbitraria. |
| `CLM-NUM-002` | Nei formati binari, segno, esponente e significando svolgono ruoli distinti. | IEEE 754-2019 | I dettagli cambiano tra i formati. |
| `CLM-NUM-003` | `torch.finfo.eps` è la distanza tra 1 e il successivo valore rappresentabile maggiore di 1. | PyTorch Type Info | Non è l'errore massimo di ogni operazione. |
| `CLM-NUM-004` | `tiny` e `max` descrivono il range normale positivo e il massimo finito del dtype. | PyTorch Type Info | Esistono anche subnormal, zero, inf e nan. |
| `CLM-NUM-005` | L'addizione floating point non è associativa in generale. | Goldberg; PyTorch Numerical Accuracy | L'esito dipende da valori, dtype e ordine. |
| `CLM-NUM-006` | Operazioni matematicamente equivalenti possono produrre risultati floating point differenti. | PyTorch Numerical Accuracy | Non implica automaticamente un bug. |
| `CLM-NUM-007` | CPU e GPU non sono garantite bitwise identiche anche con input e seed uguali. | PyTorch Numerical Accuracy; Reproducibility | Dipende da release, backend e algoritmi. |
| `CLM-NUM-008` | Un intermedio può overfloware anche quando il risultato matematico finale sarebbe rappresentabile. | PyTorch Numerical Accuracy | Esempio: norme e formule ingenue. |
| `CLM-NUM-009` | `torch.logsumexp` calcola il logaritmo della somma di esponenziali con una formulazione stabilizzata. | PyTorch `logsumexp` | Il risultato resta soggetto alla precisione finita. |
| `CLM-NUM-010` | `float16` e `bfloat16` occupano entrambi 16 bit ma allocano diversamente esponente e significando. | PyTorch Tensor Attributes; BFLOAT16 paper | bfloat16 non coincide con IEEE binary16. |
| `CLM-NUM-011` | bfloat16 ha range vicino a float32 e precisione inferiore a float16 vicino a 1. | PyTorch Type Info; Kalamkar et al. | Il confronto riguarda il formato, non la qualità di un modello specifico. |
| `CLM-NUM-012` | float16 ha massimo finito 65504 e può rappresentare 70000 come `inf`. | PyTorch Type Info; risultato eseguito | Comportamento osservato nel cast del run registrato. |
| `CLM-NUM-013` | bfloat16 rappresenta 70000 con arrotondamento a 70144 nel run registrato. | `SNIP-NUM-001` | Risultato dell'ambiente CPU dichiarato. |
| `CLM-NUM-014` | Mixed precision usa dtype differenti per operazioni differenti. | PyTorch AMP | La policy dipende da device, backend, operatore e versione. |
| `CLM-NUM-015` | Su CPU, autocast usa normalmente bfloat16 per operatori idonei e mantiene altre operazioni in float32. | PyTorch AMP | Elenco degli operatori soggetto a versione. |
| `CLM-NUM-016` | Nel training fp16, loss scaling può evitare che gradienti piccoli diventino zero prima dell'update. | Micikevicius et al.; PyTorch AMP | Non risolve instabilità di qualunque origine. |
| `CLM-NUM-017` | `GradScaler` e autocast sono componenti separati. | PyTorch AMP | Possono essere usati separatamente quando appropriato. |
| `CLM-NUM-018` | Molte moltiplicazioni fp16 o bfloat16 accumulano in float32 per maggiore accuratezza, ma alcuni backend consentono riduzioni a precisione inferiore. | PyTorch Numerical Accuracy; CUDA/cuBLAS | Dipende da hardware e configurazione. |
| `CLM-NUM-019` | TF32 conserva il range di float32 ma usa precisione ridotta negli input delle operazioni Tensor Core. | PyTorch Numerical Accuracy; NVIDIA CUDA | Supporto su GPU e operazioni pertinenti. |
| `CLM-NUM-020` | Il dtype dell'output non rivela necessariamente la precisione interna usata dalla matmul. | PyTorch `set_float32_matmul_precision`; cuBLAS | La configurazione e il backend determinano il percorso. |
| `CLM-NUM-021` | Ridurre i byte per elemento può ridurre memoria e traffico, ma non garantisce un'accelerazione end-to-end. | Roofline; PyTorch AMP | Contano kernel, shape, overhead, bandwidth e picco di calcolo. |
| `CLM-NUM-022` | Il modello Roofline separa un limite di calcolo da un limite di bandwidth tramite l'intensità aritmetica. | Williams et al. 2009 | Modello semplificato; richiede misure del sistema. |
| `CLM-NUM-023` | Gli algoritmi deterministici possono essere più lenti. | PyTorch Reproducibility | La differenza dipende dall'operazione e dal backend. |
| `CLM-NUM-024` | Impostare lo stesso seed non garantisce identità bitwise tra piattaforme e release. | PyTorch Reproducibility | Il seed controlla soltanto alcune fonti di variabilità. |
| `CLM-NUM-025` | `float64` può ridurre errori di arrotondamento e overflow in alcuni casi, ma non corregge algoritmi mal condizionati o instabili. | Higham; PyTorch Numerical Accuracy | Serve distinguere condizionamento e stabilità. |
| `CLM-NUM-026` | Nel run registrato, `(a+b)+c` vale circa 3,14 mentre `a+(b+c)` vale 0 in float32 per `a=10^20`, `b=-10^20`, `c=3,14`. | `SNIP-NUM-001` | Esempio costruito di cancellazione e arrotondamento. |
| `CLM-NUM-027` | Nel run registrato, la formula ingenua di logsumexp produce `inf`, mentre `torch.logsumexp` produce circa 1000,4076. | `SNIP-NUM-001` | Input `[1000,999,998]`, float32 CPU. |
| `CLM-NUM-028` | Nel run registrato, autocast CPU produce una matmul bfloat16 con errore massimo assoluto circa 0,0464 rispetto al riferimento float32. | `SNIP-NUM-001` | Matrici 16×16, seed 0, CPU; non è un benchmark generale. |
| `CLM-NUM-029` | Un tensore 1024×1024 richiede teoricamente 4 MiB in float32 e 2 MiB in float16, esclusi allocator e metadati. | Derivazione da element size; `SNIP-NUM-001` | Non equivale alla memoria totale del modello o del processo. |

## Regola di propagazione

Ogni modifica a valori, dtype, configurazioni AMP o semantica delle API riapre codice, claim, visuali e audit temporale.
