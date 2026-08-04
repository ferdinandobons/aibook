# Specifica visuale `HIST-01`

## Identità

- Capitolo: `CH-P01-HISTORY`
- Famiglia: timeline comparativa
- Orientamento: orizzontale
- File: `candidate-v1.png`
- Stato: `validata tecnicamente`
- Sfondo: bianco puro `#FFFFFF`

## Domanda unica

Quale collo di bottiglia diventa dominante quando cambiano rappresentazione, apprendimento, dati, calcolo e riuso?

## Contenuto

Cinque pannelli paralleli:

1. simboli e ricerca;
2. sistemi esperti e apprendimento statistico;
3. rappresentazioni apprese e reti profonde;
4. Transformer e pretraining;
5. foundation model e sistemi.

Ogni pannello contiene:

- periodo orientativo;
- rappresentazione tipica;
- collo di bottiglia dominante;
- tre esempi portanti.

## Invariante

Le famiglie si sovrappongono e continuano a convivere. Nessun pannello rappresenta un livello universale di superiorità.

## Vincoli

- nessuna freccia di progresso lineare;
- date descritte come orientative;
- nessuna affermazione secondo cui un paradigma sostituisce completamente il precedente;
- testo interamente nei box;
- palette canonica;
- nessun watermark o branding.

## Produzione

- generazione esplorativa con lo strumento immagini;
- composizione raster revisionabile: `scripts/generate_history_visuals.py`;
- decodifica verificata nel workflow `generate-book-visuals.yml`.
- domanda principale: Quale trasformazione centrale rende osservabile «Una storia di colli di bottiglia, non una marcia lineare» nel capitolo 2?

## Contratto geometrico

- raster: margine di sicurezza di 20 px sul canvas 1800x1000;
- contenimento: nessun testo oltre il proprio box o il canvas;
- composizione: nessuna sovrapposizione o tangenza intenzionale tra elementi fratelli;
- fonte: `GEOMETRY.json` e checklist dell'audit storico.
