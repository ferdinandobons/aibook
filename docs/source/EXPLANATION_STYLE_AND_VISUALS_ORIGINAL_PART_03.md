nell'articolo solo se aiuta il lettore a calcolare, verificare o prevedere
qualcosa.

### Gate del codice

Il codice può comparire dopo che l'operazione indipendente dalla libreria è
stabile.

Ogni blocco di codice deve identificare:

- input noto;
- riga che implementa l'operazione centrale;
- output osservabile;
- invariante che resterebbe uguale in un'altra implementazione.

### Gate delle varianti

Varianti, ottimizzazioni, eccezioni e differenze implementative compaiono dopo
che il caso base è stabile. Se l'accuratezza richiede di nominare una variante
prima, dichiararla solo come confine e rimandarne il meccanismo.

## Profili di articolo

Usa la stessa struttura portante, adattando la domanda dominante al tipo di soggetto.

| Profilo | Percorso dominante |
|---|---|
| Componente | input corrente -> capacità mancante -> esecuzione del componente -> contratto -> shape -> prossimo consumer |
| Processo | stato iniziale -> trigger -> transizione di stato -> invariante -> ripetizione o stop -> stato finale |
| Architettura | mappa globale -> confini dei componenti -> interfacce -> data flow -> mappa parametri/stato -> fasi |
| Metodo di training | modello prima dell'update -> segnale obiettivo -> loss -> percorso del gradiente -> update -> stato dopo |
| Tecnica | esecuzione baseline -> collo di bottiglia -> singola modifica -> comportamento invariato -> nuovo costo -> tradeoff |
| Paper | domanda -> baseline -> modifica proposta -> setup -> risultato -> interpretazione -> limite -> riproduzione |
| Confronto | livello condiviso -> input comune -> differenza controllata -> conseguenza -> condizione d'uso |
| Implementazione | algoritmo invariante -> strutture dati -> pseudocodice -> codice verificato -> check -> failure case |

## Regole di scrittura

- Scrivi in italiano calmo, preciso e progressivo. Il testo deve sembrare
  scritto direttamente in italiano, non tradotto: frasi dirette, ordine naturale
  delle parole, accenti e apostrofi corretti.
- Mantieni in inglese i termini tecnici standard quando sono l'uso corretto nel
  settore, per esempio `token`, `embedding`, `attention`, `training`,
  `inference`, `shape`, `input`, `output`, `language model`, `Transformer` e
  `PyTorch`. Inseriscili in una sintassi italiana, con articoli e preposizioni
  coerenti e stabili in tutta la sezione.
- Non usare em dash. Usa punto, virgola, due punti, punto e virgola o parentesi.
- Spiega perché un componente serve prima di spiegare come funziona.
- Usa un concetto per step, e descrivi **una sola trasformazione principale per
  paragrafo**. Dividi le frasi che mettono insieme input, operazione, output,
  eccezione e sviluppi futuri: sono quattro frasi, non una.
- Usa soggetti e referenti espliciti. Evita i pronomi che potrebbero riferirsi a
  più di un tensor, di una operazione o di uno stato.
- Preferisci nomi concreti e verbi operativi.
- Traduci il linguaggio antropomorfico nell'operazione numerica realmente
  eseguita.
- Non usare hype, keyword stuffing, introduzioni generiche o citazioni finte.
- Non usare un elenco di componenti al posto di una spiegazione causale.
- Usa elenchi puntati per informazioni senza un ordine necessario ed elenchi
  numerati soltanto per procedure o ragionamenti la cui sequenza conta.
- Distingui sempre il comportamento implementato, i valori illustrativi, i
  risultati misurati e gli sviluppi futuri. Una formulazione più chiara non deve
  eliminare una condizione né far sembrare il meccanismo più completo di quanto
  sia.

### Niente metafore

Non usare metafore, analogie con oggetti, personificazioni, etichette
infantili o domande retoriche. Descrivi direttamente il codice, il tensor, il
vocabolario o il comportamento del modello.

La regola è più stretta di quella che questo documento aveva prima, che
ammetteva l'analogia purché ne fosse dichiarato il confine. Un'analogia
dichiarata resta un secondo oggetto che il lettore deve tenere in memoria
accanto a quello vero, e nel punto in cui i due divergono la spiegazione si
ferma proprio dove serviva. Se una frase funziona solo grazie a un'immagine,
manca ancora l'operazione concreta che quella immagine sta sostituendo.

Restano ammessi i verbi tecnici consolidati che descrivono un'operazione reale
(`il modello predice`, `il layer proietta`, `la maschera azzera`), perché
nominano il calcolo e non un essere che lo compie.

### Persona e voce

La prosa è impersonale, oppure usa la prima persona plurale per le operazioni
che il testo esegue davanti al lettore: `prendiamo la frase`, `chiamiamo N la
lunghezza`, `ordiniamo i valori`.

La seconda persona è ammessa in un solo posto, il controllo di comprensione in
fondo alla pagina, dove il lettore deve fare qualcosa. Fuori da lì diventa un
riempitivo (`come sai`, `guarda la seconda colonna`, `nota che`) che aggiunge
parole senza aggiungere meccanismo, e che invecchia male quando la pagina viene
letta fuori ordine.

## Grammatica visuale

Le visuali fanno parte della spiegazione, non sono decorazione. Ogni visuale deve
rispondere a una sola domanda dichiarata e deve essere attraversata dalla prosa
vicina.