# Piano interno. Capitolo 27

- Domanda centrale: quale contratto costruisce Embedding e spazio semantico?
- Oggetto continuo: un ID e il vettore che lo rappresenta; input guida: due ID, due vettori e una query.
- Prerequisito stabile: Capitolo 26, Il testo come dato.
- Gap: lookup, pooling, similarità e normalizzazione.
- Output consegnato: embedding, ranking o predizione; consumer successivo: Capitolo 28, Embedding e spazio semantico.
- Invariante principale: la similarità dipende da training, metrica e normalizzazione.
- Visuali: EMBEDDIN-01 e EMBEDDIN-02, con famiglie compositive variabili.
- Snippet: code/snip_27_contract.py; output: code/outputs/SNIP-27-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Da ID a vettore

- Ultima affermazione stabile: un ID e il vettore che lo rappresenta.
- Concetto nuovo: Una embedding table seleziona una riga per token. La dimensione del vettore è una scelta architetturale.
- Input e shape: due ID, due vettori e una query.
- Operazione: lookup, pooling, similarità e normalizzazione.
- Output e shape: embedding, ranking o predizione.
- Che cosa cambia: il passaggio specifico di «Da ID a vettore».
- Invariante: la similarità dipende da training, metrica e normalizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: similarità coseno tra due vettori dopo la normalizzazione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Word embedding.
- Prova: SRC-27-001 e sezione pubblica corrispondente.

## Transizione 2. Word embedding

- Ultima affermazione stabile: un ID e il vettore che lo rappresenta.
- Concetto nuovo: Word2vec e GloVe usano statistiche distributive con obiettivi differenti. Similarità geometrica riflette dati e obiettivo.
- Input e shape: due ID, due vettori e una query.
- Operazione: lookup, pooling, similarità e normalizzazione.
- Output e shape: embedding, ranking o predizione.
- Che cosa cambia: il passaggio specifico di «Word embedding».
- Invariante: la similarità dipende da training, metrica e normalizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: similarità coseno tra due vettori dopo la normalizzazione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Embedding contestuale.
- Prova: SRC-27-002 e sezione pubblica corrispondente.

## Transizione 3. Embedding contestuale

- Ultima affermazione stabile: un ID e il vettore che lo rappresenta.
- Concetto nuovo: In un Transformer, la rappresentazione di un token cambia con il contesto. La stessa stringa può produrre vettori diversi.
- Input e shape: due ID, due vettori e una query.
- Operazione: lookup, pooling, similarità e normalizzazione.
- Output e shape: embedding, ranking o predizione.
- Che cosa cambia: il passaggio specifico di «Embedding contestuale».
- Invariante: la similarità dipende da training, metrica e normalizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: similarità coseno tra due vettori dopo la normalizzazione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Sentence embedding.
- Prova: SRC-27-003 e sezione pubblica corrispondente.

## Transizione 4. Sentence embedding

- Ultima affermazione stabile: un ID e il vettore che lo rappresenta.
- Concetto nuovo: Pooling o training contrastivo producono vettori per frasi e documenti. La metrica deve corrispondere all'uso previsto.
- Input e shape: due ID, due vettori e una query.
- Operazione: lookup, pooling, similarità e normalizzazione.
- Output e shape: embedding, ranking o predizione.
- Che cosa cambia: il passaggio specifico di «Sentence embedding».
- Invariante: la similarità dipende da training, metrica e normalizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: similarità coseno tra due vettori dopo la normalizzazione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Ricerca e anisotropia.
- Prova: SRC-27-004 e sezione pubblica corrispondente.

## Transizione 5. Ricerca e anisotropia

- Ultima affermazione stabile: un ID e il vettore che lo rappresenta.
- Concetto nuovo: Cosine similarity è una convenzione, non una misura universale di significato. Normalizzazione e distribuzione dello spazio influenzano il ranking.
- Input e shape: due ID, due vettori e una query.
- Operazione: lookup, pooling, similarità e normalizzazione.
- Output e shape: embedding, ranking o predizione.
- Che cosa cambia: il passaggio specifico di «Ricerca e anisotropia».
- Invariante: la similarità dipende da training, metrica e normalizzazione.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: similarità coseno tra due vettori dopo la normalizzazione; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Embedding e spazio semantico.
- Prova: SRC-27-001 e sezione pubblica corrispondente.
