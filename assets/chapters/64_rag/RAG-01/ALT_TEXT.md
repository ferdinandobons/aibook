# Testo alternativo

RAG-01, Retrieval-Augmented Generation. Come si passa da «Una pipeline in due fasi» a «Prompt con fonti» mantenendo osservabile la pipeline che collega query, contesto e risposta? La composizione rag route collega «Una pipeline in due fasi», «Chunking», «Prompt con fonti». L'input è query, chunk, fonti e prompt; l'output è risposta con evidenza e score end-to-end. Il limite esplicito è: contesto recuperato e testo generato devono restare distinguibili.
