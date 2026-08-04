# Piano interno. Capitolo 26

- Domanda centrale: quale contratto costruisce Il testo come dato?
- Oggetto continuo: il testo prima e dopo la tokenizzazione; input guida: una stringa Unicode con byte e token speciali.
- Prerequisito stabile: Capitolo 25, Diffusione, score matching e flow matching.
- Gap: normalizzazione, segmentazione e packing.
- Output consegnato: ID, confini, mask e costo in token; consumer successivo: Capitolo 27, Embedding e spazio semantico.
- Invariante principale: stringa, encoding e tokenizer devono restare dichiarati.
- Visuali: DATA-01 e DATA-02, con famiglie compositive variabili.
- Snippet: code/snip_26_contract.py; output: code/outputs/SNIP-26-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Unicode e byte

- Ultima affermazione stabile: il testo prima e dopo la tokenizzazione.
- Concetto nuovo: Il testo è una sequenza di code point codificata in byte. Normalizzazione Unicode e decoding devono essere dichiarati.
- Input e shape: una stringa Unicode con byte e token speciali.
- Operazione: normalizzazione, segmentazione e packing.
- Output e shape: ID, confini, mask e costo in token.
- Che cosa cambia: il passaggio specifico di «Unicode e byte».
- Invariante: stringa, encoding e tokenizer devono restare dichiarati.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: la stessa parola con carattere accentato osservata a livello di byte; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Tokenizzazione.
- Prova: SRC-26-001 e sezione pubblica corrispondente.

## Transizione 2. Tokenizzazione

- Ultima affermazione stabile: il testo prima e dopo la tokenizzazione.
- Concetto nuovo: BPE, WordPiece e Unigram costruiscono vocabolari subword con algoritmi differenti. Il tokenizer fa parte dell'interfaccia del checkpoint.
- Input e shape: una stringa Unicode con byte e token speciali.
- Operazione: normalizzazione, segmentazione e packing.
- Output e shape: ID, confini, mask e costo in token.
- Che cosa cambia: il passaggio specifico di «Tokenizzazione».
- Invariante: stringa, encoding e tokenizer devono restare dichiarati.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: la stessa parola con carattere accentato osservata a livello di byte; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Token speciali.
- Prova: SRC-26-002 e sezione pubblica corrispondente.

## Transizione 3. Token speciali

- Ultima affermazione stabile: il testo prima e dopo la tokenizzazione.
- Concetto nuovo: BOS, EOS, padding, separatori e marker di ruolo hanno significati operativi. ID uguali richiedono la stessa convenzione.
- Input e shape: una stringa Unicode con byte e token speciali.
- Operazione: normalizzazione, segmentazione e packing.
- Output e shape: ID, confini, mask e costo in token.
- Che cosa cambia: il passaggio specifico di «Token speciali».
- Invariante: stringa, encoding e tokenizer devono restare dichiarati.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: la stessa parola con carattere accentato osservata a livello di byte; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Packing e confini.
- Prova: SRC-26-003 e sezione pubblica corrispondente.

## Transizione 4. Packing e confini

- Ultima affermazione stabile: il testo prima e dopo la tokenizzazione.
- Concetto nuovo: Più documenti possono condividere una sequenza. Attention mask e loss mask devono impedire dipendenze non desiderate.
- Input e shape: una stringa Unicode con byte e token speciali.
- Operazione: normalizzazione, segmentazione e packing.
- Output e shape: ID, confini, mask e costo in token.
- Che cosa cambia: il passaggio specifico di «Packing e confini».
- Invariante: stringa, encoding e tokenizer devono restare dichiarati.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: la stessa parola con carattere accentato osservata a livello di byte; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Lunghezza, lingua e costi.
- Prova: SRC-26-004 e sezione pubblica corrispondente.

## Transizione 5. Lunghezza, lingua e costi

- Ultima affermazione stabile: il testo prima e dopo la tokenizzazione.
- Concetto nuovo: Token per carattere variano tra lingue e formati. La lunghezza in token influenza contesto, costo e valutazione.
- Input e shape: una stringa Unicode con byte e token speciali.
- Operazione: normalizzazione, segmentazione e packing.
- Output e shape: ID, confini, mask e costo in token.
- Che cosa cambia: il passaggio specifico di «Lunghezza, lingua e costi».
- Invariante: stringa, encoding e tokenizer devono restare dichiarati.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: la stessa parola con carattere accentato osservata a livello di byte; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Embedding e spazio semantico.
- Prova: SRC-26-001 e sezione pubblica corrispondente.
