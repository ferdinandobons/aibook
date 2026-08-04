# Piano interno. Capitolo 58

- Domanda centrale: quale contratto costruisce Modelli multimodali nativi e any-to-any?
- Oggetto continuo: token interleaved e output di più modalità; input guida: sequenza testo-immagine-audio con mask.
- Prerequisito stabile: Capitolo 57, Generazione e modifica delle immagini.
- Gap: backbone condiviso, routing e sincronizzazione.
- Output consegnato: token o artefatto nella modalità richiesta; consumer successivo: Capitolo 59, Audio, parlato e musica.
- Invariante principale: ordine, durata e maschera della modalità devono essere espliciti.
- Visuali: MULTIMODAL-01 e MULTIMODAL-02, con famiglie compositive variabili.
- Snippet: code/snip_58_contract.py; output: code/outputs/SNIP-58-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Token interleaved

- Ultima affermazione stabile: token interleaved e output di più modalità.
- Concetto nuovo: Sequenze possono alternare testo, immagini, audio e marker. Il tokenizer multimodale definisce unità e ordine.
- Input e shape: sequenza testo-immagine-audio con mask.
- Operazione: backbone condiviso, routing e sincronizzazione.
- Output e shape: token o artefatto nella modalità richiesta.
- Che cosa cambia: il passaggio specifico di «Token interleaved».
- Invariante: ordine, durata e maschera della modalità devono essere espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: testo e immagine alternati con due posizioni riservate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Backbone condiviso.
- Prova: SRC-58-001 e sezione pubblica corrispondente.

## Transizione 2. Backbone condiviso

- Ultima affermazione stabile: token interleaved e output di più modalità.
- Concetto nuovo: Un Transformer può elaborare embedding di modalità differenti con parametri condivisi e adapter specifici.
- Input e shape: sequenza testo-immagine-audio con mask.
- Operazione: backbone condiviso, routing e sincronizzazione.
- Output e shape: token o artefatto nella modalità richiesta.
- Che cosa cambia: il passaggio specifico di «Backbone condiviso».
- Invariante: ordine, durata e maschera della modalità devono essere espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: testo e immagine alternati con due posizioni riservate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Output multimodale.
- Prova: SRC-58-002 e sezione pubblica corrispondente.

## Transizione 3. Output multimodale

- Ultima affermazione stabile: token interleaved e output di più modalità.
- Concetto nuovo: La generazione di testo e media richiede head o decoder differenti, anche quando il backbone è comune.
- Input e shape: sequenza testo-immagine-audio con mask.
- Operazione: backbone condiviso, routing e sincronizzazione.
- Output e shape: token o artefatto nella modalità richiesta.
- Che cosa cambia: il passaggio specifico di «Output multimodale».
- Invariante: ordine, durata e maschera della modalità devono essere espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: testo e immagine alternati con due posizioni riservate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Any-to-any.
- Prova: SRC-58-003 e sezione pubblica corrispondente.

## Transizione 4. Any-to-any

- Ultima affermazione stabile: token interleaved e output di più modalità.
- Concetto nuovo: Un'interfaccia generale deve dichiarare quali combinazioni di input e output sono state realmente addestrate e valutate.
- Input e shape: sequenza testo-immagine-audio con mask.
- Operazione: backbone condiviso, routing e sincronizzazione.
- Output e shape: token o artefatto nella modalità richiesta.
- Che cosa cambia: il passaggio specifico di «Any-to-any».
- Invariante: ordine, durata e maschera della modalità devono essere espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: testo e immagine alternati con due posizioni riservate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sincronizzazione.
- Prova: SRC-58-004 e sezione pubblica corrispondente.

## Transizione 5. Sincronizzazione

- Ultima affermazione stabile: token interleaved e output di più modalità.
- Concetto nuovo: Audio, video e testo possiedono frequenze differenti. Allineamento temporale e turn-taking diventano parte dell'architettura.
- Input e shape: sequenza testo-immagine-audio con mask.
- Operazione: backbone condiviso, routing e sincronizzazione.
- Output e shape: token o artefatto nella modalità richiesta.
- Che cosa cambia: il passaggio specifico di «Sincronizzazione».
- Invariante: ordine, durata e maschera della modalità devono essere espliciti.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: testo e immagine alternati con due posizioni riservate; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Audio, parlato e musica.
- Prova: SRC-58-001 e sezione pubblica corrispondente.
