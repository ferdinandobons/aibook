# Piano interno. Capitolo 88

- Domanda centrale: quale contratto costruisce Robustezza, jailbreak e attacchi adversarial?
- Oggetto continuo: una superficie di attacco e il comportamento sotto perturbazione; input guida: threat model, prompt, budget e risposta.
- Prerequisito stabile: Capitolo 87, Sparse autoencoder e interpretabilità scalabile.
- Gap: jailbreak, perturbazione, difesa e adaptive evaluation.
- Output consegnato: success rate, failure mode e costo della difesa; consumer successivo: Capitolo 89, Prompt injection e sicurezza dei tool.
- Invariante principale: un test superato non copre minacce non incluse nel protocollo.
- Visuali: JAILBREAK-01 e JAILBREAK-02, con famiglie compositive variabili.
- Snippet: code/snip_88_contract.py; output: code/outputs/SNIP-88-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Threat model

- Ultima affermazione stabile: una superficie di attacco e il comportamento sotto perturbazione.
- Concetto nuovo: Attaccante, accesso, obiettivo, budget e superficie definiscono il test. Un jailbreak testuale e un attacco ai pesi hanno contratti diversi.
- Input e shape: threat model, prompt, budget e risposta.
- Operazione: jailbreak, perturbazione, difesa e adaptive evaluation.
- Output e shape: success rate, failure mode e costo della difesa.
- Che cosa cambia: il passaggio specifico di «Threat model».
- Invariante: un test superato non copre minacce non incluse nel protocollo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stesso prompt con perturbazione e controllo di policy; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Perturbazioni.
- Prova: SRC-88-001 e sezione pubblica corrispondente.

## Transizione 2. Perturbazioni

- Ultima affermazione stabile: una superficie di attacco e il comportamento sotto perturbazione.
- Concetto nuovo: Typo, parafrasi, encoding e contenuti multimodali possono aggirare filtri superficiali.
- Input e shape: threat model, prompt, budget e risposta.
- Operazione: jailbreak, perturbazione, difesa e adaptive evaluation.
- Output e shape: success rate, failure mode e costo della difesa.
- Che cosa cambia: il passaggio specifico di «Perturbazioni».
- Invariante: un test superato non copre minacce non incluse nel protocollo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stesso prompt con perturbazione e controllo di policy; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Ottimizzazione adversarial.
- Prova: SRC-88-002 e sezione pubblica corrispondente.

## Transizione 3. Ottimizzazione adversarial

- Ultima affermazione stabile: una superficie di attacco e il comportamento sotto perturbazione.
- Concetto nuovo: Suffix e prompt vengono cercati per aumentare una loss di attacco. Trasferibilità e query budget devono essere riportati.
- Input e shape: threat model, prompt, budget e risposta.
- Operazione: jailbreak, perturbazione, difesa e adaptive evaluation.
- Output e shape: success rate, failure mode e costo della difesa.
- Che cosa cambia: il passaggio specifico di «Ottimizzazione adversarial».
- Invariante: un test superato non copre minacce non incluse nel protocollo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stesso prompt con perturbazione e controllo di policy; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Difese.
- Prova: SRC-88-003 e sezione pubblica corrispondente.

## Transizione 4. Difese

- Ultima affermazione stabile: una superficie di attacco e il comportamento sotto perturbazione.
- Concetto nuovo: Training, filtri, classificatori e refusal possono ridurre alcuni attacchi e introdurre falsi positivi o nuove bypass.
- Input e shape: threat model, prompt, budget e risposta.
- Operazione: jailbreak, perturbazione, difesa e adaptive evaluation.
- Output e shape: success rate, failure mode e costo della difesa.
- Che cosa cambia: il passaggio specifico di «Difese».
- Invariante: un test superato non copre minacce non incluse nel protocollo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stesso prompt con perturbazione e controllo di policy; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Valutazione adattiva.
- Prova: SRC-88-004 e sezione pubblica corrispondente.

## Transizione 5. Valutazione adattiva

- Ultima affermazione stabile: una superficie di attacco e il comportamento sotto perturbazione.
- Concetto nuovo: Una difesa deve essere testata da attaccanti che conoscono il metodo, entro un protocollo sicuro e autorizzato.
- Input e shape: threat model, prompt, budget e risposta.
- Operazione: jailbreak, perturbazione, difesa e adaptive evaluation.
- Output e shape: success rate, failure mode e costo della difesa.
- Che cosa cambia: il passaggio specifico di «Valutazione adattiva».
- Invariante: un test superato non copre minacce non incluse nel protocollo.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: stesso prompt con perturbazione e controllo di policy; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Prompt injection e sicurezza dei tool.
- Prova: SRC-88-001 e sezione pubblica corrispondente.
