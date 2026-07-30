# Guida alla revisione del capitolo pilota

## Versione da revisionare

- Capitolo: `CH-P06-ATTENTION`
- Versione: `0.3.0-rc3`
- Review didattiche interne:
  - `DID-ATT-01`: respinta e corretta;
  - `DID-ATT-02`: superata per sequenza e gate;
  - `DID-ATT-03`: respinta dal gate anti-template;
  - `DID-ATT-04`: superata dopo la riscrittura in prosa.
- Review autoriale: aperta

## Percorso consigliato

1. `CHAPTER.md`, per tono, fluidità, progressione e confini;
2. `TEXT_AUDIT.md`, per seguire gli errori individuati nelle quattro review;
3. `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`, per la nuova regola sulla superficie editoriale;
4. `assets/.../ATT-01/candidate-v2.png`, per il confronto tra combinazione fissa e coefficienti dipendenti dalla posizione;
5. `assets/.../ATT-02/candidate-v2.png`, per il calcolo numerico;
6. `code/`, per i tre snippet eseguibili e i test;
7. `CLAIMS.md` e `FONTI_PRIMARIE.md`, per la tracciabilità;
8. `docs/18_PROTOCOLLO_QA_DIDATTICO.md`, per il gate da applicare ai capitoli successivi.

## Modifiche principali della versione `0.3.0-rc3`

- lo scaffold didattico resta verificabile, ma non viene più pubblicato come serie di intestazioni ripetute;
- titoli come `Cosa è cambiato`, `Cosa è rimasto invariato` e `Frase di continuità` sono stati assorbiti nella prosa;
- i titoli ora descrivono problemi e meccanismi reali;
- shape, invarianti e confini restano espliciti nel punto in cui servono;
- le introduzioni agli snippet sono scritte in prosa, senza box `Contratto dello snippet`;
- le visuali sono ancora inquadrate, ispezionate e concluse, ma senza etichette editoriali rigide;
- la sequenza tecnica verificata della versione precedente è rimasta invariata.

## Aspetti da valutare con particolare attenzione

- La lezione appare come prosa tecnica naturale oppure conserva ancora un ritmo troppo meccanico?
- Le transizioni sono chiare anche senza le intestazioni metacognitive?
- Invarianti e confini restano sufficientemente visibili?
- I titoli semantici aiutano a orientarsi senza rendere tutte le lezioni formalmente identiche?
- Il livello di dettaglio è adatto al capitolo base?

## Stato tecnico delle visuali

- `ATT-01`: validata tecnicamente, approvazione autoriale aperta;
- `ATT-02`: validata tecnicamente, approvazione autoriale aperta.

## Decisioni richieste all'autore

- [ ] Approvo il tono generale.
- [ ] Approvo la progressione didattica.
- [ ] Approvo la struttura in prosa senza intestazioni metacognitive ripetute.
- [ ] Approvo la profondità matematica.
- [ ] Approvo il formato dei tre snippet.
- [ ] Approvo `ATT-01`.
- [ ] Approvo `ATT-02`.
- [ ] Approvo il protocollo didattico iterativo e il gate anti-template per tutti i capitoli.
- [ ] Autorizzo l'uso di questo standard per la produzione seriale.

## Nota

Il pacchetto contiene soltanto Markdown, immagini tecniche, codice, output e audit. Non contiene pagine renderizzate o mockup editoriali.