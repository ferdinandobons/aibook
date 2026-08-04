# Testo alternativo

VLM-01, Vision encoder e Vision-Language Model. Come si passa da «Patch e vision encoder» a «Projector» mantenendo osservabile patch visivi e token linguistici in un VLM? La composizione vlm route collega «Patch e vision encoder», «Dual encoder», «Projector». L'input è immagine, patch, testo e query; l'output è token visivi, risposta e grounding. Il limite esplicito è: una risposta linguistica non certifica che il dettaglio sia nell'immagine.
