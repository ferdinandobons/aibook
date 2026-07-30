# Stile di spiegazione e visuali

Stato: metodo vincolante per ogni articolo AI su ferdinandobonsegna.com  
Lingua degli articoli pubblicati: italiano  
Fonte metodologica: `Metodo_1a1_Manuale_Universale_AI_Transformer.md`
Contratto condiviso con LearnGPT Web: `docs/COURSE_DESIGN_PRINCIPLES.md` e
`docs/VISUAL_LANGUAGE.md` del repository del corso

I due documenti di LearnGPT Web definiscono lo stesso metodo applicato a una
lezione invece che a una pagina. Le regole di scrittura italiana, la catena dei
sette punti, la selezione delle visualizzazioni e i divieti di questo documento
ne sono la versione per il sito: quando una regola cambia in uno dei due posti,
va rivista nell'altro. Restano invece separati gli oggetti concreti. LearnGPT
Web trasporta la frase `The cat sleeps here.` perché il corso addestra un
modello su testo inglese; questo sito trasporta la frase guida dichiarata al
capitolo 3 di `LEARN_GOVERNANCE.md`, che è italiana perché metà dei fatti
misurati della sezione Learn esiste solo grazie a una frase italiana. Adottare
lo stile non significa adottare l'esempio.

## Scopo

Ogni articolo deve costruire un modello mentale eseguibile. Il lettore deve
poter ricostruire il flusso, localizzare ogni componente, dire cosa entra e cosa
esce, e prevedere cosa cambia quando una parte viene modificata.

Riconoscere i termini non basta. L'articolo riesce solo quando il lettore può
spiegare il meccanismo partendo dall'esempio originale, applicarlo a un caso
modificato e dire cosa quel meccanismo non fa.

## Principio centrale

Porta un oggetto concreto dall'apertura alla ricostruzione finale. Ogni step
principale deve:

1. partire dall'output esatto dello step precedente;
2. aggiungere un solo oggetto, distinzione, operazione o relazione;
3. eseguire l'aggiunta sull'esempio continuo;
4. mostrare lo stato accumulato completo;
5. consegnare quello stato direttamente allo step successivo.

Il lettore deve vedere lo stesso oggetto diventare progressivamente più ricco:

```text
oggetto noto
-> oggetto noto più una distinzione
-> stato precedente più una operazione
-> stato precedente più un risultato
-> modello eseguibile completo
```

Non scrivere saggi tematici separati. Se una sezione può essere spostata altrove
senza rompere l'esecuzione, probabilmente non appartiene alla struttura portante
principale.

## La catena dei sette punti

Una pagina è una spiegazione continua, non una raccolta di etichette scollegate.
La spiegazione centrale collega, in quest'ordine:

1. lo stato iniziale;
2. il problema che non può ancora essere risolto in quello stato;
3. il motivo per cui la nuova operazione viene introdotta qui;
4. la trasformazione concreta, nell'ordine reale di esecuzione;
5. lo stato risultante;
6. l'invariante che deve restare vero;
7. ciò che manca ancora, intenzionalmente.

I punti 1, 5 e 6 non sono soltanto prosa: vivono anche nei campi `statoPrima`,
`statoDopo` e `invariante` del manifest, e la sezione Learn li mostra al lettore
nella bussola in testa alla pagina. Il capitolo 9 di `LEARN_GOVERNANCE.md`
definisce quel componente.

Il punto 6 è quello che si dimentica per primo. Un lettore che ha visto una
trasformazione non sa ancora che cosa quella trasformazione **non** ha toccato,
e senza quell'informazione non può prevedere l'effetto del passo successivo. Il
numero di token che entrano, la forma di una riga, l'ordine della sequenza:
quando un'operazione lascia qualcosa intatto, va detto dove il lettore la sta
guardando, non alla fine.

## Stato del lettore

Ogni paragrafo sposta il lettore tra stati di conoscenza:

| Stato | Significato |
|---|---|
| Stabile | Il lettore può già ricostruire questo oggetto o questa operazione. |
| Corrente | L'oggetto esatto che stiamo ispezionando ora. |
| Nuovo | Un solo concetto introdotto adesso. |
| Stabilizzato | Il lettore lo ha visto eseguito e può spiegare la transizione. |
| Differito | Dipendenza o variante reale rimandata intenzionalmente. |

Prima di scrivere una sezione, compilare:

```text
Ultima affermazione stabile:
Oggetto corrente:
Un concetto nuovo:
Concetti differiti:
Prova che il nuovo concetto è stabile:
```