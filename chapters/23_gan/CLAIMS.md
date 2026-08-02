# Claim

- `CL-GAN-001`. Un gioco tra due modelli: Il generatore produce campioni; il discriminatore distingue dati reali e generati. L'obiettivo è un gioco, non una loss singola ottimizzata congiuntamente.
- `CL-GAN-002`. Divergenze e gradienti: La formulazione originale è collegata alla Jensen-Shannon divergence sotto un discriminatore ottimo. I gradienti pratici dipendono dalla loss scelta.
- `CL-GAN-003`. Mode collapse: Il generatore può produrre poche modalità convincenti. Diversità e fedeltà devono essere misurate separatamente.
- `CL-GAN-004`. Wasserstein GAN: WGAN usa una distanza legata a funzioni Lipschitz. Weight clipping e gradient penalty sono implementazioni differenti del vincolo.
- `CL-GAN-005`. Stabilità e valutazione: Bilanciare update, normalizzazioni e capacità è essenziale. FID è una metrica su feature e non sostituisce l'analisi dei campioni.
