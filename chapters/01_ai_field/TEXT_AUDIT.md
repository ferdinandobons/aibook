# Audit del testo e della conformità didattica. Capitolo 1

## Stato

- Versione corrente: `0.1.1-draft2`
- Data: 30 luglio 2026
- Protocolli: `docs/04_PROTOCOLLO_QA_TESTO.md`, `docs/18_PROTOCOLLO_QA_DIDATTICO.md`, `docs/19_STRUTTURA_LOGICA_IN_PROSA.md`
- Esito fattuale e matematico del testo: **superato per la bozza**
- Esito didattico del testo: **superato dopo due letture**
- Esito visuale: **bloccato**
- Review autoriale: non aperta

# Review `DID-AI-01`. Struttura, terminologia e forza delle affermazioni

- Versione esaminata: `0.1.0-draft1`
- Ambito: intero capitolo, fonti, claim e snippet
- Esito: **respinta, correzioni richieste**

## Difetti bloccanti trovati

1. L'apertura affermava che tutti gli esempi presentati potevano essere descritti come AI system, includendo una semplice ricerca di parole senza dichiarare il confine definitorio.
2. La descrizione generale dell'AI era formulata in modo troppo ampio e non distingueva abbastanza l'ancora OECD dalla tassonomia editoriale del libro.
3. La distinzione generativo/discriminativo usava soltanto `p(y|x)`, `p(x,y)` e `p(x)` e non dichiarava il caso dei modelli generativi condizionati `p(x|c)`.
4. La distinzione tra modello e sistema era corretta come scelta editoriale, ma doveva essere marcata più chiaramente come convenzione locale.
5. `Generalista` e `specialistico` richiedevano un richiamo più esplicito alla natura relativa delle etichette.
6. L'esempio code-driven doveva ribadire che la diminuzione della loss su quattro esempi non dimostra generalizzazione.
7. La visuale `AI-01` non poteva usare un diagramma di Venn gerarchico, perché meccanismo, obiettivo e ampiezza sono assi differenti.
8. Le candidate generate dallo strumento immagini rappresentavano repository, pull request o riepiloghi del progetto e non potevano essere incluse.

## Correzioni applicate

- sostituita l'affermazione universale sugli esempi iniziali con un confine esplicito tra automazione ordinaria e AI;
- usata la definizione OECD come ancora operativa, senza presentarla come unica tassonomia possibile;
- chiarita la convenzione locale `modello` rispetto a `sistema`;
- riscritta la distinzione discriminativo/generativo includendo classificatori generativi e modelli condizionati;
- rafforzata la separazione tra meccanismo, obiettivo e ampiezza;
- dichiarata la relatività di `generalista` e `specialistico`;
- dichiarato che il risultato PyTorch non è un test di generalizzazione;
- respinte tutte le immagini non conformi e rimosse dal percorso editoriale;
- portata la versione a `0.1.1-draft2`.

## Artefatti riaperti

- `CHAPTER.md`;
- `CLAIMS.md`;
- specifiche `AI-01` e `AI-02`;
- audit visuale.

# Review `DID-AI-02`. Seconda lettura completa del testo

- Versione esaminata: `0.1.1-draft2`
- Ambito: prosa, formule, snippet, esercizi, fonti e confini
- Esito del testo: **superata**

## Oggetto continuo e progressione

- [x] La richiesta `Il pacco non è arrivato` attraversa i principali confronti.
- [x] Il testo parte dal programma, introduce la definizione di AI system e separa modello e sistema.
- [x] Regole e apprendimento precedono AI, ML e deep learning.
- [x] Parametri e training precedono inference e snippet.
- [x] Discriminativo e generativo precedono generative AI e foundation model.
- [x] I tre assi vengono ricomposti soltanto dopo la loro introduzione.

## Gate di comparsa

- [x] `Machine learning` compare dopo un esempio di comportamento appreso.
- [x] `Deep learning` compare dopo representation learning.
- [x] Parametri, loss e optimizer vengono descritti prima del codice.
- [x] Generative AI compare dopo la distinzione generativo/discriminativo.
- [x] Foundation model compare dopo generative AI e non viene usato come suo sinonimo.
- [x] Le tecniche di adattamento sono nominate come consumer futuri, senza spiegarle a metà.

## Struttura logica in prosa

- [x] I titoli descrivono oggetti e problemi reali.
- [x] Il capitolo non espone lo scaffold `input/trasformazione/invariante` come serie ripetitiva di sezioni.
- [x] Cambiamento, invarianti e confini restano ricostruibili nei paragrafi.
- [x] Le transizioni nominano l'oggetto prodotto e il passaggio successivo.
- [x] Il capitolo non appare come checklist compilata.

## Accuratezza e fonti

- [x] La definizione OECD è attribuita e non trasformata in definizione universale del campo.
- [x] Il lifecycle NIST viene riferito a prodotti, servizi e sistemi.
- [x] AI, machine learning, representation learning e deep learning sono distinti.
- [x] La soglia della profondità non viene presentata come numero universale.
- [x] La distinzione generativo/discriminativo è limitata al contratto dichiarato.
- [x] Il risultato Ng/Jordan non viene generalizzato a tutti i modelli.
- [x] NIST GAI sostiene la produzione di contenuto sintetico e il confine con i foundation model.
- [x] La definizione CRFM viene attribuita al report che introduce il termine.
- [x] Le convenzioni editoriali sono indicate come tali.

## Matematica e codice

- [x] Formula lineare con shape implicite compatibili.
- [x] `p(y|x)`, `p(x,y)` e `p(x|c)` usate con significato coerente.
- [x] Loss e output coincidono con il file eseguito.
- [x] `eval()` e `inference_mode()` mantengono ruoli distinti.
- [x] La mancata modifica dei parametri in inference è testata.
- [x] La diminuzione della loss non viene presentata come generalizzazione.

## Prosa

- [x] Italiano diretto e progressivo.
- [x] Nessun em dash.
- [x] Nessuna metafora portante o personificazione.
- [x] Termini inglesi usati in modo coerente.
- [x] Seconda persona limitata a controlli ed esercizi.
- [x] Referenti espliciti nei passaggi con modello, sistema e checkpoint.

## Controlli finali

- [x] Il lettore può ricostruire la relazione AI, ML e deep learning.
- [x] Può localizzare l'aggiornamento dei parametri.
- [x] Può delimitare generative AI e foundation model.
- [x] Può trasferire i tre assi a un filtro antispam.
- [x] Può prevedere l'effetto dell'aggiunta di un tool al sistema.

# Audit fattuale

- [x] Tutti i claim portanti sono registrati in `CLAIMS.md`.
- [x] Le fonti sono primarie, ufficiali o autorevoli e riportano limiti d'uso.
- [x] Le informazioni soggette a cambiamento sono datate.
- [x] Non sono presenti benchmark propri.
- [x] Non sono presenti inferenze fattuali editoriali presentate come fatti.

# Audit algoritmico e temporale

- [x] Training: zeroing dei gradienti, forward, loss, backward, step.
- [x] Inference: `eval()`, `inference_mode()`, forward, nessun optimizer step.
- [x] PyTorch eseguito `2.10.0+cpu` distinto dalla documentazione stable `2.13`.
- [x] AI RMF 1.0 citato come versione pubblicata, senza anticipare la revisione in corso.
- [x] Pagina NIST AI 600-1 registrata con pubblicazione 2024 e aggiornamento della pagina 2026.

# Audit visuale

Esito: **respinto e aperto**.

Le candidate prodotte durante questa sessione sono state escluse perché rappresentavano:

- pagine GitHub;
- riepiloghi di merge e branch;
- dashboard sul completamento del libro;
- indici dell'opera non richiesti.

Nessuna candidata rispondeva alla domanda di `AI-01` o `AI-02`. Nessun file è stato caricato come immagine del capitolo.

# Esito finale

Il testo `0.1.1-draft2` e il codice non presentano difetti tecnici o didattici bloccanti noti. Il capitolo resta nello stato `revisione tecnica, visuali bloccate` e non può passare alla revisione autoriale. La prossima operazione valida è produrre le due visuali conformi, sottoporle ad audit e ripetere il controllo incrociato completo.
