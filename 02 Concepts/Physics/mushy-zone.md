---
title: "Mushy zone"
category: physics
tags: [physics, mushy-zone, two-phase, permeability]
papers:
  - "[[../Spurious grain formation due to Marangoni convection during directional solidification of alloys in u-g environment of International Space Station_SEYED.pdf]]"
  - "[[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf]]"
  - "[[../Mesoscale Front Tracking Simulation of a Microgravity-based Isothermal Equiaxed Solidification Experiment of an Al20wt.percentCu Alloy performed on board the MASER 13 Sounding Rocket_MURPHY.pdf]]"
  - "[[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf]]"
  - "[[../Structures in grain-refined directionally solidified hypoeutectic Al-Cu alloys- Benchmark experiments under microgravity on-board the International Space Station_ZIMMERMANN.pdf]]"
related:
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/dendritic-growth]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/flow/thermosolutal-convection]]"
  - "[[wiki/physics/freckle-segregation]]"
  - "[[wiki/flow/marangoni-flow]]"
  - "[[wiki/modelling/sharp-interface]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/modelling/lattice-boltzmann]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/alloys/Al-Cu]]"
  - "[[wiki/alloys/Al-Si]]"
  - "[[wiki/platforms/ISS-experiments]]"
  - "[[wiki/platforms/CETSOL-MICAST-ICESOL]]"
  - "[[wiki/methods/directional-solidification]]"
created: 2026-04-18
---

# Mushy zone

**Category:** physics

---

## Overview

The **mushy zone** is the two-phase solid+liquid region between the
liquidus and solidus isotherms. It behaves as a porous medium with a
**permeability K(gs)** that plunges sharply as solid fraction grows —
classically Kozeny–Carman or Heinrich–Poirier expressions. Flow through
the mushy zone controls macrosegregation, freckle formation
([[wiki/physics/freckle-segregation|freckle segregation]]), and convective heat/solute transport
([[wiki/flow/thermosolutal-convection|thermosolutal convection]]).

## Why µg helps

Buoyancy vanishes → interdendritic liquid stays put → segregation signal
becomes mostly diffusive → ideal validation for
[[wiki/modelling/sharp-interface|sharp-interface]] / [[wiki/modelling/CA-FE-models|CA FE models]] codes.
[[../Spurious grain formation due to Marangoni convection during directional solidification of alloys in u-g environment of International Space Station_SEYED.pdf|Seyed — Marangoni-driven spurious grains ISS]] however shows **Marangoni flow still
persists** on ISS and creates spurious grains — µg is not a vacuum of
fluid dynamics.

## Key quantities

- Primary arm spacing **λ1** — Hunt / Kurz scaling.
- Secondary arm spacing **λ2** — Feurer-Wunderlin coarsening ∝ t^(1/3).
- Permeability K(gs) — calibrated via [[wiki/methods/synchrotron-Xray|X-ray radiography]].
- Local solid fraction gs — drives heat and solute advection terms.

## Connected topics

- [[wiki/physics/solidification|solidification]] · [[wiki/physics/dendritic-growth|dendritic growth]] · [[wiki/physics/nucleation-CET|nucleation CET]] · [[wiki/physics/freckle-segregation|freckle segregation]]
- [[wiki/flow/thermosolutal-convection|thermosolutal convection]] · [[wiki/flow/marangoni-flow|marangoni flow]]
- [[wiki/modelling/sharp-interface|sharp interface]] · [[wiki/modelling/CA-FE-models|CA FE models]] · [[wiki/modelling/lattice-boltzmann|lattice boltzmann]]
- [[wiki/alloys/Al-Cu|Al Cu]] · [[wiki/alloys/Al-Si|Al Si]]
- [[wiki/methods/directional-solidification|directional solidification]] · [[wiki/methods/synchrotron-Xray|synchrotron Xray]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../Spurious grain formation due to Marangoni convection during directional solidification of alloys in u-g environment of International Space Station_SEYED.pdf|Seyed — Marangoni-driven spurious grains ISS]] | Marangoni convection creates spurious grains on ISS DS |
| [[../Impact of gravity on directional solidification of refined Al-20wt.percentCu alloy investigated by in situ X-radiography_HARJER.pdf|Härjer — Al-20Cu in-situ X-radiography]] | In-situ X-radiography of grain-refined Al-20Cu DS |
| [[../Mesoscale Front Tracking Simulation of a Microgravity-based Isothermal Equiaxed Solidification Experiment of an Al20wt.percentCu Alloy performed on board the MASER 13 Sounding Rocket_MURPHY.pdf|Murphy — MASER-13 front-tracking Al-20Cu]] | Mesoscale front-tracking of MASER-13 Al-20Cu experiment |
| [[../Concurrent model for sharp and progressive columnar to equiaxed transitions validated by directional solidification experiments processed in microgravity conditions_ROBIN.pdf|Robin 2023 — sharp/progressive CET model]] | Concurrent sharp+progressive CET model vs µg DS |
| [[../Structures in grain-refined directionally solidified hypoeutectic Al-Cu alloys- Benchmark experiments under microgravity on-board the International Space Station_ZIMMERMANN.pdf|Zimmermann — grain-refined Al-Cu ISS]] | ISS benchmark on grain-refined hypoeutectic Al-Cu |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*