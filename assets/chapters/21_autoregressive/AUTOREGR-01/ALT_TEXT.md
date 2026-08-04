# Testo alternativo

AUTOREGR-01, Modelli autoregressivi. Come si passa da «Fattorizzare una sequenza» a «Maschera causale» mantenendo osservabile la sequenza di token e la distribuzione del prossimo elemento? La composizione causal sequence collega «Fattorizzare una sequenza», «Teacher forcing», «Maschera causale». L'input è un prefisso di tre token e una mask causale; l'output è logits, token scelto e traiettoria. Il limite esplicito è: nessuna posizione futura entra nella predizione causale.
