---
title: "CFD simulation for space solidification"
category: method
tags: [method, CFD, OpenFOAM, multiphysics]
papers:
  - "[[../Process Microstructure Coupling in Reduced Gravity Laser Welding via Open-Source Multiphysics Simulation Framework_RAKIBUL.pdf]]"
  - "[[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf]]"
  - "[[../An Analysis of Solidification Experiments With a Ti-46AI-8Nb Alloy Under Centrifugal Conditions- Modelling of Flow-Solidification Interaction and Grain Structure Evolution Using a Cellular Automaton With Finite Volume Method_HUANG.pdf]]"
  - "[[../1D and 3D co-simulation and self-adaptive position control of electrostatic levitation in China's Space Station_ZHANG.pdf]]"
  - "[[../Spurious grain formation due to Marangoni convection during directional solidification of alloys in u-g environment of International Space Station_SEYED.pdf]]"
related:
  - "[[wiki/modelling/phase-field]]"
  - "[[wiki/modelling/sharp-interface]]"
  - "[[wiki/modelling/CA-FE-models]]"
  - "[[wiki/modelling/lattice-boltzmann]]"
  - "[[wiki/modelling/dimensionless-numbers]]"
  - "[[wiki/flow/marangoni-flow]]"
  - "[[wiki/flow/thermosolutal-convection]]"
  - "[[wiki/flow/residual-gravity-gjitter]]"
  - "[[wiki/alloys/Ti-alloys]]"
  - "[[wiki/alloys/Ni-superalloys]]"
  - "[[wiki/alloys/Al-Cu]]"
  - "[[wiki/alloys/Al-Si]]"
  - "[[wiki/platforms/ISM-strategy]]"
  - "[[wiki/platforms/containerless-EML]]"
  - "[[wiki/platforms/ISS-experiments]]"
created: 2026-04-18
---

# CFD simulation for space solidification

**Category:** method

---

## Overview

Macroscopic **CFD** (OpenFOAM, ANSYS Fluent, in-house) simulates melt-pool,
mushy-zone, and free-surface flows — with Marangoni/buoyancy coupling —
in AM, welding, and casting under space conditions. Paired with
[[wiki/modelling/phase-field|phase field]] / [[wiki/modelling/CA-FE-models|CA FE models]] for microstructure, the pipeline closes
process → structure → property.

## Key references

- [[../Process Microstructure Coupling in Reduced Gravity Laser Welding via Open-Source Multiphysics Simulation Framework_RAKIBUL.pdf|Rakibul 2024 — reduced-g laser welding]] — open multiphysics framework for
  reduced-g laser welding.
- [[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf|Viardin — mesoscopic hypergravity]] — CFD + meso model under
  hypergravity.
- [[../An Analysis of Solidification Experiments With a Ti-46AI-8Nb Alloy Under Centrifugal Conditions- Modelling of Flow-Solidification Interaction and Grain Structure Evolution Using a Cellular Automaton With Finite Volume Method_HUANG.pdf|Huang 2024 — Ti-46Al-8Nb CA-FVM centrifugal]] — CA-FVM flow–solidification
  coupling for Ti-46Al-8Nb.
- [[../1D and 3D co-simulation and self-adaptive position control of electrostatic levitation in China's Space Station_ZHANG.pdf|Zhang 2024 — ESL control on CSS]] — 1D/3D co-simulation of ESL control on CSS.
- [[../Spurious grain formation due to Marangoni convection during directional solidification of alloys in u-g environment of International Space Station_SEYED.pdf|Seyed — Marangoni-driven spurious grains ISS]] — CFD explains Marangoni-induced
  defect formation in ISS DS.

## Connected topics

- [[wiki/modelling/phase-field|phase field]] · [[wiki/modelling/sharp-interface|sharp interface]] · [[wiki/modelling/CA-FE-models|CA FE models]] · [[wiki/modelling/lattice-boltzmann|lattice boltzmann]] · [[wiki/modelling/dimensionless-numbers|dimensionless numbers]]
- [[wiki/flow/marangoni-flow|marangoni flow]] · [[wiki/flow/thermosolutal-convection|thermosolutal convection]] · [[wiki/flow/residual-gravity-gjitter|residual gravity gjitter]]
- [[wiki/alloys/Ti-alloys|Ti alloys]] · [[wiki/alloys/Ni-superalloys|Ni superalloys]] · [[wiki/alloys/Al-Cu|Al Cu]] · [[wiki/alloys/Al-Si|Al Si]]
- [[wiki/platforms/ISM-strategy|ISM strategy]] · [[wiki/platforms/containerless-EML|containerless EML]] · [[wiki/platforms/ISS-experiments|ISS experiments]]

## Papers from `papers/` folder

| Paper | Key finding |
|-------|-------------|
| [[../Process Microstructure Coupling in Reduced Gravity Laser Welding via Open-Source Multiphysics Simulation Framework_RAKIBUL.pdf|Rakibul 2024 — reduced-g laser welding]] | Open multiphysics framework for reduced-g laser welding |
| [[../Mesoscopic modeling of equiaxed and columnar solidification microstructures under forced flow and buoyancy-driven flow in hypergravity_VIARDIN.pdf|Viardin — mesoscopic hypergravity]] | Mesoscopic CET modelling under forced+buoyant flow |
| [[../An Analysis of Solidification Experiments With a Ti-46AI-8Nb Alloy Under Centrifugal Conditions- Modelling of Flow-Solidification Interaction and Grain Structure Evolution Using a Cellular Automaton With Finite Volume Method_HUANG.pdf|Huang 2024 — Ti-46Al-8Nb CA-FVM centrifugal]] | CA-FVM of flow–solidification in Ti-46Al-8Nb centrifugal casting |
| [[../1D and 3D co-simulation and self-adaptive position control of electrostatic levitation in China's Space Station_ZHANG.pdf|Zhang 2024 — ESL control on CSS]] | Self-adaptive position control of ESL levitator on Tiangong |
| [[../Spurious grain formation due to Marangoni convection during directional solidification of alloys in u-g environment of International Space Station_SEYED.pdf|Seyed — Marangoni-driven spurious grains ISS]] | Marangoni convection creates spurious grains on ISS DS |

---
*Last updated: 2026-04-18 · Auto-generated via LLM Wiki*