# Piano interno. Capitolo 49

- Domanda centrale: quale contratto costruisce Ottimizzazione diretta delle preferenze?
- Oggetto continuo: una coppia chosen-rejected per l'ottimizzazione diretta; input guida: prompt, log-probability della policy e riferimento.
- Prerequisito stabile: Capitolo 48, Preferenze, reward model e RLHF.
- Gap: margine DPO, beta e variante offline.
- Output consegnato: loss di preferenza e policy aggiornata; consumer successivo: Capitolo 50, Process supervision, outcome supervision e verifier.
- Invariante principale: la preferenza osservata non è una verità assoluta.
- Visuali: OPT-01 e OPT-02, con famiglie compositive variabili.
- Snippet: code/snip_49_contract.py; output: code/outputs/SNIP-49-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Evitare un reward model esplicito

- Ultima affermazione stabile: una coppia chosen-rejected per l'ottimizzazione diretta.
- Concetto nuovo: DPO riscrive un obiettivo di preferenza usando log-probability della policy e del riferimento, senza una fase PPO separata.
- Input e shape: prompt, log-probability della policy e riferimento.
- Operazione: margine DPO, beta e variante offline.
- Output e shape: loss di preferenza e policy aggiornata.
- Che cosa cambia: il passaggio specifico di «Evitare un reward model esplicito».
- Invariante: la preferenza osservata non è una verità assoluta.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: margine 0,8 con beta dichiarato e riferimento invariato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Coppie chosen e rejected.
- Prova: SRC-49-001 e sezione pubblica corrispondente.

## Transizione 2. Coppie chosen e rejected

- Ultima affermazione stabile: una coppia chosen-rejected per l'ottimizzazione diretta.
- Concetto nuovo: Ogni esempio richiede la stessa condizione e due risposte confrontabili. Errori o stili spurii possono diventare scorciatoie.
- Input e shape: prompt, log-probability della policy e riferimento.
- Operazione: margine DPO, beta e variante offline.
- Output e shape: loss di preferenza e policy aggiornata.
- Che cosa cambia: il passaggio specifico di «Coppie chosen e rejected».
- Invariante: la preferenza osservata non è una verità assoluta.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: margine 0,8 con beta dichiarato e riferimento invariato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Temperatura beta.
- Prova: SRC-49-002 e sezione pubblica corrispondente.

## Transizione 3. Temperatura beta

- Ultima affermazione stabile: una coppia chosen-rejected per l'ottimizzazione diretta.
- Concetto nuovo: Beta controlla la forza relativa del vincolo rispetto al modello di riferimento e modifica i gradienti sulle coppie.
- Input e shape: prompt, log-probability della policy e riferimento.
- Operazione: margine DPO, beta e variante offline.
- Output e shape: loss di preferenza e policy aggiornata.
- Che cosa cambia: il passaggio specifico di «Temperatura beta».
- Invariante: la preferenza osservata non è una verità assoluta.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: margine 0,8 con beta dichiarato e riferimento invariato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: IPO, KTO, ORPO e varianti.
- Prova: SRC-49-003 e sezione pubblica corrispondente.

## Transizione 4. IPO, KTO, ORPO e varianti

- Ultima affermazione stabile: una coppia chosen-rejected per l'ottimizzazione diretta.
- Concetto nuovo: Le varianti cambiano assunzioni, forma della loss o tipo di feedback. I nomi non rendono gli obiettivi intercambiabili.
- Input e shape: prompt, log-probability della policy e riferimento.
- Operazione: margine DPO, beta e variante offline.
- Output e shape: loss di preferenza e policy aggiornata.
- Che cosa cambia: il passaggio specifico di «IPO, KTO, ORPO e varianti».
- Invariante: la preferenza osservata non è una verità assoluta.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: margine 0,8 con beta dichiarato e riferimento invariato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Offline preference data.
- Prova: SRC-49-004 e sezione pubblica corrispondente.

## Transizione 5. Offline preference data

- Ultima affermazione stabile: una coppia chosen-rejected per l'ottimizzazione diretta.
- Concetto nuovo: L'ottimizzazione resta limitata alla copertura del dataset. Nuove policy possono visitare risposte non rappresentate nelle coppie.
- Input e shape: prompt, log-probability della policy e riferimento.
- Operazione: margine DPO, beta e variante offline.
- Output e shape: loss di preferenza e policy aggiornata.
- Che cosa cambia: il passaggio specifico di «Offline preference data».
- Invariante: la preferenza osservata non è una verità assoluta.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: margine 0,8 con beta dichiarato e riferimento invariato; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Process supervision, outcome supervision e verifier.
- Prova: SRC-49-001 e sezione pubblica corrispondente.
