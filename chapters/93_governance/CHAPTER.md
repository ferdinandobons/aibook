<!--
chapter_id: CH-P13-GOVERNANCE
part_id: P13
order_key: 930
title: Diritto, governance e sostenibilità
maturity: CORE
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: exception
code_exception: Norme e responsabilità dipendono da ruolo, giurisdizione e data: uno script locale produrrebbe una falsa impressione di conformità automatica.
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 93. Diritto, governance e sostenibilità

La domanda guida di questa lezione è come collegare «Ruoli e responsabilità» e «Sostenibilità» senza perdere il contratto tecnico di diritto, governance e sostenibilità. L'oggetto osservato è una decisione di governance su un sistema e il suo rischio. Il contratto locale è: input, ruoli, uso previsto, evidenza, impatto e consumo; operazione, govern, map, measure, manage, document e change control; output, decisione, responsabilità, evidenza e registro d'incidente. Il caso guida è questo: Una scheda con owner, rischio, evidenza e decisione è completa, ma non certifica la compliance. Il confine da mantenere esplicito è: un framework orienta il rischio ma non certifica automaticamente la conformità.

## Ruoli e responsabilità

Owner, sviluppatore, deployer, utente e fornitore hanno controlli e informazioni differenti. Governance, accountability e comunicazione devono essere documentate. [SRC-93-001]

Governance traduce evidenza e rischio in una decisione documentata.

**Caso da seguire.** Una scheda con owner, rischio, evidenza e decisione è completa, ma non certifica la compliance.

**Controllo.** Classifica lo stesso caso lungo un solo asse alla volta e annota quale proprietà non è stata misurata.


## Risk management

NIST AI RMF organizza govern, map, measure e manage. Il framework guida un processo e non certifica automaticamente un sistema. [SRC-93-002]

**Caso da seguire.** Una tabella govern-map-measure-manage con evidenza e responsabile per ogni controllo.

**Controllo.** Cambia la proprietà che distingue «Risk management» dalle categorie vicine. Se la classificazione non cambia, la distinzione va formulata meglio.


## Norme e documentazione

Obblighi dipendono da giurisdizione, ruolo e uso. Versione, data e parere legale devono essere separati dal testo tecnico stabile. [SRC-93-003]

**Caso da seguire.** Un requisito normativo annotato con giurisdizione, ruolo, versione e data di lettura.

**Controllo.** Confronta un caso positivo e uno di confine usando la medesima definizione; non trasformare l'esempio in una graduatoria generale.


![Diritto, governance e sostenibilità: loop](../../assets/chapters/93_governance/GOVERNANCE-01/candidate-v50.png)

La prima figura segue il percorso da «Ruoli e responsabilità» a «Norme e documentazione».


## Incidenti e change management

Segnalazione, classificazione, risposta e comunicazione collegano monitoraggio e governance. [SRC-93-001]

**Caso da seguire.** Un incident record con rilevazione, classificazione, contenimento, rollback e comunicazione.

**Controllo.** Indica quale osservazione smentirebbe l'assegnazione del caso a «Incidenti e change management» e quale invece sarebbe irrilevante.


## Sostenibilità

Energia, acqua, emissioni e ciclo di vita dell'hardware richiedono indicatori, baseline e confini di misura documentati. [SRC-93-004]

**Caso da seguire.** Un confronto tra due configurazioni normalizzato per risultato utile, energia e hardware.

**Controllo.** Limita la conclusione alla proprietà dichiarata: Energia, acqua, emissioni e ciclo di vita dell'hardware richiedono indicatori, baseline e confini di misura documentati. Le dimensioni non osservate restano aperte.


![Diritto, governance e sostenibilità: checklist](../../assets/chapters/93_governance/GOVERNANCE-02/candidate-v48.png)

La seconda figura mette a confronto «Incidenti e change management» e il limite discusso in «Sostenibilità».


## Perché non forziamo un esempio Python

Norme e responsabilità dipendono da ruolo, giurisdizione e data: uno script locale produrrebbe una falsa impressione di conformità automatica. La verifica resta comunque obbligatoria attraverso fonti primarie, data di consultazione, claim delimitati e confronto tra casi.


## Come si collegano i passaggi

- **Da «Ruoli e responsabilità» a «Risk management».** Owner, sviluppatore, deployer, utente e fornitore hanno controlli e informazioni differenti. NIST AI RMF organizza govern, map, measure e manage. La definizione iniziale stabilisce l'asse del confronto; la categoria successiva aggiunge una proprietà senza creare una classifica implicita. [SRC-93-001; SRC-93-002]

- **Da «Risk management» a «Norme e documentazione».** NIST AI RMF organizza govern, map, measure e manage. Obblighi dipendono da giurisdizione, ruolo e uso. Il terzo passaggio verifica se le categorie restano distinguibili sullo stesso caso e impedisce che termini vicini diventino sinonimi. [SRC-93-002; SRC-93-003]

- **Da «Norme e documentazione» a «Incidenti e change management».** Obblighi dipendono da giurisdizione, ruolo e uso. Segnalazione, classificazione, risposta e comunicazione collegano monitoraggio e governance. La quarta sezione introduce il punto in cui l'asse scelto smette di bastare e richiede una nuova osservazione. [SRC-93-003; SRC-93-001]

- **Da «Incidenti e change management» a «Sostenibilità».** Segnalazione, classificazione, risposta e comunicazione collegano monitoraggio e governance. Energia, acqua, emissioni e ciclo di vita dell'hardware richiedono indicatori, baseline e confini di misura documentati. La sezione finale riunisce le dimensioni della valutazione, ma conserva i limiti di ciascuna invece di fonderle in un unico punteggio. [SRC-93-001; SRC-93-004]

La catena completa produce decisione, responsabilità, evidenza e registro d'incidente a partire da ruoli, uso previsto, evidenza, impatto e consumo. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: un framework orienta il rischio ma non certifica automaticamente la conformità.


## Domande per distinguere le categorie

1. Ricostruisci «Ruoli e responsabilità» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Risk management», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Norme e documentazione» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Incidenti e change management» che produca una failure riconoscibile.
5. Per «Sostenibilità», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Una mappa, non una graduatoria

La lezione parte da «ruoli, uso previsto, evidenza, impatto e consumo» e arriva fino a «decisione, responsabilità, evidenza e registro d'incidente». Il limite da conservare è questo: un framework orienta il rischio ma non certifica automaticamente la conformità. Definizioni e risultati citati sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md); la mappa dei claim è in [`CLAIMS.md`](CLAIMS.md).
