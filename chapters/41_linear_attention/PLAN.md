# Piano interno. Capitolo 41

- Domanda centrale: quale contratto costruisce Linear attention, fast weights e delta rule?
- Oggetto continuo: uno stato causale che sostituisce il prodotto quadratico; input guida: sequenza x_t, kernel fattorizzabile e stato.
- Prerequisito stabile: Capitolo 40, Attention hardware-aware.
- Gap: recurrence, normalizzazione e fast weights.
- Output consegnato: h_t e predizione con costo dichiarato; consumer successivo: Capitolo 42, State-space model, recurrence e long convolution.
- Invariante principale: la fattorizzazione cambia memoria e capacità di interazione.
- Visuali: LINATT-01 e LINATT-02, con famiglie compositive variabili.
- Snippet: code/snip_41_contract.py; output: code/outputs/SNIP-41-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Kernel fattorizzabile

- Ultima affermazione stabile: uno stato causale che sostituisce il prodotto quadratico.
- Concetto nuovo: Una feature map permette di riassociare i prodotti senza una matrice completa di score.
- Input e shape: sequenza x_t, kernel fattorizzabile e stato.
- Operazione: recurrence, normalizzazione e fast weights.
- Output e shape: h_t e predizione con costo dichiarato.
- Che cosa cambia: il passaggio specifico di «Kernel fattorizzabile».
- Invariante: la fattorizzazione cambia memoria e capacità di interazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre aggiornamenti causali con stato scalare; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Recurrence causale.
- Prova: SRC-41-001 e sezione pubblica corrispondente.

## Transizione 2. Recurrence causale

- Ultima affermazione stabile: uno stato causale che sostituisce il prodotto quadratico.
- Concetto nuovo: Statistiche S e z vengono aggiornate per token e hanno dimensione indipendente dalla lunghezza.
- Input e shape: sequenza x_t, kernel fattorizzabile e stato.
- Operazione: recurrence, normalizzazione e fast weights.
- Output e shape: h_t e predizione con costo dichiarato.
- Che cosa cambia: il passaggio specifico di «Recurrence causale».
- Invariante: la fattorizzazione cambia memoria e capacità di interazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre aggiornamenti causali con stato scalare; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Normalizzazione.
- Prova: SRC-41-002 e sezione pubblica corrispondente.

## Transizione 3. Normalizzazione

- Ultima affermazione stabile: uno stato causale che sostituisce il prodotto quadratico.
- Concetto nuovo: Il denominatore controlla la scala e richiede feature e stabilizzazione coerenti.
- Input e shape: sequenza x_t, kernel fattorizzabile e stato.
- Operazione: recurrence, normalizzazione e fast weights.
- Output e shape: h_t e predizione con costo dichiarato.
- Che cosa cambia: il passaggio specifico di «Normalizzazione».
- Invariante: la fattorizzazione cambia memoria e capacità di interazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre aggiornamenti causali con stato scalare; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Fast weights.
- Prova: SRC-41-003 e sezione pubblica corrispondente.

## Transizione 4. Fast weights

- Ultima affermazione stabile: uno stato causale che sostituisce il prodotto quadratico.
- Concetto nuovo: Lo stato può essere letto come memoria associativa che accumula coppie key-value.
- Input e shape: sequenza x_t, kernel fattorizzabile e stato.
- Operazione: recurrence, normalizzazione e fast weights.
- Output e shape: h_t e predizione con costo dichiarato.
- Che cosa cambia: il passaggio specifico di «Fast weights».
- Invariante: la fattorizzazione cambia memoria e capacità di interazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre aggiornamenti causali con stato scalare; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Delta rule.
- Prova: SRC-41-004 e sezione pubblica corrispondente.

## Transizione 5. Delta rule

- Ultima affermazione stabile: uno stato causale che sostituisce il prodotto quadratico.
- Concetto nuovo: L'update corregge l'errore tra value desiderato e value recuperato, riducendo la sovrascrittura cieca.
- Input e shape: sequenza x_t, kernel fattorizzabile e stato.
- Operazione: recurrence, normalizzazione e fast weights.
- Output e shape: h_t e predizione con costo dichiarato.
- Che cosa cambia: il passaggio specifico di «Delta rule».
- Invariante: la fattorizzazione cambia memoria e capacità di interazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre aggiornamenti causali con stato scalare; provare anche una condizione incoerente e osservare il controllo.
- Consumer: State-space model, recurrence e long convolution.
- Prova: SRC-41-001 e sezione pubblica corrispondente.
