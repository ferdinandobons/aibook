# Piano interno. Capitolo 37

- Domanda centrale: quale contratto costruisce Anatomia del blocco moderno?
- Oggetto continuo: un residual stream dentro un blocco moderno; input guida: h di shape [batch, length, d] e norma misurata.
- Prerequisito stabile: Capitolo 36, Training distribuito e continued pretraining.
- Gap: norm, attention, MLP e gating nell'ordine scelto.
- Output consegnato: h' con shape preservata e statistiche confrontabili; consumer successivo: Capitolo 38, Posizione e contesto lungo.
- Invariante principale: ordine dei sottolayer e shape sono parte del blocco.
- Visuali: BLOCK-01 e BLOCK-02, con famiglie compositive variabili.
- Snippet: code/snip_37_contract.py; output: code/outputs/SNIP-37-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Residual stream

- Ultima affermazione stabile: un residual stream dentro un blocco moderno.
- Concetto nuovo: Ogni sottolayer produce un aggiornamento sommato a un percorso identità.
- Input e shape: h di shape [batch, length, d] e norma misurata.
- Operazione: norm, attention, MLP e gating nell'ordine scelto.
- Output e shape: h' con shape preservata e statistiche confrontabili.
- Che cosa cambia: il passaggio specifico di «Residual stream».
- Invariante: ordine dei sottolayer e shape sono parte del blocco.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: pre-norm e residuale su un vettore di due coordinate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Pre-norm e post-norm.
- Prova: SRC-37-001 e sezione pubblica corrispondente.

## Transizione 2. Pre-norm e post-norm

- Ultima affermazione stabile: un residual stream dentro un blocco moderno.
- Concetto nuovo: La posizione della normalizzazione cambia il percorso dei gradienti e il contratto del blocco.
- Input e shape: h di shape [batch, length, d] e norma misurata.
- Operazione: norm, attention, MLP e gating nell'ordine scelto.
- Output e shape: h' con shape preservata e statistiche confrontabili.
- Che cosa cambia: il passaggio specifico di «Pre-norm e post-norm».
- Invariante: ordine dei sottolayer e shape sono parte del blocco.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: pre-norm e residuale su un vettore di due coordinate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: RMSNorm.
- Prova: SRC-37-002 e sezione pubblica corrispondente.

## Transizione 3. RMSNorm

- Ultima affermazione stabile: un residual stream dentro un blocco moderno.
- Concetto nuovo: RMSNorm scala usando la media quadratica e non sottrae la media.
- Input e shape: h di shape [batch, length, d] e norma misurata.
- Operazione: norm, attention, MLP e gating nell'ordine scelto.
- Output e shape: h' con shape preservata e statistiche confrontabili.
- Che cosa cambia: il passaggio specifico di «RMSNorm».
- Invariante: ordine dei sottolayer e shape sono parte del blocco.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: pre-norm e residuale su un vettore di due coordinate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: SwiGLU.
- Prova: SRC-37-003 e sezione pubblica corrispondente.

## Transizione 4. SwiGLU

- Ultima affermazione stabile: un residual stream dentro un blocco moderno.
- Concetto nuovo: Due proiezioni di ingresso costruiscono un gate moltiplicativo prima della proiezione down.
- Input e shape: h di shape [batch, length, d] e norma misurata.
- Operazione: norm, attention, MLP e gating nell'ordine scelto.
- Output e shape: h' con shape preservata e statistiche confrontabili.
- Che cosa cambia: il passaggio specifico di «SwiGLU».
- Invariante: ordine dei sottolayer e shape sono parte del blocco.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: pre-norm e residuale su un vettore di due coordinate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Ordine e parallelismo.
- Prova: SRC-37-004 e sezione pubblica corrispondente.

## Transizione 5. Ordine e parallelismo

- Ultima affermazione stabile: un residual stream dentro un blocco moderno.
- Concetto nuovo: Attention e MLP possono essere sequenziali o paralleli; il nome del modello non basta a ricostruire l'ordine.
- Input e shape: h di shape [batch, length, d] e norma misurata.
- Operazione: norm, attention, MLP e gating nell'ordine scelto.
- Output e shape: h' con shape preservata e statistiche confrontabili.
- Che cosa cambia: il passaggio specifico di «Ordine e parallelismo».
- Invariante: ordine dei sottolayer e shape sono parte del blocco.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: pre-norm e residuale su un vettore di due coordinate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Posizione e contesto lungo.
- Prova: SRC-37-001 e sezione pubblica corrispondente.
