# Alt text per `AI-02`

Confronto orizzontale su sfondo bianco. Nel grande pannello verde `Training`, i dati di training attraversano il modello e producono un output. I target entrano nella loss; dalla loss si passa ai gradienti e poi all'optimizer step, unico nodo che aggiorna i parametri da theta a theta primo e produce un nuovo checkpoint. Nel pannello blu `Inference`, un nuovo input attraversa il modello con checkpoint fissato e produce un output. Un riquadro elenca gli elementi assenti nel caso base: target, loss, gradienti e optimizer step. Il footer chiarisce che `eval()` e `inference_mode()` hanno ruoli distinti in PyTorch e che nessuno dei due esegue un optimizer step.

Stato: verificato su `candidate-v1.png`.
