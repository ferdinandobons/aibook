<!--
chapter_id: CH-P12-SPECULATIVE-DECODING
part_id: P12
order_key: 770
title: Speculative e parallel decoding
maturity: ESTABLISHED
status: revisione editoriale v2, approvazione autoriale aperta
version: 0.5.0-draft3
last_source_check: 4 agosto 2026
environment: Python 3.13.12, CPU
code_policy: reference
deferred: benchmark applicativi non eseguiti e approvazione autoriale delle visuali
-->

# Capitolo 77. Speculative e parallel decoding

La lezione prende un caso piccolo e lo accompagna da «Draft e target» fino a «Parallel decoding», senza saltare i passaggi. L'oggetto osservato è draft e target durante il decoding speculativo. Il contratto locale dichiara input, token proposti, logits draft e logits target; operazione, proposta, verifica, accettazione e fallback; output, token accettati, velocità e distribuzione preservata. La situazione minima da seguire è Tre token draft vengono verificati: due sono accettati e uno ricade nel target. Il limite da non nascondere è: lo speedup richiede verifica senza cambiare il contratto di output.

## Draft e target

Un modello economico propone più token; il modello target li verifica in parallelo. [SRC-77-001]

Speculazione e decoding parallelo richiedono una verifica del draft.

**Caso da seguire.** Tre token draft vengono verificati: due sono accettati e uno ricade nel target.

**Controllo.** Per «Draft e target», scrivi il risultato atteso prima del calcolo, modifica una sola quantità e localizza il primo passaggio che cambia. Nel caso «Draft e target», il vincolo da conservare è: Un modello economico propone più token; il modello target li verifica in parallelo.


## Acceptance

La regola di accettazione conserva esattamente la distribuzione target nel metodo speculativo standard. [SRC-77-002]

**Caso da seguire.** Tre token proposti, due accettati e uno ricalcolato.

**Controllo.** Per «Acceptance», ricalcola il caso a mano e con lo snippet. Nel caso «Acceptance», se i risultati divergono, confronta prima i valori intermedi e soltanto dopo l'output finale.


Per questo capitolo la notazione compatta chiarisce input, trasformazione e risultato.

**Schema concettuale.** `accepted = verify(draft, target)`

Speculazione e decoding parallelo richiedono una verifica del draft. [SRC-77-001]


![Speculative e parallel decoding: compare](../../assets/chapters/77_speculative_decoding/DECODING-01/candidate-v48.png)

La prima figura segue il percorso da «Draft e target» a «Speedup».


## Speedup

Il guadagno dipende da acceptance rate, costo del draft, lunghezza proposta e hardware. [SRC-77-003]

**Caso da seguire.** Un caso in cui lo speedup richiede verifica senza cambiare il contratto di output.

**Controllo.** Per «Speedup», aggiungi un valore limite e verifica separatamente forma, valore e ipotesi. Una shape valida non dimostra da sola «Speedup».


## Medusa, EAGLE e ReDrafter

Head multiple, feature prediction e recurrent drafter producono candidate con strutture differenti. [SRC-77-004]

**Caso da seguire.** Ridurre i byte per elemento cambia memoria e potenzialmente errore. Il controllo richiede confronto numerico oltre alla misura di tempo.

**Controllo.** Per «Medusa, EAGLE e ReDrafter», mantieni fisso l'input e sostituisci soltanto il meccanismo discusso nella sezione. Nel caso «Medusa, EAGLE e ReDrafter», il confronto deve attribuire la differenza a quel passaggio, non al setup.


## Esempio Python eseguito

Il caso computazionale di speculative e parallel decoding è riportato senza trasformazioni: il file e l'output sono quelli verificati. Per «Speculative e parallel decoding», il caso di default usa valori piccoli per isolare il meccanismo. La suite conserva inoltre una failure esplicita per separare il contratto osservato da «speculative e parallel decoding».

```python
def contract(case: str = "default"):
    if case != "default":
        raise ValueError("only the documented default case is supported")
    draft = ["a", "b", "c"]
    target_accepts = [True, True, False]
    accepted = [token for token, ok in zip(draft, target_accepts) if ok]
    fallback = "target_next" if not target_accepts[-1] else None
    return {"accepted": accepted, "fallback": fallback, "invariant": "speculative decoding verifies draft tokens before committing them"}
```

Esecuzione con `python snip_77_contract.py`:

```text
{"accepted": ["a", "b"], "fallback": "target_next", "invariant": "speculative decoding verifies draft tokens before committing them"}
```

Il test associato è [`code/test_77_contract.py`](code/test_77_contract.py); l'output versionato è [`code/outputs/SNIP-77-001.txt`](code/outputs/SNIP-77-001.txt).


## Parallel decoding

Metodi lookahead o Jacobi aggiornano più posizioni ma devono dichiarare se preservano esattamente la distribuzione originale. [SRC-77-001]

**Caso da seguire.** Un prefisso corretto confrontato con lo stesso prefisso dopo che il modello ha prodotto il token precedente.

**Controllo.** Per «Parallel decoding», costruisci un controesempio che rispetti il tipo di dato ma violi l'ipotesi centrale. Il test deve rendere riconoscibile perché «Parallel decoding» non si applica.


![Speculative e parallel decoding: pipeline](../../assets/chapters/77_speculative_decoding/DECODING-02/candidate-v48.png)

La seconda figura mette a confronto «Medusa, EAGLE e ReDrafter» e il limite discusso in «Parallel decoding».


## Come si collegano i passaggi

- **Da «Draft e target» a «Acceptance».** Un modello economico propone più token; il modello target li verifica in parallelo. La regola di accettazione conserva esattamente la distribuzione target nel metodo speculativo standard. Tra «Draft e target» e «Acceptance» l'ingresso viene fissato prima della regola che produce il valore. Da «Draft e target» a «Acceptance» cambia la domanda osservabile. [SRC-77-001; SRC-77-002]

- **Da «Acceptance» a «Speedup».** La regola di accettazione conserva esattamente la distribuzione target nel metodo speculativo standard. Il guadagno dipende da acceptance rate, costo del draft, lunghezza proposta e hardware. Nel caso «Speedup» il componente diventa il punto in cui localizzare l'errore. Il passaggio successivo rende misurabile «Speedup». [SRC-77-002; SRC-77-003]

- **Da «Speedup» a «Medusa, EAGLE e ReDrafter».** Il guadagno dipende da acceptance rate, costo del draft, lunghezza proposta e hardware. Head multiple, feature prediction e recurrent drafter producono candidate con strutture differenti. Dopo «Speedup», la variante di «Medusa, EAGLE e ReDrafter» cambia una proprietà alla volta. Da «Speedup» a «Medusa, EAGLE e ReDrafter» cambia la domanda osservabile. [SRC-77-003; SRC-77-004]

- **Da «Medusa, EAGLE e ReDrafter» a «Parallel decoding».** Head multiple, feature prediction e recurrent drafter producono candidate con strutture differenti. Metodi lookahead o Jacobi aggiornano più posizioni ma devono dichiarare se preservano esattamente la distribuzione originale. Da «Parallel decoding» in poi la misura resta distinta dalla correttezza locale del calcolo. Il passaggio successivo rende misurabile «Parallel decoding». [SRC-77-004; SRC-77-001]

La catena completa produce token accettati, velocità e distribuzione preservata a partire da token proposti, logits draft e logits target. Ogni collegamento conserva un oggetto osservabile diverso; per questo il risultato non può essere esteso oltre il limite dichiarato: lo speedup richiede verifica senza cambiare il contratto di output.


## Esercizi sul meccanismo

1. Ricostruisci «Draft e target» con un esempio diverso da quello mostrato e indica l'output atteso prima del calcolo.
2. Nel passaggio «Acceptance», cambia una sola ipotesi e spiega quale risultato non è più confrontabile.
3. Collega «Speedup» a una riga dello snippet oppure motiva perché la prova deve essere documentale.
4. Progetta un caso limite per «Medusa, EAGLE e ReDrafter» che produca una failure riconoscibile.
5. Per «Parallel decoding», separa una conclusione sostenuta dal caso locale da una che richiederebbe nuovi dati o un benchmark.


## Che cosa deve restare chiaro

La lezione parte da «token proposti, logits draft e logits target» e arriva fino a «token accettati, velocità e distribuzione preservata». Il limite da conservare è questo: lo speedup richiede verifica senza cambiare il contratto di output. La formula e il codice collegati a «Parallel decoding» sono rintracciabili in [`FONTI_PRIMARIE.md`](FONTI_PRIMARIE.md), [`CLAIMS.md`](CLAIMS.md) e `code/`.
