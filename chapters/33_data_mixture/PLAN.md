# Piano interno. Capitolo 33

- Domanda centrale: quale contratto costruisce Dataset mixture, curriculum e dati sintetici?
- Oggetto continuo: la miscela effettiva di sorgenti durante il training; input guida: pesi, temperatura, curriculum e conteggio dei token.
- Prerequisito stabile: Capitolo 32, Il ciclo di vita dei dati.
- Gap: campionamento, ripesatura e generazione controllata.
- Output consegnato: probabilità effettive e mix osservato; consumer successivo: Capitolo 34, Scaling law e progettazione del modello.
- Invariante principale: peso nominale e esposizione effettiva non sono la stessa misura.
- Visuali: MIX-01 e MIX-02, con famiglie compositive variabili.
- Snippet: code/snip_33_contract.py; output: code/outputs/SNIP-33-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Peso effettivo delle sorgenti

- Ultima affermazione stabile: la miscela effettiva di sorgenti durante il training.
- Concetto nuovo: Dimensione grezza, probabilità di campionamento e ripetizione determinano le esposizioni.
- Input e shape: pesi, temperatura, curriculum e conteggio dei token.
- Operazione: campionamento, ripesatura e generazione controllata.
- Output e shape: probabilità effettive e mix osservato.
- Che cosa cambia: il passaggio specifico di «Peso effettivo delle sorgenti».
- Invariante: peso nominale e esposizione effettiva non sono la stessa misura.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre sorgenti ripesate con temperatura e conteggio finale; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Temperature sampling.
- Prova: SRC-33-001 e sezione pubblica corrispondente.

## Transizione 2. Temperature sampling

- Ultima affermazione stabile: la miscela effettiva di sorgenti durante il training.
- Concetto nuovo: Un esponente sulle proporzioni aumenta o riduce il peso relativo dei domini piccoli.
- Input e shape: pesi, temperatura, curriculum e conteggio dei token.
- Operazione: campionamento, ripesatura e generazione controllata.
- Output e shape: probabilità effettive e mix osservato.
- Che cosa cambia: il passaggio specifico di «Temperature sampling».
- Invariante: peso nominale e esposizione effettiva non sono la stessa misura.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre sorgenti ripesate con temperatura e conteggio finale; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Mixture ottimizzata.
- Prova: SRC-33-002 e sezione pubblica corrispondente.

## Transizione 3. Mixture ottimizzata

- Ultima affermazione stabile: la miscela effettiva di sorgenti durante il training.
- Concetto nuovo: Pesi appresi con proxy model dipendono da domini, validation e budget.
- Input e shape: pesi, temperatura, curriculum e conteggio dei token.
- Operazione: campionamento, ripesatura e generazione controllata.
- Output e shape: probabilità effettive e mix osservato.
- Che cosa cambia: il passaggio specifico di «Mixture ottimizzata».
- Invariante: peso nominale e esposizione effettiva non sono la stessa misura.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre sorgenti ripesate con temperatura e conteggio finale; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Curriculum.
- Prova: SRC-33-003 e sezione pubblica corrispondente.

## Transizione 4. Curriculum

- Ultima affermazione stabile: la miscela effettiva di sorgenti durante il training.
- Concetto nuovo: Cambiare ordine e difficoltà nel tempo modifica la traiettoria di ottimizzazione.
- Input e shape: pesi, temperatura, curriculum e conteggio dei token.
- Operazione: campionamento, ripesatura e generazione controllata.
- Output e shape: probabilità effettive e mix osservato.
- Che cosa cambia: il passaggio specifico di «Curriculum».
- Invariante: peso nominale e esposizione effettiva non sono la stessa misura.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre sorgenti ripesate con temperatura e conteggio finale; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Dati sintetici.
- Prova: SRC-33-004 e sezione pubblica corrispondente.

## Transizione 5. Dati sintetici

- Ultima affermazione stabile: la miscela effettiva di sorgenti durante il training.
- Concetto nuovo: Modello generatore, prompt, filtri e provenienza devono essere registrati per evitare feedback non controllato.
- Input e shape: pesi, temperatura, curriculum e conteggio dei token.
- Operazione: campionamento, ripesatura e generazione controllata.
- Output e shape: probabilità effettive e mix osservato.
- Che cosa cambia: il passaggio specifico di «Dati sintetici».
- Invariante: peso nominale e esposizione effettiva non sono la stessa misura.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: tre sorgenti ripesate con temperatura e conteggio finale; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Scaling law e progettazione del modello.
- Prova: SRC-33-001 e sezione pubblica corrispondente.
