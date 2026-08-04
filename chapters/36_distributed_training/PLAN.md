# Piano interno. Capitolo 36

- Domanda centrale: quale contratto costruisce Training distribuito e continued pretraining?
- Oggetto continuo: gradienti e stato distribuiti tra worker; input guida: microbatch, worker, shard e topologia.
- Prerequisito stabile: Capitolo 35, La ricetta di pretraining.
- Gap: all-reduce, sharding, pipeline e recovery.
- Output consegnato: gradiente ridotto, stato sincronizzato e fault osservato; consumer successivo: Capitolo 37, Anatomia del blocco moderno.
- Invariante principale: la riduzione e il conteggio del batch devono essere dichiarati.
- Visuali: DIST-01 e DIST-02, con famiglie compositive variabili.
- Snippet: code/snip_36_contract.py; output: code/outputs/SNIP-36-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Data parallelism

- Ultima affermazione stabile: gradienti e stato distribuiti tra worker.
- Concetto nuovo: Repliche elaborano sotto-batch e aggregano gradienti. Media e loss reduction devono essere coerenti.
- Input e shape: microbatch, worker, shard e topologia.
- Operazione: all-reduce, sharding, pipeline e recovery.
- Output e shape: gradiente ridotto, stato sincronizzato e fault osservato.
- Che cosa cambia: il passaggio specifico di «Data parallelism».
- Invariante: la riduzione e il conteggio del batch devono essere dichiarati.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due worker con gradienti diversi e media esplicita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: ZeRO e FSDP.
- Prova: SRC-36-001 e sezione pubblica corrispondente.

## Transizione 2. ZeRO e FSDP

- Ultima affermazione stabile: gradienti e stato distribuiti tra worker.
- Concetto nuovo: Parametri, gradienti e optimizer state vengono shardati tra worker.
- Input e shape: microbatch, worker, shard e topologia.
- Operazione: all-reduce, sharding, pipeline e recovery.
- Output e shape: gradiente ridotto, stato sincronizzato e fault osservato.
- Che cosa cambia: il passaggio specifico di «ZeRO e FSDP».
- Invariante: la riduzione e il conteggio del batch devono essere dichiarati.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due worker con gradienti diversi e media esplicita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Tensor e pipeline parallelism.
- Prova: SRC-36-002 e sezione pubblica corrispondente.

## Transizione 3. Tensor e pipeline parallelism

- Ultima affermazione stabile: gradienti e stato distribuiti tra worker.
- Concetto nuovo: Matrici o gruppi di layer vengono divisi, introducendo collective e microbatch.
- Input e shape: microbatch, worker, shard e topologia.
- Operazione: all-reduce, sharding, pipeline e recovery.
- Output e shape: gradiente ridotto, stato sincronizzato e fault osservato.
- Che cosa cambia: il passaggio specifico di «Tensor e pipeline parallelism».
- Invariante: la riduzione e il conteggio del batch devono essere dichiarati.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due worker con gradienti diversi e media esplicita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Topologia e fault tolerance.
- Prova: SRC-36-003 e sezione pubblica corrispondente.

## Transizione 4. Topologia e fault tolerance

- Ultima affermazione stabile: gradienti e stato distribuiti tra worker.
- Concetto nuovo: Banda, latenza, checkpoint e cursor dei dati diventano parte della ricetta.
- Input e shape: microbatch, worker, shard e topologia.
- Operazione: all-reduce, sharding, pipeline e recovery.
- Output e shape: gradiente ridotto, stato sincronizzato e fault osservato.
- Che cosa cambia: il passaggio specifico di «Topologia e fault tolerance».
- Invariante: la riduzione e il conteggio del batch devono essere dichiarati.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due worker con gradienti diversi e media esplicita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Continued pretraining.
- Prova: SRC-36-004 e sezione pubblica corrispondente.

## Transizione 5. Continued pretraining

- Ultima affermazione stabile: gradienti e stato distribuiti tra worker.
- Concetto nuovo: Un checkpoint viene adattato a nuovi dati con learning rate, mixture e valutazioni di regressione dichiarate.
- Input e shape: microbatch, worker, shard e topologia.
- Operazione: all-reduce, sharding, pipeline e recovery.
- Output e shape: gradiente ridotto, stato sincronizzato e fault osservato.
- Che cosa cambia: il passaggio specifico di «Continued pretraining».
- Invariante: la riduzione e il conteggio del batch devono essere dichiarati.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due worker con gradienti diversi e media esplicita; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Anatomia del blocco moderno.
- Prova: SRC-36-001 e sezione pubblica corrispondente.
