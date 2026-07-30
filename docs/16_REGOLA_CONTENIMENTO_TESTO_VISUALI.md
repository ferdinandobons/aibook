# Regola canonica per il contenimento del testo nelle visuali

## Stato

- Stato: `vincolante`
- Data di adozione: 30 luglio 2026
- Ambito: tutte le immagini tecniche del libro
- Documenti collegati: `02_TEMPLATE_VISUALE.md`, `03_PROTOCOLLO_QA_VISUALE.md`, `EXPLANATION_STYLE_AND_VISUALS.md`

## Principio

Ogni testo deve appartenere in modo inequivocabile a un solo contenitore e deve rimanere integralmente entro il bordo di quel contenitore.

Sono considerati contenitori:

- box;
- celle;
- badge;
- callout;
- pannelli;
- nodi di un diagramma;
- aree delimitate per formule, shape o valori.

## Requisiti obbligatori

Una visuale può essere approvata soltanto quando:

1. nessun carattere oltrepassa il bordo del proprio contenitore;
2. nessun carattere viene tagliato dal bordo o dal limite dell'immagine;
3. rimane un margine interno visibile su tutti i lati;
4. il testo non tocca il bordo;
5. il testo non invade un contenitore adiacente;
6. il testo non si sovrappone a frecce, linee, simboli o altro testo;
7. pedici, apici, segni matematici e accenti sono completamente visibili;
8. il testo conserva la stessa appartenenza semantica anche senza colore;
9. la leggibilità è verificata alla dimensione editoriale prevista, non soltanto a piena risoluzione;
10. l'immagine raster effettiva viene ispezionata dopo la generazione.

## Margine di sicurezza

La composizione deve lasciare un margine di sicurezza reale. Non basta che il testo non attraversi geometricamente il bordo. Un testo troppo vicino al bordo è respinto quando può sembrare associato a un elemento vicino o quando la rasterizzazione riduce la separazione visiva.

Per i box con testo su più righe si richiedono:

- altezza sufficiente per l'interlinea;
- larghezza sufficiente per evitare spezzature casuali;
- spazio sopra e sotto la prima e l'ultima riga;
- spazio laterale sufficiente per lettere larghe, pedici e simboli.

## Ordine delle correzioni

Quando un testo non entra, si interviene in questo ordine:

1. aumentare il box;
2. ridisporre i nodi e aumentare lo spazio disponibile;
3. usare un ritorno a capo intenzionale;
4. accorciare la label preservando il significato tecnico;
5. spostare dettagli secondari nella prosa o nell'alt text;
6. dividere la figura in più visuali.

Ridurre il font è l'ultima opzione. Non è ammesso risolvere un overflow rendendo il testo troppo piccolo.

## Difetti bloccanti

La visuale viene classificata `da modificare` o `da rigenerare` quando presenta almeno uno dei seguenti difetti:

- testo fuori dal box;
- testo a contatto con il bordo;
- testo tagliato;
- testo sovrapposto;
- label che invade una cella vicina;
- glifo parzialmente nascosto;
- ritorno a capo che separa impropriamente un termine tecnico;
- dimensione del font insufficiente;
- appartenenza del testo ambigua per prossimità.

## Audit dopo ogni modifica

Dopo ogni correzione si ripete il controllo completo di:

- contenimento;
- collegamenti;
- formule;
- numeri;
- shape;
- ordine di lettura;
- densità;
- accessibilità.

Una correzione del testo può spostare nodi o frecce e introdurre nuovi errori. Per questo motivo non è ammesso controllare soltanto il difetto precedente.

## Regola per i file finali

Un file può essere denominato `final.png` soltanto dopo che l'audit registra esplicitamente:

```text
Testo integralmente contenuto: sì
Margini interni verificati: sì
Sovrapposizioni: assenti
Controllo alla dimensione editoriale: superato
Approvazione tecnica: sì
Approvazione autoriale: sì
```
