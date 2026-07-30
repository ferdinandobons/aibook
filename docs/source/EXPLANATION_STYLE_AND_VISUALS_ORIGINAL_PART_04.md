Usa ogni visuale in tre fasi:

1. **Inquadra.** Dichiara la domanda a cui risponde.
2. **Ispeziona.** Attraversa gli elementi etichettati in ordine di lettura.
3. **Concludi.** Dichiara il risultato e il prossimo consumer.

Una caption non sostituisce la spiegazione.

## Contratto visuale LearnGPT

Le superfici tecniche degli articoli riusano il linguaggio visuale di LearnGPT
Web.

### Fonte di verità dei token

L'unica fonte di verità dei token di colore è il blocco `:root` di
`app/globals.css`. Questo documento ne riporta una copia leggibile, e uno
scarto tra i due è un errore che il validatore deve fermare: nessun valore va
scritto a mano in un componente, in un articolo o in un mockup.

| Variabile | Valore | Ruolo |
|---|---|---|
| `--bg` | `#0d1117` | sfondo canonico LearnGPT |
| `--text` | `#e7edf5` | testo canonico LearnGPT |
| `--paper` | `var(--bg)` | alias editoriale dello sfondo |
| `--ink` | `var(--text)` | alias editoriale del testo |
| `--surface-sunken` | `#10161d` | superficie incassata |
| `--surface` | `#151b23` | superficie |
| `--surface-2` | `#1b222c` | superficie rialzata |
| `--surface-3` | `#222b36` | superficie rialzata di secondo livello |
| `--line` | `#2a3542` | bordo |
| `--line-strong` | `#3b4858` | bordo marcato |
| `--muted` | `#a8b3c2` | testo attenuato |
| `--dim` | `#748192` | testo tenue |
| `--accent` | `#65b4e8` | accento, operazione corrente |
| `--accent-deep` | `#28648d` | accento profondo |
| `--accent-soft` | `rgba(101, 180, 232, 0.12)` | sfondo di accento |
| `--green` | `#3fb880` | output verificato |
| `--amber` | `#d5a957` | vincolo |
| `--red` | `#d0616d` | stato invalido o errore |
| `--max` | `1180px` | larghezza massima di una pagina a colonna sola |
| `--max-learn` | `1720px` | larghezza massima del guscio a tre colonne di Learn |
| `--font-sans` | `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` | famiglia della prosa e dell'interfaccia |
| `--font-mono` | `ui-monospace, SFMono-Regular, Menlo, monospace` | famiglia di codice, shape e label tecniche |
| `--titolo-pagina` | `clamp(44px, 5vw, 68px)` | titolo di una pagina, sulla scala LearnGPT |
| `--titolo-sezione` | `clamp(34px, 4.2vw, 54px)` | titolo di una sezione, sulla scala LearnGPT |
| `--testo-apertura` | `clamp(17px, 1.55vw, 20px)` | paragrafo di apertura sotto un titolo |
| `--testo-lettura` | `16px` | prosa tecnica desktop, stabile al collasso delle colonne |
| `--larghezza-lettura` | `72ch` | misura massima di paragrafi ed elenchi |

La tabella copre l'intero blocco `:root`, non i soli colori: la scala
tipografica e le larghezze sono decisioni di progetto quanto le tinte, e il
controllo 18 le confronta tutte. Un token nuovo in `globals.css` senza la sua
riga qui fa fallire la build.

Prosa tecnica e heading usano il sistema sans-serif di LearnGPT. Token, shape,
ID, formule e codice usano il sistema monospace. Il codice inline è un badge
tecnico con bordo visibile, superficie scura e testo cyan.

### Scelta della visualizzazione

Si usa lo strumento più semplice che rappresenta correttamente la relazione, e
non si aggiunge una visuale perché la pagina ne è priva:

| Strumento | Serve per | Non serve per |
|---|---|---|
| Blocchi `learngpt-visual` | Matrici concrete, griglie allineate di token e valori, transizioni di shape | Prosa, codice sorgente, mappe generali del sistema |
| KaTeX | Notazione, formule, derivazioni, regole simboliche sulle shape | Layout, processi, aritmetica che si vede meglio come matrice |
| Tabella Markdown | Confronti piccoli ed esatti, le cui righe e colonne spiegano già la relazione | Processi lunghi o relazioni spaziali |
| Blocco di codice | Output di console letterale, serializzazioni, testo la cui spaziatura è essa stessa il soggetto | Relazioni più chiare come nodi, celle allineate o matrici |

Una formula entra solo dopo che la stessa quantità è comparsa come numero, come
prescrive il gate di simboli e formule. Diagrammi di architettura, grafi
manipolabili e grafici quantitativi con assi non hanno oggi uno strumento in
questo sito: si aggiungono quando un contenuto reale li richiede, non prima, e
insieme alla riga corrispondente in questa tabella.

### Visuali supportate

- `token-sequence` per token, posizione e ID;
- `labeled-grid` per relazioni esatte tra righe e celle;
- `tensor-flow` per transizioni ordinate di architettura o shape;
- `matrix-operation` per operazioni numeriche esplicite;
- tabelle Markdown semantiche per confronti compatti;
- espressioni KaTeX, delimitate da `$` inline e da `$$` in blocco, per la sola
  notazione matematica.

Lo schema che valida questi blocchi è `lib/article-visual.ts`, il rendering è
`components/article-visual.tsx`. Un tipo nuovo si aggiunge solo quando un
contenuto reale ne dimostra il bisogno, e va aggiunto in tutti e tre i posti:
schema, rendering e questo documento.

### Badge

I badge identificano un ruolo, e nient'altro:

| Badge | Uso | Colore |
|---|---|---|
| `Input` | ciò che entra in un'operazione | `--accent` |
| `Operazione` | il calcolo attualmente in esame | `--accent` |