# Registro dei claim. Capitolo 61

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `3d` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-61-01

- Affermazione esatta: Una scena 3D richiede sistemi di riferimento, intrinseci ed estrinseci della camera. Errori di coordinate cambiano il rendering.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-61-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis; Neural 3D shape representations; 3 Neural Radiance Field Scene Representation (claim collegato alla sezione «Coordinate e camera» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-61-02

- Affermazione esatta: Una funzione neurale mappa posizione e direzione a densità e colore. Volume rendering integra campioni lungo i raggi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-61-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; 3D Gaussian Splatting for Real-Time Radiance Field Rendering; 2.1. Traditional Scene Reconstruction and Rendering; 2.3. Point-Based Rendering and Radiance Fields (claim collegato alla sezione «NeRF» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-61-03

- Affermazione esatta: Gaussiane 3D con posizione, covarianza e colore vengono rasterizzate efficientemente da punti di vista nuovi.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-61-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation; Point Cloud Features; Deep Learning on 3D Data (claim collegato alla sezione «Gaussian splatting» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-61-04

- Affermazione esatta: Rappresentazioni discrete offrono trade-off differenti tra topologia, memoria e rendering.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-61-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; DreamFusion: Text-to-3D using 2D Diffusion; 3.1 Neural Rendering of a 3D Model; 3.2 Text-to-3D synthesis (claim collegato alla sezione «Mesh, point cloud e voxel» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-61-05

- Affermazione esatta: Testo e immagini possono condizionare scene, ma consistenza geometrica e fisica richiedono valutazioni dedicate.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-61-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis; Neural 3D shape representations; 3 Neural Radiance Field Scene Representation (claim collegato alla sezione «Generazione e grounding spaziale» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-61-CODE

- Affermazione esatta: lo snippet snip_61_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_61_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
