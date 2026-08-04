# Registro delle ricerche approfondite

## Funzione

Questo documento registra le ricerche globali che modificano la tassonomia, il catalogo, l'indice o la maturità dei contenuti.

Le ricerche specifiche di un capitolo restano anche nel relativo `FONTI_PRIMARIE.md`. Questo registro non sostituisce il controllo puntuale delle fonti quando viene scritta una frase.

# DR-2026-07-30-01

## Stato

- ID: `DR-2026-07-30-01`
- Tipo: ricerca approfondita globale
- Data di chiusura: **30 luglio 2026**
- Ambito temporale dichiarato: fonti e documentazione individuate e ricontrollate fino alla data di chiusura
- Esito: tassonomia editoriale aggiornata e catalogo iniziale creato
- Documenti prodotti o modificati:
  - `12_ARCHITETTURA_EDITORIALE_EVOLUTIVA.md`;
  - `13_PROTOCOLLO_AGGIORNAMENTO_CONTENUTI.md`;
  - `14_CATALOGO_STATO_ARTE.md`;
  - `10_INDICE_EDITORIALE.md`;
  - `08_REGISTRO_DECISIONI.md`;
  - `../GUIDELINE.md`;
  - `../README.md`.

## Domanda della ricerca

Come organizzare un libro completo sull'AI generativa in modo che:

- le parti restino stabili quando compaiono nuove architetture;
- le tecniche recenti possano essere inserite senza rinominare o riordinare l'opera;
- la maturità possa cambiare da `FRONTIER` a `ESTABLISHED` o `CORE` senza spostare la collocazione primaria;
- le principali famiglie di architetture, training, post-training, multimodalità, agenti, inference e sicurezza siano censite alla data della ricerca;
- un sistema AI privo del contesto originario possa aggiornare il progetto seguendo regole esplicite.

## Criteri di inclusione

Una famiglia o tecnica è stata registrata quando soddisfaceva almeno questi criteri:

1. contributo tecnico distinguibile;
2. fonte primaria o documentazione ufficiale accessibile;
3. rilevanza per architettura, training, post-training, generazione, inference, valutazione o governance;
4. possibilità di descrivere input, operazione, output, invariante e confine;
5. collocazione determinabile nella tassonomia funzionale;
6. influenza, adozione o potenziale sufficiente per la maturità assegnata.

Una configurazione, un nome commerciale o una semplice combinazione di tecniche non è stata automaticamente trasformata in voce autonoma.

## Aree coperte

- fondamenti matematici e computazionali;
- famiglie generative;
- tokenizzazione, attention e Transformer;
- dati, scaling e distributed training;
- positional methods e contesto lungo;
- MQA, GQA, MLA e gestione KV;
- exact, sparse, local, ring e linear attention;
- SSM, recurrence, long convolution, fast weights e memory layers;
- MoE, routing, adaptive depth e conditional compute;
- language diffusion e predizione multi-token;
- PEFT, RLHF, preference optimization e RL con reward verificabili;
- reasoning, verifier e test-time compute;
- multimodalità, image, audio, video, 3D, world model ed embodied AI;
- retrieval, RAG, memoria, tool, protocolli e agenti;
- quantizzazione, pruning, distillazione e decoding accelerato;
- serving, cache, batching, disaggregazione, kernel e compiler;
- valutazione, interpretabilità, sicurezza, privacy, provenance e governance.

## Fonti primarie e ufficiali di riferimento

La lista seguente è un insieme di fonti seme usato per costruire la tassonomia. Ogni capitolo deve riaprire le fonti pertinenti e registrare sezioni, versioni e limiti nel proprio dossier.

### Attention, Transformer e contesto

- Vaswani et al., *Attention Is All You Need*, NeurIPS 2017, arXiv:1706.03762.
- Bahdanau et al., *Neural Machine Translation by Jointly Learning to Align and Translate*, arXiv:1409.0473.
- Shazeer, *Fast Transformer Decoding: One Write-Head is All You Need*, arXiv:1911.02150.
- Ainslie et al., *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints*, arXiv:2305.13245.
- Su et al., *RoFormer: Enhanced Transformer with Rotary Position Embedding*, arXiv:2104.09864.
- Press et al., *Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation*, arXiv:2108.12409.
- Peng et al., *YaRN: Efficient Context Window Extension of Large Language Models*, arXiv:2309.00071.
- Ding et al., *LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens*, arXiv:2402.13753.
- Liu et al., *Ring Attention with Blockwise Transformers for Near-Infinite Context*, arXiv:2310.01889.
- Dao et al., *FlashAttention*, arXiv:2205.14135.
- Dao, *FlashAttention-2*, arXiv:2307.08691.
- Shah et al., *FlashAttention-3*, arXiv:2407.08608.
- DeepSeek-AI, *DeepSeek-V2*, arXiv:2405.04434.

### State-space, recurrence e architetture ibride

- Gu et al., *Efficiently Modeling Long Sequences with Structured State Spaces*, arXiv:2111.00396.
- Gu e Dao, *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*, arXiv:2312.00752.
- Dao e Gu, *Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality*, arXiv:2405.21060.
- Mamba-3 research report, arXiv:2603.15569.
- Sun et al., *Retentive Network*, arXiv:2307.08621.
- Peng et al., *RWKV: Reinventing RNNs for the Transformer Era*, arXiv:2305.13048.
- Poli et al., *Hyena Hierarchy*, arXiv:2302.10866.
- Beck et al., *xLSTM: Extended Long Short-Term Memory*, arXiv:2405.04517.
- De et al., *Griffin: Mixing Gated Linear Recurrences with Local Attention*, arXiv:2402.19427.
- Yang et al., *Gated Delta Networks*, arXiv:2412.06464.
- *Gated DeltaNet-2*, arXiv:2602.21487.
- *Hybrid Linear Attention Done Right*, arXiv:2603.12201.
- Moonshot AI, *Kimi Linear*, arXiv:2510.26692.
- Behrouz et al., *Titans: Learning to Memorize at Test Time*, arXiv:2501.00663.

### MoE e conditional computation

- Shazeer et al., *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer*, arXiv:1701.06538.
- Fedus et al., *Switch Transformers*, arXiv:2101.03961.
- Dai et al., *DeepSeekMoE*, arXiv:2401.06066.
- Raposo et al., *Mixture-of-Depths*, arXiv:2404.02258.
- DeepSeek-AI, *DeepSeek-V3 Technical Report*, arXiv:2412.19437.

### Tokenizzazione, byte e predizione

- Xue et al., *ByT5*, arXiv:2105.13626.
- Yu et al., *MEGABYTE*, arXiv:2305.07185.
- Meta AI, *Byte Latent Transformer*, arXiv:2412.09871.
- Gloeckle et al., *Better & Faster Large Language Models via Multi-token Prediction*, arXiv:2404.19737.

### Generazione, diffusion e flow

- Ho et al., *Denoising Diffusion Probabilistic Models*, arXiv:2006.11239.
- Rombach et al., *High-Resolution Image Synthesis with Latent Diffusion Models*, arXiv:2112.10752.
- Lipman et al., *Flow Matching for Generative Modeling*, arXiv:2210.02747.
- Peebles e Xie, *Scalable Diffusion Models with Transformers*, arXiv:2212.09748.
- Austin et al., *Structured Denoising Diffusion Models in Discrete State-Spaces*, arXiv:2107.03006.
- Li et al., *Diffusion-LM*, arXiv:2205.14217.
- Sahoo et al., *Simple and Effective Masked Diffusion Language Models*, arXiv:2406.07524.
- Nie et al., *Large Language Diffusion Models*, arXiv:2502.09992.

### Scaling, dati e training

- Kaplan et al., *Scaling Laws for Neural Language Models*, arXiv:2001.08361.
- Hoffmann et al., *Training Compute-Optimal Large Language Models*, arXiv:2203.15556.
- Yang et al., *Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer*, arXiv:2203.03466.
- Shoeybi et al., *Megatron-LM*, arXiv:1909.08053.
- Rajbhandari et al., *ZeRO*, arXiv:1910.02054.
- PyTorch official documentation for distributed training, FSDP, mixed precision and current APIs.

### Post-training, preferenze e reasoning

- Ouyang et al., *Training Language Models to Follow Instructions with Human Feedback*, arXiv:2203.02155.
- Bai et al., *Constitutional AI*, arXiv:2212.08073.
- Rafailov et al., *Direct Preference Optimization*, arXiv:2305.18290.
- Azar et al., *A General Theoretical Paradigm to Understand Learning from Human Preferences*, arXiv:2310.12036.
- Ethayarajh et al., *KTO: Model Alignment as Prospect Theoretic Optimization*, arXiv:2402.01306.
- Hong et al., *ORPO*, arXiv:2403.07691.
- Meng et al., *SimPO*, arXiv:2405.14734.
- Lightman et al., *Let's Verify Step by Step*, arXiv:2305.20050.
- Shao et al., *DeepSeekMath*, arXiv:2402.03300.
- DeepSeek-AI, *DeepSeek-R1*, arXiv:2501.12948.
- Wang et al., *Self-Consistency Improves Chain of Thought Reasoning*, arXiv:2203.11171.
- Snell et al., *Scaling LLM Test-Time Compute Optimally*, arXiv:2408.03314.

### Multimodalità e world model

- Dosovitskiy et al., *An Image is Worth 16x16 Words*, arXiv:2010.11929.
- Radford et al., *Learning Transferable Visual Models From Natural Language Supervision*, arXiv:2103.00020.
- Alayrac et al., *Flamingo*, arXiv:2204.14198.
- Li et al., *BLIP-2*, arXiv:2301.12597.
- Liu et al., *Visual Instruction Tuning*, arXiv:2304.08485.
- Team Chameleon, *Chameleon*, arXiv:2405.09818.
- Girdhar et al., *ImageBind*, arXiv:2305.05665.
- Meta, *Movie Gen*, arXiv:2410.13720.
- Ha e Schmidhuber, *World Models*, arXiv:1803.10122.
- Hafner et al., *Mastering Diverse Domains through World Models*, arXiv:2301.04104.

### Retrieval, memoria, tool e agenti

- Lewis et al., *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, arXiv:2005.11401.
- Karpukhin et al., *Dense Passage Retrieval*, arXiv:2004.04906.
- Khattab e Zaharia, *ColBERT*, arXiv:2004.12832.
- Gao et al., *Precise Zero-Shot Dense Retrieval without Relevance Labels*, arXiv:2212.10496.
- Asai et al., *Self-RAG*, arXiv:2310.11511.
- Sarthi et al., *RAPTOR*, arXiv:2401.18059.
- Yao et al., *ReAct*, arXiv:2210.03629.
- Schick et al., *Toolformer*, arXiv:2302.04761.
- Packer et al., *MemGPT*, arXiv:2310.08560.
- Yang et al., *SWE-agent*, arXiv:2405.15793.
- Specifiche ufficiali versionate per Model Context Protocol e protocolli agent-to-agent.

### Adattamento, compressione, decoding e serving

- Hu et al., *LoRA*, arXiv:2106.09685.
- Dettmers et al., *QLoRA*, arXiv:2305.14314.
- Frantar et al., *GPTQ*, arXiv:2210.17323.
- Xiao et al., *SmoothQuant*, arXiv:2211.10438.
- Lin et al., *AWQ*, arXiv:2306.00978.
- Frantar e Alistarh, *SparseGPT*, arXiv:2301.00774.
- Sun et al., *A Simple and Effective Pruning Approach for Large Language Models*, arXiv:2306.11695.
- Leviathan et al., *Fast Inference from Transformers via Speculative Decoding*, arXiv:2211.17192.
- Chen et al., *Accelerating Large Language Model Decoding with Speculative Sampling*, arXiv:2302.01318.
- Cai et al., *Medusa*, arXiv:2401.10774.
- Li et al., *EAGLE*, arXiv:2401.15077.
- Kwon et al., *Efficient Memory Management for Large Language Model Serving with PagedAttention*, arXiv:2309.06180.
- Zheng et al., *SGLang*, arXiv:2312.07104.
- Zhong et al., *DistServe*, arXiv:2401.09670.
- Documentazione ufficiale versionata di PyTorch, Triton e runtime di serving usati nei capitoli.

### Valutazione, interpretabilità e sicurezza

- Liang et al., *Holistic Evaluation of Language Models*, arXiv:2211.09110.
- Hendrycks et al., *Measuring Massive Multitask Language Understanding*, arXiv:2009.03300.
- Jimenez et al., *SWE-bench*, arXiv:2310.06770.
- Zou et al., *Universal and Transferable Adversarial Attacks on Aligned Language Models*, arXiv:2307.15043.
- Greshake et al., *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*, arXiv:2302.12173.
- Abadi et al., *Deep Learning with Differential Privacy*, arXiv:1607.00133.
- Kirchenbauer et al., *A Watermark for Large Language Models*, arXiv:2301.10226.
- Documenti e repository ufficiali per circuit analysis, sparse autoencoder, model cards, C2PA e standard di provenance.

## Risultati strutturali della ricerca

### Opera unica

È stata sostituita la divisione canonica in due volumi con una sola opera continua. La divisione in tomi è diventata una scelta di export.

### Parti stabili

Sono state definite quattordici parti funzionali con ID da `P01` a `P14`. I nomi non contengono riferimenti a una generazione di modelli o a un periodo temporale specifico.

### Routing

Le novità vengono collocate in base all'oggetto modificato e al problema risolto. Le relazioni secondarie vengono mantenute tramite tag e cross-reference.

### Maturità

Sono stati definiti gli stati `CORE`, `ESTABLISHED` e `FRONTIER`. La maturità è separata dalla collocazione e può cambiare senza spostare la voce.

### Identità dei capitoli

È stato separato l'ID semantico stabile dal numero stampato specifico dell'edizione.

### Frontiera distribuita

Le voci frontier restano nella propria parte funzionale. `P14` conserva soltanto l'osservatorio, le repliche, la cronologia e le domande aperte.

## Limiti della ricerca

- La ricerca non dimostra l'assenza di altri lavori rilevanti.
- La classificazione di maturità è editoriale e deve essere riesaminata.
- Una fonte seme non autorizza a riportare ogni dettaglio senza riaprire il documento originale.
- I risultati quantitativi non vengono trasferiti nel libro senza setup, versione e verifica puntuale.
- API, standard, repository e normative devono essere ricontrollati alla data del capitolo.
- Le aree frontier possono cambiare rapidamente dopo la data di chiusura.

## Prossima revisione

Durante la produzione attiva:

- controllo locale prima di ogni capitolo;
- revisione delle voci `FRONTIER` entro 90 giorni dall'ultima verifica;
- ricerca globale prima della prima edizione congelata;
- ricerca straordinaria quando una nuova famiglia non è collocabile con il routing corrente.

Ogni ricerca successiva riceve un nuovo ID e non sovrascrive retroattivamente questa scheda.

# DR-2026-08-03-01

## Stato

- ID: `DR-2026-08-03-01`
- Tipo: audit di completamento editoriale, fonti e visuali
- Data di chiusura del passaggio: **3 agosto 2026**
- Ambito: capitoli `14-27`, `29-30` e `46-98`, esclusi i capitoli `31-45` già presenti come candidati più sviluppati
- Esito: 69 candidature didattiche rigenerate con testo, claim, fonti, codice, test e due visuali candidate ciascuna
- Stato editoriale: candidatura completa in revisione autoriale; non equivale ad approvazione o congelamento

## Verifiche locali

- `validate_complete_book()`: `98` capitoli, `12` appendici, `208` immagini collegate e verificabili
- Capitoli rigenerati: `69`; immagini `candidate-v2`: `138`
- Ogni candidatura ha cinque sezioni tematiche, un riepilogo, formula o contratto procedurale, output Python e test
- I riferimenti `SRC` presenti nel testo sono stati confrontati con il dossier `FONTI_PRIMARIE.md` del capitolo
- Renderer visuale: PNG RGB `1800x1000`, angoli bianchi, testo contenuto nel box, ordine di lettura esplicito

## Fonti riaperte

Sono stati ricontrollati, come fonti seme primarie o ufficiali, InstructGPT, LoRA, DPO, RAG, CLIP, BLIP-2, Dense Passage Retrieval, PagedAttention, C2PA, NIST AI RMF e membership inference. Le schede di capitolo mantengono il dossier più ampio pertinente al proprio profilo.

Un controllo HTTP sui dossier ha individuato 256 URL distinti: 238 raggiungibili direttamente o dopo redirect e 18 che richiedono accesso alternativo, tra pagine DOI/ACM con risposta `403` e un endpoint storico non raggiungibile. I link che risultavano obsoleti nel perimetro modificato sono stati sostituiti con riferimenti ufficiali versionati.

## Limiti

- L'esecuzione Python verifica contratti piccoli e deterministici, non la qualità di un modello di produzione.
- Le fonti sostengono definizioni e meccanismi delimitati; non autorizzano risultati quantitativi oltre il setup citato.
- Le figure sono candidate: la rilettura autoriale deve ancora approvare testo, claim, layout e alt text prima di un eventuale `final.png`.

# DR-2026-08-03-02

## Stato

- ID: DR-2026-08-03-02
- Tipo: revisione completa di prosa, fonti, codice e visuali
- Data: **3 agosto 2026**
- Ambito: capitoli 14-98, con esclusione del capitolo 28 già consolidato; il capitolo 44 è stato ricondotto al percorso canonico 44_moe_conditional
- Esito: 84 capitoli rivisti, inclusi i 31-45 che nella passata precedente non erano stati riscritti
- Stato editoriale: candidatura tecnica completa; approvazione autoriale ancora aperta

## Verifiche locali

- validate_complete_book(): 98 capitoli, 12 appendici, 208 immagini collegate e verificabili
- Ogni capitolo rivisto ha prosa continua, cinque sezioni, esempio o derivazione, formula o contratto procedurale, esercizi, dossier fonti, claim, audit e codice eseguibile
- 84 suite di test locali superate; ogni nuova suite verifica determinismo, output, invariante e rifiuto di una shape incoerente
- I link collegati dal testo puntano a 168 candidate PNG, due per capitolo rivisto
- Audit raster: PNG RGB 1800x1000, sfondo bianco, angoli bianchi e contenimento controllati

## Visuali

Le visuali non usano più una composizione unica: il set collegato distribuisce 15 famiglie tra pipeline, branching, chart, architettura, matrici, loop, timeline, scatter, confronto, manifest, queue, graph, funnel, threat e checklist. Le figure a ciclo sono state ricontrollate dopo aver spostato il nodo superiore e i collegamenti per non invadere la domanda.

## Fonti riaperte

Il controllo HTTP sui 73 URL unici presenti nei dossier ha rilevato 65 risposte raggiungibili o redirette e 8 endpoint che richiedono accesso alternativo, principalmente pagine DOI, ACM, Wiley o Science con 403 e un PDF storico con connessione rifiutata. Questi limiti restano espliciti e non vengono trasformati in una falsa approvazione automatica.

## Limiti della revisione

- Gli snippet verificano meccanismi piccoli e deterministici, non la qualità di modelli o servizi di produzione.
- Le fonti sostengono definizioni e meccanismi delimitati; nessun risultato quantitativo viene trasferito senza setup.
- Le immagini sono candidate: prima della pubblicazione servono lettura ad alta voce, revisione autoriale e approvazione di testo, claim, layout e alt text.

# DR-2026-08-03-03

## Stato

- ID: DR-2026-08-03-03
- Tipo: revisione globale di profondità, coerenza, codice, fonti e visuali
- Data: **3 agosto 2026**
- Ambito: tutti i 98 capitoli e le 196 immagini attualmente collegate da `CHAPTER.md`
- Esito: audit tecnico e visivo completato; passaggi testuali resi più specifici nei capitoli generati 14-98
- Stato editoriale: candidatura completa in revisione autoriale; non è un'approvazione per la pubblicazione

## Struttura e prosa

- Ogni capitolo contiene un oggetto continuo, cinque sezioni tematiche, esempio o derivazione, formula o contratto procedurale, codice, verifica della comprensione, esercizi, fonti e limiti.
- La richiesta «Il pacco non è arrivato» resta l'esempio comune; l'oggetto tecnico cambia per capitolo e il passaggio al consumer successivo è registrato nei piani interni.
- La prosa dei capitoli 14-98 è stata rifinita con esempi legati al concetto della sezione: token e mask, dati e manifest, reward, retrieval, tool, quantizzazione, costi, sicurezza e valutazione.
- Audit statico: 98 capitoli, minimo 1.524 parole e massimo 3.670, nessun placeholder, nessun link immagine mancante e nessun paragrafo ripetuto in almeno otto capitoli.

## Codice

- Test eseguiti dopo l'ultima rigenerazione: `166` passati, `0` falliti.
- File Python compilati: `307` passati, `0` falliti.
- I risultati locali restano esempi deterministici su CPU e non vengono presentati come benchmark di produzione.

## Visuali

- Audit raster sulle 196 immagini collegate: `0` problemi automatici di esistenza, dimensioni, modalità, angoli, sfondo e contenimento.
- Il set usa famiglie diverse, tra cui pipeline, branch, chart, architecture, matrix, loop, timeline, scatter, compare, manifest, queue, graph, funnel, threat e checklist.
- Le immagini generiche dei capitoli 8-13 sono state sostituite con composizioni specifiche per il contenuto; ATT-01 è stata rifatta come `candidate-v4` e ATT-02 come `candidate-v2`.
- È stata eseguita una rilettura tramite contact sheet di tutte le figure. Non sono emersi overlap, testo tagliato o frecce ambigue a livello raster; resta necessaria l'approvazione autoriale del significato, dell'alt text e della composizione finale.

## Fonti

- Sono stati estratti `180` URL unici da `chapters/` e `docs/`.
- Il probe HTTP corrente ha restituito `158` risposte 2xx/3xx; `22` URL richiedono accesso alternativo o controllo manuale: `18` risposte 403, `2` risposte 404 del trasporto usato e `2` timeout/connessioni rifiutate.
- Un 403 o un timeout non viene interpretato come smentita della fonte: DOI, ACM, Wiley, Science e archivi storici richiedono spesso un accesso diverso. Le affermazioni restano delimitate al dossier e alla fonte primaria indicata.
- I riferimenti, claim e mapping locali non hanno prodotto problemi strutturali nell'audit.

## Limiti e gate ancora aperti

- L'audit automatico controlla struttura, collegamenti, contratti eseguibili e difetti raster; non sostituisce la lettura ad alta voce né l'approvazione autoriale riga per riga.
- Le figure restano candidate finché non viene approvata ogni coppia testo-visuale e non viene deciso se promuoverla a `final.png`.
- Prima del congelamento editoriale vanno ricontrollate le affermazioni sensibili a versioni, standard, API e normativa alla data di pubblicazione.

# DR-2026-08-03-04

## Stato

- ID: DR-2026-08-03-04
- Tipo: controllo finale di allineamento semantico, raster, fonti e repository
- Data: **3 agosto 2026**
- Ambito: tutti i 98 capitoli, 196 immagini attive e i dossier presenti in `chapters/` e `docs/`
- Esito: candidatura tecnica coerente e verificata; approvazione autoriale ancora aperta

## Allineamento e prosa

- `audit_semantic_alignment.py`: `98` capitoli puliti, `0` problemi di routing, oggetto, input, output, invariante, esempio comune, claim o dossier fonte.
- `audit_book_general.py`: `98` capitoli, `196` immagini uniche collegate, `0` immagini mancanti, `0` problemi raster strutturali, `0` problemi di codice, nessun paragrafo ripetuto in almeno otto capitoli; lunghezza da `1.520` a `3.670` parole.
- I capitoli generati da 14 a 98, escluso il 28 già preservato, usano un routing tematico specifico e non un profilo generico condiviso. Sono stati corretti in particolare i dossier di interoperabilità, governance, piccolo language model, produzione, replica e frontiera.

## Codice e fonti

- Suite locali: `166` test passati, `0` falliti dopo la rigenerazione finale.
- File Python controllati in memoria: `309` compilati, `0` falliti.
- Sono stati sostituiti riferimenti obsoleti o ambigui con fonti ufficiali o primarie più adatte, tra cui NIST AI RMF, NIST GenAI Profile, NeurIPS Paper Checklist, Mirasol3B e la pagina dell'editore per LSTM.
- Probe URL con fallback GET: `361` URL distinti, `335` risposte 2xx/3xx, `26` accessi manuali o non raggiungibili per 403/406, timeout o archivi che richiedono un percorso alternativo; nessun 404 confermato dopo il fallback GET.

## Visuali e pulizia

- Le 196 immagini attive sono PNG RGB `1800x1000`; apertura, dimensioni, modalità e collegamenti sono superati per tutte.
- La rilettura raster a piena risoluzione ha portato a correggere etichette di grafico troncate, frasi visuali chiuse artificialmente e note sospese nelle figure di attenzione hardware, sicurezza agentica, progettazione della valutazione, governance e frontiera.
- Le figure usano composizioni diverse e guidate dal concetto: pipeline, branch, chart, architecture, matrix, loop, timeline, scatter, compare, manifest, queue, graph, funnel, threat e checklist.
- I vecchi candidati non referenziati sono stati spostati in cartelle temporanee recuperabili sotto `/private/tmp/aibook-unused-pngs-20260803-r2/`, `r3/` e `r4/`; nessun asset attivo è stato rimosso.

## Gate aperti

- Le figure restano `candidate-vN.png` finché l'autore non approva coppia testo-visuale, alt text, leggibilità e composizione; non vengono promosse automaticamente a `final.png`.
- Restano necessarie lettura ad alta voce, verifica editoriale riga per riga e ricontrollo delle affermazioni sensibili a versioni, standard, API e normativa alla data di pubblicazione.

# DR-2026-08-03-05

## Stato

- ID: `DR-2026-08-03-05`
- Tipo: verifica conclusiva di prosa, immagini, fonti, codice e pulizia degli artefatti
- Data: **3 agosto 2026**
- Ambito: tutti i 98 capitoli, 196 immagini attive, dossier fonte, claim e snippet
- Esito: candidatura tecnica completa e coerente; approvazione autoriale e pubblicazione ancora escluse

## Prosa e struttura

- I capitoli candidati 14-98, escluso il 28 preservato, sono stati rigenerati con esempi, meccanismi, controlli e limiti specifici al tema. Sono 84 capitoli, non un unico testo copiato.
- Il controllo finale sulla parte pubblica misura da `1.927` a `3.623` parole per capitolo; negli 84 candidati generati da 14 a 98 escluso il 28, da `1.927` a `2.262` parole.
- I paragrafi pubblici ripetuti esattamente sono `0`; anche i vecchi fallback testuali individuati durante la revisione sono stati rimossi. La profondità non viene però dichiarata sufficiente per la pubblicazione senza lettura ad alta voce.
- Il percorso continuo resta tracciato dall'esempio comune «Il pacco non è arrivato» agli oggetti, input, operazioni, output e invarianti specifici di capitolo.

## Codice, claim e fonti

- `audit_book_general.py`: `98` capitoli, `196` immagini collegate, `0` immagini mancanti, `0` problemi raster automatici, `0` problemi di fonti, claim o codice.
- `audit_semantic_alignment.py`: `98` capitoli puliti, `0` problemi di routing semantico, profondità, dossier, claim o metadata visuali.
- Suite locale: `166/166` file di test eseguiti con esito positivo; `309/309` file Python compilati in memoria.
- Il probe GET concorrente ha esaminato `363` URL unici: `342` risposte 2xx/3xx, `21` accessi da controllare manualmente e `0` 404/410 confermati. I casi manuali sono soprattutto DOI, ACM, Wiley, Science, CVF, Harvard Stat110 e archivi con timeout o restrizioni di accesso; non vengono trasformati automaticamente in fonti respinte.

## Immagini e pulizia

- Tutti i `196` riferimenti attivi sono PNG RGB `1800x1000`, con metadata `SPEC.md`, `AUDIT.md` e `ALT_TEXT.md`; il raster audit non rileva clipping, angoli non bianchi, modalità errate o riferimenti mancanti.
- La revisione tramite otto contact sheet ha coperto tutti i 196 asset; campioni ad alta risoluzione hanno verificato testo contenuto, frecce leggibili, assenza di sovrapposizioni e composizioni coerenti. Le famiglie includono pipeline, branch, chart, architecture, matrix, loop, timeline, scatter, compare, manifest, queue, graph, funnel, threat e checklist.
- I PNG non più referenziati sono stati spostati in modo recuperabile fuori dal repository, nelle cartelle `/private/tmp/aibook-unused-pngs-20260803-r5/` fino a `/private/tmp/aibook-unused-pngs-20260803-r9/`; nessun asset attivo è stato cancellato.
- Le figure restano `candidate-vN.png`: la decisione finale deve ancora stabilire, per ciascuna coppia capitolo-visuale, se la composizione spiega meglio il concetto rispetto alle alternative e se promuoverla a `final.png`.

## Gate aperti

- Lettura ad alta voce e revisione autoriale riga per riga.
- Approvazione finale di testo, fonti, claim, alt text e coppie testo-immagine.
- Ricontrollo delle affermazioni sensibili a versioni, API, standard e normativa alla data di pubblicazione.
- Eventuale passaggio da candidata tecnica a artefatto editoriale finale, senza confondere i test locali con un benchmark di produzione.

# DR-2026-08-03-06

## Stato

- ID: `DR-2026-08-03-06`
- Tipo: verifica conclusiva di prosa, immagini, fonti, codice e pulizia dopo la rigenerazione
- Data: **3 agosto 2026**
- Ambito: tutti i 98 capitoli, 196 immagini attive, dossier fonte e 84 capitoli rigenerati da 14 a 98, escluso il 28 preservato
- Esito: candidatura tecnica completa, coerente e riproducibile nei gate automatici; approvazione editoriale ancora aperta

## Prosa e continuità

- `audit_semantic_alignment.py`: `98/98` capitoli puliti, con `0` problemi di routing, oggetto, input, output, invariante, esempio comune, claim o dossier.
- `audit_editorial_quality.py --strict`: `98/98` capitoli senza problemi, lunghezza da `1.805` a `3.402` parole nella parte editoriale analizzata, `314` formule, `0` formule non etichettate, `0` occorrenze malformate e `0` paragrafi duplicati.
- La passata di generazione ha reso gli esempi delle lezioni 46-98 specifici per il concetto: loss mask, delta low-rank, reward, DPO, verifier, retrieval, tool scope, quantizzazione, valutazione, provenienza e readiness.
- Una scansione linguistica dedicata ha rilevato `0` costruzioni residue `da l'`, `a l'`, `fino a la`, inserzioni malformate o punteggiatura duplicata nei capitoli attivi.

## Codice e fonti

- `166/166` file di test sono stati eseguiti dopo l'ultima rigenerazione, con `0` fallimenti.
- `311/311` file Python del repository sono stati compilati in memoria, con `0` errori.
- `docs/source_verification_2026-08-03.json` registra `262` fonti uniche e `336` collegamenti fonte-claim: `280` con contesto aperto, `44` con contesto parziale e `12` confermati tramite accesso web ufficiale.
- Nei dossier risultano `452` claim con esito `verificata` e `52` con esito `corretta`; gli ultimi sono stati ristretti al perimetro sostenuto dalla fonte e non vengono presentati come verifiche quantitative più ampie.

## Immagini e pulizia

- Le `196` immagini attive sono PNG RGB `1800x1000`, tutte referenziate, con `0` problemi automatici di apertura, dimensioni, modalità, contenimento o duplicazione.
- Sette contact sheet hanno coperto tutte le immagini attive. La rilettura ha verificato composizioni differenziate tra pipeline, branch, chart, architecture, matrix, loop, timeline, scatter, compare, manifest, queue, graph, funnel, threat e checklist; non sono emersi clipping, overlap o frecce ambigue.
- Le versioni candidate non referenziate sono state spostate in modo recuperabile nella cartella temporanea `/private/tmp/aibook-unused-pngs-20260803-r11/`; nessun asset attivo è stato rimosso.
- Le immagini restano `candidate-vN.png`: la promozione a `final.png` richiede ancora approvazione autoriale della coppia testo-visuale, dell'alt text e della composizione.

## Gate ancora aperti

- Lettura ad alta voce e revisione riga per riga per un lettore non esperto.
- Ricontrollo autoriale delle affermazioni sensibili a versioni, API, standard e normativa alla data di pubblicazione.
- Approvazione finale delle figure e congelamento degli artefatti editoriali.

# DR-2026-08-03-07

## Stato

- ID: `DR-2026-08-03-07`
- Tipo: audit finale ripetuto dopo la variazione della prosa e la pulizia delle visuali candidate
- Data: **3 agosto 2026**
- Ambito: tutti i 98 capitoli, 12 appendici, 196 immagini attive, codice, claim, dossier fonte e repository
- Esito: candidatura tecnica completa e riproducibile; approvazione autoriale, lettura ad alta voce e pubblicazione restano escluse

## Testo, struttura e profondità

- `audit_semantic_alignment.py`: `98/98` capitoli puliti, `0` problemi di routing, oggetto, input, output, invariante, esempio comune, claim o dossier.
- `audit_editorial_quality.py --strict`: `98/98` capitoli senza problemi, `2.159-3.402` parole, `314` formule, `0` formule non etichettate, `0` occorrenze malformate e `0` paragrafi duplicati.
- `audit_book_general.py --json`: `98` capitoli, `2.186-3.670` parole secondo il conteggio generale, `0` problemi di fonti, claim, codice o struttura.
- La variazione della prosa ha introdotto cadenzamenti e descrittori specifici per le famiglie tematiche, mantenendo il contratto comune senza riutilizzare un unico paragrafo pubblico per tutti i capitoli.

## Codice e fonti

- Sono stati eseguiti `166/166` file di test, con `0` fallimenti.
- Sono stati compilati in memoria `311/311` file Python, con `0` errori.
- `git diff --check` è terminato senza segnalazioni.
- `docs/source_verification_2026-08-03.json` è stato rigenerato: `262` fonti uniche, `336` record fonte-claim, `280` con contesto aperto, `44` con contesto parziale e `12` confermati tramite accesso web ufficiale.
- Nei dossier restano `452` claim marcati `verificata` e `52` marcati `corretta`; questi ultimi sono stati ristretti al perimetro sostenuto dalla fonte. Il risultato non equivale a una nuova verifica manuale di ogni affermazione sensibile alla data di pubblicazione.

## Immagini e varietà compositiva

- I riferimenti attivi sono `196`, tutti risolti e unici, due per ciascuno dei `98` capitoli; il raster audit segnala `0` problemi di apertura, dimensioni, modalità, contenimento o duplicazione.
- Le 196 visuali sono distribuite in 15 famiglie compositive principali: pipeline, branch, chart, architecture, matrix, loop, timeline, scatter, compare, manifest, queue, graph, funnel, threat e checklist.
- Sette contact sheet hanno coperto l'intero set; i campioni ad alta risoluzione hanno verificato testo contenuto, frecce leggibili, assenza di clipping e assenza di sovrapposizioni osservabili.
- `1.848` PNG candidati non più referenziati sono stati spostati in modo recuperabile in `/private/tmp/aibook-unused-pngs-20260803-r12/`; nessun asset attivo è stato rimosso.
- Le figure restano `candidate-vN.png`: la promozione a `final.png` richiede ancora la decisione autoriale sulla coppia testo-visuale, sull'alt text e sulla composizione.

## Gate ancora aperti

- Lettura integrale ad alta voce e revisione riga per riga per un lettore non esperto.
- Ricontrollo autoriale delle affermazioni sensibili a versioni, API, standard e normativa alla data di pubblicazione.
- Approvazione finale delle figure, degli alt text e delle coppie testo-immagine.
- Congelamento degli artefatti editoriali e, solo dopo i gate, eventuale promozione delle candidate a `final.png`.

# DR-2026-08-03-08

## Stato

- ID: `DR-2026-08-03-08`
- Tipo: gate operativo finale dopo la revisione della prosa, la verifica delle fonti, la rigenerazione delle figure e la pulizia del repository
- Data: **3 agosto 2026**
- Ambito: tutti i 98 capitoli, 12 appendici, 208 immagini attive, codice, claim, dossier fonte e artefatti temporanei
- Esito: candidatura tecnica completa e riproducibile; approvazione autoriale, lettura ad alta voce e pubblicazione restano escluse

## Testo, struttura e profondità

- `audit_semantic_alignment.py`: `98/98` capitoli puliti, con `0` problemi di routing, oggetto, input, output, invariante, esempio comune, claim o dossier.
- `audit_editorial_quality.py --strict`: `98/98` capitoli senza problemi, `2.112-3.402` parole, `314` formule, `0` formule non etichettate, `0` occorrenze malformate e `0` paragrafi duplicati.
- `audit_book_general.py --json`: `98` capitoli, `2.151-3.670` parole secondo il conteggio generale, `0` problemi di fonti, claim, codice, struttura o immagini.
- La prosa è stata rigenerata con esempi e spiegazioni causali specifici per sezione; il contratto comune input-operazione-output-invariante resta leggibile senza esporre lo scaffolding editoriale nel testo pubblico.

## Codice e fonti

- Sono stati eseguiti `616` test in `166` file di test, con `0` fallimenti; è comparso soltanto un warning PyTorch non bloccante nel test della ricetta di pretraining.
- Sono stati compilati in memoria `311/311` file Python, con `0` errori; `git diff --check` è terminato senza segnalazioni.
- `docs/source_verification_2026-08-03.json` registra `419` fonti uniche e `502` record fonte-claim: `332` con contesto aperto, `127` con contesto parziale e `43` confermati tramite accesso web ufficiale.
- Tutti i `502` record sono ora classificati nel registro, con `0` elementi `manual-required`; questo è un controllo bounded di URL, metadati e contesto estratto, non la lettura riga per riga di ogni fonte né una garanzia permanente per affermazioni sensibili a versioni, standard o normativa.

## Immagini e pulizia

- I capitoli hanno `196` immagini attive, due ciascuno; le appendici ne aggiungono `12`, per `208` riferimenti attivi. Non risultano immagini mancanti, duplicate o con problemi automatici di apertura, dimensione, modalità o contenimento.
- Le immagini dei capitoli usano composizioni differenziate per concetto, tra pipeline, branch, chart, architecture, matrix, loop, timeline, scatter, compare, manifest, queue, graph, funnel, threat e checklist. Le appendici mantengono invece una mappa comune perché svolgono una funzione di orientamento.
- Contact sheet sull'intero set e spot check ad alta risoluzione hanno verificato leggibilità del testo, contenimento, frecce e assenza di overlap osservabili. Le visuali restano candidate, non approvate editorialmente.
- `842` PNG candidati non più referenziati sono stati spostati in modo recuperabile in `/private/tmp/aibook-unused-pngs-20260803-r13/`; nessun asset attivo è stato rimosso.

## Gate ancora aperti

- Lettura integrale ad alta voce e revisione riga per riga per un lettore non esperto.
- Ricontrollo autoriale delle affermazioni sensibili e approvazione finale delle fonti alla data di pubblicazione.
- Approvazione di ogni coppia testo-visuale, alt text e composizione, poi eventuale promozione da `candidate-vN.png` a `final.png`.
- Congelamento degli artefatti editoriali; non sono stati eseguiti commit, push, tag o release.

# DR-2026-08-04-01

## Stato

- ID: `DR-2026-08-04-01`
- Tipo: revisione integrale lezione per lezione, ricostruzione visuale e pulizia dell'evidenza Python
- Data: **4 agosto 2026**
- Ambito: 98 capitoli, 12 appendici, testo, claim, fonti sensibili, codice, output, visuali e pipeline minima
- Esito: candidatura tecnica revisionata; approvazione autoriale e congelamento restano aperti

## Testo e struttura

- `audit_book_quality.py --strict`: `98/98` capitoli e `12/12` appendici puliti; nessun paragrafo lungo riutilizzato in tre o più capitoli.
- `audit_semantic_alignment.py`: `98/98` capitoli puliti.
- `audit_editorial_quality.py --strict`: `0` capitoli problematici, `910-3.402` parole pubbliche, `279` formule, `0` formule schematiche non etichettate, `0` paragrafi duplicati e `0` immagini problematiche.
- `audit_book_general.py`: `0` problemi di fonti, claim, codice, immagini o paragrafi ripetuti nel proprio perimetro.
- I capitoli 14-98, escluso il pilota 28, sono stati ricostruiti da nuclei semantici specifici e non da un paragrafo pubblico comune. Prerequisiti, casi, controlli, connessioni ed esercizi restano locali alla lezione.

## Codice

- `94/98` capitoli conservano un riferimento eseguibile con blocco Python nel testo, output letterale, file completo, test e output versionato.
- I capitoli 20, 30, 93 e 98 dichiarano un'eccezione motivata. I vecchi script generici sono stati rimossi, perché contraddicevano la prova documentale richiesta dal tema.
- Sono stati eseguiti `541` test in `114` file con Python 3.13.12, NumPy 2.5.1 e PyTorch 2.12.1; altri `3` test JAX sono passati nell'ambiente JAX 0.11.0. Totale: `544` test in `115` file, `0` fallimenti.
- `272/272` file Python sono stati analizzati sintatticamente.
- Sono stati rimossi 51 test storici scollegati che importavano funzioni non più presenti e 159 output o record ambiente duplicati della prima materializzazione.

## Fonti

- La passata globale corrente è registrata in `source_verification_2026-08-04.json`: `420` fonti uniche e `503` record fonte-claim; `332` contesti aperti, `128` parziali e `43` confermati tramite accesso web ufficiale.
- Il 4 agosto sono stati ricontrollati i punti corretti ad alto rischio: tassonomia generativa e precision-recall del capitolo 20, lifecycle MCP e protocollo A2A del capitolo 68, QAT, GPTQ, AWQ e SmoothQuant del capitolo 74, testo ufficiale dell'AI Act e misura ambientale NIST del capitolo 93.
- Questo controllo non trasforma automaticamente l'intero libro in un'opera fattualmente congelata: API, standard e normativa vanno ricontrollati alla data di pubblicazione.

## Visuali

- Sono state rigenerate e riaperte `168` visuali dei capitoli 14-98, escluso 28, e `12` visuali di appendice. Con le 28 figure iniziali preservate, i capitoli mantengono `196` riferimenti attivi e unici; il totale con le appendici è `208`.
- Le 84 coppie revisionate usano 165 modelli semantici ricondotti a dieci primitive deterministiche: processi, cicli, stack, confronti, tree, grid, boundary, grafi, strutture dell'evidenza e tile.
- I vecchi grafici quantitativi illustrativi sono stati eliminati dal percorso attivo. Una figura con numeri è ammessa soltanto quando conserva dati eseguiti o una fonte con setup e unità.
- Sei contact sheet hanno coperto l'intero set revisionato; spot check a piena risoluzione hanno incluso attention hardware-aware, test-time compute, interoperabilità, quantizzazione, prompt injection e piccolo language model.
- Tutte le figure restano candidate tecniche con approvazione autoriale aperta.

## Gate trasversali aggiunti

- `audit_visual_geometry.py --strict`: `208/208` immagini attive senza problemi; `180` manifest semantici e `28` asset storici controllati con raster e checklist.
- `audit_editorial_variation.py --strict`: nessun marker dello scaffold storico e nessuna frase condivisa da più di `12` capitoli.
- `audit_formula_contracts.py --strict`: `68/68` formule o schemi previsti presenti, delimitati e accompagnati da una spiegazione.
- `audit_code_alignment.py --strict`: `80/80` capitoli generati con policy `reference` hanno blocchi Python e output inline contenuti negli artefatti eseguiti e versionati.
- `run_all_examples.py --include-appendix-a`: `541` test in `114` file senza failure; l'appendice B aggiunge `3` test JAX in ambiente CPU, per `544` test in `115` file.
- `ruff check` sui blocchi Python dei capitoli e sugli script di audit: nessun errore.

## Gate ancora aperti

- lettura autoriale integrale e prova ad alta voce;
- approvazione delle coppie testo-visuale nel layout editoriale;
- ricontrollo temporale delle fonti sensibili alla data di pubblicazione;
- congelamento, promozione degli asset approvati a `final.png` ed eventuale release.
