# Scheda visuale

## Identità

- ID:
- Capitolo:
- Sezione:
- Tipo: architecture / process / tensor-shape / matrix-operation / comparison / trade-off
- Stato: storyboard / bozza vN / da correggere / validata tecnicamente / approvata

## Domanda unica

Quale domanda precisa deve risolvere la figura?

## Contratto didattico

- Stato prima:
- Trasformazione nuova:
- Stato dopo:
- Invariante:
- Confine:
- Prossimo consumer:

## Contenuto

- Nodi:
- Frecce:
- Label:
- Shape:
- Valori illustrativi:
- Valori misurati:

## Contratto di contenimento del testo

Per ogni box, cella, badge, callout e area delimitata si registrano:

- testo esatto previsto;
- numero massimo di righe;
- allineamento;
- margine interno minimo;
- dimensione minima leggibile;
- comportamento richiesto quando il testo non entra.

Regola obbligatoria: ogni carattere deve rimanere integralmente dentro il contenitore a cui appartiene. Il testo non può oltrepassare, toccare o essere tagliato dal bordo. Non può sovrapporsi ad altri testi, frecce, simboli o box.

Quando il testo non entra, si applica questo ordine di correzione:

1. aumentare il contenitore;
2. ridisporre i componenti;
3. spezzare il testo su righe leggibili;
4. ridurre la quantità di testo senza perdere il significato;
5. dividere la visuale in più figure.

La riduzione del font è l'ultima opzione e non può portare il testo sotto la dimensione minima prevista per l'uso editoriale.

## Provenienza

- Fonte del meccanismo:
- Fonte dei valori:
- Data di consultazione:
- Setup di riproduzione:

## Accessibilità

- Alt text:
- Equivalente testuale:
- Ordine di lettura:
- Significato non affidato al colore:
- Strategia mobile:

## Stile

- Strumento di produzione: image generation
- Formato editoriale: PNG ad alta risoluzione
- Sfondo e palette: coerenti con `EXPLANATION_STYLE_AND_VISUALS.md`
- Font: sans-serif leggibile; simboli tecnici chiaramente distinti
- Watermark, firme e branding di terzi: assenti
- Il colore non è l'unico portatore di significato

## Audit preliminare

- [ ] Una sola domanda
- [ ] Una sola trasformazione non ancora insegnata
- [ ] Label note o introdotte accanto
- [ ] Shape coerenti con la prosa
- [ ] Colore non essenziale
- [ ] Valori illustrativi dichiarati
- [ ] Dati misurati completi di setup
- [ ] Alt text presente
- [ ] Equivalente semantico presente
- [ ] Dimensione editoriale verificata
- [ ] Tutto il testo resta dentro il proprio contenitore
- [ ] Ogni contenitore conserva margine interno visibile su tutti i lati
- [ ] Nessun testo tocca bordi, frecce, simboli o testi adiacenti

## Registro iterazioni

| Versione | Stato | Problemi trovati | Correzioni richieste | Esito del nuovo audit |
|---|---|---|---|---|
| v1 | | | | |

## Audit dei collegamenti

- [ ] Ogni freccia parte dal bordo o dalla porta corretta del nodo sorgente
- [ ] Ogni freccia termina sul nodo consumer corretto
- [ ] Nessuna linea sembra collegarsi a un flusso che attraversa soltanto
- [ ] Gli incroci inevitabili sono separati visivamente e non sembrano giunzioni
- [ ] I rami hanno origine comune esplicita
- [ ] Le annotazioni non possono essere scambiate per flussi dati
- [ ] Mask, residual path, skip connection e feedback loop hanno semantica distinta

## Audit tecnico

- [ ] Formule ricontrollate
- [ ] Valori numerici ricalcolati
- [ ] Shape ricontrollate
- [ ] Softmax e normalizzazioni coerenti
- [ ] Celle mascherate e ammesse non ambigue
- [ ] Input, parametri, operazioni e output non confusi
- [ ] Il diagramma coincide con la prosa e con le fonti

## Audit compositivo

- [ ] Una sola domanda principale
- [ ] Ordine di lettura evidente
- [ ] Nessuna area sovraccarica
- [ ] Testo leggibile alla dimensione editoriale prevista
- [ ] Tutto il testo è contenuto integralmente nei box previsti
- [ ] Nessun glifo è tagliato o coperto dal bordo
- [ ] Il padding interno resta uniforme e sufficiente
- [ ] Il controllo è stato ripetuto sull'immagine raster reale, non soltanto sul prompt
- [ ] Spaziatura sufficiente tra nodi e linee
- [ ] Gerarchia visiva coerente
- [ ] La figura non anticipa concetti non ancora stabilizzati
- [ ] La figura è ancora comprensibile senza colore

## Decisione finale

- Difetti bloccanti rimasti:
- Difetti non bloccanti accettati:
- Motivazione dell'approvazione:
- Data dell'approvazione:
