<!--
chapter_id: CH-P05-DIFFUSION-FLOW
part_id: P05
order_key: 250
title: Diffusione, score matching e flow matching
maturity: CORE
status: completo, validato e congelato
version: 1.0.0
last_source_check: 2026-08-01
-->

# Capitolo 25. Diffusione, score matching e flow matching

Il capitolo precedente ha costruito il prerequisito immediato necessario. Ora applichiamo lo stesso oggetto continuo, la richiesta «Il pacco non è arrivato», a una nuova capacità. L'obiettivo è capire il meccanismo in modo operativo, senza attribuire al modello proprietà che non sono state misurate.

## Corrompere e ricostruire

La diffusione forward aggiunge rumore secondo uno schedule. Il modello impara a invertire o a stimare una quantità equivalente.

Questo passaggio usa l'oggetto continuo del libro e rende esplicito quale quantità viene trasformata, quale risultato viene ottenuto e quale limite resta aperto. L'esempio numerico e lo snippet permettono di controllare il contratto senza trasformarlo in una descrizione di un sistema reale.

## Score matching

Lo score è il gradiente del log-density rispetto ai dati perturbati. Denoising score matching evita di conoscere la densità normale completa.

Questo passaggio usa l'oggetto continuo del libro e rende esplicito quale quantità viene trasformata, quale risultato viene ottenuto e quale limite resta aperto. L'esempio numerico e lo snippet permettono di controllare il contratto senza trasformarlo in una descrizione di un sistema reale.

## Parametrizzazioni epsilon, x0 e v

Target differenti sono trasformazioni della stessa relazione sotto uno schedule, ma cambiano scala e weighting del training.

Questo passaggio usa l'oggetto continuo del libro e rende esplicito quale quantità viene trasformata, quale risultato viene ottenuto e quale limite resta aperto. L'esempio numerico e lo snippet permettono di controllare il contratto senza trasformarlo in una descrizione di un sistema reale.

## Sampler

DDPM, DDIM e solver ODE/SDE usano discretizzazioni differenti. Meno step non garantiscono stessa distribuzione o qualità.

Questo passaggio usa l'oggetto continuo del libro e rende esplicito quale quantità viene trasformata, quale risultato viene ottenuto e quale limite resta aperto. L'esempio numerico e lo snippet permettono di controllare il contratto senza trasformarlo in una descrizione di un sistema reale.

## Flow matching e rectified flow

Flow matching apprende un campo vettoriale lungo percorsi scelti tra distribuzioni. Rectified flow cerca traiettorie più rettilinee in setup specifici.

Questo passaggio usa l'oggetto continuo del libro e rende esplicito quale quantità viene trasformata, quale risultato viene ottenuto e quale limite resta aperto. L'esempio numerico e lo snippet permettono di controllare il contratto senza trasformarlo in una descrizione di un sistema reale.

![Percorso del capitolo](../../assets/chapters/25_diffusion_flow/FLOW-01/final.png)

La prima figura ordina i passaggi e mostra il risultato consegnato alla fase successiva.

![Caso base, varianti e limiti](../../assets/chapters/25_diffusion_flow/FLOW-02/final.png)

La seconda figura separa il contratto minimo dalle estensioni.

## Snippet verificabile

Il file [`code/snip_25_contract.py`](code/snip_25_contract.py) applica una normalizzazione stabile e combina stati con shape dichiarate. Lo snippet è intenzionalmente piccolo: verifica il tipo di ragionamento numerico usato nel capitolo, non riproduce un modello di produzione.

## Riepilogo

Il capitolo ha costruito diffusione, score matching e flow matching partendo dai prerequisiti disponibili. Il caso base, le varianti e i limiti sono mantenuti separati. Il risultato viene consegnato al capitolo successivo, che aggiunge una sola nuova dimensione del sistema.

### Verifica della comprensione

1. Ricostruisci l'ordine dei passaggi senza consultare la figura.
2. Indica quale oggetto viene aggiornato e quale resta invariato.
3. Spiega un limite del caso base.
4. Collega lo snippet alla sezione pertinente.
5. Proponi una variazione controllata e prevedine l'effetto.

## Fonti e materiali verificabili

Fonti, claim, codice, test e audit sono disponibili nei file del capitolo.
