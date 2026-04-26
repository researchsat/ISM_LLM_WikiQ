---
title: "Cellular-Automaton + Finite-Element (CA-FE) models"
category: modelling
tags: [CA-FE, cellular-automaton, grain-structure, mesoscale]
papers:
  - "[[../An Analysis of Solidification Experiments With a Ti-46AI-8Nb Alloy Under Centrifugal Conditions- Modelling of Flow-Solidification Interaction and Grain Structure Evolution Using a Cellular Automaton With Finite Volume Method_HUANG.pdf]]"
  - "[[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf]]"
  - "[[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf]]"
  - "[[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf]]"
related:
  - "[[wiki/modelling/phase-field]]"
  - "[[wiki/modelling/sharp-interface]]"
  - "[[wiki/methods/CFD-simulation]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/physics/dendritic-growth]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/physics/freckle-segregation]]"
  - "[[wiki/alloys/Al-Cu]]"
  - "[[wiki/alloys/Ti-alloys]]"
  - "[[wiki/alloys/Ni-superalloys]]"
  - "[[wiki/alloys/Al-Si]]"
  - "[[wiki/platforms/ISS-experiments]]"
  - "[[wiki/platforms/CETSOL-MICAST-ICESOL]]"
  - "[[wiki/authors/Christoph-Beckermann]]"
created: 2026-04-18
---

# Cellular-Automaton + Finite-Element (CA-FE) models

**Category:** modelling

---

## Overview

**CA-FE** (also CA-FVM, CA-FV) couples a finite-element / finite-volume
solver for heat and solute transport to a cellular-automaton model for
grain nucleation and envelope growth. It is the **grain-scale** engine
used for CET prediction in industrial DS and for space benchmarks.

## Representative papers

- [[../An Analysis of Solidification Experiments With a Ti-46AI-8Nb Alloy Under Centrifugal Conditions- Modelling of Flow-Solidification Interaction and Grain Structure Evolution Using a Cellular Automaton With Finite Volume Method_HUANG.pdf|Huang 2024 — Ti-46Al-8Nb CA-FVM centrifugal]] — Ti-46Al-8Nb with CA coupled to
  FVM under centrifugal conditions.
- [[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf|Viardin — mesoscopic hypergravity]] — mesoscopic CA-FE of equiaxed
  and columnar structures under hyper-g forced flow.
- [[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf|Robin 2023 — sharp/progressive CET model]] — sharp + progressive CET.
- [[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf|Thomas 2023 — Al-Cu benchmark µg+1g]] — used as experimental input for
  CA-FE calibration.

## Connected topics

- [[wiki/modelling/phase-field|phase field]] · [[wiki/modelling/sharp-interface|sharp interface]] · [[wiki/methods/CFD-simulation|CFD simulation]] · [[wiki/modelling/dimensionless-numbers|dimensionless numbers]]
- [[wiki/physics/solidification|solidification]] · [[wiki/physics/nucleation-CET|nucleation CET]] · [[wiki/physics/dendritic-growth|dendritic growth]] · [[wiki/physics/freckle-segregation|freckle segregation]]
- [[wiki/alloys/Al-Cu|Al Cu]] · [[wiki/alloys/Ti-alloys|Ti alloys]] · [[wiki/alloys/Ni-superalloys|Ni superalloys]] · [[wiki/alloys/Al-Si|Al Si]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../An Analysis of Solidification Experiments With a Ti-46AI-8Nb Alloy Under Centrifugal Conditions- Modelling of Flow-Solidification Interaction and Grain Structure Evolution Using a Cellular Automaton With Finite Volume Method_HUANG.pdf|Huang 2024 — Ti-46Al-8Nb CA-FVM centrifugal]] | CA-FVM of flow–solidification in Ti-46Al-8Nb centrifugal casting |
| [[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf|Viardin — mesoscopic hypergravity]] | Mesoscopic CET modelling under forced+buoyant flow |
| [[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf|Robin 2023 — sharp/progressive CET model]] | Concurrent sharp+progressive CET model vs µg DS |
| [[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf|Thomas 2023 — Al-Cu benchmark µg+1g]] | Canonical Al-Cu ISS benchmark for CET models |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*