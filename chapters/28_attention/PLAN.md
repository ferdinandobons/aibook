# Piano del Capitolo 28

- `chapter_id`: `CH-P06-ATTENTION`
- Versione candidata: `0.2.0-rc2`
- Domanda centrale: come un vettore corrente costruisce una combinazione dei vettori sorgente che dipende dai confronti con la sorgente?
- Oggetto continuo: un vettore corrente e tre coppie sorgente con `d_k=d_v=2`.
- Stato finale: esempio numerico, pseudocodice, formula, shape, causal mask, implementazione diretta e confronto API.
- Concetti differiti: posizione, multi-head attention, varianti KV, cache e implementazioni hardware-aware.

## Progressione didattica

1. vettori sorgente già noti;
2. insufficienza di una combinazione fissa;
3. coefficienti dipendenti dalla posizione corrente;
4. descrizione dei tre ruoli prima dei nomi query, key e value;
5. score numerici;
6. scaling numerico;
7. softmax numerica;
8. combinazione numerica delle value;
9. ispezione guidata di `ATT-02`;
10. pseudocodice;
11. nome tecnico e formula generale;
12. provenienza di `Q`, `K` e `V`;
13. causal mask matematica;
14. codice diretto;
15. API e semantica delle mask;
16. complessità e confini;
17. ponte verso multi-head attention.

## Visuali incluse

- `ATT-01`: differenza tra contesto fisso e coefficienti dipendenti dalla posizione corrente.
- `ATT-02`: esempio numerico completo per una query.

Ogni visuale viene inquadrata, attraversata e conclusa nella prosa.

## Codice incluso

- `SNIP-ATT-001`: singola query e valori numerici.
- `SNIP-ATT-002`: formula matriciale e confronto API.
- `SNIP-ATT-003`: causal mask e coefficienti futuri nulli.

## Materiale rimosso dopo la review didattica

- formula e snippet completi della multi-head attention, trasferiti al capitolo successivo;
- spiegazione interna di FlashAttention, ridotta a confine hardware-aware;
- semantica API delle mask nella stessa transizione della mask matematica;
- uso anticipato del nome `scaled dot-product attention` prima del calcolo completo.

## Gate di completamento

- termini introdotti dopo i referenti;
- esempio, shape e pseudocodice prima della formula generale;
- blocchi atomici per score, scaling, softmax, output e mask;
- codice dopo il meccanismo;
- varianti soltanto come confini;
- due review didattiche complete registrate in `TEXT_AUDIT.md`;
- nessun difetto bloccante residuo prima della revisione autoriale.
