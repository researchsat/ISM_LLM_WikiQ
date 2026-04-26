---
title: "Residual gravity & g-jitter"
category: flow
tags: [g-jitter, residual-gravity, microgravity, ISS]
papers:
  - "[[../The Effect of g-Level Fluctuations on Equiaxed Solidification of an Al-20wt.percentCu Alloy in Microgravity_GENG.pdf]]"
  - "[[../Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation_BERGEON.pdf]]"
  - "[[../Structures in grain-refined directionally solidified hypoeutectic Al-Cu alloys- Benchmark experiments under microgravity on-board the International Space Station_ZIMMERMANN.pdf]]"
  - "[[../Analysis of preparatory directional solidification experiments for a new X-ray facility for the International Space Station_REINHART.pdf]]"
  - "[[../XRISE-M- X-radiography facility for solidification and diffusion studies of alloys aboard sounding rockets_KARGL.pdf]]"
  - "[[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf]]"
related:
  - "[[wiki/flow/marangoni-flow]]"
  - "[[wiki/flow/thermosolutal-convection]]"
  - "[[wiki/flow/marangoni-oscillations]]"
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/physics/freckle-segregation]]"
  - "[[wiki/platforms/ISS-experiments]]"
  - "[[wiki/platforms/CETSOL-MICAST-ICESOL]]"
  - "[[wiki/platforms/sounding-rockets]]"
  - "[[wiki/platforms/DECLIC-DSI]]"
  - "[[wiki/methods/CFD-simulation]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/modelling/CA-FE-models]]"
created: 2026-04-18
---

# Residual gravity & g-jitter

**Category:** flow

---

## Overview

"Microgravity" is not zero-g. The ISS experiences quasi-steady residual
**g₀ ~ 10⁻⁶ g**, plus transient **g-jitter** from attitude changes,
exercise, dockings, and machinery, with spectral components up to
several Hz. g-jitter is random forcing on top of thermosolutal +
Marangoni flow and can re-introduce convective transport inside an
otherwise diffusive mushy zone.

## Key finding

[[../The Effect of g-Level Fluctuations on Equiaxed Solidification of an Al-20wt.percentCu Alloy in Microgravity_GENG.pdf|Geng — g-jitter on Al-20Cu]] explicitly shows that g-level fluctuations
modify equiaxed growth in Al-20Cu — meaning g-jitter must be considered
when interpreting the [[wiki/alloys/Al-Cu|Al-Cu]] ISS benchmarks
([[../Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_THOMAS.pdf|Thomas 2023 — Al-Cu benchmark µg+1g]]).

## Platform considerations

- [[wiki/platforms/sounding-rockets|Sounding rockets]] give shorter but cleaner µg
  (~10⁻⁴ g steady) — good for [[../XRISE-M- X-radiography facility for solidification and diffusion studies of alloys aboard sounding rockets_KARGL.pdf|Kargl — XRISE-M sounding rocket]] and MASER.
- [[wiki/platforms/ISS-experiments|ISS experiments]] gives long duration but noisier g-environment — matters
  for [[wiki/platforms/CETSOL-MICAST-ICESOL|CETSOL MICAST ICESOL]], [[wiki/platforms/DECLIC-DSI|DECLIC DSI]], XRMON campaigns.

## Connected topics

- [[wiki/flow/marangoni-flow|marangoni flow]] · [[wiki/flow/thermosolutal-convection|thermosolutal convection]] · [[wiki/flow/marangoni-oscillations|marangoni oscillations]]
- [[wiki/physics/solidification|solidification]] · [[wiki/physics/mushy-zone|mushy zone]] · [[wiki/physics/nucleation-CET|nucleation CET]] · [[wiki/physics/freckle-segregation|freckle segregation]]
- [[wiki/platforms/ISS-experiments|ISS experiments]] · [[wiki/platforms/CETSOL-MICAST-ICESOL|CETSOL MICAST ICESOL]] · [[wiki/platforms/sounding-rockets|sounding rockets]] · [[wiki/platforms/DECLIC-DSI|DECLIC DSI]]
- [[wiki/methods/CFD-simulation|CFD simulation]] · [[wiki/modelling/dimensionless-numbers|dimensionless numbers]] · [[wiki/modelling/CA-FE-models|CA FE models]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../The Effect of g-Level Fluctuations on Equiaxed Solidification of an Al-20wt.percentCu Alloy in Microgravity_GENG.pdf|Geng — g-jitter on Al-20Cu]] | g-jitter modifies equiaxed Al-20Cu solidification in µg |
| [[../Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation_BERGEON.pdf|Bergeon 2022 — µg vs 1g DS in-situ]] | Directly contrasts µg vs 1g directional solidification patterns |
| [[../Structures in grain-refined directionally solidified hypoeutectic Al-Cu alloys- Benchmark experiments under microgravity on-board the International Space Station_ZIMMERMANN.pdf|Zimmermann — grain-refined Al-Cu ISS]] | ISS benchmark on grain-refined hypoeutectic Al-Cu |
| [[../Analysis of preparatory directional solidification experiments for a new X-ray facility for the International Space Station_REINHART.pdf|Reinhart 2022 — XRMON-ISS prep]] | Ground-based preparation for new ISS X-ray facility (XRMON) |
| [[../XRISE-M- X-radiography facility for solidification and diffusion studies of alloys aboard sounding rockets_KARGL.pdf|Kargl — XRISE-M sounding rocket]] | XRISE-M sounding-rocket X-radiography facility |
| [[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf|Viardin — mesoscopic hypergravity]] | Mesoscopic CET modelling under forced+buoyant flow |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*