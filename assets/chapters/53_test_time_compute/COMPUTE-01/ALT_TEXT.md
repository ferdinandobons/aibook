# Testo alternativo

COMPUTE-01, Test-time compute, ricerca e controllo del budget. Come si passa da «Più compute dopo il training» a «Tree search» mantenendo osservabile un budget di compute aggiunto durante l'inferenza? La composizione sample and vote collega «Più compute dopo il training», «Best-of-n», «Tree search». L'input è prompt, numero di campioni, token e deadline; l'output è risposta, costo, latenza e qualità. Il limite esplicito è: qualità e costo devono essere riportati insieme.
