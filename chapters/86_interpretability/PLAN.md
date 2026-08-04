# Piano interno. Capitolo 86

- Domanda centrale: quale contratto costruisce Interpretabilità delle rappresentazioni e dei circuiti?
- Oggetto continuo: un comportamento del modello e l'intervento che lo modifica; input guida: attivazioni, probe, attribution e baseline.
- Prerequisito stabile: Capitolo 85, Valutare contesto lungo, RAG, multimodalità e agenti.
- Gap: probing, attribution, causal intervention e circuit tracing.
- Output consegnato: effetto osservato con controllo e confondenti; consumer successivo: Capitolo 87, Sparse autoencoder e interpretabilità scalabile.
- Invariante principale: correlazione di una feature non prova causalità.
- Visuali: INTERPRETA-01 e INTERPRETA-02, con famiglie compositive variabili.
- Snippet: code/snip_86_contract.py; output: code/outputs/SNIP-86-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Oggetto dell'interpretazione

- Ultima affermazione stabile: un comportamento del modello e l'intervento che lo modifica.
- Concetto nuovo: Pesi, attivazioni, feature, head e comportamento sono livelli differenti. Il metodo deve dichiarare quale livello analizza.
- Input e shape: attivazioni, probe, attribution e baseline.
- Operazione: probing, attribution, causal intervention e circuit tracing.
- Output e shape: effetto osservato con controllo e confondenti.
- Che cosa cambia: il passaggio specifico di «Oggetto dell'interpretazione».
- Invariante: correlazione di una feature non prova causalità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: ablazione di una componente e differenza rispetto alla baseline; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Probing.
- Prova: SRC-86-001 e sezione pubblica corrispondente.

## Transizione 2. Probing

- Ultima affermazione stabile: un comportamento del modello e l'intervento che lo modifica.
- Concetto nuovo: Un probe misura informazione decodificabile da una rappresentazione. Non prova che il modello usi quella informazione causalmente.
- Input e shape: attivazioni, probe, attribution e baseline.
- Operazione: probing, attribution, causal intervention e circuit tracing.
- Output e shape: effetto osservato con controllo e confondenti.
- Che cosa cambia: il passaggio specifico di «Probing».
- Invariante: correlazione di una feature non prova causalità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: ablazione di una componente e differenza rispetto alla baseline; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Attribution.
- Prova: SRC-86-002 e sezione pubblica corrispondente.

## Transizione 3. Attribution

- Ultima affermazione stabile: un comportamento del modello e l'intervento che lo modifica.
- Concetto nuovo: Gradienti, integrated gradients e perturbazioni assegnano importanza secondo definizioni differenti e possono essere instabili.
- Input e shape: attivazioni, probe, attribution e baseline.
- Operazione: probing, attribution, causal intervention e circuit tracing.
- Output e shape: effetto osservato con controllo e confondenti.
- Che cosa cambia: il passaggio specifico di «Attribution».
- Invariante: correlazione di una feature non prova causalità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: ablazione di una componente e differenza rispetto alla baseline; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Causal intervention.
- Prova: SRC-86-003 e sezione pubblica corrispondente.

## Transizione 4. Causal intervention

- Ultima affermazione stabile: un comportamento del modello e l'intervento che lo modifica.
- Concetto nuovo: Ablation, activation patching e path patching modificano componenti e misurano effetti sul comportamento.
- Input e shape: attivazioni, probe, attribution e baseline.
- Operazione: probing, attribution, causal intervention e circuit tracing.
- Output e shape: effetto osservato con controllo e confondenti.
- Che cosa cambia: il passaggio specifico di «Causal intervention».
- Invariante: correlazione di una feature non prova causalità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: ablazione di una componente e differenza rispetto alla baseline; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Circuiti.
- Prova: SRC-86-004 e sezione pubblica corrispondente.

## Transizione 5. Circuiti

- Ultima affermazione stabile: un comportamento del modello e l'intervento che lo modifica.
- Concetto nuovo: Un circuito è un insieme di componenti e connessioni sufficienti per un comportamento nel setup studiato. Sufficienza e necessità richiedono test separati.
- Input e shape: attivazioni, probe, attribution e baseline.
- Operazione: probing, attribution, causal intervention e circuit tracing.
- Output e shape: effetto osservato con controllo e confondenti.
- Che cosa cambia: il passaggio specifico di «Circuiti».
- Invariante: correlazione di una feature non prova causalità.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: ablazione di una componente e differenza rispetto alla baseline; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sparse autoencoder e interpretabilità scalabile.
- Prova: SRC-86-001 e sezione pubblica corrispondente.
