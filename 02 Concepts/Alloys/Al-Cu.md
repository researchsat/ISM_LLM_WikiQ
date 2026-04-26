---
title: "Al-Cu alloys"
category: alloy
tags: [alloy, Al-Cu, solidification, microgravity, benchmark]
papers:
  - "[[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf]]"
  - "[[../Structures in grain-refined directionally solidified hypoeutectic Al-Cu alloys- Benchmark experiments under microgravity on-board the International Space Station_ZIMMERMANN.pdf]]"
  - "[[../In situ investigation of the Columnar-to-Equiaxed Transition during microgravity recoral solidification of Al-20 wt cu alloys on Earth_NGOMESSE.pdf]]"
  - "[[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf]]"
  - "[[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf]]"
  - "[[../Mesoscale Front Tracking Simulation of a Microgravity-based Isothermal Equiaxed Solidification Experiment of an Al20wt.percentCu Alloy performed on board the MASER 13 Sounding Rocket_MURPHY.pdf]]"
  - "[[../The Effect of g-Level Fluctuations on Equiaxed Solidification of an Al-20wt.percentCu Alloy in Microgravity_GENG.pdf]]"
  - "[[../Comparative study of gravity effects in directional solidification of Al-3.5 wt.percent Si and Al-10 wt.percent Cu alloys_GUIYUAN.pdf]]"
  - "[[../Gravity and Composition Modulated Solidification and Mechanical Properties of Al-Cu Nanostructures_APURBA.pdf]]"
  - "[[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf]]"
related:
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/dendritic-growth]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/physics/freckle-segregation]]"
  - "[[wiki/flow/thermosolutal-convection]]"
  - "[[wiki/flow/residual-gravity-gjitter]]"
  - "[[wiki/modelling/phase-field]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/modelling/sharp-interface]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/methods/directional-solidification]]"
  - "[[wiki/methods/grain-refinement]]"
  - "[[wiki/methods/synchrotron-Xray]]"
  - "[[wiki/platforms/ISS-experiments]]"
  - "[[wiki/platforms/CETSOL-MICAST-ICESOL]]"
  - "[[wiki/platforms/sounding-rockets]]"
  - "[[wiki/authors/Christoph-Beckermann]]"
  - "[[wiki/authors/Rohit-Trivedi]]"
  - "[[wiki/authors/ESA-researchers]]"
created: 2026-04-18
---

# Al-Cu alloys

**Category:** alloy  
**Key researchers:** [[wiki/authors/Christoph-Beckermann]], [[wiki/authors/Rohit-Trivedi]]  
**Platforms studied on:** [[wiki/platforms/ISS-experiments]], [[wiki/platforms/CETSOL-MICAST-ICESOL]], [[wiki/platforms/sounding-rockets]]

---

## Overview

Al-Cu is the **workhorse binary** for space solidification research:
simple eutectic phase diagram, well-known thermophysics, and strong
segregation contrast in X-radiography. Al-20 wt% Cu in particular is
the European [[wiki/platforms/CETSOL-MICAST-ICESOL|CETSOL/MICAST]] benchmark. Results here
are the touchstone for validating every CET model in the wiki.

## Key physical phenomena

- Columnar → equiaxed ([[wiki/physics/nucleation-CET|nucleation CET]]) controlled by grain-refiner
  density, G, V, and Rayleigh.
- [[wiki/physics/dendritic-growth|dendritic growth]] growth — thin-sample µg imaging.
- [[wiki/physics/freckle-segregation|freckle segregation]] channels strongly visible due to Cu rejection
  (k ≈ 0.17).
- [[wiki/flow/residual-gravity-gjitter|residual gravity gjitter]] sensitivity — confirmed on ISS.

## Space campaigns

| Paper | Platform | Angle |
|-------|----------|-------|
| [[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf|Thomas 2023 — Al-Cu benchmark µg+1g]] | [[wiki/platforms/ISS-experiments|ISS experiments]] / [[wiki/platforms/CETSOL-MICAST-ICESOL|CETSOL MICAST ICESOL]] | Benchmark |
| [[../Structures in grain-refined directionally solidified hypoeutectic Al-Cu alloys- Benchmark experiments under microgravity on-board the International Space Station_ZIMMERMANN.pdf|Zimmermann — grain-refined Al-Cu ISS]] | [[wiki/platforms/ISS-experiments|ISS experiments]] | Grain-refined hypoeutectic |
| [[../In situ investigation of the Columnar-to-Equiaxed Transition during microgravity recoral solidification of Al-20 wt cu alloys on Earth_NGOMESSE.pdf|Ngomesse 2023 — Al-20Cu CET in-situ]] | [[wiki/platforms/ISS-experiments|ISS experiments]] / Earth | In-situ CET |
| [[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf|Härjer — Al-20Cu in-situ X-radiography]] | [[wiki/platforms/ISS-experiments|ISS experiments]] / Earth | X-radiography |
| [[../Mesoscale Front Tracking Simulation of a Microgravity-based Isothermal Equiaxed Solidification Experiment of an Al20wt.percentCu Alloy performed on board the MASER 13 Sounding Rocket_MURPHY.pdf|Murphy — MASER-13 front-tracking Al-20Cu]] | [[wiki/platforms/sounding-rockets|MASER-13]] | Front tracking |
| [[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf|Becker 2023 — Al-Cu / Al-Ge equiaxed µg]] | [[wiki/platforms/ISS-experiments|ISS experiments]] | Thin-sample equiaxed |
| [[../The Effect of g-Level Fluctuations on Equiaxed Solidification of an Al-20wt.percentCu Alloy in Microgravity_GENG.pdf|Geng — g-jitter on Al-20Cu]] | [[wiki/platforms/ISS-experiments|ISS experiments]] | g-jitter sensitivity |

## Modelling hooks

[[wiki/modelling/phase-field|phase field]] for tip; [[wiki/modelling/CA-FE-models|CA FE models]] for grain structure; [[wiki/modelling/sharp-interface|sharp interface]]
front tracking (MASER-13); MD down to nanoscale
([[../Gravity and Composition Modulated Solidification and Mechanical Properties of Al-Cu Nanostructures_APURBA.pdf|Apurba — Al-Cu nanostructure MD]]).

## Connected topics

- [[wiki/physics/solidification|solidification]] · [[wiki/physics/dendritic-growth|dendritic growth]] · [[wiki/physics/nucleation-CET|nucleation CET]] · [[wiki/physics/freckle-segregation|freckle segregation]]
- [[wiki/flow/thermosolutal-convection|thermosolutal convection]] · [[wiki/flow/residual-gravity-gjitter|residual gravity gjitter]]
- [[wiki/modelling/phase-field|phase field]] · [[wiki/modelling/CA-FE-models|CA FE models]] · [[wiki/modelling/sharp-interface|sharp interface]]
- [[wiki/methods/directional-solidification|directional solidification]] · [[wiki/methods/grain-refinement|grain refinement]] · [[wiki/methods/synchrotron-Xray|synchrotron Xray]]
- [[wiki/platforms/ISS-experiments|ISS experiments]] · [[wiki/platforms/CETSOL-MICAST-ICESOL|CETSOL MICAST ICESOL]] · [[wiki/platforms/sounding-rockets|sounding rockets]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf|Thomas 2023 — Al-Cu benchmark µg+1g]] | Canonical Al-Cu ISS benchmark for CET models |
| [[../Structures in grain-refined directionally solidified hypoeutectic Al-Cu alloys- Benchmark experiments under microgravity on-board the International Space Station_ZIMMERMANN.pdf|Zimmermann — grain-refined Al-Cu ISS]] | ISS benchmark on grain-refined hypoeutectic Al-Cu |
| [[../In situ investigation of the Columnar-to-Equiaxed Transition during microgravity recoral solidification of Al-20 wt cu alloys on Earth_NGOMESSE.pdf|Ngomesse 2023 — Al-20Cu CET in-situ]] | In-situ CET observation in Al-20Cu, µg vs 1g |
| [[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf|Härjer — Al-20Cu in-situ X-radiography]] | In-situ X-radiography of grain-refined Al-20Cu DS |
| [[../Nucleation and Growth Dynamics of Equiaxed Dendrites in Thin Metallic Al-Cu and Al-Ge Samples in Microgravity and on Earth_BECKER.pdf|Becker 2023 — Al-Cu / Al-Ge equiaxed µg]] | Equiaxed nucleation/growth in thin Al-Cu / Al-Ge under µg |
| [[../Mesoscale Front Tracking Simulation of a Microgravity-based Isothermal Equiaxed Solidification Experiment of an Al20wt.percentCu Alloy performed on board the MASER 13 Sounding Rocket_MURPHY.pdf|Murphy — MASER-13 front-tracking Al-20Cu]] | Mesoscale front-tracking of MASER-13 Al-20Cu experiment |
| [[../The Effect of g-Level Fluctuations on Equiaxed Solidification of an Al-20wt.percentCu Alloy in Microgravity_GENG.pdf|Geng — g-jitter on Al-20Cu]] | g-jitter modifies equiaxed Al-20Cu solidification in µg |
| [[../Comparative study of gravity effects in directional solidification of Al-3.5 wt.percent Si and Al-10 wt.percent Cu alloys_GUIYUAN.pdf|Guiyuan — Al-Si vs Al-Cu DS]] | Gravity effects compared for Al-Si and Al-Cu DS |
| [[../Gravity and Composition Modulated Solidification and Mechanical Properties of Al-Cu Nanostructures_APURBA.pdf|Apurba — Al-Cu nanostructure MD]] | Gravity + composition effects on Al-Cu nanostructures (MD) |
| [[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf|Robin 2023 — sharp/progressive CET model]] | Concurrent sharp+progressive CET model vs µg DS |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*