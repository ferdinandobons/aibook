# Registro dei claim. Capitolo 57

- Data di revisione: 3 agosto 2026
- Routing verificato: tema `imagegen` con dossier fonte specifico del capitolo.
- Stati usati: aperta, verificata, corretta, respinta, rimossa.

## CL-57-01

- Affermazione esatta: Un autoencoder comprime l'immagine e il denoiser opera nello spazio latente. Il decoder ricostruisce pixel al termine.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-57-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Denoising Diffusion Probabilistic Models; 3 Diffusion models and denoising autoencoders (claim collegato alla sezione «Latent diffusion» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-57-02

- Affermazione esatta: Testo, classi, immagini o mappe strutturali entrano attraverso cross-attention, concatenazione o moduli dedicati.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-57-002, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; High-Resolution Image Synthesis with Latent Diffusion Models; 3.2 Latent Diffusion Models; 4.2 Image Generation with Latent Diffusion (claim collegato alla sezione «Conditioning» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-57-03

- Affermazione esatta: Combinare predizioni condizionate e non condizionate aumenta aderenza, con un trade-off rispetto a diversità e saturazione.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-57-003, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Adding Conditional Control to Text-to-Image Diffusion Models; 2.2 Image Diffusion; 2.3 Image-to-Image Translation (claim collegato alla sezione «Classifier-free guidance» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-57-04

- Affermazione esatta: Una mask stabilisce regioni modificabili. La coerenza con le aree conservate dipende da noise schedule e condition.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-57-004, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; InstructPix2Pix: Learning to Follow Image Editing Instructions; 3.1.2 Generating Paired Images from Paired Captions; A.2 Paired Image Generation (claim collegato alla sezione «Editing e inpainting» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-57-05

- Affermazione esatta: ControlNet, adapter e reference image aggiungono vincoli. Dataset, diritti e metadati restano parte del sistema.
- Tipo: definizione o meccanismo attribuito alla fonte.
- Fonte o prova: SRC-57-001, dossier FONTI_PRIMARIE.md.
- Sezione o pagina: Abstract / pagina iniziale; Denoising Diffusion Probabilistic Models; 3 Diffusion models and denoising autoencoders (claim collegato alla sezione «Controllo e provenienza» del capitolo).
- Versione o data: revisione locale 3 agosto 2026; versione della fonte registrata nel dossier.
- Controllo indipendente: pagina originale aperta; titolo, testo e intestazioni estratti; nessun risultato numerico trasferito; claim ristretto a definizione o meccanismo e nessun risultato quantitativo trasferito senza setup.
- Esito: verificata
- Note: il limite della fonte resta nel paragrafo e nel dossier.

## CL-57-CODE

- Affermazione esatta: lo snippet snip_57_contract.py produce l'output osservabile e il test rifiuta un input incoerente.
- Tipo: risultato eseguito localmente.
- Fonte o prova: code/snip_57_contract.py, test associato e output SNIP.
- Sezione o pagina: Dall'algoritmo al codice.
- Versione o data: Python 3.13.12, CPU, 3 agosto 2026.
- Controllo indipendente: esecuzione dello snippet e unittest nello stesso ambiente.
- Esito: verificata
- Note: esempio delimitato, non benchmark di produzione.
