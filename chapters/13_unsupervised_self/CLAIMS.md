# Registro dei claim. Capitolo 13

| ID | Claim sostenibile | Prova | Stato |
|---|---|---|---|
| `CLM-UNSUP-001` | Un obiettivo di apprendimento senza label esterne incorpora comunque scelte su distanza, corruzione, augmentazioni, contesto o coppie. | derivazione metodologica; `SRC-UNSUP-002`, `SRC-UNSUP-004`, `SRC-UNSUP-005`, `SRC-UNSUP-008` | verificato |
| `CLM-UNSUP-002` | Nel libro, self-supervised indica target costruiti automaticamente dal dato stesso. | convenzione editoriale dichiarata; esempi `SRC-UNSUP-005`, `SRC-UNSUP-006`, `SRC-UNSUP-008`, `SRC-UNSUP-009` | verificato come convenzione |
| `CLM-UNSUP-003` | K-means minimizza una somma di distanze quadratiche tra punti e centroidi nella formulazione usata. | `SRC-UNSUP-001`; derivazione | verificato |
| `CLM-UNSUP-004` | Alternare assegnazione al centroide più vicino e media dei membri non aumenta l'obiettivo rispetto al blocco fissato. | derivazione dell'algoritmo batch | verificato |
| `CLM-UNSUP-005` | K-means dipende da K, metrica, scala, rappresentazione e inizializzazione. | `SRC-UNSUP-001`, `SRC-UNSUP-002` | verificato |
| `CLM-UNSUP-006` | L'identificatore numerico di un cluster non è un nome semantico stabile. | proprietà di permutazione delle assegnazioni | verificato |
| `CLM-UNSUP-007` | Un autoencoder usa encoder e decoder per produrre una rappresentazione e ricostruire l'input. | `SRC-UNSUP-002`, `SRC-UNSUP-003` | verificato |
| `CLM-UNSUP-008` | Una bassa reconstruction loss non garantisce una rappresentazione utile per ogni task downstream. | limite metodologico; `SRC-UNSUP-002` | verificato con limite |
| `CLM-UNSUP-009` | Il denoising autoencoder riceve una versione corrotta e ricostruisce quella originale. | `SRC-UNSUP-004` | verificato |
| `CLM-UNSUP-010` | Nel masked modeling, il target può essere costituito dalla parte nascosta dell'input originale. | `SRC-UNSUP-006`, `SRC-UNSUP-009` | verificato |
| `CLM-UNSUP-011` | BERT pre-addestra rappresentazioni bidirezionali su testo senza label downstream e usa masked prediction tra gli obiettivi. | `SRC-UNSUP-006` | verificato |
| `CLM-UNSUP-012` | MAE maschera patch e ricostruisce pixel mancanti con encoder e decoder asimmetrici nel setup del paper. | `SRC-UNSUP-009` | verificato |
| `CLM-UNSUP-013` | CPC apprende rappresentazioni prevedendo il futuro in spazio latente con una loss contrastiva. | `SRC-UNSUP-005` | verificato |
| `CLM-UNSUP-014` | In SimCLR le augmentazioni definiscono le viste positive e svolgono un ruolo centrale nel compito. | `SRC-UNSUP-008` | verificato |
| `CLM-UNSUP-015` | Coppie, negative e temperatura cambiano la loss contrastiva. | formula e `SRC-UNSUP-005`, `SRC-UNSUP-008` | verificato |
| `CLM-UNSUP-016` | Una rappresentazione collassata assegna output uguali o quasi uguali a molti input; il meccanismo che la contrasta dipende dal metodo. | definizione operativa e letteratura contrastiva | verificato con limite |
| `CLM-UNSUP-017` | DeepCluster alterna k-means sulle feature e uso delle assegnazioni come pseudo-label per aggiornare la rete. | `SRC-UNSUP-007` | verificato |
| `CLM-UNSUP-018` | Una pseudo-label generata dal modello o dal clustering non è una annotazione umana. | `SRC-UNSUP-007` | verificato |
| `CLM-UNSUP-019` | Linear probe congela l'encoder e addestra un classificatore lineare; fine-tuning aggiorna anche l'encoder. | protocolli in `SRC-UNSUP-006`, `SRC-UNSUP-008`, `SRC-UNSUP-009` | verificato |
| `CLM-UNSUP-020` | Label downstream possono essere usate per valutare una rappresentazione senza entrare nella loss di pretraining. | `SRC-UNSUP-006`, `SRC-UNSUP-008`, `SRC-UNSUP-009` | verificato |
| `CLM-UNSUP-021` | Tuning ripetuto su un benchmark etichettato introduce informazione downstream nel processo complessivo. | derivazione metodologica; continuità con Capitolo 4 | verificato con contesto |
| `CLM-UNSUP-022` | Nel run, k-means riduce l'obiettivo da `203,144502` a `60,284823`. | `SNIP-UNSUP-001` | eseguito |
| `CLM-UNSUP-023` | Nel run, i tre cluster contengono 40 esempi ciascuno, senza uso dei gruppi segreti nel training. | `SNIP-UNSUP-001`, test | eseguito |
| `CLM-UNSUP-024` | Nel run, la loss mascherata di training scende da `2,218895` a `0,359401`. | `SNIP-UNSUP-001` | eseguito |
| `CLM-UNSUP-025` | Nel test fissato, la masked reconstruction loss è `0,391415` contro `1,900604` della baseline media. | `SNIP-UNSUP-001`, test | eseguito |
| `CLM-UNSUP-026` | Nel run, l'embedding di test ha shape `[60,2]`. | `SNIP-UNSUP-001`, test | eseguito |
| `CLM-UNSUP-027` | I nove test automatici risultano superati nell'ambiente registrato. | `code/outputs/TESTS.txt` | eseguito |

## Claim esclusi

- i cluster del toy dataset non dimostrano scoperta semantica;
- il conteggio 40/40/40 non è una garanzia di k-means;
- il masked autoencoder non viene presentato come modello generativo completo;
- una loss test inferiore alla baseline non dimostra trasferibilità;
- l'embedding a due dimensioni non viene interpretato senza evaluation downstream;
- la formula contrastiva non viene attribuita a ogni metodo self-supervised;
- augmentazioni e campioni negativi non sono universalmente appropriati;
- le metriche dei paper citati non vengono confrontate tra setup differenti;
- l'assenza di label non elimina rischi di privacy, bias o memorization;
- il capitolo non sostiene che self-supervised e unsupervised siano sinonimi universali.
