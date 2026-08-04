<!--
chapter_id: CH-P10-SPATIAL-3D
part_id: P10
order_key: 610
title: 3D, spazio e rappresentazione delle scene
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 61. 3D, spazio e rappresentazione delle scene

Il percorso di 3d, spazio e rappresentazione delle scene attraversa «Coordinate e camera» e «Generazione e grounding spaziale» senza attribuire al solo modello ciò che dipende dal sistema. L'oggetto osservato è punti e coordinate che descrivono una scena 3D. Il contratto locale dichiara input, punti, camera, raggi e profondità; operazione, proiezione, rendering, splatting o ricostruzione; output, immagine, campo radiance o geometria. Il caso di partenza è Tre punti 3D producono un centroide con tre coordinate. Il limite da non nascondere è: una vista proiettata non determina da sola la scena completa.

## Coordinate e camera

Una scena 3D richiede sistemi di riferimento, intrinseci ed estrinseci della camera. Errori di coordinate cambiano il rendering. [SRC-61-001]

La proiezione non ricostruisce da sola la geometria completa.

**Caso da seguire.** Tre punti 3D producono un centroide con tre coordinate.

**Controllo.** Per «Coordinate e camera», registra richiesta, decisione, stato e output finale. Nel caso «Coordinate e camera», un esito plausibile non deve nascondere il componente che lo ha prodotto.


## NeRF

Una funzione neurale mappa posizione e direzione a densità e colore. Volume rendering integra campioni lungo i raggi. [SRC-61-002]

**Caso da seguire.** Due punti proiettati con camera e profondità dichiarate.

**Controllo.** Ripeti «NeRF» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


La relazione seguente è una mappa operativa e non una misura del sistema.

**Schema concettuale.** `scene = project(points, camera)`

La proiezione non ricostruisce da sola la geometria completa. [SRC-61-001]


![3D, spazio e rappresentazione delle scene: architecture](../../assets/chapters/61_spatial_3d/3D-01/candidate-v48.png)

La prima figura segue il percorso da «Coordinate e camera» a «Gaussian splatting».


## Gaussian splatting

Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da punti di vista nuovi. [SRC-61-003]

**Caso da seguire.** Un caso in cui una vista proiettata non determina da sola la scena completa.

**Controllo.** Per «Gaussian splatting», separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Mesh, point cloud e voxel

Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering. [SRC-61-004]

**Caso da seguire.** Due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito.

**Controllo.** Per «Mesh, point cloud e voxel», introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Generazione e grounding spaziale

Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate. [SRC-61-001]

**Caso da seguire.** Per «Generazione e grounding spaziale» si mantiene l'input del capitolo e si isola questa condizione: Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate.

**Controllo.** Per «Generazione e grounding spaziale», confronta il comportamento completo, non soltanto l'ultimo messaggio. Nel caso «Generazione e grounding spaziale», il risultato resta limitato da: Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate.


![3D, spazio e rappresentazione delle scene: scatter](../../assets/chapters/61_spatial_3d/3D-02/candidate-v48.png)

La seconda figura mette a confronto «Mesh, point cloud e voxel» e il limite discusso in «Generazione e grounding spaziale».


## Esempio Python eseguito

Il caso computazionale di 3d, spazio e rappresentazione delle scene è riportato senza trasformazioni: il file e l'output sono quelli verificati. Per «3D, spazio e rappresentazione delle scene», il caso di default usa valori piccoli per isolare il meccanismo. La suite conserva inoltre una failure esplicita per separare il contratto osservato da «3d, spazio e rappresentazione delle scene».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    points = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
    centroid = [sum(point[index] for point in points) / len(points) for index in range(3)]
    return {"count": len(points), "centroid": centroid, "invariant": "a 3D representation preserves coordinate dimension"}
```

Esecuzione con `python snip_61_contract.py`:

```text
{"centroid": [0.3333333333333333, 0.3333333333333333, 0.0], "count": 3, "invariant": "a 3D representation preserves coordinate dimension"}
```

Il test associato è [`code/test_61_contract.py`](code/test_61_contract.py); l'output versionato è [`code/outputs/SNIP-61-001.txt`](code/outputs/SNIP-61-001.txt).


## Come si collegano i passaggi

- **Da «Coordinate e camera» a «NeRF».** Una scena 3D richiede sistemi di riferimento, intrinseci ed estrinseci della camera. Una funzione neurale mappa posizione e direzione a densità e colore. «Coordinate e camera» nomina il confine e «NeRF» implementa il percorso senza ereditare autorizzazioni implicite. Da «Coordinate e camera» a «NeRF» cambia la domanda osservabile. [SRC-61-001; SRC-61-002]

- **Da «NeRF» a «Gaussian splatting».** Una funzione neurale mappa posizione e direzione a densità e colore. Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da punti di vista nuovi. Componendo «NeRF» e «Gaussian splatting» diventa necessario conservare stato, identità e decisione. Il passaggio successivo rende misurabile «Gaussian splatting». [SRC-61-002; SRC-61-003]

- **Da «Gaussian splatting» a «Mesh, point cloud e voxel».** Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da punti di vista nuovi. Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering. «Mesh, point cloud e voxel» introduce failure e recovery prima di un side effect o di una perdita di stato. Da «Gaussian splatting» a «Mesh, point cloud e voxel» cambia la domanda osservabile. [SRC-61-003; SRC-61-004]

- **Da «Mesh, point cloud e voxel» a «Generazione e grounding spaziale».** Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering. Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate. La chiusura su «Generazione e grounding spaziale» valuta il sistema completo, non soltanto il componente iniziale. Il passaggio successivo rende misurabile «Generazione e grounding spaziale». [SRC-61-004; SRC-61-001]

La catena completa produce immagine, campo radiance o geometria a partire da punti, camera, raggi e profondità. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: una vista proiettata non determina da sola la scena completa.


## Prove sui confini del sistema

1. Ricostruisci «Coordinate e camera» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «NeRF», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Gaussian splatting» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Mesh, point cloud e voxel» che produca una failure riconoscibile.
5. Per «Generazione e grounding spaziale», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «punti, camera, raggi e profondità» e arriva fino a «immagine, campo radiance o geometria». Il limite da conservare è questo: una vista proiettata non determina da sola la scena completa. Il confine di «Generazione e grounding spaziale» va ricontrollato tra claim, fonti e artefatti: i rinvii sono [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
