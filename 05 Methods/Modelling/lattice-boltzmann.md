---
title: "Lattice-Boltzmann methods (LBM)"
category: modelling
tags: [LBM, lattice-Boltzmann, mesoscale, porous]
papers:
  - "[[../Automatic Detection of Dendritic Microstructure Using Computer Vision Deep Learning Models Trained with Phase Field Simulations_VIARDIN.pdf]]"
  - "[[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf]]"
related:
  - "[[wiki/methods/CFD-simulation]]"
  - "[[wiki/modelling/phase-field]]"
  - "[[wiki/modelling/sharp-interface]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/flow/marangoni-flow]]"
  - "[[wiki/flow/thermosolutal-convection]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/physics/freckle-segregation]]"
created: 2026-04-18
---

# Lattice-Boltzmann methods (LBM)

**Category:** modelling

---

## Overview

**Lattice-Boltzmann (LBM)** is a kinetic-theory-based mesoscopic CFD
method excellent for simulating flow through the [[wiki/physics/mushy-zone|mushy zone]] zone,
free-surface problems, and multicomponent alloy convection. LBM pairs
well with [[wiki/modelling/phase-field|phase-field]] dendrite envelopes for
solidification under buoyancy or Marangoni.

## Wiki links

- [[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf|Viardin — mesoscopic hypergravity]] explicitly uses mesoscopic flow
  modelling to capture forced-flow CET under hypergravity.
- [[../Automatic Detection of Dendritic Microstructure Using Computer Vision Deep Learning Models Trained with Phase Field Simulations_VIARDIN.pdf|Viardin 2023 — CV/DL on phase-field dendrites]] leverages phase-field + flow synthetic
  data for ML training.

## Connected topics

- [[wiki/methods/CFD-simulation|CFD simulation]] · [[wiki/modelling/phase-field|phase field]] · [[wiki/modelling/sharp-interface|sharp interface]] · [[wiki/modelling/CA-FE-models|CA FE models]] · [[wiki/modelling/dimensionless-numbers|dimensionless numbers]]
- [[wiki/flow/marangoni-flow|marangoni flow]] · [[wiki/flow/thermosolutal-convection|thermosolutal convection]] · [[wiki/physics/mushy-zone|mushy zone]] · [[wiki/physics/freckle-segregation|freckle segregation]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../Automatic Detection of Dendritic Microstructure Using Computer Vision Deep Learning Models Trained with Phase Field Simulations_VIARDIN.pdf|Viardin 2023 — CV/DL on phase-field dendrites]] | CV/DL segmentation of dendrites trained on phase-field data |
| [[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf|Viardin — mesoscopic hypergravity]] | Mesoscopic CET modelling under forced+buoyant flow |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*