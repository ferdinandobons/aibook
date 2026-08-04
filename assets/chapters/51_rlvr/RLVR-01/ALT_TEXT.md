# Testo alternativo

RLVR-01, Reinforcement learning con reward verificabili. Come si passa da «Reward verificabile» a «GRPO e policy update» mantenendo osservabile una risposta valutata da una regola verificabile? La composizione rlvr loop collega «Reward verificabile», «Rollout e gruppi», «GRPO e policy update». L'input è prompt, rollout, gruppo di risposte e verifier; l'output è reward, vantaggio e nuova policy. Il limite esplicito è: la verificabilità vale solo per il dominio coperto dal verifier.
