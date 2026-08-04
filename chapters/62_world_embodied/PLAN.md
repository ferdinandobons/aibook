# Piano interno. Capitolo 62

- Domanda centrale: quale contratto costruisce World model, embodied AI e vision-language-action?
- Oggetto continuo: lo stato di un agente embodied nel mondo; input guida: osservazione, stato, azione e dinamica.
- Prerequisito stabile: Capitolo 61, 3D, spazio e rappresentazione delle scene.
- Gap: world model, planning, VLA e controllo.
- Output consegnato: azione, stato previsto e risultato fisico; consumer successivo: Capitolo 63, Information retrieval.
- Invariante principale: sim-to-real richiede una misura sul sistema reale.
- Visuali: EMBODIED-01 e EMBODIED-02, con famiglie compositive variabili.
- Snippet: code/snip_62_contract.py; output: code/outputs/SNIP-62-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Modello della dinamica

- Ultima affermazione stabile: lo stato di un agente embodied nel mondo.
- Concetto nuovo: Un world model predice stati, osservazioni o latent futuri dato lo stato corrente e un'azione.
- Input e shape: osservazione, stato, azione e dinamica.
- Operazione: world model, planning, VLA e controllo.
- Output e shape: azione, stato previsto e risultato fisico.
- Che cosa cambia: il passaggio specifico di «Modello della dinamica».
- Invariante: sim-to-real richiede una misura sul sistema reale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un'azione prevista in simulazione e il controllo del suo esito; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Planning nel modello.
- Prova: SRC-62-001 e sezione pubblica corrispondente.

## Transizione 2. Planning nel modello

- Ultima affermazione stabile: lo stato di un agente embodied nel mondo.
- Concetto nuovo: Traiettorie candidate vengono simulate e valutate prima di agire. Errori del modello possono essere sfruttati dal planner.
- Input e shape: osservazione, stato, azione e dinamica.
- Operazione: world model, planning, VLA e controllo.
- Output e shape: azione, stato previsto e risultato fisico.
- Che cosa cambia: il passaggio specifico di «Planning nel modello».
- Invariante: sim-to-real richiede una misura sul sistema reale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un'azione prevista in simulazione e il controllo del suo esito; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Embodied perception.
- Prova: SRC-62-002 e sezione pubblica corrispondente.

## Transizione 3. Embodied perception

- Ultima affermazione stabile: lo stato di un agente embodied nel mondo.
- Concetto nuovo: Un agente fisico collega camera, propriocezione, linguaggio e coordinate. Latenza e calibrazione influenzano ogni azione.
- Input e shape: osservazione, stato, azione e dinamica.
- Operazione: world model, planning, VLA e controllo.
- Output e shape: azione, stato previsto e risultato fisico.
- Che cosa cambia: il passaggio specifico di «Embodied perception».
- Invariante: sim-to-real richiede una misura sul sistema reale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un'azione prevista in simulazione e il controllo del suo esito; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Vision-language-action.
- Prova: SRC-62-003 e sezione pubblica corrispondente.

## Transizione 4. Vision-language-action

- Ultima affermazione stabile: lo stato di un agente embodied nel mondo.
- Concetto nuovo: VLA mappa osservazioni e istruzioni a token o controlli di azione. Frequenza e discretizzazione devono essere dichiarate.
- Input e shape: osservazione, stato, azione e dinamica.
- Operazione: world model, planning, VLA e controllo.
- Output e shape: azione, stato previsto e risultato fisico.
- Che cosa cambia: il passaggio specifico di «Vision-language-action».
- Invariante: sim-to-real richiede una misura sul sistema reale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un'azione prevista in simulazione e il controllo del suo esito; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sicurezza e sim-to-real.
- Prova: SRC-62-004 e sezione pubblica corrispondente.

## Transizione 5. Sicurezza e sim-to-real

- Ultima affermazione stabile: lo stato di un agente embodied nel mondo.
- Concetto nuovo: Simulazione, fallback, limiti di forza e supervisione umana riducono rischio, ma non eliminano mismatch con il mondo reale.
- Input e shape: osservazione, stato, azione e dinamica.
- Operazione: world model, planning, VLA e controllo.
- Output e shape: azione, stato previsto e risultato fisico.
- Che cosa cambia: il passaggio specifico di «Sicurezza e sim-to-real».
- Invariante: sim-to-real richiede una misura sul sistema reale.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un'azione prevista in simulazione e il controllo del suo esito; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Information retrieval.
- Prova: SRC-62-001 e sezione pubblica corrispondente.
