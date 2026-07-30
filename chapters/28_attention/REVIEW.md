# Guida alla revisione del capitolo pilota

## Versione da revisionare

- Capitolo: `CH-P06-ATTENTION`
- Versione: `0.2.0-rc2`
- Review didattiche interne: `DID-ATT-01` respinta e corretta; `DID-ATT-02` superata
- Review autoriale: aperta

## Percorso consigliato

1. `CHAPTER.md`, per tono, progressione e confini;
2. `TEXT_AUDIT.md`, per vedere gli errori della prima versione e le due review complete;
3. `assets/.../ATT-01/candidate-v2.png`, per il confronto tra combinazione fissa e coefficienti dipendenti dalla posizione;
4. `assets/.../ATT-02/candidate-v2.png`, per il calcolo numerico;
5. `code/`, per i tre snippet eseguibili e i test;
6. `CLAIMS.md` e `FONTI_PRIMARIE.md`, per la tracciabilità;
7. `docs/18_PROTOCOLLO_QA_DIDATTICO.md`, per il gate da applicare ai capitoli successivi.

## Modifiche didattiche principali

- ruoli descritti prima dei nomi query, key e value;
- termine scaled dot-product attention introdotto dopo l'esempio completo;
- pseudocodice prima della formula generale;
- stato accumulato esplicito;
- visuali attraversate dalla prosa;
- mask matematica separata dalla semantica API;
- multi-head spostata al capitolo successivo, salvo il ponte finale;
- implementazioni hardware-aware ridotte a confine.

## Stato tecnico delle visuali

- `ATT-01`: validata tecnicamente, approvazione autoriale aperta;
- `ATT-02`: validata tecnicamente, approvazione autoriale aperta.

## Decisioni richieste all'autore

- [ ] Approvo il tono generale.
- [ ] Approvo la progressione didattica.
- [ ] Approvo la profondità matematica.
- [ ] Approvo il formato dei tre snippet.
- [ ] Approvo `ATT-01`.
- [ ] Approvo `ATT-02`.
- [ ] Approvo il protocollo didattico iterativo per tutti i capitoli.
- [ ] Autorizzo l'uso di questo standard per la produzione seriale.

## Nota

Il pacchetto contiene soltanto Markdown, immagini tecniche, codice, output e audit. Non contiene pagine renderizzate o mockup editoriali.
