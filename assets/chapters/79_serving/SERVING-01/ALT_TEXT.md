# Testo alternativo

SERVING-01, Serving, batching e scheduling. Come si passa da «Richieste eterogenee» a «Throughput e latency» mantenendo osservabile richieste eterogenee in una coda di serving? La composizione serving queue collega «Richieste eterogenee», «Continuous batching», «Throughput e latency». L'input è prompt, deadline, lunghezza, memoria e priorità; l'output è throughput, latency p50/p99 e richieste ammesse. Il limite esplicito è: throughput e latenza devono essere misurati insieme.
