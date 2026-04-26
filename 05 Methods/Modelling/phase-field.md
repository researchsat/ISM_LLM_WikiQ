---
title: "Phase-field modelling"
category: modelling
tags: [phase-field, Karma, diffuse-interface, solidification]
papers:
  - "[[../Automatic Detection of Dendritic Microstructure Using Computer Vision Deep Learning Models Trained with Phase Field Simulations_VIARDIN.pdf]]"
  - "[[../In situ experiments in microgravity and phase-field simulations of th amellar-to-rod transition during eutectic growth_AKAMATSU.pdf]]"
  - "[[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf]]"
  - "[[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf]]"
  - "[[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf]]"
related:
  - "[[wiki/modelling/sharp-interface]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/modelling/lattice-boltzmann]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/dendritic-growth]]"
  - "[[wiki/physics/eutectic-solidification]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/alloys/Al-Cu]]"
  - "[[wiki/alloys/SCN-transparent-analog]]"
  - "[[wiki/alloys/Al-Si]]"
  - "[[wiki/alloys/Ni-superalloys]]"
  - "[[wiki/authors/Alain-Karma]]"
  - "[[wiki/authors/Christoph-Beckermann]]"
  - "[[wiki/authors/Rohit-Trivedi]]"
  - "[[wiki/platforms/ISS-experiments]]"
  - "[[wiki/platforms/CETSOL-MICAST-ICESOL]]"
  - "[[wiki/platforms/DECLIC-DSI]]"
created: 2026-04-18
---

# Phase-field modelling

**Category:** modelling

---

## Overview

**Phase-field (PF)** uses a smoothly varying order parameter φ to
implicitly track solidification fronts, avoiding expensive explicit
tracking. [[wiki/authors/Alain-Karma|Karma's]] **thin-interface / antitrapping**
formulation gives quantitative V, ρ, λ without interface-width
artefacts. PF is the micro-scale pillar of the simulation hierarchy:

**MD → PF → [[wiki/modelling/CA-FE-models|CA-FE]] → [[wiki/methods/CFD-simulation|macro CFD]].**

## Use cases in the wiki

- Al-Cu ISS benchmarks: [[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf|Thomas 2023 — Al-Cu benchmark µg+1g]],
  [[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf|Becker 2023 — Al-Cu / Al-Ge equiaxed µg]].
- Eutectic lamellar-to-rod: [[../In situ experiments in microgravity and phase-field simulations of th amellar-to-rod transition during eutectic growth_AKAMATSU.pdf|Akamatsu — lamellar-to-rod in µg]].
- CET: [[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf|Robin 2023 — sharp/progressive CET model]].
- Synthetic training data for ML: [[../Automatic Detection of Dendritic Microstructure Using Computer Vision Deep Learning Models Trained with Phase Field Simulations_VIARDIN.pdf|Viardin 2023 — CV/DL on phase-field dendrites]].

## Key physics knobs

- **d0** (capillary length) ∝ γ / ΔSf·ΔT.
- **ε₄** anisotropy of γ — sets dendrite orientation.
- **Antitrapping current** — removes spurious solute trapping.
- **Noise** term seeds sidebranching spectra.

## Connected topics

- [[wiki/modelling/sharp-interface|sharp interface]] · [[wiki/modelling/CA-FE-models|CA FE models]] · [[wiki/modelling/lattice-boltzmann|lattice boltzmann]] · [[wiki/modelling/dimensionless-numbers|dimensionless numbers]]
- [[wiki/physics/solidification|solidification]] · [[wiki/physics/dendritic-growth|dendritic growth]] · [[wiki/physics/eutectic-solidification|eutectic solidification]] · [[wiki/physics/nucleation-CET|nucleation CET]] · [[wiki/physics/mushy-zone|mushy zone]]
- [[wiki/alloys/Al-Cu|Al Cu]] · [[wiki/alloys/SCN-transparent-analog|SCN transparent analog]] · [[wiki/alloys/Al-Si|Al Si]] · [[wiki/alloys/Ni-superalloys|Ni superalloys]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../Automatic Detection of Dendritic Microstructure Using Computer Vision Deep Learning Models Trained with Phase Field Simulations_VIARDIN.pdf|Viardin 2023 — CV/DL on phase-field dendrites]] | CV/DL segmentation of dendrites trained on phase-field data |
| [[../In situ experiments in microgravity and phase-field simulations of th amellar-to-rod transition during eutectic growth_AKAMATSU.pdf|Akamatsu — lamellar-to-rod in µg]] | Lamellar-to-rod eutectic transition via µg + phase-field |
| [[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf|Becker 2023 — Al-Cu / Al-Ge equiaxed µg]] | Equiaxed nucleation/growth in thin Al-Cu / Al-Ge under µg |
| [[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf|Thomas 2023 — Al-Cu benchmark µg+1g]] | Canonical Al-Cu ISS benchmark for CET models |
| [[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf|Robin 2023 — sharp/progressive CET model]] | Concurrent sharp+progressive CET model vs µg DS |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*