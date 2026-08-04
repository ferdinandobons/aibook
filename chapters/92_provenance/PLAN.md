# Piano interno. Capitolo 92

- Domanda centrale: quale contratto costruisce Watermarking e provenienza dei contenuti?
- Oggetto continuo: un contenuto e la sua attestazione di provenienza; input guida: payload, metadata, manifest e chiave o watermark.
- Prerequisito stabile: Capitolo 91, Privacy, fairness e unlearning.
- Gap: digest, firma, C2PA, watermark e detection.
- Output consegnato: record verificabile e stato di rilevazione; consumer successivo: Capitolo 93, Diritto, governance e sostenibilità.
- Invariante principale: provenienza dell'artefatto non certifica la verità del contenuto.
- Visuali: PROVENANCE-01 e PROVENANCE-02, con famiglie compositive variabili.
- Snippet: code/snip_92_contract.py; output: code/outputs/SNIP-92-001.txt.
- Gate aperti: revisione autoriale, lettura ad alta voce e approvazione finale delle visuali.

## Transizione 1. Provenienza crittografica

- Ultima affermazione stabile: un contenuto e la sua attestazione di provenienza.
- Concetto nuovo: Firma e manifest collegano un contenuto a un attore o a una catena di modifiche, se le chiavi e il workflow sono affidabili.
- Input e shape: payload, metadata, manifest e chiave o watermark.
- Operazione: digest, firma, C2PA, watermark e detection.
- Output e shape: record verificabile e stato di rilevazione.
- Che cosa cambia: il passaggio specifico di «Provenienza crittografica».
- Invariante: provenienza dell'artefatto non certifica la verità del contenuto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: digest di payload e metadati con verifica di una modifica; provare anche una condizione incoerente e osservare il controllo.
- Consumer: C2PA.
- Prova: SRC-92-001 e sezione pubblica corrispondente.

## Transizione 2. C2PA

- Ultima affermazione stabile: un contenuto e la sua attestazione di provenienza.
- Concetto nuovo: Credenziali di contenuto registrano asserzioni e ingredienti. Assenza di credenziali non prova che un contenuto sia sintetico.
- Input e shape: payload, metadata, manifest e chiave o watermark.
- Operazione: digest, firma, C2PA, watermark e detection.
- Output e shape: record verificabile e stato di rilevazione.
- Che cosa cambia: il passaggio specifico di «C2PA».
- Invariante: provenienza dell'artefatto non certifica la verità del contenuto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: digest di payload e metadati con verifica di una modifica; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Watermarking.
- Prova: SRC-92-002 e sezione pubblica corrispondente.

## Transizione 3. Watermarking

- Ultima affermazione stabile: un contenuto e la sua attestazione di provenienza.
- Concetto nuovo: Un generatore può modulare token o segnali per consentire rilevamento statistico. Robustezza e falsi positivi dipendono dal canale.
- Input e shape: payload, metadata, manifest e chiave o watermark.
- Operazione: digest, firma, C2PA, watermark e detection.
- Output e shape: record verificabile e stato di rilevazione.
- Che cosa cambia: il passaggio specifico di «Watermarking».
- Invariante: provenienza dell'artefatto non certifica la verità del contenuto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: digest di payload e metadati con verifica di una modifica; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Detection.
- Prova: SRC-92-003 e sezione pubblica corrispondente.

## Transizione 4. Detection

- Ultima affermazione stabile: un contenuto e la sua attestazione di provenienza.
- Concetto nuovo: Classificatori di contenuto sintetico degradano sotto editing, nuovi modelli e shift. Un punteggio non è una prova forense isolata.
- Input e shape: payload, metadata, manifest e chiave o watermark.
- Operazione: digest, firma, C2PA, watermark e detection.
- Output e shape: record verificabile e stato di rilevazione.
- Che cosa cambia: il passaggio specifico di «Detection».
- Invariante: provenienza dell'artefatto non certifica la verità del contenuto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: digest di payload e metadati con verifica di una modifica; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Policy e interfaccia.
- Prova: SRC-92-003 e sezione pubblica corrispondente.

## Transizione 5. Policy e interfaccia

- Ultima affermazione stabile: un contenuto e la sua attestazione di provenienza.
- Concetto nuovo: Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pipeline di pubblicazione.
- Input e shape: payload, metadata, manifest e chiave o watermark.
- Operazione: digest, firma, C2PA, watermark e detection.
- Output e shape: record verificabile e stato di rilevazione.
- Che cosa cambia: il passaggio specifico di «Policy e interfaccia».
- Invariante: provenienza dell'artefatto non certifica la verità del contenuto.
- Che cosa non fa: non dimostra da solo qualità generale, causalità o readiness di produzione.
- Esempio o errore: digest di payload e metadati con verifica di una modifica; provare anche una condizione incoerente e osservare il controllo.
- Consumer: Diritto, governance e sostenibilità.
- Prova: SRC-92-004 e sezione pubblica corrispondente.
