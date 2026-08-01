# Audit del testo. Capitolo 5

## Stato

- Versione candidata: `0.2.0-rc1`
- Data: 31 luglio 2026
- Protocollo: `docs/02_STILE_E_QA_TESTO.md`
- Fonti e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`
- Esito fattuale e matematico: **superato**
- Esito didattico: **superato**
- Esito editoriale e linguistico: **superato**
- Esito per lettore non esperto: **superato**
- Codice: **quattro test superati**
- Visuali: **validate tecnicamente**
- Review autoriale: aperta

## Review didattica

- [x] Il capitolo parte da una richiesta rappresentata da quattro numeri.
- [x] Scalare, vettore, matrice e tensore vengono introdotti in ordine.
- [x] Shape e significato degli assi restano distinti.
- [x] Operazioni elemento per elemento, prodotto scalare e prodotto matriciale non vengono sovrapposti.
- [x] La contrazione dell'asse feature viene mostrata prima della formula generale.
- [x] Il bias e il broadcasting vengono spiegati sullo stesso batch.
- [x] Span, indipendenza e rango entrano dopo che la combinazione lineare è stabilizzata.
- [x] La SVD viene letta prima come decomposizione e poi come somma di componenti di rango uno.
- [x] Storage, stride e contiguità sono confinati alla sezione implementativa.

## Review editoriale e linguistica

- [x] Il testo usa sezioni semantiche e prosa continua.
- [x] I termini matematici ricevono una definizione nel punto d'uso.
- [x] Le formule sono precedute da una domanda o da un esempio.
- [x] Le cautele su semantica, rango numerico e SVD non interrompono il percorso principale.
- [x] Il codice conferma il meccanismo senza trasformare la lezione in una reference API.
- [x] La lettura ad alta voce non ha evidenziato calchi dominanti o periodi eccessivamente compressi.

## Audit matematico

- [x] `X`, `W`, `W^T`, bias, intermedio e output hanno shape coerenti.
- [x] I valori di `XW^T` e `XW^T+b` sono distinti correttamente.
- [x] La matrice di Gram coincide con i prodotti scalari tra righe.
- [x] La seconda riga della matrice A è il doppio della prima.
- [x] Il rango numerico è due nell'ambiente dichiarato.
- [x] I valori singolari corrispondono all'output eseguito.
- [x] La ricostruzione SVD è verificata entro `1e-12`.
- [x] Il testo distingue rango esatto, rango numerico e scelta della tolleranza.

## Audit delle API

- [x] `torch.matmul` è usato secondo la semantica documentata.
- [x] Il broadcasting del bias rispetta le regole delle dimensioni finali.
- [x] `torch.linalg.svd` è usato nella forma ridotta.
- [x] `matrix_rank` è descritto come stima numerica dipendente da tolleranza.
- [x] View, reshape e contiguità sono descritti entro i limiti della documentazione PyTorch.
- [x] La documentazione stable è distinta dalla versione 2.10.0 effettivamente eseguita.

## Audit delle visuali

- [x] `LA-01` usa l'intermedio prima del bias e l'output dopo il bias.
- [x] `LA-01` mostra l'asse feature come dimensione contratta.
- [x] `LA-02` usa i valori singolari eseguiti.
- [x] `LA-02` non presenta la soglia numerica come universale.
- [x] Sfondo, testo, collegamenti e contenimento rispettano lo standard canonico.
- [x] Le candidate errate prodotte dallo strumento immagini sono state respinte e non pubblicate.

## Difetti bloccanti rimasti

Nessuno noto nella candidatura interna. Rimane la revisione autoriale di testo, livello matematico e visuali.

## Esito

Il Capitolo 5 può passare alla revisione autoriale come candidatura `0.2.0-rc1`. Modifiche successive a matrici, shape, valori singolari o layout riaprono audit matematico e incrociato.
