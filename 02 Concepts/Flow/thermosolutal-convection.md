---
title: "Thermosolutal (double-diffusive) convection"
category: flow
tags: [buoyancy, double-diffusive, Ra, Le]
papers:
  - "[[../Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation_BERGEON.pdf]]"
  - "[[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf]]"
  - "[[../Comparative study of gravity effects in directional solidification of Al-3.5 wt.percent Si and Al-10 wt.percent Cu alloys_GUIYUAN.pdf]]"
  - "[[../Modification of the microstructure by rotating magnetic field during the solidification of Al-7 wt.percent Si alloy under microgravity_YUZE.pdf]]"
  - "[[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf]]"
  - "[[../A review on solidification of alloys under hypergravity_FANGJIE.pdf]]"
related:
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/physics/freckle-segregation]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/flow/marangoni-flow]]"
  - "[[wiki/flow/residual-gravity-gjitter]]"
  - "[[wiki/methods/CFD-simulation]]"
  - "[[wiki/modelling/lattice-boltzmann]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/alloys/Al-Cu]]"
  - "[[wiki/alloys/Al-Si]]"
  - "[[wiki/alloys/Pb-Sn]]"
  - "[[wiki/alloys/Ni-superalloys]]"
  - "[[wiki/platforms/ISS-experiments]]"
  - "[[wiki/platforms/CETSOL-MICAST-ICESOL]]"
  - "[[wiki/methods/directional-solidification]]"
  - "[[wiki/authors/Christoph-Beckermann]]"
created: 2026-04-18
---

# Thermosolutal (double-diffusive) convection

**Category:** flow

---

## Overview

Thermosolutal (double-diffusive) convection couples thermal and solutal
buoyancy through Lewis number **Le = α/D ≫ 1**. It is the main driver
of macrosegregation, freckles, and convective CET on Earth. µg sets
the thermal+solutal Rayleigh numbers toward zero, isolating diffusion.

## Key expressions

- Thermal Rayleigh **Ra_T = g β_T ΔT L³ / (ν α)**
- Solutal Rayleigh **Ra_C = g β_C ΔC L³ / (ν D)**
- Buoyancy ratio **N = Ra_C / Ra_T** — sign decides whether density
  stratification is stable or unstable (double-diffusive fingers).

## Microgravity vs hypergravity

- µg: [[../Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation_BERGEON.pdf|Bergeon 2022 — µg vs 1g DS in-situ]] and [[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf|Härjer — Al-20Cu in-situ X-radiography]]
  show morphology shifts as Ra is reduced.
- Hypergravity: [[../A review on solidification of alloys under hypergravity_FANGJIE.pdf|Fangjie 2023 — hypergravity review]] reviews enhanced
  convection and its use to probe the mushy zone, complemented by
  [[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf|Viardin — mesoscopic hypergravity]] mesoscopic modelling.

## Connected topics

- [[wiki/physics/solidification|solidification]] · [[wiki/physics/mushy-zone|mushy zone]] · [[wiki/physics/freckle-segregation|freckle segregation]] · [[wiki/physics/nucleation-CET|nucleation CET]]
- [[wiki/flow/marangoni-flow|marangoni flow]] · [[wiki/flow/residual-gravity-gjitter|residual gravity gjitter]]
- [[wiki/methods/CFD-simulation|CFD simulation]] · [[wiki/modelling/lattice-boltzmann|lattice boltzmann]] · [[wiki/modelling/dimensionless-numbers|dimensionless numbers]] · [[wiki/modelling/CA-FE-models|CA FE models]]
- [[wiki/alloys/Al-Cu|Al Cu]] · [[wiki/alloys/Al-Si|Al Si]] · [[wiki/alloys/Pb-Sn|Pb Sn]] · [[wiki/alloys/Ni-superalloys|Ni superalloys]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation_BERGEON.pdf|Bergeon 2022 — µg vs 1g DS in-situ]] | Directly contrasts µg vs 1g directional solidification patterns |
| [[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf|Härjer — Al-20Cu in-situ X-radiography]] | In-situ X-radiography of grain-refined Al-20Cu DS |
| [[../Comparative study of gravity effects in directional solidification of Al-3.5 wt.percent Si and Al-10 wt.percent Cu alloys_GUIYUAN.pdf|Guiyuan — Al-Si vs Al-Cu DS]] | Gravity effects compared for Al-Si and Al-Cu DS |
| [[../Modification of the microstructure by rotating magnetic field during the solidification of Al-7 wt.percent Si alloy under microgravity_YUZE.pdf|Yuze — RMF on Al-7Si µg]] | Rotating magnetic field modifies Al-7Si µg microstructure |
| [[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf|Viardin — mesoscopic hypergravity]] | Mesoscopic CET modelling under forced+buoyant flow |
| [[../A review on solidification of alloys under hypergravity_FANGJIE.pdf|Fangjie 2023 — hypergravity review]] | Review of solidification under hypergravity (centrifuge) |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*