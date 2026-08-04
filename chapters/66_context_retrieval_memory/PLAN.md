# Piano interno. Capitolo 66

- Domanda centrale: quale contratto costruisce Contesto lungo, retrieval e memoria?
- Oggetto continuo: la decisione tra contesto, retrieval e memoria; input guida: segmento, query, budget e durata.
- Prerequisito stabile: Capitolo 65, RAG adattivo, correttivo e basato su grafi.
- Gap: routing, scrittura episodica e recupero.
- Output consegnato: contesto scelto, memoria aggiornata e costo; consumer successivo: Capitolo 67, Output strutturato e uso degli strumenti.
- Invariante principale: memoria persistente e contesto temporaneo hanno politiche diverse.
- Visuali: MEMORY-01 e MEMORY-02, con famiglie compositive variabili.
- Snippet: code/snip_66_contract.py; output: code/outputs/SNIP-66-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Tre risorse differenti

- Ultima affermazione stabile: la decisione tra contesto, retrieval e memoria.
- Concetto nuovo: Contesto lungo, retrieval esterno e memoria persistente offrono capacità, costo e aggiornabilità differenti.
- Input e shape: segmento, query, budget e durata.
- Operazione: routing, scrittura episodica e recupero.
- Output e shape: contesto scelto, memoria aggiornata e costo.
- Che cosa cambia: il passaggio specifico di «Tre risorse differenti».
- Invariante: memoria persistente e contesto temporaneo hanno politiche diverse.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un fatto stabile salvato e un dettaglio recente escluso; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Quando usare il contesto.
- Prova: SRC-66-001 e sezione pubblica corrispondente.

## Transizione 2. Quando usare il contesto

- Ultima affermazione stabile: la decisione tra contesto, retrieval e memoria.
- Concetto nuovo: Inserire tutti i documenti evita un indice separato ma aumenta prefill, distrattori e costo per richiesta.
- Input e shape: segmento, query, budget e durata.
- Operazione: routing, scrittura episodica e recupero.
- Output e shape: contesto scelto, memoria aggiornata e costo.
- Che cosa cambia: il passaggio specifico di «Quando usare il contesto».
- Invariante: memoria persistente e contesto temporaneo hanno politiche diverse.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un fatto stabile salvato e un dettaglio recente escluso; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Quando recuperare.
- Prova: SRC-66-002 e sezione pubblica corrispondente.

## Transizione 3. Quando recuperare

- Ultima affermazione stabile: la decisione tra contesto, retrieval e memoria.
- Concetto nuovo: Retrieval seleziona un sottoinsieme aggiornabile e attribuibile. Può fallire per query, indice o ranking.
- Input e shape: segmento, query, budget e durata.
- Operazione: routing, scrittura episodica e recupero.
- Output e shape: contesto scelto, memoria aggiornata e costo.
- Che cosa cambia: il passaggio specifico di «Quando recuperare».
- Invariante: memoria persistente e contesto temporaneo hanno politiche diverse.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un fatto stabile salvato e un dettaglio recente escluso; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Memoria episodica.
- Prova: SRC-66-003 e sezione pubblica corrispondente.

## Transizione 4. Memoria episodica

- Ultima affermazione stabile: la decisione tra contesto, retrieval e memoria.
- Concetto nuovo: Un sistema può salvare fatti o riassunti tra sessioni. Provenienza, consenso, scadenza e correzione diventano parte del contratto.
- Input e shape: segmento, query, budget e durata.
- Operazione: routing, scrittura episodica e recupero.
- Output e shape: contesto scelto, memoria aggiornata e costo.
- Che cosa cambia: il passaggio specifico di «Memoria episodica».
- Invariante: memoria persistente e contesto temporaneo hanno politiche diverse.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un fatto stabile salvato e un dettaglio recente escluso; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Routing ibrido.
- Prova: SRC-66-004 e sezione pubblica corrispondente.

## Transizione 5. Routing ibrido

- Ultima affermazione stabile: la decisione tra contesto, retrieval e memoria.
- Concetto nuovo: Una policy può scegliere cache, contesto, retrieval o memoria. La decisione deve essere misurata rispetto a qualità, latenza e privacy.
- Input e shape: segmento, query, budget e durata.
- Operazione: routing, scrittura episodica e recupero.
- Output e shape: contesto scelto, memoria aggiornata e costo.
- Che cosa cambia: il passaggio specifico di «Routing ibrido».
- Invariante: memoria persistente e contesto temporaneo hanno politiche diverse.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: un fatto stabile salvato e un dettaglio recente escluso; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Output strutturato e uso degli strumenti.
- Prova: SRC-66-001 e sezione pubblica corrispondente.
