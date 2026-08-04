# Piano interno. Capitolo 48

- Domanda centrale: quale contratto costruisce Preferenze, reward model e RLHF?
- Oggetto continuo: dimostrazioni, preferenze, reward model e policy; input guida: prompt, risposta scelta, rifiutata e score.
- Prerequisito stabile: Capitolo 47, Fine-tuning efficiente.
- Gap: fit del reward, KL e aggiornamento della policy.
- Output consegnato: reward, log-probability e comportamento aggiornato; consumer successivo: Capitolo 49, Ottimizzazione diretta delle preferenze.
- Invariante principale: il reward è un proxy e può essere ottimizzato in modo scorretto.
- Visuali: RLHF-01 e RLHF-02, con famiglie compositive variabili.
- Snippet: code/snip_48_contract.py; output: code/outputs/SNIP-48-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Dalle dimostrazioni alle preferenze

- Ultima affermazione stabile: dimostrazioni, preferenze, reward model e policy.
- Concetto nuovo: Dati di confronto ordinano risposte alla stessa richiesta. Il protocollo deve registrare istruzioni ai valutatori, accordo e slice.
- Input e shape: prompt, risposta scelta, rifiutata e score.
- Operazione: fit del reward, KL e aggiornamento della policy.
- Output e shape: reward, log-probability e comportamento aggiornato.
- Che cosa cambia: il passaggio specifico di «Dalle dimostrazioni alle preferenze».
- Invariante: il reward è un proxy e può essere ottimizzato in modo scorretto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due risposte con margine di reward e penalità KL; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Reward model.
- Prova: SRC-48-001 e sezione pubblica corrispondente.

## Transizione 2. Reward model

- Ultima affermazione stabile: dimostrazioni, preferenze, reward model e policy.
- Concetto nuovo: Un modello assegna uno score alle risposte e viene addestrato con una loss di ranking. Lo score è una stima del dataset di preferenze, non una misura universale di qualità.
- Input e shape: prompt, risposta scelta, rifiutata e score.
- Operazione: fit del reward, KL e aggiornamento della policy.
- Output e shape: reward, log-probability e comportamento aggiornato.
- Che cosa cambia: il passaggio specifico di «Reward model».
- Invariante: il reward è un proxy e può essere ottimizzato in modo scorretto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due risposte con margine di reward e penalità KL; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Policy optimization.
- Prova: SRC-48-002 e sezione pubblica corrispondente.

## Transizione 3. Policy optimization

- Ultima affermazione stabile: dimostrazioni, preferenze, reward model e policy.
- Concetto nuovo: PPO o algoritmi affini aggiornano la policy per aumentare reward mantenendo un vincolo rispetto al modello di riferimento.
- Input e shape: prompt, risposta scelta, rifiutata e score.
- Operazione: fit del reward, KL e aggiornamento della policy.
- Output e shape: reward, log-probability e comportamento aggiornato.
- Che cosa cambia: il passaggio specifico di «Policy optimization».
- Invariante: il reward è un proxy e può essere ottimizzato in modo scorretto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due risposte con margine di reward e penalità KL; provare anche una condizione incoerente e osservare il controllo.
- Consumer: KL e reward hacking.
- Prova: SRC-48-003 e sezione pubblica corrispondente.

## Transizione 4. KL e reward hacking

- Ultima affermazione stabile: dimostrazioni, preferenze, reward model e policy.
- Concetto nuovo: Il termine KL limita lo spostamento della policy. Un reward imperfetto può essere sfruttato senza migliorare l'obiettivo umano.
- Input e shape: prompt, risposta scelta, rifiutata e score.
- Operazione: fit del reward, KL e aggiornamento della policy.
- Output e shape: reward, log-probability e comportamento aggiornato.
- Che cosa cambia: il passaggio specifico di «KL e reward hacking».
- Invariante: il reward è un proxy e può essere ottimizzato in modo scorretto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due risposte con margine di reward e penalità KL; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Valutazione e sicurezza.
- Prova: SRC-48-004 e sezione pubblica corrispondente.

## Transizione 5. Valutazione e sicurezza

- Ultima affermazione stabile: dimostrazioni, preferenze, reward model e policy.
- Concetto nuovo: Win rate, reward e giudizi automatici devono essere affiancati da controlli indipendenti, red teaming e analisi di regressione.
- Input e shape: prompt, risposta scelta, rifiutata e score.
- Operazione: fit del reward, KL e aggiornamento della policy.
- Output e shape: reward, log-probability e comportamento aggiornato.
- Che cosa cambia: il passaggio specifico di «Valutazione e sicurezza».
- Invariante: il reward è un proxy e può essere ottimizzato in modo scorretto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due risposte con margine di reward e penalità KL; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Ottimizzazione diretta delle preferenze.
- Prova: SRC-48-001 e sezione pubblica corrispondente.
