# Audit del testo. Capitolo 4

## Stato

- Versione candidata: `0.2.0-rc1`
- Data: 31 luglio 2026
- Protocollo: `docs/02_STILE_E_QA_TESTO.md`
- Fonti e riproducibilità: `docs/04_CODICE_FONTI_E_RIPRODUCIBILITA.md`
- Esito fattuale: **superato**
- Esito didattico: **superato**
- Esito editoriale e linguistico: **superato**
- Esito per lettore non esperto: **superato**
- Codice: **quattro test superati**
- Visuali: **validate tecnicamente**
- Review autoriale: aperta

## Review didattica

- [x] Il confronto tra A e B appare prima dei termini statistici.
- [x] La domanda sperimentale precede metrica e protocollo.
- [x] Baseline, media, slice, costo e variabilità vengono introdotti separatamente ma confluiscono nello stesso esempio.
- [x] Il bootstrap compare dopo che il lettore ha visto predizioni appaiate e differenza osservata.
- [x] Leakage, riuso adattivo del test set e contaminazione sono distinti.
- [x] Shortcut learning e ablation vengono spiegati come problemi di attribuzione, senza anticipare causal inference formale.
- [x] Il riepilogo torna alla differenza `0,833` contro `0,792` e ne restringe il significato.

## Review editoriale e linguistica

- [x] Il capitolo usa titoli semantici e sezioni abbastanza ampie.
- [x] La prosa non espone lo scaffold di audit.
- [x] Termini come baseline, slice, leakage, bootstrap e ablation sono spiegati nel punto d'uso.
- [x] Formule e codice aggiungono precisione dopo l'intuizione.
- [x] Le cautele non interrompono continuamente la spiegazione e sono collegate al claim limitato.
- [x] Le citazioni restano vicine alle affermazioni portanti.
- [x] La lettura ad alta voce non ha rilevato periodi opachi o calchi dominanti.

## Audit fattuale

- [x] NIST AI RMF è usato per collegare misurazione, contesto e rischio, non come protocollo sperimentale unico.
- [x] Bouthillier et al. sostengono la presenza di più fonti di variabilità nei benchmark.
- [x] Dror et al. sono usati per il principio che il test dipende da setup e misura.
- [x] Recht et al. sono descritti entro il perimetro di CIFAR-10 e ImageNet.
- [x] Northcutt et al. non vengono usati per attribuire percentuali universali di label errate.
- [x] Oren et al. sono descritti come metodo specifico con ipotesi dichiarate.
- [x] Model card e checklist non sono presentate come certificazioni.

## Audit matematico e del codice

- [x] Accuratezze, slice e costi sono coerenti con i 24 esempi.
- [x] Il confronto bootstrap conserva l'accoppiamento delle predizioni.
- [x] Seed `7` e `10.000` resample sono registrati.
- [x] La differenza osservata è `1/24`, arrotondata a `0,042`.
- [x] L'intervallo percentile registrato è `[-0,208, 0,292]`.
- [x] L'inclusione di zero non viene interpretata come equivalenza.
- [x] I pesi degli errori sono marcati come illustrativi.
- [x] Quattro test automatici risultano superati.

## Audit delle visuali

- [x] `EVAL-01` mostra il percorso dal problema al claim.
- [x] `EVAL-02` usa i valori esatti dello snippet.
- [x] Media, slice, costo e intervallo restano visivamente distinti.
- [x] Sfondo bianco, contenimento e collegamenti rispettano lo standard canonico.

## Difetti bloccanti rimasti

Nessuno noto nella candidatura interna. Rimane la revisione autoriale del perimetro, del livello statistico e delle due visuali.

## Esito

Il Capitolo 4 può passare alla revisione autoriale come candidatura `0.2.0-rc1`. Una modifica sostanziale a dati, formule, intervallo o visuali riapre l'audit completo.
