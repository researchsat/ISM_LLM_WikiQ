---
title: Metal Alloy Processing for In-Space Manufacturing MOC
aliases:
  - PhD Wiki Home
  - In-Space Manufacturing MOC
tags:
  - moc
  - phd
  - in-space-manufacturing
status: active
---

# Metal Alloy Processing for In-Space Manufacturing MOC

This is the home map for the PhD wiki on metal alloy solidification and manufacturing in space microgravity.

## Core Literature Review

- [[Interactive PhD Dashboard]]
- [[Earth 1g vs Microgravity Solidification Processing]]
- [[Validation Report]]

## Fundamentals

- [[Why Gravity Matters in Alloy Solidification]]
- [[Microgravity as a Diffusion-Controlled Benchmark]]
- [[Constitutional Undercooling]]
- [[Columnar-to-Equiaxed Transition]]
- [[Dendritic Growth]]
- [[Interdendritic Flow and Macrosegregation]]
- [[Marangoni Convection in Melt Pools]]

## Processing Routes

- [[Directional Solidification]]
- [[Containerless Electromagnetic Levitation]]
- [[Liquid-Solid Mixture Processing]]
- [[Immiscible Alloy Solidification]]
- [[In-Space Additive Manufacturing]]

## High-Priority Papers

- [[Analysis of gravity effects during binary alloy directional solidification]]
- [[Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth]]
- [[In situ investigation of CET during Al-20wtCu solidification]]
- [[Comparative study of Al-7wtSi directional solidification in Space and on Earth]]
- [[Directional solidification of Al-1.5wtNi under diffusion transport in space]]
- [[Precise Measurements of Liquid Ti64 Thermophysical Properties on ISS]]
- [[Effect of microgravity on Al-Bi-Sn immiscible alloys]]

## Evidence Tables

- `06 Data/Literature Review Extraction/paper-extraction-matrix.csv`
- `06 Data/Literature Review Extraction/numerical-data-extract.csv`
- `06 Data/Literature Review Extraction/comparison-data-earth-vs-microgravity.csv`
- `06 Data/Literature Review Extraction/comparison-data-summary-by-paper.csv`

## Imported Archive

- [[Archive Import Map]]
- [[Archive Index]]
- [[1_All_Papers_Database]]
- [[2_Review_Queue_and_Gaps]]
- [[3_Platforms_and_Alloys]]

## Current Writing Questions

- Which mechanisms make Earth 1g solidification non-transferable to microgravity processing maps?
- Which microgravity effects are fundamental physics, and which are artifacts of the facility?
- How can liquid-solid mixture processing reduce the risk of handling fully molten metal in space?
- Which alloy system should anchor the first experimental chapter?

## Dataview Starters

Papers to read:

```dataview
TABLE status, system, method, relevance
FROM "03 Papers"
SORT priority ASC
```

Concept notes:

```dataview
TABLE status, related
FROM "02 Concepts"
SORT file.name ASC
```
