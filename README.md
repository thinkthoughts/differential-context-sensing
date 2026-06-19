# differential-context-sensing

Exploring how differential context preserves precision in noisy measurement systems.

This repo starts from arXiv:2504.09158 and the AION demonstration of common-mode noise rejection in atom interferometry. The goal is to build small, readable notebooks that connect the physics result to a broader engineering statement:

> Common-mode rejection preserves precision: identify the shared disturbance, measure the differential phase, and build the sensor around the constraint.

## Paper

- arXiv: https://arxiv.org/abs/2504.09158
- HTML: https://arxiv.org/html/2504.09158
- Lab report: https://labreports.app/2504-09158/

## Notebook roadmap

| Notebook | Focus | Output |
|---|---|---|
| 00_context.ipynb | Paper context, AION motivation, and differential sensing premise | Concept map |
| 07_signal_vs_noise.ipynb | Separate physical signal, shared laser phase noise, and shot noise | Signal/noise traces |
| 13_common_mode_rejection.ipynb | Show how A − B cancels shared noise | Common-mode rejection figure |
| 17_differential_phase.ipynb | Phase model: phi_diff = phi_A − phi_B | Phase diagram |
| 23_standard_quantum_limit.ipynb | Shot-noise scaling and SQL intuition | SQL scaling plot |
| 29_long_baseline_motivation.ipynb | Why long-baseline atom interferometers care about laser phase noise | Architecture sketch |
| 37_hidden_context_recovery.ipynb | Connect common-mode rejection to hidden-state recovery | Recovery comparison |
| 43_context_as_noise_cancellation.ipynb | Generalize to forecasting and sensing systems | Cross-domain summary figure |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then open the notebooks:

```bash
jupyter lab
```

## Repo structure

```text
notebooks/   Notebook sequence
src/         Small reusable helpers
figures/     Saved outputs for README and lab report reuse
data/        Optional generated CSVs
reports/     Draft text, tables, or export artifacts
```
