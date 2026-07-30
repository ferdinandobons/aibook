# Capitolo 28. Il meccanismo di attention

## Metadati

- `chapter_id`: `CH-P06-ATTENTION`
- Parte: `P06`, Sequenze, linguaggio e contesto
- Maturità: `CORE`
- Stato: **revisione autoriale del capitolo pilota**
- Versione candidata: `0.3.0-rc3`
- Data di apertura: 30 luglio 2026
- Data dell'ultima ricerca web: 30 luglio 2026
- Data dell'ultima verifica delle fonti: 30 luglio 2026
- Data di congelamento editoriale: non assegnata
- Documentazione PyTorch verificata: stable `2.13`
- Ambiente eseguito: Python `3.13.5`, PyTorch `2.10.0+cpu`
- Oggetto continuo: un vettore corrente e tre coppie di vettori sorgente, tutti di dimensione 2
- Concetti differiti: informazione posizionale, multi-head attention, varianti KV, KV cache e implementazioni hardware-aware

> **Stato della candidatura.** Questa versione conserva la logica verificata nelle review precedenti, ma la presenta come prosa tecnica continua. Lo scaffold didattico resta nei file di piano e audit. Le figure `ATT-01/candidate-v2.png` e `ATT-02/candidate-v2.png` sono validate tecnicamente e attendono l'approvazione autoriale. Nessuna pagina del libro è stata rasterizzata.

## In questo capitolo

Partiamo da una sequenza già rappresentata come vettori. Il problema è che una combinazione fissa della sorgente non può adattarsi a posizioni correnti che richiedono informazioni diverse. Costruiremo quindi, su un unico esempio numerico, una regola che confronta un vettore corrente con più vettori sorgente, trasforma i risultati in coefficienti e usa quei coefficienti per produrre un nuovo vettore.

Alla fine del percorso sapremo calcolare il caso base, generalizzarlo in forma matriciale, applicare una causal mask e collegarlo a una implementazione PyTorch verificata. L'informazione posizionale, la multi-head attention, le varianti della KV cache e le implementazioni hardware-aware restano fuori dal meccanismo portante di questo capitolo.

Il testo assume noti vettori, matrici, prodotto scalare, prodotto matriciale, shape, trasposizione, proiezioni lineari, softmax ed embedding.

# 1. Perché una combinazione fissa non basta

Consideriamo tre vettori sorgente:

$$
v_1=[1,0],\qquad v_2=[0,1],\qquad v_3=[1,1].
$$

I valori sono **illustrativi** e sono stati scelti per rendere ogni passaggio verificabile a mano.

Se la sorgente viene riassunta una sola volta in un vettore `c`, tutti i consumer ricevono la stessa combinazione. Questa scelta diventa un limite quando due posizioni correnti richiedono contributi diversi. Il primo consumer potrebbe aver bisogno di

$$
c_1=0{,}10v_1+0{,}60v_2+0{,}30v_3,
$$

mentre il secondo potrebbe richiedere

$$
c_2=0{,}05v_1+0{,}15v_2+0{,}80v_3.
$$

La sorgente non è cambiata. Sono cambiati soltanto i coefficienti con cui viene combinata.

La figura seguente mette a confronto le due configurazioni.

![Confronto tra contesto fisso e coefficienti dipendenti dalla posizione corrente](../../assets/chapters/28_attention/ATT-01/candidate-v2.png)

Nel pannello sinistro, `v1`, `v2` e `v3` confluiscono in un unico vettore `c`, poi riutilizzato da entrambi i consumer. Nel pannello destro, gli stessi tre vettori restano disponibili, ma due vettori correnti distinti producono due righe di coefficienti e quindi due combinazioni differenti. La figura non mostra ancora come calcolare quei coefficienti. Stabilisce il requisito che il calcolo dovrà soddisfare.

Serve dunque una regola che riceva il vettore corrente e restituisca un numero per ogni posizione sorgente. Per costruirla dobbiamo separare tre ruoli che finora erano mescolati.

# 2. I tre ruoli del calcolo

Il primo ruolo appartiene al vettore della posizione corrente. Il secondo appartiene ai vettori con cui quel vettore viene confrontato. Il terzo appartiene ai vettori che verranno effettivamente combinati nell'output.

Chiamiamo questi oggetti:

- **query**, il vettore corrente;
- **key**, ogni vettore usato nel confronto;
- **value**, ogni vettore che può contribuire all'output.

Nel nostro esempio usiamo

$$
q=[1,0],
$$

$$
K=
\begin{bmatrix}
1&0\\
0&1\\
1&1
\end{bmatrix},
\qquad
V=
\begin{bmatrix}
1&0\\
0&1\\
1&1
\end{bmatrix}.
$$

La query ha shape `[d_k]=[2]`. Le matrici `K` e `V` hanno rispettivamente shape `[S,d_k]=[3,2]` e `[S,d_v]=[3,2]`, dove `S=3` è il numero di posizioni sorgente.

In questo esempio `d_k` e `d_v` coincidono, ma non è un requisito generale. La corrispondenza necessaria è tra le righe: la riga `j` di `K` e la riga `j` di `V` appartengono alla stessa posizione sorgente. Una permutazione applicata soltanto a una delle due matrici romperebbe questa corrispondenza.

Ora possiamo usare la query per produrre un valore relativo a ciascuna key. Le value restano disponibili, ma non vengono ancora lette dal calcolo.

# 3. Dal confronto agli score

Calcoliamo il prodotto scalare tra `q` e ogni riga di `K`:

$$
[1,0]\cdot[1,0]=1,
$$

$$
[1,0]\cdot[0,1]=0,
$$

$$
[1,0]\cdot[1,1]=1.
$$

Otteniamo quindi

$$
qK^T=[1,0,1].
$$

Il vettore risultante ha shape `[S]=[3]`: esiste uno score per ogni key. Ogni numero dipende dalla query corrente e dalla key corrispondente. `V` non è ancora coinvolta, e il numero di posizioni sorgente resta invariato.

Questi score non sono ancora coefficienti di combinazione. Possono essere negativi e non devono sommare a 1. Prima della normalizzazione, il Transformer originale ne controlla la scala.

# 4. Perché dividiamo per `sqrt(d_k)`

Con `d_k=2`, dividiamo i tre score per `sqrt(2)`:

$$
\sqrt{d_k}=\sqrt{2}\approx1{,}4142,
$$

$$
[1,0,1]/1{,}4142=[0{,}7071,0,0{,}7071].
$$

La shape resta `[3]` e l'ordine relativo dei valori non cambia. Cambia soltanto la loro magnitudine prima della softmax.

Vaswani et al. introducono il fattore `1/sqrt(d_k)` perché prodotti scalari di grande magnitudine possono portare la softmax in regioni con gradienti molto piccoli [Vaswani et al., 2017, §3.2.1]. Una derivazione idealizzata rende visibile il ruolo del fattore. Se le componenti dei vettori sono indipendenti, con media 0 e varianza 1, il prodotto scalare contiene `d_k` termini e la varianza della somma cresce come `d_k`. La divisione per `sqrt(d_k)` riporta la varianza a ordine unitario.

Questa derivazione non descrive necessariamente la distribuzione delle componenti apprese in un modello reale. Spiega il comportamento del fattore di scala sotto le ipotesi dichiarate.

Gli score sono ora ridimensionati, ma non sono ancora normalizzati. Il passaggio successivo li trasforma in coefficienti confrontabili sulla stessa riga.

# 5. Dagli score ai coefficienti

Applichiamo la softmax lungo le tre posizioni sorgente:

$$
\alpha_j=\frac{e^{s_j}}{\sum_{m=1}^{S}e^{s_m}}.
$$

Con gli score dell'esempio otteniamo, arrotondando a tre decimali,

$$
\alpha=[0{,}401,0{,}198,0{,}401].
$$

Il vettore mantiene shape `[S]=[3]`. I tre valori sono non negativi e sommano a 1, a condizione che almeno uno score della riga sia finito e che non venga applicato dropout dopo la softmax. Ogni coefficiente continua a riferirsi alla stessa riga di `K` e `V`.

La softmax non combina ancora le value. Produce i coefficienti necessari a farlo. Confondere gli score con questi coefficienti è un errore frequente: gli score sono i logit prima della normalizzazione, mentre i coefficienti sono l'output della softmax.

# 6. Combinare le value

Usiamo ora, per la prima volta, le righe di `V`. Ogni value viene moltiplicata per il coefficiente associato alla stessa posizione sorgente:

$$
0{,}401[1,0]+0{,}198[0,1]+0{,}401[1,1].
$$

La somma produce

$$
o=[0{,}802,0{,}599].
$$

L'output ha shape `[d_v]=[2]`. Le righe originali di `V` non vengono modificate: il calcolo crea una combinazione aggiuntiva. Inoltre non introduce informazione esterna, perché l'output appartiene allo spazio generato dalle value disponibili.

La figura seguente ripercorre l'intero esempio numerico.

![Esempio numerico completo per una query](../../assets/chapters/28_attention/ATT-02/candidate-v2.png)

La lettura procede da sinistra a destra. Il primo pannello contiene `q`, `K` e `V`; il secondo calcola i prodotti scalari; il terzo applica il fattore di scala; il quarto normalizza i valori con la softmax; il quinto combina le value; il sesto mostra l'output e la sua shape. La query non viene sommata direttamente alle value. Determina i coefficienti attraverso il confronto con le key, e sono quei coefficienti a controllare la combinazione finale.

Il meccanismo è ora completo su numeri concreti. Prima di comprimere tutto in una formula, possiamo descriverne l'algoritmo senza dipendere dalla notazione matematica.

# 7. L'algoritmo prima della formula

Il blocco seguente è pseudocodice, non Python eseguibile.

```text
input:
    un vettore corrente
    S vettori di confronto
    S vettori da combinare

per ogni posizione sorgente j:
    calcola il prodotto scalare tra il vettore corrente e il vettore di confronto j

dividi tutti gli score per la radice della dimensione dei vettori di confronto
normalizza gli score con softmax lungo le S posizioni
moltiplica ogni vettore da combinare per il coefficiente corrispondente
somma i vettori pesati

output:
    un vettore con la stessa dimensione dei vettori combinati
```

Il numero dei coefficienti coincide con il numero di coppie sorgente. La dimensione dell'output coincide con `d_v`. Questi due vincoli non dipendono dalla libreria usata per l'implementazione.

# 8. La scaled dot-product attention in forma matriciale

La trasformazione appena costruita si chiama **scaled dot-product attention**.

Per una query:

$$
\mathrm{Attention}(q,K,V)=
\mathrm{softmax}\left(\frac{qK^T}{\sqrt{d_k}}\right)V.
$$

Per elaborare più query in parallelo, raccogliamo i vettori correnti nelle righe di una matrice `Q`:

- `Q\in\mathbb{R}^{L\times d_k}`;
- `K\in\mathbb{R}^{S\times d_k}`;
- `V\in\mathbb{R}^{S\times d_v}`.

La formula diventa

$$
\mathrm{Attention}(Q,K,V)=
\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V.
$$

La softmax viene applicata per riga. Ogni riga di `QK^T` appartiene a una query e ogni colonna a una key [Vaswani et al., 2017, §3.2.1].

| Oggetto | Shape | Ruolo |
|---|---:|---|
| `Q` | `[L,d_k]` | una riga per query |
| `K` | `[S,d_k]` | una riga per key |
| `V` | `[S,d_v]` | una riga per value |
| `QK^T` | `[L,S]` | uno score per coppia query-key |
| `A` | `[L,S]` | coefficienti normalizzati per query |
| `O=AV` | `[L,d_v]` | una riga di output per query |

Passare da una query a `L` query ripete lo stesso contratto su più righe. Il numero di righe di `K` deve continuare a coincidere con quello di `V`, mentre la dimensione finale di ogni output resta `d_v`.

La formula non impone che `Q`, `K` e `V` provengano dalla stessa sequenza. Questa provenienza distingue tre configurazioni importanti.

# 9. Self-attention, cross-attention e causalità

Nella **self-attention**, `Q`, `K` e `V` derivano dalla stessa sequenza tramite proiezioni apprese. Le tre proiezioni possono produrre valori differenti anche quando condividono l'input.

Nella **cross-attention**, le query derivano da una sequenza, mentre key e value derivano da un'altra sorgente. Il contratto delle shape resta invariato, ma `L` e `S` possono essere diversi.

Nella **causal self-attention**, i tre gruppi derivano dalla stessa sequenza, ma la query in posizione `i` non può usare key collocate in posizioni future. Il vincolo non modifica le value: interviene sugli score prima della softmax.

# 10. Escludere le posizioni future

Introduciamo una mask additiva `M\in\mathbb{R}^{L\times S}` e calcoliamo

$$
A=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right).
$$

Nel caso causale quadrato:

$$
M_{ij}=
\begin{cases}
0 & \text{se } j\le i,\\
-\infty & \text{se } j>i.
\end{cases}
$$

Una cella futura riceve quindi un logit `-inf`; dopo la softmax, il coefficiente corrispondente è 0. La mask cambia quali score partecipano alla normalizzazione, ma lascia invariati `L`, `S`, `d_k`, `d_v` e le righe di `V`.

Applicare la mask direttamente a `V` cambierebbe i dati trasportati e non rappresenterebbe lo stesso vincolo. La posizione corretta della mask è parte del contratto algoritmico.

# 11. Implementare l'esempio in PyTorch

Lo snippet seguente usa gli stessi `q`, `K` e `V` del calcolo manuale. Le tre righe centrali implementano scaling, softmax e combinazione delle value; le asserzioni controllano la somma dei coefficienti e le shape.

```python
from __future__ import annotations

import math
import torch

q = torch.tensor([1.0, 0.0], dtype=torch.float64)
k = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype=torch.float64)
v = torch.tensor([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]], dtype=torch.float64)

scores = (q @ k.transpose(0, 1)) / math.sqrt(q.numel())
weights = torch.softmax(scores, dim=-1)
output = weights @ v

assert scores.shape == (3,)
assert output.shape == (2,)
torch.testing.assert_close(weights.sum(), torch.tensor(1.0, dtype=weights.dtype))
```

Il file eseguito è [`code/snip_att_001_single_query.py`](code/snip_att_001_single_query.py), mentre l'output registrato è in [`code/outputs/SNIP-ATT-001.txt`](code/outputs/SNIP-ATT-001.txt). Il codice ripete l'algoritmo già costruito; non introduce una seconda spiegazione.

# 12. Dalla formula all'API ufficiale

Con batch e head esplicite usiamo le shape `[B,H,L,d_k]`, `[B,H,S,d_k]` e `[B,H,S,d_v]`. Il confronto seguente verifica che l'implementazione diretta coincida con `torch.nn.functional.scaled_dot_product_attention` nell'ambiente registrato quando `dropout_p=0.0`.

```python
import math
import torch
import torch.nn.functional as F

scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
weights = torch.softmax(scores, dim=-1)
output = weights @ v

api_output = F.scaled_dot_product_attention(q, k, v, dropout_p=0.0)
torch.testing.assert_close(output, api_output, rtol=1e-12, atol=1e-12)
```

Il confronto è stato eseguito con PyTorch `2.10.0+cpu`; la firma e la semantica correnti dell'API sono state ricontrollate nella documentazione stable `2.13`. Non viene dichiarata un'esecuzione locale sotto `2.13`.

Il file completo è [`code/snip_att_002_matrix_api.py`](code/snip_att_002_matrix_api.py).

L'API applica dropout quando `dropout_p>0`, indipendentemente dallo stato di training di un modulo chiamante. Nel caso base passiamo quindi `0.0` in modo esplicito [PyTorch 2.13 Docs, `scaled_dot_product_attention`]. L'operatore può inoltre selezionare backend differenti, ma questo capitolo non misura kernel o prestazioni hardware.

# 13. La causal mask nell'API PyTorch

Una mask booleana triangolare inferiore rappresenta le posizioni ammesse:

```python
allowed = torch.ones(3, 3, dtype=torch.bool).tril()
output = F.scaled_dot_product_attention(
    q,
    k,
    v,
    attn_mask=allowed,
    dropout_p=0.0,
)
```

Nel file [`code/snip_att_003_causal_mask.py`](code/snip_att_003_causal_mask.py), l'output dell'API viene confrontato con una implementazione diretta che inserisce `-inf` negli score non ammessi. Il test verifica che i coefficienti delle posizioni future siano nulli e che la shape dell'output non cambi.

Le convenzioni booleane non sono uniformi tra tutte le API PyTorch. In `F.scaled_dot_product_attention`, `True` indica una posizione che partecipa all'attention; in `MultiheadAttention.key_padding_mask`, `True` indica invece una posizione da ignorare [PyTorch 2.13 Docs]. Questa differenza appartiene al contratto delle API, non alla definizione matematica della causal mask.

# 14. Costo computazionale e limiti del caso base

Per `Q[L,d_k]`, `K[S,d_k]` e `V[S,d_v]`, il prodotto `QK^T` richiede ordine `O(LSd_k)` operazioni, mentre `AV` richiede ordine `O(LSd_v)`. Una realizzazione che conserva score o coefficienti materializza inoltre un intermedio di shape `[L,S]`.

Nel caso di self-attention con `L=S=n`, quell'intermedio contiene `n^2` elementi. Altre implementazioni possono calcolare lo stesso operatore con strategie differenti di accesso alla memoria e ricomputazione. Il relativo meccanismo hardware-aware appartiene alla Parte `P12` e resta fuori dalla spiegazione di base.

Il meccanismo stabilizzato in questo capitolo possiede alcuni confini importanti:

- non inserisce da solo informazione posizionale;
- non modifica l'ordine delle righe;
- non introduce dati esterni;
- non decide la correttezza del contenuto;
- non elimina automaticamente il costo quadratico degli score quando `L=S=n`;
- non definisce l'intero blocco Transformer.

Se `Q`, `K` e `V` vengono permutati in modo coerente e non contengono segnali posizionali, l'output segue la stessa permutazione. Per distinguere l'ordine, il sistema deve introdurre informazione posizionale nei dati o nel calcolo.

# 15. Errori comuni

1. **Applicare la softmax sulla dimensione sbagliata.** Per ogni query, la normalizzazione avviene lungo le key.
2. **Usare `KQ^T` al posto di `QK^T`.** Le righe non rappresenterebbero più le query nel contratto adottato.
3. **Applicare la mask a `V`.** La mask modifica gli score o un bias sommato agli score.
4. **Confondere mask booleane tra API diverse.** Il significato di `True` dipende dal contratto dell'API.
5. **Omettere `sqrt(d_k)`.** Si ottiene dot-product attention non scalata.
6. **Chiamare pesi gli score.** I coefficienti normalizzati compaiono soltanto dopo la softmax.
7. **Assumere che i coefficienti dopo dropout sommino a 1.** Nell'API descritta il dropout viene applicato dopo la softmax.

# 16. Dove si innesta la multi-head attention

Il caso base usa un singolo insieme di proiezioni per costruire `Q`, `K` e `V`. Il capitolo successivo introdurrà più insiemi di proiezioni, eseguirà lo stesso meccanismo in parallelo e ricomporrà gli output.

Formula completa, concatenazione, proiezione finale e shape per head restano differite perché costituiscono una nuova struttura. Il risultato di questo capitolo è il componente che quella struttura ripeterà.

# 17. Ricostruzione del percorso

Partiamo da un vettore corrente e da `S` coppie sorgente. Assegniamo i ruoli query, key e value, confrontiamo la query con ogni key, dividiamo gli score per `sqrt(d_k)`, aggiungiamo una mask quando il vincolo lo richiede, applichiamo la softmax lungo le key e usiamo i coefficienti per combinare le value. Ripetendo lo stesso calcolo per `L` query otteniamo un output di shape `[L,d_v]`.

Lo stesso ordine compare nell'esempio numerico, nel pseudocodice, nella formula, nelle visuali e negli snippet.

## Controlli di comprensione

### Ricostruzione

Ricostruire l'ordine esatto di confronto, scaling, mask, softmax e combinazione delle value.

### Localizzazione

Indicare quale operazione usa `V` per la prima volta.

### Confine

Spiegare perché una causal mask viene applicata agli score e non direttamente alle righe di `V`.

### Trasferimento

Sostituire `q=[1,0]` con `q=[0,1]` e prevedere gli score prima di calcolare la softmax.

### Variazione

Prevedere la shape dell'output con `L=5`, `S=7`, `d_k=64` e `d_v=32`.

# 18. Esercizi

1. Calcolare a mano i coefficienti e l'output per `q=[0,1]` usando le stesse `K` e `V`.
2. Modificare `SNIP-ATT-002` usando `d_v=3` e verificare la nuova shape dell'output.
3. Sostituire la causal mask booleana con una mask additiva contenente `0` e `-inf`.
4. Creare un caso in cui tutte le key producano lo stesso score e spiegare il risultato della softmax.
5. Verificare con un test che una permutazione coerente di query, key e value permuti coerentemente l'output in assenza di posizione.

# 19. Fonti primarie

Le schede complete, le sezioni consultate e i limiti d'uso sono in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md).

- Vaswani et al., *Attention Is All You Need*, NeurIPS 2017.
- Bahdanau, Cho e Bengio, *Neural Machine Translation by Jointly Learning to Align and Translate*, ICLR 2015 / arXiv.
- Luong, Pham e Manning, *Effective Approaches to Attention-based Neural Machine Translation*, EMNLP 2015.

# 20. Documentazione ufficiale

- PyTorch stable `2.13`, `torch.nn.functional.scaled_dot_product_attention`.
- PyTorch stable `2.13`, `torch.nn.MultiheadAttention`.
- PyTorch stable `2.13`, `torch.nn.attention`.

# 21. Artefatti di riproduzione

- ambiente: [`code/environments/python-pytorch.txt`](code/environments/python-pytorch.txt);
- test: [`code/test_attention_snippets.py`](code/test_attention_snippets.py);
- output: [`code/outputs/`](code/outputs/);
- audit codice: [`code/CODE_AUDIT.md`](code/CODE_AUDIT.md);
- audit testo: [`TEXT_AUDIT.md`](TEXT_AUDIT.md);
- claim: [`CLAIMS.md`](CLAIMS.md);
- visuale `ATT-01`: [`candidate-v2.png`](../../assets/chapters/28_attention/ATT-01/candidate-v2.png);
- visuale `ATT-02`: [`candidate-v2.png`](../../assets/chapters/28_attention/ATT-02/candidate-v2.png).

# 22. Registro di approvazione

- Review fattuale: completata per la candidatura `0.3.0-rc3`
- Review matematica: completata per la candidatura `0.3.0-rc3`
- Review codice: test registrati superati; codice invariato rispetto alla candidatura precedente
- Review visuale: `ATT-01` e `ATT-02` validate tecnicamente; approvazione autoriale aperta
- Review didattica: riscrittura in prosa completata; nuova review integrale registrata in `TEXT_AUDIT.md`
- Review anti-template: completata internamente; revisione autoriale aperta
- Review autoriale: **aperta**
- Commit congelato: non assegnato