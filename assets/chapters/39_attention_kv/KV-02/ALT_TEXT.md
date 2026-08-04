# Testo alternativo

KV-02, Varianti dell'attention e gestione KV. Quale controllo collega «Local e sparse attention» a «MLA e cache» senza superare il limite dichiarato? La composizione kv layout collega «Local e sparse attention», «MLA e cache». L'input è Q con h_q teste e KV con h_kv teste; l'output è score, cache e pattern di comunicazione. Il limite esplicito è: raggruppamento delle teste e costo della KV cache restano espliciti.
