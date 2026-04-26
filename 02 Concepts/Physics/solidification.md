---
title: "Solidification"
category: physics
tags: [physics, solidification, microgravity, review]
papers:
  - "[[../Analysis of the Solidification Process of Metal Alloys Under Microgravity Conditions_FREDRIKSSON.pdf]]"
  - "[[../In-situ X-ray monitoring of solidification and related processes of metal alloys_REINHART.pdf]]"
  - "[[../Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation_BERGEON.pdf]]"
  - "[[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf]]"
  - "[[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf]]"
  - "[[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf]]"
  - "[[../Comparative study of gravity effects in directional solidification of Al-3.5 wt.percent Si and Al-10 wt.percent Cu alloys_GUIYUAN.pdf]]"
  - "[[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf]]"
  - "[[../In situ investigation of the Columnar-to-Equiaxed Transition during microgravity recoral solidification of Al-20 wt cu alloys on Earth_NGOMESSE.pdf]]"
  - "[[../Influence of Gravity on Atomic Mobility in a Liquid_ELKE.pdf]]"
related:
  - "[[wiki/physics/dendritic-growth]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/physics/eutectic-solidification]]"
  - "[[wiki/physics/freckle-segregation]]"
  - "[[wiki/flow/marangoni-flow]]"
  - "[[wiki/flow/thermosolutal-convection]]"
  - "[[wiki/flow/residual-gravity-gjitter]]"
  - "[[wiki/modelling/phase-field]]"
  - "[[wiki/modelling/sharp-interface]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/alloys/Al-Cu]]"
  - "[[wiki/alloys/Al-Si]]"
  - "[[wiki/alloys/SCN-transparent-analog]]"
  - "[[wiki/platforms/ISS-experiments]]"
  - "[[wiki/platforms/sounding-rockets]]"
  - "[[wiki/platforms/containerless-EML]]"
  - "[[wiki/methods/synchrotron-Xray]]"
  - "[[wiki/methods/directional-solidification]]"
created: 2026-04-18
---

# Solidification

**Category:** physics  
**Key researchers:** [[wiki/authors/Alain-Karma]], [[wiki/authors/Christoph-Beckermann]], [[wiki/authors/Rohit-Trivedi]], [[wiki/authors/Martin-Glicksman]]  
**Platforms studied on:** [[wiki/platforms/ISS-experiments]], [[wiki/platforms/CETSOL-MICAST-ICESOL]], [[wiki/platforms/sounding-rockets]]

---

## Overview

**Solidification** is the liquid→solid phase change that governs grain
morphology, segregation, defect formation, and ultimately the mechanical
properties of every cast, welded, or 3D-printed metal part produced for
[[wiki/platforms/ISM-strategy|In-Space Manufacturing]]. On Earth, buoyancy-driven
[[wiki/flow/thermosolutal-convection|thermosolutal convection]] and sedimentation perturb the diffusion field around
growing crystals. In microgravity these terms are ~10⁻⁴–10⁻⁶ g, so the
"pure diffusion + surface-tension + capillarity" textbook becomes
experimentally accessible — plus new residual flows appear
([[wiki/flow/marangoni-flow|marangoni flow]], [[wiki/flow/residual-gravity-gjitter|residual gravity gjitter]]).

## Key physical regimes

- **Pure diffusive growth** — the µg limit targeted by [[wiki/platforms/CETSOL-MICAST-ICESOL|CETSOL MICAST ICESOL]]
  and [[wiki/platforms/DECLIC-DSI|DECLIC DSI]].
- **Columnar** growth in an imposed thermal gradient → [[wiki/methods/directional-solidification|directional solidification]].
- **Equiaxed** nucleation + growth, often triggered by
  [[wiki/methods/grain-refinement|grain-refiner]] inoculation or fragment advection
  ([[wiki/physics/nucleation-CET|nucleation CET]]).
- **Eutectic** and **peritectic** co-growth ([[wiki/physics/eutectic-solidification|eutectic solidification]]).
- **Rapid solidification** in levitated droplets ([[wiki/platforms/containerless-EML|containerless EML]]).

## Controlling variables

Thermal gradient G, growth velocity V, alloy composition C₀,
[[wiki/modelling/dimensionless-numbers|Péclet & Lewis numbers]], and convective strength
(Rayleigh, Marangoni). On the ISS, G/V explores regions of the
Hunt / Kurz-Fisher CET diagrams inaccessible at 1 g.

## Why microgravity matters for ISM

[[../Analysis of the Solidification Process of Metal Alloys Under Microgravity Conditions_FREDRIKSSON.pdf|Fredriksson — µg solidification analysis]] and [[../In-situ X-ray monitoring of solidification and related processes of metal alloys_REINHART.pdf|Reinhart — in-situ X-ray review]]
lay out the case: by removing buoyancy, µg experiments isolate the
[[wiki/physics/nucleation-CET|nucleation CET]] mechanism, enabling *validated* [[wiki/modelling/phase-field|phase-field]] and
[[wiki/modelling/CA-FE-models|CA FE models]] models that can later be used to design
[[wiki/platforms/ISM-strategy|ISM processes]] such as in-orbit casting, laser welding, and
metal [[wiki/platforms/commercial-ISM-Varda|additive manufacturing]].

## Connected topics

- [[wiki/physics/dendritic-growth|dendritic growth]] — microscopic tip growth
- [[wiki/physics/mushy-zone|mushy zone]] — two-phase permeable zone
- [[wiki/physics/nucleation-CET|nucleation CET]] — columnar-to-equiaxed transition
- [[wiki/physics/eutectic-solidification|eutectic solidification]] — coupled two-solid growth
- [[wiki/physics/freckle-segregation|freckle segregation]] — convective segregation channels
- [[wiki/flow/marangoni-flow|marangoni flow]] — surface-tension flow
- [[wiki/flow/thermosolutal-convection|thermosolutal convection]] — buoyancy flow
- [[wiki/flow/residual-gravity-gjitter|residual gravity gjitter]] — residual g & jitter
- [[wiki/modelling/phase-field|phase field]] / [[wiki/modelling/sharp-interface|sharp interface]] / [[wiki/modelling/CA-FE-models|CA FE models]] — modelling hierarchy
- [[wiki/methods/directional-solidification|directional solidification]] — directional-solidification method
- [[wiki/methods/synchrotron-Xray|synchrotron Xray]] — in-situ imaging

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../Analysis of the Solidification Process of Metal Alloys Under Microgravity Conditions_FREDRIKSSON.pdf|Fredriksson — µg solidification analysis]] | Analytic framework for solidification of metals in µg |
| [[../In-situ X-ray monitoring of solidification and related processes of metal alloys_REINHART.pdf|Reinhart — in-situ X-ray review]] | Review of in-situ X-ray monitoring in alloy solidification |
| [[../Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation_BERGEON.pdf|Bergeon 2022 — µg vs 1g DS in-situ]] | Directly contrasts µg vs 1g directional solidification patterns |
| [[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf|Thomas 2023 — Al-Cu benchmark µg+1g]] | Canonical Al-Cu ISS benchmark for CET models |
| [[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf|Robin 2023 — sharp/progressive CET model]] | Concurrent sharp+progressive CET model vs µg DS |
| [[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf|Becker 2023 — Al-Cu / Al-Ge equiaxed µg]] | Equiaxed nucleation/growth in thin Al-Cu / Al-Ge under µg |
| [[../Comparative study of gravity effects in directional solidification of Al-3.5 wt.percent Si and Al-10 wt.percent Cu alloys_GUIYUAN.pdf|Guiyuan — Al-Si vs Al-Cu DS]] | Gravity effects compared for Al-Si and Al-Cu DS |
| [[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf|Härjer — Al-20Cu in-situ X-radiography]] | In-situ X-radiography of grain-refined Al-20Cu DS |
| [[../In situ investigation of the Columnar-to-Equiaxed Transition during microgravity recoral solidification of Al-20 wt cu alloys on Earth_NGOMESSE.pdf|Ngomesse 2023 — Al-20Cu CET in-situ]] | In-situ CET observation in Al-20Cu, µg vs 1g |
| [[../Influence of Gravity on Atomic Mobility in a Liquid_ELKE.pdf|Elke — gravity on liquid diffusion]] | Gravity modifies atomic mobility/diffusion in melts |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*