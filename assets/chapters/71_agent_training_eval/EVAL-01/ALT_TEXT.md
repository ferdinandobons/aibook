# Testo alternativo

EVAL-01, Training e valutazione degli agenti. Come si passa da «Traiettorie come dati» a «RL in ambienti» mantenendo osservabile traiettorie agentiche usate come dati e valutazione? La composizione trajectory eval collega «Traiettorie come dati», «Imitation e SFT», «RL in ambienti». L'input è task, trace, policy, outcome e costo; l'output è score di task, violazioni e failure per step. Il limite esplicito è: task riuscito e traiettoria sicura sono criteri distinti.
