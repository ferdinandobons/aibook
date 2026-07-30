| `Vincolo` | un limite o una condizione da rispettare | `--amber` |
| `Output` | ciò che l'operazione produce | `--accent` |
| `Verificato` | un valore misurato e riproducibile | `--green` |
| `Confine` | ciò che il meccanismo non fa | `--amber` |
| `Illustrativo` | un valore inventato per l'esempio, non misurato | `--dim` |

Il campo `badge` del blocco visuale ammette solo i due badge di provenienza,
`Verificato` e `Illustrativo`: dicono se i numeri mostrati sono stati misurati o
inventati per l'esempio, ed è la sola domanda a cui il lettore non può
rispondere da solo guardando la figura. Gli altri cinque restano badge di prosa
e di interfaccia. Un valore diverso dai due fa fallire il parsing del blocco.

Il colore non basta mai. Ogni badge porta sempre la propria etichetta testuale,
e label, ordine, shape e testo devono restare sufficienti quando il colore viene
rimosso. Il rosso `--red` è riservato agli stati invalidi e agli errori, e non
appare mai come badge di contenuto.

## Regole di ammissione visuale

Una visuale è ammessa solo quando:

- tutte le label sono già note o introdotte subito accanto;
- contiene al massimo una trasformazione non ancora insegnata;
- il colore non è l'unico portatore di significato;
- i valori illustrativi sono dichiarati come illustrativi;
- i valori misurati nominano ambiente, modello, checkpoint, comando e data;
- l'articolo dichiara cosa è cambiato e cosa è rimasto invariato;
- la stessa informazione resta accessibile in testo o markup semantico;
- è leggibile su mobile senza ridurre le label sotto una dimensione utile.

Non mostrare l'output di un meccanismo prima che l'articolo abbia stabilito
perché quell'output serve.

## Responsive e accessibilità per le visuali

- Le tabelle Markdown devono stare dentro un wrapper scrollabile e focusable da
  tastiera.
- Header, celle, contrasto di riga, badge inline e hover state devono restare
  leggibili senza dipendere dal colore.
- Le token card vanno a capo in una griglia leggibile su mobile.
- I tensor flow si impilano verticalmente su mobile.
- Le tabelle scrollabili mantengono il contenuto completo.
- Gli heading degli step impilano il badge sopra il titolo quando serve.
- Le label tecniche non devono essere ridotte sotto una dimensione leggibile.
- Evitare screenshot di diagrammi tecnici: non sono responsive, ricercabili o
  accessibili in modo strutturale.

## Audit visuale obbligatorio

Prima dell'approvazione, ispezionare la pagina renderizzata e verificare:

1. ogni tabella Markdown ha header, bordi, celle leggibili e contenimento;
2. token, ID, shape e codice sono distinti dalla prosa;
3. le sequenze architetturali sono visualizzate come flow, non come blocchi di
   codice grezzi;
4. il meccanismo corrente è etichettato e evidenziato senza dipendere dal
   colore;
5. le visuali usano stesse label, valori, ordine e shape della prosa;
6. desktop e mobile preservano ordine di lettura e non tagliano informazioni;
7. le regioni scrollabili possono ricevere focus da tastiera;
8. nessuna visuale è decorativa o ridondante;
9. testo prima e dopo ogni visuale la inquadra, la ispeziona e la conclude;
10. l'articolo resta comprensibile senza stile e senza colore.

## Check finali di comprensione

Ogni articolo chiude testando:

| Check | Azione del lettore |
|---|---|
| Ricostruzione | Raccontare la transizione dall'input originale. |
| Localizzazione | Dire cosa viene prima e dopo il meccanismo. |
| Confine | Dire cosa il meccanismo non fa. |
| Trasferimento | Applicarlo a un nuovo input o parametro cambiato. |
| Variazione | Prevedere un effetto di rimozione, sostituzione o cambio parametro. |

Se il lettore non può rispondere, torna all'ultimo punto stabile e ripara una
giunzione. Non aggiungere altro materiale dopo il punto rotto.

## Istruzione Compatta

```text
Costruisci l'articolo come una sequenza di transizioni nello stato del lettore.

Ancora l'articolo all'ultimo oggetto stabile. Dimostra un gap concreto. Esegui
la più piccola operazione reale prima di nominarla. Porta un oggetto concreto
dal primo paragrafo alla ricostruzione finale. Ogni step parte dall'output esatto
dello step precedente, aggiunge una cosa e mostra lo stato accumulato completo.
Non interrompere l'esecuzione con sezioni tematiche staccate. Registra prima,
azione, dopo, cambiato e invariato. Generalizza una dimensione alla volta.
Ammetti termini, simboli, frecce, formule, codice, varianti e visuali solo dopo
che i referenti concreti sono stabili. Reintegra ogni output nel sistema più
grande. Verifica ricostruzione, localizzazione, confine, trasferimento e una
variazione. Mantieni l'articolo come bozza AI finché Ferdinando non valida la
versione renderizzata esatta.
```