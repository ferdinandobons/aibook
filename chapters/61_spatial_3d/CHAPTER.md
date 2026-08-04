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

La domanda guida di questa lezione è come collegare «Coordinate e camera» e «Generazione e grounding spaziale» senza perdere il contratto tecnico di 3d, spazio e rappresentazione delle scene. L'oggetto osservato è punti e coordinate che descrivono una scena 3D. Il contratto locale è: input, punti, camera, raggi e profondità; operazione, proiezione, rendering, splatting o ricostruzione; output, immagine, campo radiance o geometria. Il caso guida è questo: Tre punti 3D producono un centroide con tre coordinate. Il confine da mantenere esplicito è: una vista proiettata non determina da sola la scena completa.

## Coordinate e camera

Una scena 3D richiede sistemi di riferimento, intrinseci ed estrinseci della camera. Errori di coordinate cambiano il rendering. [SRC-61-001]

La proiezione non ricostruisce da sola la geometria completa.

**Caso da seguire.** Tre punti 3D producono un centroide con tre coordinate.

**Controllo.** Registra richiesta, decisione, stato e output finale. Un esito plausibile non deve nascondere il componente che lo ha prodotto.


## NeRF

Una funzione neurale mappa posizione e direzione a densità e colore. Volume rendering integra campioni lungo i raggi. [SRC-61-002]

**Caso da seguire.** Due punti proiettati con camera e profondità dichiarate.

**Controllo.** Ripeti «NeRF» con una capability o un'autorizzazione rimossa e verifica che la failure preceda qualsiasi side effect.


![3D, spazio e rappresentazione delle scene: architecture](../../assets/chapters/61_spatial_3d/3D-01/candidate-v48.png)

La prima figura segue il percorso da «Coordinate e camera» a «Gaussian splatting».


## Gaussian splatting

Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da punti di vista nuovi. [SRC-61-003]

**Caso da seguire.** Un caso in cui una vista proiettata non determina da sola la scena completa.

**Controllo.** Separa il test del singolo componente dal test end-to-end, usando lo stesso input e la stessa configurazione versionata.


## Mesh, point cloud e voxel

Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering. [SRC-61-004]

**Caso da seguire.** Due vettori di modalità diverse vengono proiettati in uno spazio comune prima della similarità o della fusione; la dimensione comune è un invariante esplicito.

**Controllo.** Introduci una failure a un solo confine e controlla che log, stato e recovery identifichino quel confine senza ambiguità.


## Generazione e grounding spaziale

Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate. [SRC-61-001]

**Caso da seguire.** Per «Generazione e grounding spaziale» si mantiene l'input del capitolo e si isola questa condizione: Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate.

**Controllo.** Confronta il comportamento completo, non soltanto l'ultimo messaggio. Il risultato resta limitato da: Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate.


![3D, spazio e rappresentazione delle scene: scatter](../../assets/chapters/61_spatial_3d/3D-02/candidate-v48.png)

La seconda figura mette a confronto «Mesh, point cloud e voxel» e il limite discusso in «Generazione e grounding spaziale».


## Esempio Python eseguito

Il frammento seguente è lo stesso conservato nel repository. Usa valori piccoli perché l'obiettivo è osservare il meccanismo, non simulare una scala che non abbiamo eseguito.

```python
def contract():
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

- **Da «Coordinate e camera» a «NeRF».** Una scena 3D richiede sistemi di riferimento, intrinseci ed estrinseci della camera. Una funzione neurale mappa posizione e direzione a densità e colore. Il contratto iniziale nomina messaggi e confini; il componente successivo implementa una parte del percorso senza ereditare autorizzazioni implicite. [SRC-61-001; SRC-61-002]

- **Da «NeRF» a «Gaussian splatting».** Una funzione neurale mappa posizione e direzione a densità e colore. Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da punti di vista nuovi. Il terzo passaggio compone più componenti e rende quindi necessario conservare stato, identità e decisione oltre all'output finale. [SRC-61-002; SRC-61-003]

- **Da «Gaussian splatting» a «Mesh, point cloud e voxel».** Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da punti di vista nuovi. Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering. La quarta sezione introduce failure e recovery nel punto in cui possono ancora precedere un side effect o una perdita di stato. [SRC-61-003; SRC-61-004]

- **Da «Mesh, point cloud e voxel» a «Generazione e grounding spaziale».** Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering. Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate. La chiusura valuta il comportamento end-to-end: un componente corretto non basta se il collegamento, il carico o la policy cambiano l'esito. [SRC-61-004; SRC-61-001]

La catena completa produce immagine, campo radiance o geometria a partire da punti, camera, raggi e profondità. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: una vista proiettata non determina da sola la scena completa.


## Prove sui confini del sistema

1. Ricostruisci «Coordinate e camera» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «NeRF», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Gaussian splatting» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Mesh, point cloud e voxel» che produca una failure riconoscibile.
5. Per «Generazione e grounding spaziale», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Il confine operativo

La lezione parte da «punti, camera, raggi e profondità» e arriva fino a «immagine, campo radiance o geometria». Il limite da conservare è questo: una vista proiettata non determina da sola la scena completa. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
