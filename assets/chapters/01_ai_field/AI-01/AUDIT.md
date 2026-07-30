# Audit visuale `AI-01`

## Stato

- Esito: **da rigenerare**
- Approvazione tecnica: no
- Approvazione autoriale: no
- File candidato nel repository: nessuno
- Data: 30 luglio 2026

## Iterazioni respinte

| Tentativo | Output prodotto | Difetto bloccante | Decisione |
|---|---|---|---|
| 1 | schermata GitHub di una pull request | contenuto completamente diverso dalla tassonomia richiesta | respinta |
| 2 | schermata repository dopo un merge | contenuto completamente diverso | respinta |
| 3 | pagina GitHub con elenco di pull request | contenuto completamente diverso | respinta |
| 4 | dashboard `libro completato` | affermazioni false sullo stato del progetto e nessuno dei tre assi | respinta |
| 5 | dashboard sull'indice del libro | oggetto sbagliato, numerazione inventata, nessuna tassonomia | respinta |
| 6 | schermata GitHub scura | oggetto sbagliato e violazione dello sfondo canonico | respinta |

## Controlli tecnici

Non applicabili alle candidate, perché nessuna rappresentava l'oggetto specificato. Una immagine esteticamente pulita non può superare l'audit quando risponde a una domanda diversa.

## Problema osservato

Lo strumento immagini ha privilegiato il contesto recente relativo a repository, merge e produzione del libro, ignorando la specifica locale della figura. Nessuna candidata è stata caricata come asset del capitolo.

## Condizione per la nuova iterazione

La prossima generazione deve essere avviata in un contesto in cui la richiesta visuale `AI-01` sia il referente dominante e deve essere verificata contro `SPEC.md` prima di qualsiasi pubblicazione.

## Gate di approvazione

La visuale potrà essere validata soltanto quando:

- contiene il box centrale con la richiesta;
- contiene esattamente i tre assi dichiarati;
- non presenta gerarchie false tra gli assi;
- usa sfondo bianco puro;
- tutte le label sono integralmente contenute;
- nessuna freccia è ambigua;
- non contiene elementi relativi al repository o allo stato del progetto;
- coincide con la prosa e con la tassonomia del capitolo.
