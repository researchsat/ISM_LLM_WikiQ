---
title: "Sharp-interface and front-tracking models"
category: modelling
tags: [sharp-interface, front-tracking, level-set, solidification]
papers:
  - "[[../Mesoscale Front Tracking Simulation of a Microgravity-based Isothermal Equiaxed Solidification Experiment of an Al20wt.percentCu Alloy performed on board the MASER 13 Sounding Rocket_MURPHY.pdf]]"
  - "[[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf]]"
  - "[[../In-situ X-ray monitoring of solidification and related processes of metal alloys_REINHART.pdf]]"
related:
  - "[[wiki/modelling/phase-field]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/modelling/lattice-boltzmann]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/dendritic-growth]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/alloys/Al-Cu]]"
  - "[[wiki/alloys/Al-Si]]"
  - "[[wiki/authors/Christoph-Beckermann]]"
  - "[[wiki/authors/Rohit-Trivedi]]"
  - "[[wiki/platforms/sounding-rockets]]"
  - "[[wiki/platforms/ISS-experiments]]"
created: 2026-04-18
---

# Sharp-interface and front-tracking models

**Category:** modelling

---

## Overview

**Sharp-interface / front-tracking** models resolve the solid–liquid
boundary explicitly (level-set, VOF, Lagrangian markers). They are
cheaper than [[wiki/modelling/phase-field|phase-field]] at the mesoscale and are a
natural bridge to [[wiki/modelling/CA-FE-models|CA-FE]] grain-scale simulations.

## Examples in wiki

- [[../Mesoscale Front Tracking Simulation of a Microgravity-based Isothermal Equiaxed Solidification Experiment of an Al20wt.percentCu Alloy performed on board the MASER 13 Sounding Rocket_MURPHY.pdf|Murphy — MASER-13 front-tracking Al-20Cu]] — MASER-13 Al-20Cu mesoscopic
  front tracking.
- [[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf|Robin 2023 — sharp/progressive CET model]] — concurrent sharp + progressive CET
  model.
- [[../In-situ X-ray monitoring of solidification and related processes of metal alloys_REINHART.pdf|Reinhart — in-situ X-ray review]] — comparison basis against
  in-situ X-ray.

## Connected topics

- [[wiki/modelling/phase-field|phase field]] · [[wiki/modelling/CA-FE-models|CA FE models]] · [[wiki/modelling/lattice-boltzmann|lattice boltzmann]] · [[wiki/modelling/dimensionless-numbers|dimensionless numbers]]
- [[wiki/physics/solidification|solidification]] · [[wiki/physics/dendritic-growth|dendritic growth]] · [[wiki/physics/mushy-zone|mushy zone]] · [[wiki/physics/nucleation-CET|nucleation CET]]
- [[wiki/alloys/Al-Cu|Al Cu]] · [[wiki/alloys/Al-Si|Al Si]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../Mesoscale Front Tracking Simulation of a Microgravity-based Isothermal Equiaxed Solidification Experiment of an Al20wt.percentCu Alloy performed on board the MASER 13 Sounding Rocket_MURPHY.pdf|Murphy — MASER-13 front-tracking Al-20Cu]] | Mesoscale front-tracking of MASER-13 Al-20Cu experiment |
| [[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf|Robin 2023 — sharp/progressive CET model]] | Concurrent sharp+progressive CET model vs µg DS |
| [[../In-situ X-ray monitoring of solidification and related processes of metal alloys_REINHART.pdf|Reinhart — in-situ X-ray review]] | Review of in-situ X-ray monitoring in alloy solidification |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*