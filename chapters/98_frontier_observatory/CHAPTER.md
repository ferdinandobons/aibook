<!--
chapter_id: CH-P14-FRONTIER-OBSERVATORY
part_id: P14
order_key: 980
title: Osservatorio della frontiera
maturity: FRONTIER
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: exception
code_exception: Un osservatorio di frontiera valuta evidenza aggiornata e maturità editoriale; il controllo centrale è documentale e datato, non computazionale. Ogni scheda conserva data, versione, disponibilità degli artefatti, replica indipendente, incertezza e condizione esplicita di riapertura.
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 98. Osservatorio della frontiera

Questa mappa di osservatorio della frontiera parte da «Scouting» e arriva a «Edizioni» conservando le proprietà che non sono state misurate. L'oggetto osservato è un claim di frontiera accompagnato da data e incertezza. Il contratto locale dichiara input, paper, release, benchmark, fonte e data di osservazione; operazione, scouting, routing, maturità, confronto e promozione; output, scheda con evidenza, stato e prossima verifica. Il primo esempio osservabile è Una scheda registra claim, data, evidenza e maturità FRONTIER separatamente. Il limite da non nascondere è: novità, adozione e prova end-to-end sono dimensioni diverse.

## Scouting

Nuovi paper, report e standard entrano in un registro con data, fonte e problema risolto. [SRC-98-001]

Un osservatorio di frontiera deve distinguere evidenza, data e incertezza.

**Caso da seguire.** Una scheda registra claim, data, evidenza e maturità FRONTIER separatamente.

**Controllo.** Per «Scouting», classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Routing

Ogni tecnica viene collocata nella parte proprietaria dell'oggetto modificato, senza creare una sezione generica della frontiera. [SRC-98-002]

**Caso da seguire.** Una tecnica instradata per oggetto modificato, prerequisito e consumer.

**Controllo.** Cambia la proprietà che distingue «Routing» dalle categorie vicine. Nel caso «Routing», se la classificazione non cambia, la distinzione va formulata meglio.


## Maturità

CORE, ESTABLISHED e FRONTIER descrivono evidenza e stabilità editoriale, non prestigio o popolarità. [SRC-98-003]

**Caso da seguire.** Una matrice che separa novità, replica, adozione, standard e readiness.

**Controllo.** Per «Maturità», confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


Lo schema seguente rende esplicito il confine tra il meccanismo e la sua valutazione.

**Schema concettuale.** `claim = evidence + date + uncertainty`

Un osservatorio di frontiera deve distinguere evidenza, data e incertezza. [SRC-98-001]


![Osservatorio della frontiera: chart](../../assets/chapters/98_frontier_observatory/OBSERVATOR-01/candidate-v48.png)

La prima figura segue il percorso da «Scouting» a «Maturità».


## Promozione

Una tecnica cambia maturità dopo nuove repliche, adozione, standardizzazione o chiarimento dei limiti. [SRC-98-004]

**Caso da seguire.** Una decisione di promozione basata su evidenza nuova e soglie registrate.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Promozione» e quale invece sarebbe irrilevante.


## Edizioni

Nuovi contenuti aggiornano catalogo, claim, capitoli e alias senza rinumerare identità stabili. [SRC-98-001]

**Caso da seguire.** Un'edizione che aggiorna claim, fonti e data senza cambiare identità storiche.

**Controllo.** Per «Edizioni», limita la conclusione alla proprietà dichiarata: Nuovi contenuti aggiornano catalogo, claim, capitoli e alias senza rinumerare identità stabili. Nel caso «Edizioni», le dimensioni non osservate restano aperte.


![Osservatorio della frontiera: timeline](../../assets/chapters/98_frontier_observatory/OBSERVATOR-02/candidate-v48.png)

La seconda figura mette a confronto «Promozione» e il limite discusso in «Edizioni».


## Perché non forziamo un esempio Python

Un osservatorio di frontiera valuta evidenza aggiornata e maturità editoriale; il controllo centrale è documentale e datato, non computazionale. Ogni scheda conserva data, versione, disponibilità degli artefatti, replica indipendente, incertezza e condizione esplicita di riapertura. La verifica resta comunque obbligatoria attraverso fonti primarie, data di consultazione, claim delimitati e confronto tra casi.


## Come si collegano i passaggi

- **Da «Scouting» a «Routing».** Nuovi paper, report e standard entrano in un registro con data, fonte e problema risolto. Ogni tecnica viene collocata nella parte proprietaria dell'oggetto modificato, senza creare una sezione generica della frontiera. «Scouting» stabilisce l'asse e «Routing» aggiunge una proprietà senza creare una graduatoria. Il passaggio successivo rende misurabile «Routing». [SRC-98-001; SRC-98-002]

- **Da «Routing» a «Maturità».** Ogni tecnica viene collocata nella parte proprietaria dell'oggetto modificato, senza creare una sezione generica della frontiera. CORE, ESTABLISHED e FRONTIER descrivono evidenza e stabilità editoriale, non prestigio o popolarità. Il confronto tra «Routing» e «Maturità» mantiene le categorie distinguibili sullo stesso caso. Da «Routing» a «Maturità» cambia la domanda osservabile. [SRC-98-002; SRC-98-003]

- **Da «Maturità» a «Promozione».** CORE, ESTABLISHED e FRONTIER descrivono evidenza e stabilità editoriale, non prestigio o popolarità. Una tecnica cambia maturità dopo nuove repliche, adozione, standardizzazione o chiarimento dei limiti. «Promozione» mostra il punto in cui l'asse di «Maturità» non è più sufficiente. Il passaggio successivo rende misurabile «Promozione». [SRC-98-003; SRC-98-004]

- **Da «Promozione» a «Edizioni».** Una tecnica cambia maturità dopo nuove repliche, adozione, standardizzazione o chiarimento dei limiti. Nuovi contenuti aggiornano catalogo, claim, capitoli e alias senza rinumerare identità stabili. Il passaggio su «Edizioni» riunisce più dimensioni senza cancellarne i limiti. Da «Promozione» a «Edizioni» cambia la domanda osservabile. [SRC-98-004; SRC-98-001]

La catena completa produce scheda con evidenza, stato e prossima verifica a partire da paper, release, benchmark, fonte e data di osservazione. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: novità, adozione e prova end-to-end sono dimensioni diverse.


## Domande per distinguere le categorie

1. Ricostruisci «Scouting» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Routing», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Maturità» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Promozione» che produca una failure riconoscibile.
5. Per «Edizioni», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «paper, release, benchmark, fonte e data di osservazione» e arriva fino a «scheda con evidenza, stato e prossima verifica». Il limite da conservare è questo: novità, adozione e prova end-to-end sono dimensioni diverse. Il confronto di «Edizioni» resta verificabile nei dossier [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md) e [`CLAIMS.md`](CLAIMS.md), senza trasformare la mappa in una graduatoria.
