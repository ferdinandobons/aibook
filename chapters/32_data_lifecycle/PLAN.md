# Piano interno. Capitolo 32

- Domanda centrale: quale contratto costruisce Il ciclo di vita dei dati?
- Oggetto continuo: un record di dataset dalla sorgente al manifest; input guida: testo grezzo, metadati, split e digest.
- Prerequisito stabile: Capitolo 31, Dalla rappresentazione linguistica agli LLM.
- Gap: parsing, filtro, deduplicazione e tokenizzazione.
- Output consegnato: record ammesso, conteggi e manifest; consumer successivo: Capitolo 33, Dataset mixture, curriculum e dati sintetici.
- Invariante principale: ogni trasformazione deve restare ricostruibile e ordinata.
- Visuali: DATA-01 e DATA-02, con famiglie compositive variabili.
- Snippet: code/snip_32_contract.py; output: code/outputs/SNIP-32-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Sorgenti e provenienza

- Ultima affermazione stabile: un record di dataset dalla sorgente al manifest.
- Concetto nuovo: Record, documenti, timestamp e licenze devono restare tracciabili dalla raccolta allo shard.
- Input e shape: testo grezzo, metadati, split e digest.
- Operazione: parsing, filtro, deduplicazione e tokenizzazione.
- Output e shape: record ammesso, conteggi e manifest.
- Che cosa cambia: il passaggio specifico di «Sorgenti e provenienza».
- Invariante: ogni trasformazione deve restare ricostruibile e ordinata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due record, uno duplicato, con digest prima e dopo il filtro; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Parsing e normalizzazione.
- Prova: SRC-32-001 e sezione pubblica corrispondente.

## Transizione 2. Parsing e normalizzazione

- Ultima affermazione stabile: un record di dataset dalla sorgente al manifest.
- Concetto nuovo: Trasformazioni di HTML, PDF, codice e conversazioni possono perdere informazione e devono essere versionate.
- Input e shape: testo grezzo, metadati, split e digest.
- Operazione: parsing, filtro, deduplicazione e tokenizzazione.
- Output e shape: record ammesso, conteggi e manifest.
- Che cosa cambia: il passaggio specifico di «Parsing e normalizzazione».
- Invariante: ogni trasformazione deve restare ricostruibile e ordinata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due record, uno duplicato, con digest prima e dopo il filtro; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Filtri.
- Prova: SRC-32-002 e sezione pubblica corrispondente.

## Transizione 3. Filtri

- Ultima affermazione stabile: un record di dataset dalla sorgente al manifest.
- Concetto nuovo: Filtri di qualità, lingua, sicurezza e PII modificano la distribuzione e richiedono statistiche prima e dopo.
- Input e shape: testo grezzo, metadati, split e digest.
- Operazione: parsing, filtro, deduplicazione e tokenizzazione.
- Output e shape: record ammesso, conteggi e manifest.
- Che cosa cambia: il passaggio specifico di «Filtri».
- Invariante: ogni trasformazione deve restare ricostruibile e ordinata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due record, uno duplicato, con digest prima e dopo il filtro; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Deduplicazione e contaminazione.
- Prova: SRC-32-003 e sezione pubblica corrispondente.

## Transizione 4. Deduplicazione e contaminazione

- Ultima affermazione stabile: un record di dataset dalla sorgente al manifest.
- Concetto nuovo: Hash esatti e similarità approssimata rilevano forme differenti di duplicazione. I benchmark richiedono controlli separati.
- Input e shape: testo grezzo, metadati, split e digest.
- Operazione: parsing, filtro, deduplicazione e tokenizzazione.
- Output e shape: record ammesso, conteggi e manifest.
- Che cosa cambia: il passaggio specifico di «Deduplicazione e contaminazione».
- Invariante: ogni trasformazione deve restare ricostruibile e ordinata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due record, uno duplicato, con digest prima e dopo il filtro; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Split, tokenizzazione e manifest.
- Prova: SRC-32-004 e sezione pubblica corrispondente.

## Transizione 5. Split, tokenizzazione e manifest

- Ultima affermazione stabile: un record di dataset dalla sorgente al manifest.
- Concetto nuovo: Confini temporali, tokenizer, packing, checksum e conteggi definiscono l'artefatto usato dal training.
- Input e shape: testo grezzo, metadati, split e digest.
- Operazione: parsing, filtro, deduplicazione e tokenizzazione.
- Output e shape: record ammesso, conteggi e manifest.
- Che cosa cambia: il passaggio specifico di «Split, tokenizzazione e manifest».
- Invariante: ogni trasformazione deve restare ricostruibile e ordinata.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: due record, uno duplicato, con digest prima e dopo il filtro; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Dataset mixture, curriculum e dati sintetici.
- Prova: SRC-32-001 e sezione pubblica corrispondente.
