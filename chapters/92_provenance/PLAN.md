# Piano editoriale. Capitolo 92

## Obiettivo didattico

Seguire **Watermarking e provenienza dei contenuti** da payload, metadata, manifest e chiave o watermark a record verificabile e stato di rilevazione, osservando digest, firma, C2PA, watermark e detection senza oltrepassare questo limite: provenienza dell'artefatto non certifica la verità del contenuto.

## Prerequisiti reali

- Capitolo 68: Protocolli e interoperabilità
- Capitolo 90: Poisoning, backdoor, extraction e supply chain

## Percorso della lezione

1. **Provenienza crittografica.** Firma e manifest collegano un contenuto a un attore o a una catena di modifiche, se le chiavi e il workflow sono affidabili. Prova: SRC-92-001.
2. **C2PA.** Credenziali di contenuto registrano asserzioni e ingredienti. Assenza di credenziali non prova che un contenuto sia sintetico. Prova: SRC-92-002.
3. **Watermarking.** Un generatore può modulare token o segnali per consentire rilevamento statistico. Robustezza e falsi positivi dipendono dal canale. Prova: SRC-92-003.
4. **Detection.** Classificatori di contenuto sintetico degradano sotto editing, nuovi modelli e shift. Un punteggio non è una prova forense isolata. Prova: SRC-92-003.
5. **Policy e interfaccia.** Provenienza, disclosure e conservazione dei metadati devono essere progettate lungo la pipeline di pubblicazione. Prova: SRC-92-004.

## Prove e artefatti

- riferimento minimo: `code/snip_92_contract.py`; test: `code/test_92_contract.py`; output: `code/outputs/SNIP-92-001.txt`.
- visuali candidate: PROVENANCE-01, PROVENANCE-02; le domande pedagogiche sono distinte e l'approvazione autoriale resta aperta.
- fonti: `FONTI_PRIMARIE.md`; corrispondenza claim-fonte: `CLAIMS.md`.

## Gate aperti

- lettura editoriale finale da parte dell'autore;
- approvazione delle visuali nel contesto impaginato;
- benchmark esterni solo quando il capitolo formula un claim di scala o di produzione.
