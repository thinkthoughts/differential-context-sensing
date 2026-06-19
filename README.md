# differential-context-sensing

Exploring how differential context preserves precision in noisy measurement systems.

This repository starts from arXiv:2504.09158 and the AION demonstration of common-mode noise rejection in atom interferometry. Through a sequence of small, readable notebooks, it develops a broader engineering statement:

> Differential context preserves precision. Shared structure can be identified, compared, and removed, allowing physical signals to remain visible even in noisy environments.

The notebooks progress from simple common-mode rejection models to correlation, geometry, differential sensing architectures, and a toy atom-interferometer demonstration.

## Paper

- arXiv: https://arxiv.org/abs/2504.09158
- HTML: https://arxiv.org/html/2504.09158
- Lab report: https://labreports.app/2504-09158/

## Repository overview

The central idea is simple:

```text
shared structure
        ↓
 differential comparison
        ↓
 common-mode rejection
        ↓
 improved signal recovery
```

In atom interferometry, the shared structure is laser phase noise.

In other sensing systems it may be spatial correlations, common disturbances, latent state, or other forms of context.

## Notebook roadmap

00 → 07 → 13 → 17 → 23 → 29 → 37 → 43

## Notebook roadmap

| Notebook | Focus |
|-----------|-----------|
| 00_context.ipynb | Shared noise is not automatically lost information |
| 07_signal_noise.ipynb | Common-mode noise versus local noise |
| 13_correlation_context.ipynb | Correlation creates context |
| 17_baseline_separation.ipynb | Baseline distance reduces shared structure |
| 23_noise_channels.ipynb | Which disturbances are removable? |
| 29_differential_geometries.ipynb | Geometry determines measurable modes |
| 37_atom_interferometer_demo.ipynb | Toy AION-style differential sensing |
| 43_context_reveals_signal.ipynb | Context as shared structure across domains |

## Key figures

Recommended figures for the README:

- Differential sensing overview infographic
- 13_correlation_sweep.png
- 37_individual_vs_differential.png
- 43_context_map.png

## Engineering statement

Common-mode rejection does not eliminate noise universally.

It removes disturbances with the appropriate symmetry.

Differential sensing succeeds when:

1. A disturbance is shared across measurements.
2. The geometry preserves the signal while rejecting the disturbance.
3. Local noise remains below the desired precision threshold.

The AION result demonstrates this principle using atom interferometers and laser phase noise.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Launch Jupyter:

```bash
jupyter lab
```

## Repository structure

```text
notebooks/   Notebook sequence
src/         Reusable helpers
figures/     Saved figures
data/        Generated CSV outputs
reports/     Draft reports and exports
```

## Related links

- Lab report: https://labreports.app/2504-09158/
- Engineering statements: https://github.com/thinkthoughts/engineering-statements
- Lab reports: https://labreports.app
