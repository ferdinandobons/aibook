# Capitolo 28. Il meccanismo di attention

## Metadati

- `chapter_id`: `CH-P06-ATTENTION`
- Parte: `P06`, Sequenze, linguaggio e contesto
- Maturità: `CORE`
- Stato: **revisione autoriale del capitolo pilota**
- Versione candidata: `0.2.0-rc2`
- Data di apertura: 30 luglio 2026
- Data dell'ultima ricerca web: 30 luglio 2026
- Data dell'ultima verifica delle fonti: 30 luglio 2026
- Data di congelamento editoriale: non assegnata
- Documentazione PyTorch verificata: stable `2.13`
- Ambiente eseguito: Python `3.13.5`, PyTorch `2.10.0+cpu`
- Oggetto continuo: un vettore corrente e tre coppie di vettori sorgente, tutti di dimensione 2
- Concetti differiti: informazione posizionale, multi-head attention, varianti KV, KV cache e implementazioni hardware-aware

> **Stato della candidatura.** Il capitolo è stato riscritto dopo una review didattica completa e sottoposto a una seconda review integrale. Le figure `ATT-01/candidate-v2.png` e `ATT-02/candidate-v2.png` sono validate tecnicamente e attendono l'approvazione autoriale. Nessuna pagina del libro è stata rasterizzata.

## Bussola

- **Stato prima:** disponiamo di una sequenza di vettori, ma non di una regola che scelga contributi diversi in funzione della posizione corrente.
- **Problema:** produrre, per ogni posizione corrente, una combinazione dei vettori sorgente con coefficienti che dipendano da quella posizione.
- **Stato dopo:** sappiamo calcolare score, scaling, normalizzazione e somma pesata per una posizione e generalizzare il calcolo a più posizioni.
- **Invariante:** il numero di output coincide con il numero di vettori correnti; la dimensione di ogni output coincide con la dimensione dei vettori combinati.
- **Confine:** il meccanismo base non aggiunge informazione posizionale, memoria esterna o dati non presenti nei vettori sorgente.

## Obiettivo operativo

Al termine del capitolo il lettore può:

1. spiegare perché coefficienti fissi non bastano quando posizioni diverse richiedono combinazioni diverse;
2. distinguere i tre ruoli successivamente denominati query, key e value;
3. calcolare score, scaling, softmax e somma pesata in un esempio numerico;
4. ricostruire la formula matriciale e verificare le shape;
5. applicare una causal mask agli score;
6. implementare il caso base con operazioni PyTorch;
7. confrontare l'implementazione diretta con `torch.nn.functional.scaled_dot_product_attention`;
8. localizzare il passaggio successivo verso la multi-head attention senza anticiparne il meccanismo completo.

## Prerequisiti stabili

Il capitolo assume noti:

- vettori, matrici, prodotto scalare e prodotto matriciale;
- shape e trasposizione;
- proiezione lineare;
- softmax applicata a un vettore;
- embedding come sequenza di vettori.

# 1. Ancora: abbiamo vettori, ma non una selezione dipendente dalla posizione

## Stato del lettore

```text
Ultima affermazione stabile: una sequenza può essere rappresentata come una sequenza di vettori.
Oggetto corrente: tre vettori sorgente v1, v2 e v3.
Un concetto nuovo: una posizione corrente può richiedere coefficienti propri.
Concetti differiti: il calcolo dei coefficienti e i nomi tecnici dei tre ruoli.
Prova che il nuovo concetto è stabile: il lettore può confrontare coefficienti fissi e coefficienti diversi per due consumer.
```

Consideriamo tre vettori sorgente:

$$
v_1=[1,0],\qquad v_2=[0,1],\qquad v_3=[1,1].
$$

I valori sono **illustrativi**. Servono a rendere ogni passaggio verificabile a mano.

## Problema

Un unico vettore di contesto, costruito una volta e riutilizzato da tutti i consumer, assegna implicitamente la stessa combinazione della sorgente a richieste diverse. Se due posizioni correnti richiedono informazioni diverse, la combinazione deve poter cambiare.

Per esempio, il primo consumer può usare:

$$
c_1=0{,}10v_1+0{,}60v_2+0{,}30v_3,
$$

mentre il secondo può usare:

$$
c_2=0{,}05v_1+0{,}15v_2+0{,}80v_3.
$$

I vettori sorgente restano gli stessi. Cambiano soltanto i coefficienti usati per combinarli.

## Visuale `ATT-01`

**Domanda della figura:** perché la combinazione deve dipendere dalla posizione corrente?

![Confronto tra contesto fisso e coefficienti dipendenti dalla posizione corrente](../../assets/chapters/28_attention/ATT-01/candidate-v2.png)

Nel pannello sinistro, `v1`, `v2` e `v3` confluiscono in un unico vettore `c`. Lo stesso `c` viene consegnato a entrambi i consumer.

Nel pannello destro, la sequenza sorgente non cambia. Il primo vettore corrente produce la prima riga di coefficienti, il secondo produce la seconda riga. Le due righe generano `c1` e `c2`, che sono combinazioni diverse degli stessi tre vettori.

**Conclusione della figura:** serve una regola che riceva il vettore corrente e produca un coefficiente per ogni vettore sorgente. Ora dobbiamo costruire quella regola.

## Cosa è cambiato

Abbiamo introdotto la possibilità di usare coefficienti diversi per posizioni correnti diverse.

## Cosa è rimasto invariato

I vettori `v1`, `v2` e `v3` non sono stati modificati.

## Cosa non fa ancora questo passaggio

Non calcola i coefficienti. Stabilisce soltanto il requisito che dovranno soddisfare.

## Frase di continuità

Ora che sappiamo quale comportamento manca, possiamo separare il vettore corrente, i vettori usati per il confronto e i vettori da combinare.

# 2. Tre ruoli distinti nello stesso calcolo

## Dove siamo

Disponiamo di un vettore corrente e di tre coppie di vettori sorgente. Vogliamo produrre tre coefficienti dipendenti dal vettore corrente.

## Descrizione prima dei nomi

Il calcolo usa tre ruoli:

1. un vettore che rappresenta la posizione corrente;
2. un vettore di confronto per ogni posizione sorgente;
3. un vettore da trasportare per ogni posizione sorgente.

Chiamiamo questi ruoli:

- **query**, il vettore corrente;
- **key**, ciascun vettore usato nel confronto;
- **value**, ciascun vettore che verrà combinato.

Nel nostro esempio:

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

## Input e shape

- `q`: `[d_k]=[2]`
- `K`: `[S,d_k]=[3,2]`
- `V`: `[S,d_v]=[3,2]`

`S=3` è il numero di coppie key-value. In questo esempio `d_k=d_v=2`, ma il calcolo generale non richiede che le due dimensioni coincidano.

## Invariante

La riga `j` di `K` e la riga `j` di `V` appartengono alla stessa posizione sorgente. Cambiare l'ordine di una matrice senza applicare la stessa permutazione all'altra romperebbe la corrispondenza.

## Confine

I tre nomi descrivono ruoli nel calcolo. Non stabiliscono ancora come ottenere i coefficienti.

## Frase di continuità

Ora che i ruoli sono distinti, la query può essere confrontata con ogni key per produrre un numero per posizione sorgente.

# 3. Prima transizione: una query produce uno score per ogni key

## Stato del lettore

```text
Ultima affermazione stabile: query, key e value hanno ruoli distinti.
Oggetto corrente: q, K e V con shape note.
Un concetto nuovo: prodotto scalare tra q e ogni riga di K.
Concetti differiti: scaling, softmax e uso di V.
Prova che il nuovo concetto è stabile: il lettore calcola i tre score e ne indica la shape.
```

## Problema locale

Servono tre numeri, uno per ogni key, che dipendano dalla query corrente.

## Trasformazione

Calcoliamo tre prodotti scalari:

$$
[1,0]\cdot[1,0]=1,
$$

$$
[1,0]\cdot[0,1]=0,
$$

$$
[1,0]\cdot[1,1]=1.
$$

Lo stato accumulato è:

```text
q, K, V
score grezzi = [1, 0, 1]
```

## Output e shape

Il vettore degli score ha shape `[S]=[3]`.

## Cosa è cambiato

Ogni key è stata ridotta a un numero relativo alla query corrente.

## Cosa è rimasto invariato

`V` non è stato ancora usato. Il numero di posizioni sorgente resta `S=3`.

## Cosa non fa

Gli score non sono coefficienti normalizzati. Possono essere negativi e non devono sommare a 1.

## Errore comune

Gli score non sono i pesi finali. Sono valori intermedi prima della normalizzazione.

## Frase di continuità

Ora che abbiamo uno score per ogni key, dobbiamo controllarne la scala prima di normalizzarlo.

# 4. Seconda transizione: ridimensionare gli score

## Dove siamo

Lo stato corrente contiene `q`, `K`, `V` e gli score grezzi `[1,0,1]`.

## Problema locale

Al crescere di `d_k`, la magnitudine dei prodotti scalari può crescere. Il Transformer originale divide gli score per `sqrt(d_k)` prima della softmax [Vaswani et al., 2017, §3.2.1].

## Trasformazione nell'esempio

Con `d_k=2`:

$$
\sqrt{d_k}=\sqrt{2}\approx1{,}4142.
$$

Dividiamo ogni score:

$$
[1,0,1]/1{,}4142=[0{,}7071,0,0{,}7071].
$$

Lo stato accumulato è:

```text
q, K, V
score grezzi = [1, 0, 1]
score scalati = [0,7071, 0, 0,7071]
```

## Output e shape

Gli score scalati mantengono shape `[S]=[3]`.

## Cosa è cambiato

È cambiata la magnitudine dei tre score.

## Cosa è rimasto invariato

L'ordine relativo degli score e la loro shape non cambiano. `V` non è ancora stato usato.

## Derivazione sotto ipotesi esplicite

Supponiamo, soltanto per questa derivazione, che le componenti di due vettori di confronto siano indipendenti, con media 0 e varianza 1. Il prodotto scalare è una somma di `d_k` prodotti. Sotto queste ipotesi, la varianza della somma cresce come `d_k`; la divisione per `sqrt(d_k)` la riporta a ordine unitario.

Questa derivazione descrive un caso idealizzato. Non afferma che le componenti apprese in un modello reale siano indipendenti o standardizzate.

## Confine

Lo scaling non normalizza gli score e non produce ancora coefficienti che sommano a 1.

## Frase di continuità

Ora che gli score sono stati ridimensionati, la softmax può trasformarli in coefficienti confrontabili sulla stessa riga.

# 5. Terza transizione: dagli score scalati ai coefficienti

## Input

Gli score scalati sono:

$$
[0{,}7071,0,0{,}7071].
$$

## Trasformazione

Applichiamo la softmax lungo le tre posizioni sorgente. Otteniamo, con arrotondamento a tre decimali:

$$
[0{,}401,0{,}198,0{,}401].
$$

Lo stato accumulato è:

```text
q, K, V
score grezzi
score scalati
coefficienti = [0,401, 0,198, 0,401]
```

## Output e shape

Il vettore dei coefficienti mantiene shape `[S]=[3]`.

## Cosa è cambiato

Gli score sono diventati coefficienti non negativi. La loro somma è 1, se almeno uno score della riga è finito e non viene applicato dropout dopo la softmax.

## Cosa è rimasto invariato

Ogni coefficiente continua a corrispondere alla stessa riga di `K` e `V`.

## Cosa non fa

La softmax non combina le value. Produce soltanto i coefficienti che verranno usati nel passaggio successivo.

## Errore comune

Applicare la softmax sulla dimensione sbagliata cambia il contratto. Per una query, la normalizzazione deve avvenire lungo le key consultabili.

## Frase di continuità

Ora che abbiamo un coefficiente per ogni posizione sorgente, possiamo usare per la prima volta le value.

# 6. Quarta transizione: combinare le value

## Dove siamo

Disponiamo di tre coefficienti e di tre value corrispondenti.

## Trasformazione

Moltiplichiamo ogni value per il proprio coefficiente e sommiamo:

$$
0{,}401[1,0]+0{,}198[0,1]+0{,}401[1,1].
$$

Il risultato è:

$$
o=[0{,}802,0{,}599].
$$

Lo stato accumulato completo è:

```text
q, K, V
score grezzi
score scalati
coefficienti normalizzati
output o = [0,802, 0,599]
```

## Output e shape

L'output ha shape `[d_v]=[2]`.

## Cosa è cambiato

È stato creato un nuovo vettore che combina le tre value.

## Cosa è rimasto invariato

Le righe originali di `V` non vengono modificate. Il nuovo vettore è una combinazione aggiuntiva.

## Cosa non fa

L'operazione non aggiunge informazione esterna. L'output appartiene allo spazio generato dalle value disponibili.

## Visuale `ATT-02`

**Domanda della figura:** come viene prodotto l'output numerico per una query?

![Esempio numerico completo per una query](../../assets/chapters/28_attention/ATT-02/candidate-v2.png)

La figura si legge da sinistra a destra. Il primo pannello contiene `q`, `K` e `V`. Il secondo calcola i tre prodotti scalari. Il terzo divide gli score per `sqrt(d_k)`. Il quarto applica la softmax e verifica che i coefficienti sommino a 1. Il quinto combina le value. Il sesto mostra l'output e la sua shape.

**Conclusione della figura:** la query non viene sommata alle value. La query determina i coefficienti tramite il confronto con le key; i coefficienti combinano le value.

## Frase di continuità

Ora che l'intera trasformazione è osservabile su numeri concreti, possiamo esprimerne l'algoritmo senza dipendere dalla notazione matematica compatta.

# 7. Pseudocodice del caso base

Il seguente blocco è pseudocodice, non Python eseguibile.

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

## Invariante algoritmico

Il numero dei coefficienti coincide con il numero di coppie sorgente. La dimensione dell'output coincide con `d_v`.

## Frase di continuità

Ora che l'algoritmo è stabile, possiamo assegnare un nome alla trasformazione e scriverla in forma matriciale.

# 8. Nome tecnico e contratto matematico

La trasformazione completa appena eseguita si chiama **scaled dot-product attention**.

Per una query:

$$
\mathrm{Attention}(q,K,V)=
\mathrm{softmax}\left(\frac{qK^T}{\sqrt{d_k}}\right)V.
$$

Per più query, raccogliamo i vettori correnti nelle righe di `Q`:

- `Q\in\mathbb{R}^{L\times d_k}`;
- `K\in\mathbb{R}^{S\times d_k}`;
- `V\in\mathbb{R}^{S\times d_v}`.

La forma matriciale è:

$$
\mathrm{Attention}(Q,K,V)=
\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V.
$$

La softmax viene applicata per riga. Ogni riga dell'output appartiene a una query [Vaswani et al., 2017, §3.2.1].

## Contratto delle shape

| Oggetto | Shape | Ruolo |
|---|---:|---|
| `Q` | `[L,d_k]` | una riga per query |
| `K` | `[S,d_k]` | una riga per key |
| `V` | `[S,d_v]` | una riga per value |
| `QK^T` | `[L,S]` | uno score per coppia query-key |
| `A` | `[L,S]` | coefficienti normalizzati per query |
| `O=AV` | `[L,d_v]` | una riga di output per query |

## Cosa cambia passando da una query a più query

Il calcolo viene ripetuto per `L` righe in parallelo. Ogni riga di `A` contiene i coefficienti di una query.

## Cosa resta invariato

Il numero di righe di `K` deve coincidere con il numero di righe di `V`. La dimensione finale di ogni output resta `d_v`.

## Confine

La formula non stabilisce da quali sequenze provengano `Q`, `K` e `V`. Questa distinzione viene introdotta ora, dopo la stabilizzazione dell'operatore.

# 9. Provenienza di `Q`, `K` e `V`

## Self-attention

`Q`, `K` e `V` derivano dalla stessa sequenza di input tramite proiezioni apprese. Le proiezioni possono produrre valori diversi anche quando la sequenza sorgente è la stessa.

## Cross-attention

Le query derivano da una sequenza, mentre key e value derivano da un'altra sorgente. Il contratto delle shape resta lo stesso, con `L` e `S` potenzialmente diversi.

## Causal self-attention

`Q`, `K` e `V` derivano dalla stessa sequenza, ma la query in posizione `i` non può usare key in posizioni future. Questo vincolo richiede una modifica agli score prima della softmax.

## Frase di continuità

Ora che il caso causale è localizzato, possiamo aggiungere un solo nuovo oggetto: una mask applicata alla matrice degli score.

# 10. Causal mask: modificare gli score ammessi

## Stato del lettore

```text
Ultima affermazione stabile: la formula produce una matrice di score [L,S].
Oggetto corrente: score scalati prima della softmax.
Un concetto nuovo: una mask additiva con la stessa shape degli score.
Concetti differiti: semantica delle mask nelle API.
Prova che il nuovo concetto è stabile: il lettore identifica celle ammesse e bloccate e spiega perché il peso futuro diventa zero.
```

## Problema locale

In generazione causale, una posizione non deve usare elementi futuri.

## Trasformazione

Introduciamo `M\in\mathbb{R}^{L\times S}` e calcoliamo:

$$
A=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right).
$$

Nel caso quadrato:

$$
M_{ij}=
\begin{cases}
0 & \text{se } j\le i,\\
-\infty & \text{se } j>i.
\end{cases}
$$

Una cella bloccata riceve un logit `-inf`. Dopo la softmax, il coefficiente corrispondente è 0.

## Cosa è cambiato

Alcuni score non possono più contribuire alla normalizzazione.

## Cosa è rimasto invariato

`L`, `S`, `d_k` e `d_v` non cambiano. La mask non modifica direttamente le righe di `V`.

## Errore comune

Applicare la mask a `V` cambia i dati trasportati e non implementa il vincolo causale sugli score.

## Frase di continuità

Ora che la mask è stabile come operazione matematica, possiamo verificare la stessa sequenza di operazioni in PyTorch.

# 11. Implementazione minima per una query

## Contratto dello snippet

- **Input noto:** `q`, `K` e `V` dell'esempio numerico.
- **Operazione centrale:** prodotto tra `q` e `K^T`, divisione per `sqrt(d_k)`, softmax e prodotto con `V`.
- **Output da osservare:** coefficienti che sommano a 1 e output `[0.8022,0.5989]`.
- **Invariante:** shape degli score `[3]`, shape dell'output `[2]`.

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

File eseguito: [`code/snip_att_001_single_query.py`](code/snip_att_001_single_query.py).

Output registrato: [`code/outputs/SNIP-ATT-001.txt`](code/outputs/SNIP-ATT-001.txt).

## Reintegrazione

Le quattro righe centrali corrispondono ai quattro passaggi già eseguiti a mano. Il codice non introduce un secondo algoritmo.

# 12. Implementazione matriciale e confronto con l'API ufficiale

## Contratto dello snippet

- **Input noto:** batch e head esplicite con `Q`, `K` e `V` di shape `[B,H,L,d]`.
- **Operazione centrale:** stessa formula matriciale del caso base.
- **Output da osservare:** equivalenza numerica con `F.scaled_dot_product_attention` quando `dropout_p=0.0`.
- **Invariante:** output `[B,H,L,d_v]`.

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

Il confronto è stato eseguito con PyTorch `2.10.0+cpu`. La firma e la semantica correnti dell'API sono state ricontrollate nella documentazione stable `2.13`. Non viene dichiarata un'esecuzione locale sotto `2.13`.

File eseguito: [`code/snip_att_002_matrix_api.py`](code/snip_att_002_matrix_api.py).

## Nota separata sul dropout

`F.scaled_dot_product_attention` applica dropout quando `dropout_p>0`, indipendentemente dallo stato di training di un modulo chiamante. Nel caso base passiamo esplicitamente `dropout_p=0.0` [PyTorch 2.13 Docs, `scaled_dot_product_attention`].

## Confine

L'API può selezionare backend differenti. Il capitolo non misura kernel o prestazioni hardware.

# 13. Causal mask nell'API PyTorch

## Contratto dello snippet

- **Input noto:** la matrice di score quadrata del caso causale.
- **Operazione centrale:** una mask booleana triangolare inferiore.
- **Output da osservare:** coefficienti futuri uguali a zero.
- **Invariante:** shape dell'output invariata.

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

Nel file eseguito, l'output viene confrontato con un'implementazione diretta che inserisce `-inf` negli score non ammessi.

File: [`code/snip_att_003_causal_mask.py`](code/snip_att_003_causal_mask.py).

## Semantica booleana, dopo il caso matematico

In `F.scaled_dot_product_attention`, `True` indica una posizione che partecipa all'attention. In `MultiheadAttention.key_padding_mask`, `True` indica invece una posizione da ignorare. Le due convenzioni appartengono ad API diverse e non devono essere scambiate [PyTorch 2.13 Docs].

# 14. Complessità del caso materializzato

Per `Q[L,d_k]`, `K[S,d_k]` e `V[S,d_v]`:

1. `QK^T` richiede ordine `O(LSd_k)` operazioni;
2. `AV` richiede ordine `O(LSd_v)` operazioni;
3. una realizzazione che conserva score o coefficienti materializza un intermedio `[L,S]`.

Con self-attention e `L=S=n`, questo intermedio ha `n^2` elementi.

## Confine hardware-aware

Altre implementazioni possono calcolare lo stesso operatore con strategie differenti di accesso alla memoria e ricomputazione. Il loro meccanismo viene trattato nella Parte `P12`, non in questo capitolo base.

# 15. Proprietà stabilizzate e confini

## Proprietà stabilizzate

- ogni riga di `QK^T` appartiene a una query;
- ogni colonna appartiene a una key;
- la softmax viene applicata lungo le key;
- senza dropout, ogni riga valida dei coefficienti è non negativa e somma a 1;
- ogni riga di output è una combinazione delle righe di `V`;
- il numero delle righe di output è `L`;
- la dimensione finale di ogni riga è `d_v`.

## Cosa non fa il meccanismo base

- non inserisce da solo informazione posizionale;
- non modifica l'ordine delle righe;
- non introduce dati esterni;
- non decide la correttezza del contenuto;
- non elimina automaticamente il costo quadratico degli score nel caso `L=S=n`;
- non definisce l'intero blocco Transformer.

## Posizione e permutazioni

Se `Q`, `K` e `V` vengono permutati in modo coerente e non contengono segnali posizionali, l'output segue la stessa permutazione. Per distinguere l'ordine, il sistema deve inserire informazione posizionale nei dati o nel calcolo.

# 16. Errori comuni

1. **Applicare la softmax sulla dimensione sbagliata.** Per ogni query, la normalizzazione avviene lungo le key.
2. **Usare `KQ^T` al posto di `QK^T`.** Le righe non rappresenterebbero più le query nel contratto adottato.
3. **Applicare la mask a `V`.** La mask modifica gli score o un bias sommato agli score.
4. **Confondere mask booleane tra API diverse.** Il significato di `True` dipende dal contratto dell'API.
5. **Omettere `sqrt(d_k)`.** Si ottiene dot-product attention non scalata.
6. **Chiamare pesi gli score.** I coefficienti normalizzati compaiono soltanto dopo la softmax.
7. **Assumere che i coefficienti dopo dropout sommino a 1.** Il dropout viene applicato dopo la softmax nell'API descritta.

# 17. Ponte verso la multi-head attention

Il caso base usa un singolo insieme di proiezioni per costruire `Q`, `K` e `V`. Il capitolo successivo introdurrà più insiemi di proiezioni, eseguirà il meccanismo in parallelo e ricomporrà gli output.

Questa è una nuova struttura, non un dettaglio necessario per calcolare il caso base. Formula completa, concatenazione, proiezione finale e shape per head restano quindi differite.

## Frase di continuità

Ora che una singola trasformazione produce rappresentazioni dipendenti dal contesto, il componente successivo può ripeterla su proiezioni separate e combinare i risultati nel blocco Transformer.

# 18. Ricostruzione completa

Partiamo da un vettore corrente e da `S` coppie sorgente.

1. assegniamo i ruoli query, key e value;
2. confrontiamo la query con ogni key;
3. dividiamo gli score per `sqrt(d_k)`;
4. aggiungiamo una mask, se il vincolo la richiede;
5. applichiamo la softmax lungo le key;
6. usiamo i coefficienti per combinare le value;
7. ripetiamo il calcolo per `L` query e otteniamo `O[L,d_v]`.

Lo stesso ordine compare nell'esempio numerico, nel pseudocodice, nella formula, negli snippet e nelle visuali.

# 19. Controlli di comprensione

## Ricostruzione

Ricostruire l'ordine esatto di confronto, scaling, mask, softmax e combinazione delle value.

## Localizzazione

Indicare quale operazione usa `V` per la prima volta.

## Confine

Spiegare perché una causal mask viene applicata agli score e non direttamente alle righe di `V`.

## Trasferimento

Sostituire `q=[1,0]` con `q=[0,1]`. Prevedere gli score prima di calcolare la softmax.

## Variazione

Prevedere la shape dell'output con `L=5`, `S=7`, `d_k=64` e `d_v=32`.

# 20. Esercizi

1. Calcolare a mano i coefficienti e l'output per `q=[0,1]` usando le stesse `K` e `V`.
2. Modificare `SNIP-ATT-002` usando `d_v=3` e verificare la nuova shape dell'output.
3. Sostituire la causal mask booleana con una mask additiva contenente `0` e `-inf`.
4. Creare un caso in cui tutte le key producano lo stesso score e spiegare il risultato della softmax.
5. Verificare con un test che una permutazione coerente di query, key e value permuti coerentemente l'output in assenza di posizione.

# 21. Fonti primarie

Le schede complete, le sezioni consultate e i limiti sono in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md).

- Vaswani et al., *Attention Is All You Need*, NeurIPS 2017.
- Bahdanau, Cho e Bengio, *Neural Machine Translation by Jointly Learning to Align and Translate*, ICLR 2015.

# 22. Documentazione ufficiale

- PyTorch stable `2.13`, `torch.nn.functional.scaled_dot_product_attention`.
- PyTorch stable `2.13`, `torch.nn.MultiheadAttention`.

# 23. Artefatti di riproduzione

- ambiente: [`code/environments/python-pytorch.txt`](code/environments/python-pytorch.txt);
- test: [`code/test_attention_snippets.py`](code/test_attention_snippets.py);
- output: [`code/outputs/`](code/outputs/);
- audit codice: [`code/CODE_AUDIT.md`](code/CODE_AUDIT.md);
- audit testo e didattica: [`TEXT_AUDIT.md`](TEXT_AUDIT.md);
- claim: [`CLAIMS.md`](CLAIMS.md);
- visuale `ATT-01`: [`candidate-v2.png`](../../assets/chapters/28_attention/ATT-01/candidate-v2.png);
- visuale `ATT-02`: [`candidate-v2.png`](../../assets/chapters/28_attention/ATT-02/candidate-v2.png).

# 24. Registro finale di approvazione

- Review fattuale: completata per `0.2.0-rc2`
- Review matematica: completata per `0.2.0-rc2`
- Review codice: tre test locali superati
- Review visuale: `ATT-01` e `ATT-02` validate tecnicamente; approvazione autoriale aperta
- Review didattica 1: completata, capitolo respinto e corretto
- Review didattica 2: completata, nessun difetto bloccante residuo
- Review autoriale: **aperta**
- Commit congelato: non assegnato
