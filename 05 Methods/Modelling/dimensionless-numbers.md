---
title: "Dimensionless numbers (Ra, Ma, Pe, Pr, Le, Gr, Bo)"
category: modelling
tags: [dimensionless, scaling, Rayleigh, Marangoni, Peclet]
papers:
  - "[[../A review on solidification of alloys under hypergravity_FANGJIE.pdf]]"
  - "[[../Analysis of the Solidification Process of Metal Alloys Under Microgravity Conditions_FREDRIKSSON.pdf]]"
  - "[[../In-situ X-ray monitoring of solidification and related processes of metal alloys_REINHART.pdf]]"
related:
  - "[[wiki/flow/marangoni-flow]]"
  - "[[wiki/flow/thermosolutal-convection]]"
  - "[[wiki/flow/residual-gravity-gjitter]]"
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/physics/freckle-segregation]]"
  - "[[wiki/modelling/phase-field]]"
  - "[[wiki/modelling/sharp-interface]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/modelling/lattice-boltzmann]]"
  - "[[wiki/methods/CFD-simulation]]"
created: 2026-04-18
---

# Dimensionless numbers (Ra, Ma, Pe, Pr, Le, Gr, Bo)

**Category:** modelling

---

## Overview

A compact cheat-sheet for the non-dimensional groups that classify the
regimes discussed in this wiki.

| Number | Definition | Physics |
|--------|-----------|---------|
| **Pe** | V·L/D | Advection vs diffusion (dendrite tip) |
| **Pr** | ν/α | Momentum vs thermal diffusivity |
| **Le** | α/D | Thermal vs solutal diffusivity (≫1 for metals) |
| **Gr** | g·β·ΔT·L³/ν² | Buoyant vs viscous |
| **Ra** | Gr·Pr | Thermal buoyancy driver |
| **Ra_C** | g·β_C·ΔC·L³/(ν·D) | Solutal buoyancy driver |
| **Ma** | −(∂σ/∂T)·ΔT·L/(µ·α) | Thermocapillary driver |
| **Bo_d** | Ra/Ma | Buoyancy vs Marangoni |
| **Sc** | ν/D | Momentum vs solutal diffusivity |
| **We** | ρ·V²·L/σ | Inertia vs capillary (droplets) |

## Space takeaways

Lowering g by ~10⁶ drops **Ra → 0** but leaves **Ma** unchanged — so
Marangoni and g-jitter dominate the residual µg flow field. Hypergravity
[[../A review on solidification of alloys under hypergravity_FANGJIE.pdf|Fangjie 2023 — hypergravity review]] inverts this: Ra increases, Ma
essentially fixed.

## Connected topics

- [[wiki/flow/marangoni-flow|marangoni flow]] · [[wiki/flow/thermosolutal-convection|thermosolutal convection]] · [[wiki/flow/residual-gravity-gjitter|residual gravity gjitter]]
- [[wiki/physics/solidification|solidification]] · [[wiki/physics/mushy-zone|mushy zone]] · [[wiki/physics/nucleation-CET|nucleation CET]] · [[wiki/physics/freckle-segregation|freckle segregation]]
- [[wiki/modelling/phase-field|phase field]] · [[wiki/modelling/sharp-interface|sharp interface]] · [[wiki/modelling/CA-FE-models|CA FE models]] · [[wiki/modelling/lattice-boltzmann|lattice boltzmann]] · [[wiki/methods/CFD-simulation|CFD simulation]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../A review on solidification of alloys under hypergravity_FANGJIE.pdf|Fangjie 2023 — hypergravity review]] | Review of solidification under hypergravity (centrifuge) |
| [[../Analysis of the Solidification Process of Metal Alloys Under Microgravity Conditions_FREDRIKSSON.pdf|Fredriksson — µg solidification analysis]] | Analytic framework for solidification of metals in µg |
| [[../In-situ X-ray monitoring of solidification and related processes of metal alloys_REINHART.pdf|Reinhart — in-situ X-ray review]] | Review of in-situ X-ray monitoring in alloy solidification |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*