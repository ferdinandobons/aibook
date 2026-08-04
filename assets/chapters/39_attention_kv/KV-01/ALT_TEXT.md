# Testo alternativo

KV-01, Varianti dell'attention e gestione KV. Come si passa da «MHA» a «GQA» mantenendo osservabile le teste di query e key-value che alimentano l'attention? La composizione attention compare collega «MHA», «MQA», «GQA». L'input è Q con h_q teste e KV con h_kv teste; l'output è score, cache e pattern di comunicazione. Il limite esplicito è: raggruppamento delle teste e costo della KV cache restano espliciti.
