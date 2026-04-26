---
title: "Dendritic growth"
category: physics
tags: [physics, dendrite, tip-selection, microgravity]
papers:
  - "[[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf]]"
  - "[[../Automatic Detection of Dendritic Microstructure Using Computer Vision Deep Learning Models Trained with Phase Field Simulations_VIARDIN.pdf]]"
  - "[[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf]]"
  - "[[../Three-dimensional investigation of fragment distribution in Al - 7 wt.percent Si solidified in microgravity_ABOUKHALIL.pdf]]"
  - "[[../Freezing Shrinkage Dynamics and Surface Dendritic Growth of Floating Refractory Alloy Droplets in Outer Space_HAIPENG.pdf]]"
  - "[[../Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation_BERGEON.pdf]]"
  - "[[../In situ investigation of the Columnar-to-Equiaxed Transition during microgravity recoral solidification of Al-20 wt cu alloys on Earth_NGOMESSE.pdf]]"
related:
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/physics/eutectic-solidification]]"
  - "[[wiki/modelling/phase-field]]"
  - "[[wiki/modelling/sharp-interface]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/alloys/Al-Cu]]"
  - "[[wiki/alloys/Al-Si]]"
  - "[[wiki/alloys/SCN-transparent-analog]]"
  - "[[wiki/methods/synchrotron-Xray]]"
  - "[[wiki/methods/directional-solidification]]"
  - "[[wiki/authors/Alain-Karma]]"
  - "[[wiki/authors/Martin-Glicksman]]"
  - "[[wiki/authors/Christoph-Beckermann]]"
  - "[[wiki/platforms/ISS-experiments]]"
  - "[[wiki/platforms/sounding-rockets]]"
  - "[[wiki/platforms/CETSOL-MICAST-ICESOL]]"
created: 2026-04-18
---

# Dendritic growth

**Category:** physics  
**Key researchers:** [[wiki/authors/Alain-Karma]], [[wiki/authors/Martin-Glicksman]]  
**Platforms studied on:** [[wiki/platforms/ISS-experiments]], [[wiki/platforms/CETSOL-MICAST-ICESOL]], [[wiki/platforms/sounding-rockets]]

---

## Overview

A dendrite is a tree-like single crystal whose tip selects a steady-state
shape dictated by diffusion, capillarity, and anisotropy. The
**Ivantsov–microsolvability** framework (extended by
[[wiki/authors/Alain-Karma|Karma]]) gives tip radius ρ and velocity V at the required
undercooling. Earth-based data are contaminated by buoyant
[[wiki/flow/thermosolutal-convection|convection]]; µg strips this, making
[[wiki/authors/Alain-Karma|Karma's]] σ* selection and the sidebranching spectrum
directly testable.

## Key observables (µg benchmarks)

- Tip radius ρ(t) and velocity V(t) under pure diffusion — [[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf|Becker 2023 — Al-Cu / Al-Ge equiaxed µg]].
- Sidebranch amplitude vs distance — phase-field benchmarks
  ([[wiki/modelling/phase-field|phase field]]).
- Fragmentation / remelting producing [[wiki/physics/nucleation-CET|equiaxed grains]] —
  [[../Three-dimensional investigation of fragment distribution in Al - 7 wt.percent Si solidified in microgravity_ABOUKHALIL.pdf|Aboukhalil — Al-7Si 3D fragment µg]].

## Classic scalings

- Ivantsov: `C* = Iv(Pe)` with Pe = V·ρ / (2D).
- Microsolvability: `σ* = 2 D d0 / (ρ² V)` — sets a unique (ρ, V).
- Lipton-Glicksman-Kurz (LGK) for equiaxed growth at undercooling ΔT.

## ML on dendrite images

[[../Automatic Detection of Dendritic Microstructure Using Computer Vision Deep Learning Models Trained with Phase Field Simulations_VIARDIN.pdf|Viardin 2023 — CV/DL on phase-field dendrites]] uses CV/DL trained on [[wiki/modelling/phase-field|phase field]] synthetic
data to segment dendrites in experimental imagery — a bridge between
[[wiki/modelling/CA-FE-models|mesoscale models]] and µg imaging.

## Connected topics

- [[wiki/physics/solidification|solidification]] · [[wiki/physics/mushy-zone|mushy zone]] · [[wiki/physics/nucleation-CET|nucleation CET]] · [[wiki/physics/eutectic-solidification|eutectic solidification]]
- [[wiki/modelling/phase-field|phase field]] · [[wiki/modelling/sharp-interface|sharp interface]] · [[wiki/modelling/CA-FE-models|CA FE models]]
- [[wiki/alloys/SCN-transparent-analog|SCN transparent analog]] — transparent analogue
- [[wiki/alloys/Al-Cu|Al Cu]] · [[wiki/alloys/Al-Si|Al Si]]
- [[wiki/methods/synchrotron-Xray|synchrotron Xray]] · [[wiki/methods/directional-solidification|directional solidification]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf|Becker 2023 — Al-Cu / Al-Ge equiaxed µg]] | Equiaxed nucleation/growth in thin Al-Cu / Al-Ge under µg |
| [[../Automatic Detection of Dendritic Microstructure Using Computer Vision Deep Learning Models Trained with Phase Field Simulations_VIARDIN.pdf|Viardin 2023 — CV/DL on phase-field dendrites]] | CV/DL segmentation of dendrites trained on phase-field data |
| [[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf|Härjer — Al-20Cu in-situ X-radiography]] | In-situ X-radiography of grain-refined Al-20Cu DS |
| [[../Three-dimensional investigation of fragment distribution in Al - 7 wt.percent Si solidified in microgravity_ABOUKHALIL.pdf|Aboukhalil — Al-7Si 3D fragment µg]] | 3D tomography of fragments in Al-7Si µg |
| [[../Freezing Shrinkage Dynamics and Surface Dendritic Growth of Floating Refractory Alloy Droplets in Outer Space_HAIPENG.pdf|Haipeng 2024 — refractory droplet freezing in space]] | Freezing shrinkage and surface dendrites on space-floated droplets |
| [[../Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation_BERGEON.pdf|Bergeon 2022 — µg vs 1g DS in-situ]] | Directly contrasts µg vs 1g directional solidification patterns |
| [[../In situ investigation of the Columnar-to-Equiaxed Transition during microgravity recoral solidification of Al-20 wt cu alloys on Earth_NGOMESSE.pdf|Ngomesse 2023 — Al-20Cu CET in-situ]] | In-situ CET observation in Al-20Cu, µg vs 1g |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*