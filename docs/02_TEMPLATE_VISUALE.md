# Scheda visuale

## Identità

- ID:
- Capitolo:
- Sezione:
- Famiglia primaria: process / comparison / architecture / tensor-shape / matrix-operation / taxonomy / quantitative-chart
- Orientamento: orizzontale / verticale
- Motivazione dell'orientamento:
- Stato: storyboard / bozza vN / da correggere / validata tecnicamente / approvata

## Standard applicato

- Standard visivo: `17_STANDARD_VISIVO_CANONICO.md`
- Regola di contenimento: `16_REGOLA_CONTENIMENTO_TESTO_VISUALI.md`
- Sfondo globale: bianco puro `#FFFFFF`
- Gradiente o texture di sfondo: assenti
- Render di pagina completa: no

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
- Formula o relazione principale:
- Footer tecnico previsto: invariante / shape / confine / nessuno

## Contratto di layout

- Direzione di lettura:
- Numero di pannelli:
- Griglia e allineamenti:
- Margine esterno:
- Zona di sicurezza:
- Elementi che devono avere dimensione uniforme:
- Collegamenti che non devono incrociarsi:
- Elementi da separare in una seconda figura se la densità aumenta:

L'orientamento viene scelto in funzione del contenuto. Un processo sequenziale o un confronto parallelo può usare un canvas orizzontale. Uno stack, una tassonomia o un flusso con molti livelli può usare un canvas verticale. Non esiste un orientamento predefinito valido per ogni immagine.

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

## Palette semantica

Registrare i ruoli effettivamente usati:

- testo principale `#0F172A`:
- testo secondario `#475569`:
- blu `#2563EB` con riempimento `#EFF6FF`:
- viola `#7C3AED` con riempimento `#F5F3FF`:
- verde `#16A34A` con riempimento `#F0FDF4`:
- ambra `#D97706` con riempimento `#FFFBEB`:
- rosso `#DC2626` con riempimento `#FEF2F2`:
- neutro `#CBD5E1` con riempimento `#F8FAFC`:

Il colore non è mai l'unico portatore di significato.

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
- Leggibilità in scala di grigi:
- Strategia per dimensione ridotta:

## Stile

- Strumento di produzione: image generation
- Formato editoriale: PNG ad alta risoluzione
- Sfondo globale: `#FFFFFF`
- Orientamento: adattato al contenuto
- Box: bordi sottili, angoli moderatamente arrotondati, riempimenti pastello chiari, padding visibile
- Frecce: spessore coerente, origine e destinazione esplicite
- Font: sans-serif leggibile; simboli tecnici chiaramente distinti
- Watermark, firme e branding di terzi: assenti
- Ombre pesanti: assenti
- Gradiente globale: assente

## Audit preliminare

- [ ] Una sola domanda
- [ ] Una sola trasformazione non ancora insegnata
- [ ] Famiglia visuale dichiarata
- [ ] Orientamento motivato dal contenuto
- [ ] Sfondo esattamente bianco
- [ ] Nessun gradiente o texture globale
- [ ] Label note o introdotte accanto
- [ ] Shape coerenti con la prosa
- [ ] Palette semantica rispettata
- [ ] Colore non essenziale
- [ ] Valori illustrativi dichiarati
- [ ] Dati misurati completi di setup
- [ ] Alt text presente
- [ ] Equivalente semantico presente
- [ ] Dimensione editoriale verificata
- [ ] Tutto il testo resta dentro il proprio contenitore
- [ ] Ogni contenitore conserva margine interno visibile su tutti i lati
- [ ] Nessun testo tocca bordi, frecce, simboli o testi adiacenti
- [ ] La figura è un'immagine tecnica, non una pagina renderizzata

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
- [ ] Nessuna freccia attraversa testo o formule

## Audit tecnico

- [ ] Formule ricontrollate
- [ ] Valori numerici ricalcolati
- [ ] Shape ricontrollate
- [ ] Softmax e normalizzazioni coerenti
- [ ] Celle mascherate e ammesse non ambigue
- [ ] Input, parametri, operazioni e output non confusi
- [ ] Il diagramma coincide con la prosa e con le fonti
- [ ] La notazione coincide con il codice del capitolo

## Audit compositivo

- [ ] Una sola domanda principale
- [ ] Ordine di lettura evidente
- [ ] Orientamento adeguato al contenuto
- [ ] Nessuna area sovraccarica
- [ ] Testo leggibile alla dimensione editoriale prevista
- [ ] Tutto il testo è contenuto integralmente nei box previsti
- [ ] Nessun glifo è tagliato o coperto dal bordo
- [ ] Il padding interno resta uniforme e sufficiente
- [ ] Il controllo è stato ripetuto sull'immagine raster reale, non soltanto sul prompt
- [ ] Sfondo bianco uniforme fino ai bordi
- [ ] Palette e stile dei box coerenti con le altre figure del libro
- [ ] Spaziatura sufficiente tra nodi e linee
- [ ] Gerarchia visiva coerente
- [ ] La figura non anticipa concetti non ancora stabilizzati
- [ ] La figura è ancora comprensibile senza colore

## Decisione finale

- Difetti bloccanti rimasti:
- Difetti non bloccanti accettati:
- Sfondo bianco verificato:
- Orientamento approvato:
- Conformità a `17_STANDARD_VISIVO_CANONICO.md`:
- Motivazione dell'approvazione:
- Data dell'approvazione:
