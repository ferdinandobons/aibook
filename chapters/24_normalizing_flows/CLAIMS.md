# Claim

- `CL-FLOWS-001`. Cambio di variabile: Una trasformazione invertibile collega una distribuzione semplice ai dati. La densità usa il determinante Jacobiano.
- `CL-FLOWS-002`. Coupling layer: RealNVP e Glow costruiscono trasformazioni triangolari, con inversa e log-determinante efficienti.
- `CL-FLOWS-003`. Invertibilità e architettura: L'invertibilità limita operazioni e dimensioni. Squeeze, split e permutazioni riorganizzano l'informazione senza perderla.
- `CL-FLOWS-004`. Continuous normalizing flow: Una ODE definisce una trasformazione continua. La likelihood usa la variazione del log-density lungo il flusso.
- `CL-FLOWS-005`. Sampling e costo: I flow offrono likelihood e campionamento esatto rispetto al modello, ma possono richiedere molte trasformazioni o solve numerici.
