---
title: "In-Space Manufacturing (ISM) strategy"
category: platform
tags: [ISM, strategy, AM, ISRU, space-manufacturing]
papers:
  - "[[../A comprehensive review on metal laser additive manufacturing in space- Modeling and perspectives_MITRA.pdf]]"
  - "[[../Research Progress of Metal Additive Manufacturing Technology and Application in Space- A Review_XUNZUO.pdf]]"
  - "[[../Additive Manufacturing Under Lunar Gravity and Microgravity_REITZ.pdf]]"
  - "[[../Additive manufacturing of metallic glass from powder in space_NEUMANN.pdf]]"
  - "[[../Process Microstructure Coupling in Reduced Gravity Laser Welding via Open-Source Multiphysics Simulation Framework_RAKIBUL.pdf]]"
  - "[[../Comparison study of ductile iron produced with Martian regolith harvested iron from ionic liquids and Bosch byproduct carbon for in-situ resource utilization versus commercially available 65-45-12 ductile iron_BLAKE.pdf]]"
  - "[[../System analysis of an ISRU production plant- Extraction of metals and oxygen from lunar regolith_FRANCISCO.pdf]]"
  - "[[../Recent Progress in Space Science and Applications on Chinese Space Station in 2022-2024_YIDONG.pdf]]"
related:
  - "[[wiki/platforms/commercial-ISM-Varda]]"
  - "[[wiki/platforms/ISS-experiments]]"
  - "[[wiki/platforms/containerless-EML]]"
  - "[[wiki/physics/solidification]]"
  - "[[wiki/physics/nucleation-CET]]"
  - "[[wiki/flow/marangoni-flow]]"
  - "[[wiki/methods/CFD-simulation]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/modelling/phase-field]]"
  - "[[wiki/modelling/sharp-interface]]"
  - "[[wiki/alloys/Ni-superalloys]]"
  - "[[wiki/alloys/Ti-alloys]]"
  - "[[wiki/alloys/Al-Cu]]"
  - "[[wiki/alloys/Al-Si]]"
created: 2026-04-18
---

# In-Space Manufacturing (ISM) strategy

**Category:** platform

---

## Overview

**In-Space Manufacturing (ISM)** is the umbrella program for
fabricating or repairing metal parts in orbit, on the Moon, and on
Mars. Two dominant technology families:

1. **Laser / electron-beam AM** — [[../A comprehensive review on metal laser additive manufacturing in space- Modeling and perspectives_MITRA.pdf|Mitra 2024 — laser AM in space review]],
   [[../Research Progress of Metal Additive Manufacturing Technology and Application in Space- A Review_XUNZUO.pdf|Xunzuo 2024 — metal AM in space review]], [[../Process Microstructure Coupling in Reduced Gravity Laser Welding via Open-Source Multiphysics Simulation Framework_RAKIBUL.pdf|Rakibul 2024 — reduced-g laser welding]].
2. **ISRU metallurgy** using lunar / Martian regolith —
   [[../Comparison study of ductile iron produced with Martian regolith harvested iron from ionic liquids and Bosch byproduct carbon for in-situ resource utilization versus commercially available 65-45-12 ductile iron_BLAKE.pdf|Blake 2024 — ISRU ductile iron]], [[../System analysis of an ISRU production plant- Extraction of metals and oxygen from lunar regolith_FRANCISCO.pdf|Francisco — ISRU lunar plant analysis]].

## Microgravity + hypogravity testbeds

- Parabolic flights & lunar-g AM — [[../Additive Manufacturing Under Lunar Gravity and Microgravity_REITZ.pdf|Reitz 2021 — AM under lunar-g / µg]].
- BMG powder AM in space — [[../Additive manufacturing of metallic glass from powder in space_NEUMANN.pdf|Neumann 2023 — BMG powder AM in space]].
- CSS space-science progress — [[../Recent Progress in Space Science and Applications on Chinese Space Station in 2022-2024_YIDONG.pdf|Yidong 2024 — CSS space-science progress]].

## Physics hooks

Every ISM process is ultimately a constrained [[wiki/physics/solidification|solidification]]
problem dominated by [[wiki/flow/marangoni-flow|marangoni flow]] + [[wiki/flow/thermosolutal-convection|thermosolutal convection]] flow
with strong [[wiki/flow/residual-gravity-gjitter|residual gravity gjitter]] sensitivity. Models reuse the full
[[wiki/modelling/phase-field|phase field]] → [[wiki/modelling/CA-FE-models|CA FE models]] → [[wiki/methods/CFD-simulation|CFD simulation]] stack validated against ISS /
CSS benchmarks.

## Connected topics

- [[wiki/platforms/commercial-ISM-Varda|commercial ISM Varda]] · [[wiki/platforms/ISS-experiments|ISS experiments]] · [[wiki/platforms/containerless-EML|containerless EML]]
- [[wiki/physics/solidification|solidification]] · [[wiki/physics/nucleation-CET|nucleation CET]] · [[wiki/flow/marangoni-flow|marangoni flow]]
- [[wiki/methods/CFD-simulation|CFD simulation]] · [[wiki/modelling/CA-FE-models|CA FE models]] · [[wiki/modelling/phase-field|phase field]] · [[wiki/modelling/sharp-interface|sharp interface]]
- [[wiki/alloys/Ni-superalloys|Ni superalloys]] · [[wiki/alloys/Ti-alloys|Ti alloys]] · [[wiki/alloys/Al-Cu|Al Cu]] · [[wiki/alloys/Al-Si|Al Si]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../A comprehensive review on metal laser additive manufacturing in space- Modeling and perspectives_MITRA.pdf|Mitra 2024 — laser AM in space review]] | Comprehensive review of metal laser AM modelling for space |
| [[../Research Progress of Metal Additive Manufacturing Technology and Application in Space- A Review_XUNZUO.pdf|Xunzuo 2024 — metal AM in space review]] | Broad review of metal AM progress & application in space |
| [[../Additive Manufacturing Under Lunar Gravity and Microgravity_REITZ.pdf|Reitz 2021 — AM under lunar-g / µg]] | Parabolic-flight AM under lunar- and micro-gravity |
| [[../Additive manufacturing of metallic glass from powder in space_NEUMANN.pdf|Neumann 2023 — BMG powder AM in space]] | Metallic-glass powder AM demonstrated in space |
| [[../Process Microstructure Coupling in Reduced Gravity Laser Welding via Open-Source Multiphysics Simulation Framework_RAKIBUL.pdf|Rakibul 2024 — reduced-g laser welding]] | Open multiphysics framework for reduced-g laser welding |
| [[../Comparison study of ductile iron produced with Martian regolith harvested iron from ionic liquids and Bosch byproduct carbon for in-situ resource utilization versus commercially available 65-45-12 ductile iron_BLAKE.pdf|Blake 2024 — ISRU ductile iron]] | Ductile iron from Mars regolith iron + Bosch carbon (ISRU) |
| [[../System analysis of an ISRU production plant- Extraction of metals and oxygen from lunar regolith_FRANCISCO.pdf|Francisco — ISRU lunar plant analysis]] | System analysis for metals/O2 extraction from lunar regolith |
| [[../Recent Progress in Space Science and Applications on Chinese Space Station in 2022-2024_YIDONG.pdf|Yidong 2024 — CSS space-science progress]] | Survey of CSS space-science/applications 2022–2024 |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*