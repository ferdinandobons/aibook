# Testo alternativo

MIX-01, Dataset mixture, curriculum e dati sintetici. Come si passa da «Peso effettivo delle sorgenti» a «Mixture ottimizzata» mantenendo osservabile la miscela effettiva di sorgenti durante il training? La composizione mixture channels collega «Peso effettivo delle sorgenti», «Temperature sampling», «Mixture ottimizzata». L'input è pesi, temperatura, curriculum e conteggio dei token; l'output è probabilità effettive e mix osservato. Il limite esplicito è: peso nominale e esposizione effettiva non sono la stessa misura.
