---
title: "Marangoni flow"
category: flow
tags: [Marangoni, surface-tension, free-surface, microgravity]
papers:
  - "[[../Spurious grain formation due to Marangoni convection during directional solidification of alloys in u-g environment of International Space Station_SEYED.pdf]]"
  - "[[../Metastable Liquid Properties and Surface Flow Patterns of Ultrahigh Temperature Alloys Explored In Outer Space_WANG.pdf]]"
  - "[[../Spiral eutectic growth dynamics facilitated by space Marangoni convection and liquid surface wave_HAIPENG.pdf]]"
  - "[[../Dynamic Localization Effect of Dendritic and Eutectic Growth Patterns Stimulated by Space Fluid Flow_LIAO.pdf]]"
  - "[[../Electromagnetic levitation containerless processing of metallic materials in microgravity- rapid solidification_MATSON.pdf]]"
  - "[[../Electromagnetic levitation containerless processing of metallic materials in microgravity- thermophysical properties_MOHR.pdf]]"
related:
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/mushy-zone]]"
  - "[[wiki/physics/freckle-segregation]]"
  - "[[wiki/physics/eutectic-solidification]]"
  - "[[wiki/flow/thermosolutal-convection]]"
  - "[[wiki/flow/marangoni-oscillations]]"
  - "[[wiki/flow/residual-gravity-gjitter]]"
  - "[[wiki/platforms/containerless-EML]]"
  - "[[wiki/platforms/ISS-experiments]]"
  - "[[wiki/platforms/CETSOL-MICAST-ICESOL]]"
  - "[[wiki/methods/CFD-simulation]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/modelling/lattice-boltzmann]]"
  - "[[wiki/alloys/Al-Cu]]"
  - "[[wiki/alloys/Ti-alloys]]"
  - "[[wiki/alloys/Ni-superalloys]]"
created: 2026-04-18
---

# Marangoni flow

**Category:** flow

---

## Overview

**Marangoni (thermocapillary / solutocapillary) flow** is driven by
surface-tension gradients, not by gravity, so it **survives in µg** and
often dominates once buoyancy is suppressed. Characteristic number:

**Ma = − (∂σ/∂T) · ΔT · L / (µ · α)**

and the dynamic-to-buoyant ratio **Bo_d = Ra/Ma ∝ g**.

## Where it matters for this wiki

- **ISS DS ingots** — [[../Spurious grain formation due to Marangoni convection during directional solidification of alloys in u-g environment of International Space Station_SEYED.pdf|Seyed — Marangoni-driven spurious grains ISS]] shows Marangoni
  flow at the melt free surface seeds spurious grains during
  directional solidification.
- **Levitated droplets** — surface flow patterns on UHT alloys
  ([[../Metastable Liquid Properties and Surface Flow Patterns of Ultrahigh Temperature Alloys Explored In Outer Space_WANG.pdf|Wang — UHT alloys & Marangoni in space]]) and on EML/ESL samples
  ([[../Electromagnetic levitation containerless processing of metallic materials in microgravity- rapid solidification_MATSON.pdf|Matson — ISS-EML rapid solidification]], [[../Electromagnetic levitation containerless processing of metallic materials in microgravity- thermophysical properties_MOHR.pdf|Mohr — ISS-EML thermophysical properties]]).
- **Eutectic patterns** — drives spiral eutectic growth
  ([[../Spiral eutectic growth dynamics facilitated by space Marangoni convection and liquid surface wave_HAIPENG.pdf|Haipeng — spiral eutectic via Marangoni]]) and pattern localization
  ([[../Dynamic Localization Effect of Dendritic and Eutectic Growth Patterns Stimulated by Space Fluid Flow_LIAO.pdf|Liao 2024 — space flow on dendritic/eutectic growth]]).

## Coupling

In real µg runs Marangoni couples with [[wiki/flow/residual-gravity-gjitter|residual gravity gjitter]] and residual
[[wiki/flow/thermosolutal-convection|thermosolutal convection]]. CFD/[[wiki/modelling/lattice-boltzmann|lattice boltzmann]] models must include surface
tracking and σ(T, C) constitutive laws.

## Connected topics

- [[wiki/physics/solidification|solidification]] · [[wiki/physics/mushy-zone|mushy zone]] · [[wiki/physics/freckle-segregation|freckle segregation]] · [[wiki/physics/eutectic-solidification|eutectic solidification]]
- [[wiki/flow/thermosolutal-convection|thermosolutal convection]] · [[wiki/flow/marangoni-oscillations|marangoni oscillations]] · [[wiki/flow/residual-gravity-gjitter|residual gravity gjitter]]
- [[wiki/platforms/containerless-EML|containerless EML]] · [[wiki/platforms/ISS-experiments|ISS experiments]] · [[wiki/platforms/CETSOL-MICAST-ICESOL|CETSOL MICAST ICESOL]]
- [[wiki/methods/CFD-simulation|CFD simulation]] · [[wiki/modelling/dimensionless-numbers|dimensionless numbers]] · [[wiki/modelling/lattice-boltzmann|lattice boltzmann]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../Spurious grain formation due to Marangoni convection during directional solidification of alloys in u-g environment of International Space Station_SEYED.pdf|Seyed — Marangoni-driven spurious grains ISS]] | Marangoni convection creates spurious grains on ISS DS |
| [[../Metastable Liquid Properties and Surface Flow Patterns of Ultrahigh Temperature Alloys Explored In Outer Space_WANG.pdf|Wang — UHT alloys & Marangoni in space]] | Metastable-liquid surface Marangoni patterns on UHT alloys |
| [[../Spiral eutectic growth dynamics facilitated by space Marangoni convection and liquid surface wave_HAIPENG.pdf|Haipeng — spiral eutectic via Marangoni]] | Space Marangoni drives spiral eutectic growth |
| [[../Dynamic Localization Effect of Dendritic and Eutectic Growth Patterns Stimulated by Space Fluid Flow_LIAO.pdf|Liao 2024 — space flow on dendritic/eutectic growth]] | Space fluid flow localizes dendritic and eutectic growth |
| [[../Electromagnetic levitation containerless processing of metallic materials in microgravity- rapid solidification_MATSON.pdf|Matson — ISS-EML rapid solidification]] | ISS-EML rapid solidification of industrial alloys |
| [[../Electromagnetic levitation containerless processing of metallic materials in microgravity- thermophysical properties_MOHR.pdf|Mohr — ISS-EML thermophysical properties]] | Density, viscosity, surface tension via ISS-EML |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*