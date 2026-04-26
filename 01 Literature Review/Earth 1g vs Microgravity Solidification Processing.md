---
title: Earth 1g vs Microgravity Solidification Processing
aliases:
  - 1g vs microgravity solidification
  - gravity effects in alloy solidification
tags:
  - phd
  - literature-review
  - materials-science
  - microgravity
  - solidification
  - in-space-manufacturing
status: working-note
source_scope: local ReferencePapers PDFs parsed 2026-04-26
---

# Earth 1g vs Microgravity Solidification Processing

This note synthesizes the local `ReferencePapers` library for a PhD literature review on [[Metal Alloy Processing for In-Space Manufacturing]]. It focuses on the physical contrast between terrestrial alloy solidification and reduced-gravity solidification, especially where the papers provide numerical comparison data.

Generated evidence tables:

- `06 Data/Literature Review Extraction/paper-extraction-matrix.csv`: paper-level tags, method snippets, outcome snippets, and counts.
- `06 Data/Literature Review Extraction/numerical-data-extract.csv`: all automatically extracted numerical snippets with page numbers and gravity-context tags.
- `06 Data/Literature Review Extraction/comparison-data-earth-vs-microgravity.csv`: filtered numerical snippets where the surrounding text mentions Earth/1g, microgravity, space, ISS, sounding rockets, or direct comparison.
- `06 Data/Literature Review Extraction/comparison-data-summary-by-paper.csv`: count summary by paper, topic, and gravity context.

Extraction caveat: the CSVs are automated pypdf extractions. They are good for discovery and audit trails, but values used in thesis prose should be checked against the original PDF figures/tables.

## Central Thesis

On Earth, solidification is rarely governed by pure heat and solute diffusion because buoyancy couples thermal gradients, solutal gradients, density inversion, solid-particle transport, and shrinkage feeding into the evolving mushy zone. In microgravity, the buoyancy term is strongly suppressed, so alloy solidification moves closer to a diffusion-controlled benchmark. That makes microgravity scientifically valuable because it isolates intrinsic dendrite, cellular, eutectic, monotectic, nucleation, and phase-selection mechanisms. It also creates manufacturing challenges: without buoyancy drainage or hydrostatic settling, gas bubbles, free surfaces, Marangoni stresses, shrinkage flow, electromagnetic forces, and residual accelerations become proportionally more important.

## Mechanism-Level Comparison

| Topic | Earth 1g Processing | Microgravity Processing | Review Implication |
|---|---|---|---|
| Momentum transport | Buoyancy enters the momentum equation through thermal and solutal density differences. Natural convection can dominate solute redistribution. | Buoyancy-driven convection is suppressed, but not all flow disappears. Residual acceleration, Marangoni flow, electromagnetic forcing, shrinkage, and g-jitter can remain. | Do not equate microgravity with "no convection"; write "reduced buoyancy convection" unless the paper demonstrates diffusion control. |
| Heat transfer | Melt flow can alter thermal boundary layers and interface shape. Radial heat loss often drives thermosolutal loops. | Heat transfer is closer to conductive/radiative control, especially in containerless or well-designed directional experiments. | Microgravity experiments are benchmark cases for validating heat-transfer boundary conditions in simulations. |
| Solute transport | Convective solute transport distorts constitutional undercooling, cellular/dendritic spacing, and macrosegregation. | Solute boundary layers are closer to diffusion length scales such as `D/V`; steady state can be more interpretable. | Use microgravity as the reference case for intrinsic spacing selection and macrosegregation models. |
| Solid transport | Equiaxed grains, dendrite fragments, and droplets sediment or float depending on density contrast. | Grain motion by buoyancy is reduced; motion can still occur by shrinkage flow, thermocapillary flow, or collisions. | For CET, distinguish "nucleation ahead of front" from "transport of grains after nucleation." |
| Interface morphology | Convection shifts planar-cellular-dendritic thresholds, bends isotherms, changes primary spacing distributions, and localizes microstructure. | Interface patterns become more uniform and often more comparable with diffusion-limited theory, but residual flow can still destabilize. | Useful comparison language: microgravity exposes the diffusive baseline; 1g shows the convective perturbation. |
| Macrosegregation | Strongly affected by interdendritic flow, shrinkage feeding, thermal-solutal convection, and detached grains. | Reduced buoyancy decreases many macrosegregation modes, but geometry, wall contact, and residual acceleration remain. | Compare macrosegregation by geometry, alloy density inversion, and growth orientation, not just gravity label. |
| Container interaction | Hydrostatic pressure and wetting/contact with crucibles affect defects and impurity uptake. | Detached solidification and levitated processing can reduce wall contact and contamination. | Relevant to in-space manufacturing because containerless or semi-solid routes may reduce contamination and handling risk. |

## Governing Fundamentals To Anchor The Literature Review

Use these as the conceptual scaffold for the review.

1. [[Navier-Stokes With Buoyancy]]: in terrestrial processing, the Boussinesq term scales as `rho * g * (beta_T * Delta T + beta_C * Delta C)`. In microgravity, `g` is reduced by orders of magnitude, so the balance shifts toward viscosity, capillarity, externally driven flow, and diffusion.

2. [[Rayleigh and Grashof Numbers in Solidification]]: the thermal Rayleigh/Grashof and solutal Rayleigh/Grashof numbers collapse with gravity. This is why microgravity is used to test diffusion-limited solidification models. Papers on Al-Ni, Al-Si, Al-Cu, SCN-camphor, and DECLIC-DSI repeatedly frame microgravity as a way to remove buoyancy-driven convection.

3. [[Constitutional Undercooling]]: in directional solidification, the stability of a planar front depends on the imposed temperature gradient, growth velocity, partitioning, and solute diffusivity. The extracted papers show gravity shifts the effective threshold by changing the solute boundary layer through convection.

4. [[Columnar-to-Equiaxed Transition]]: CET is not only a nucleation problem. It is also a grain-transport problem. Earth-based flow can carry grains away from or toward the front, remelt them, or concentrate them. Microgravity suppresses buoyant grain transport, allowing cleaner study of nucleation distance and front blocking.

5. [[Mushy Zone Flow and Macrosegregation]]: interdendritic liquid flow is driven by buoyancy, shrinkage, thermal contraction, permeability, and pressure gradients. In 1g, all can interact; in microgravity, buoyancy drops out, which clarifies the relative importance of shrinkage feeding and diffusion.

6. [[Marangoni Convection]]: microgravity elevates the relative importance of surface-tension-gradient flow, especially in levitated droplets, free-surface melts, and containerless experiments. This matters for EML, ESL, and in-space additive-manufacturing melt pools.

7. [[Thermophysical Property Measurement]]: microgravity levitation reduces the need for large electromagnetic levitation forces and minimizes container contamination, improving measurements of density, surface tension, viscosity, emissivity, heat capacity, and thermal conductivity.

## Validated Numerical Evidence Register

This register replaces the raw extraction dump with thesis-usable comparison statements. Each item keeps the exact local PDF filename so it can be checked against the source.

### CET in Refined Al-Cu

Source: `ReferencePapers/In situ investigation of the Columnar-to-Equiaxed Transition during directional solidification of Al–20wt%Cu alloys on Earth and in microgravity.pdf`

- Alloy and facility: Al-20 wt.% Cu with 0.1 wt.% Al-Ti-B grain refiner, XRMON-GF2 Bridgman-type furnace, MASER-14 sounding rocket.
- Extracted setup values: apogee about 245 km; roughly 6 min microgravity; furnace gradient capability 5-15 °C/mm; cooling-rate capability 0.01-1.5 °C/s; sample about 50 mm x 5 mm x 210 µm; effective pixel size about 4 µm.
- Processing timeline: preheat at 2 °C/s from 20 °C to 540 °C; first cooling rate R1 = 0.08 °C/s; second cooling rate R2 = 1 °C/s.
- Earth vs microgravity result: first equiaxed grains appeared farther ahead of the columnar front in microgravity, about 240 µm, compared with about 150 µm in Earth experiments.
- Interpretation: this is direct evidence that gravity changes the CET precursor field, not only the final grain map.

### 1g Orientation Baseline in Refined Al-Cu

Source: `ReferencePapers/Impact of gravity on directional solidification of refined Al-20wt.%Cu alloy investigated by in situ X-radiography.pdf`

- Alloy and method: refined Al-20 wt.% Cu, in situ X-radiography, horizontal, vertical upward, and vertical downward directional solidification.
- Extracted result: the paper reports that natural convection in the liquid and buoyancy on solid grains strongly affect grain-structure formation.
- Earth-specific value: this is a 1g orientation-control paper, not a microgravity comparison paper.
- Interpretation: use it as the terrestrial control logic for the MASER/XRMON microgravity comparison. The review should describe gravity direction relative to thermal gradient, not simply "Earth vs space."

### Al-Si Directional Solidification on ISS and Earth

Source: `ReferencePapers/Comparative study of directional solidification of Al-7 wt% Si alloys in Space and on Earth- Effects of gravity on dendrite growth and Columnar-to-equiaxed transition.pdf`

- Alloy and facility: grain-refined Al-7 wt% Si in the Materials Science Laboratory on the ISS and a ground analogue.
- Extracted setup values: 0.5 wt% AlTi5B; cylindrical sample 8 mm diameter x 245 mm length; thermocouples spaced by 10 mm; initial gradient about 0.9 K/mm; v1 = 0.01 mm/s over 20 mm; cooling rate 0.067 K/s; final pulling velocity 3 mm/s.
- Earth vs microgravity result: stage-II dendrite arm spacing was about 117 µm on Earth and about 95 µm in the flight sample. The paper also reports a much more progressive CET and longer dendrites aligned with the temperature gradient under 1g; the longest extracted dendrite length was up to 62 mm.
- Interpretation: 1g convection transports solute and equiaxed grains, making CET more progressive; microgravity suppresses that transport and gives a finer, less convectively stretched microstructure.

### Al-Si and Al-Cu Rapid Solidification in Drop-Tube Microgravity

Source: `ReferencePapers/Comparative study of gravity effects in directional solidification of Al-3.5 wt.% Si and Al-10 wt.% Cu alloys_GUIYUAN 2.pdf`

- Alloy and method: Al-3.5 wt.% Si and Al-10 wt.% Cu, 1g comparison against short-duration drop-tube microgravity.
- Extracted setup values: samples heated above 700 °C in about 10 s, then cooled to liquidus in about 1 s; cooling rates about 88 °C/s for Al-Si and 85 °C/s for Al-Cu; vacuum about 1 x 10^-4 Pa; microgravity time about 3.2 s.
- Al-3.5 wt.% Si result: 1g DAS 45.95 +/- 3.55 µm and eutectic content 25.46 +/- 2.91%; microgravity DAS 39.49 +/- 3.26 µm and eutectic content 22.12 +/- 2.82%.
- Al-10 wt.% Cu result: 1g DAS 39.33 +/- 3.92 µm and eutectic content 51.27 +/- 4.24%; microgravity DAS 35.82 +/- 3.04 µm and eutectic content 43.73 +/- 4.03%.
- Interpretation: compared with 1g, microgravity reduced average DAS by about 14% in Al-Si and 9% in Al-Cu, and reduced eutectic content by about 13% and 9%, respectively.

### Benchmark Al-Cu Solidification on ISS and Earth

Source: `ReferencePapers/Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_Thomas.pdf`

- Alloy and method: Al-4, Al-10, and Al-18 wt.% Cu solidified upward on Earth and in SUBSA aboard the ISS.
- Extracted setup values: alumina ampoule inner diameter 9.5 mm; sample nominal diameter 9 mm; sample nominal length 60 mm; thermocouples at 0, 20, 40, and 60 mm; temperature logged at 1 Hz; 30 min molten hold.
- Earth result: terrestrial samples exhibited a columnar-to-equiaxed transition; Al-4 wt.% Cu showed evidence of grain sedimentation, and Al-18 wt.% Cu showed buoyancy-related solid transport differences.
- Microgravity result: all microgravity samples were entirely equiaxed.
- Interpretation: one of the clearest benchmark papers for the statement that gravity-driven melt convection and unattached solid transport control CET and grain structure.

### Al-Ni Diffusion Transport in Space

Source: `ReferencePapers/Directional solidification of Al-1.5 wt% Ni alloys under diffusion transport in space_Thi.pdf`

- Alloy and method: Al-1.5 wt% Ni, space diffusion-transport samples compared with Earth convection-plus-diffusion samples.
- Extracted setup values: reported gradients include about 24 K/cm and 40 K/cm; examples of microgravity primary-spacing ranges include about 150-600 µm; growth conditions sit near the cell-dendrite transition.
- Earth result: ground samples showed macroscopic growth-front deformation and microstructure localization from radial-temperature-gradient-driven flow.
- Microgravity result: space samples were close enough to diffusion transport to test spacing Peclet number and tip constitutional-supercooling arguments.
- Interpretation: use this paper for spacing-selection theory and to explain why 1g bulk samples are not clean tests of diffusion-based models.

### Transparent Alloy and Metallic Directional-Solidification Synthesis

Source: `ReferencePapers/Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation.pdf`

- Materials: SCN-camphor transparent alloys plus metallic Al-Cu examples.
- Extracted values: SCN-0.24 wt% camphor and SCN-0.46 wt% camphor; example G = 19 K/cm and V = 4 µm/s; Al-20 wt.% Cu example G about 15 K/mm and R = 0.15 K/s.
- Earth vs microgravity result: in one extracted comparison, the ground planar front remained stable up to about 1 µm/s, while microgravity morphological instability occurred below about 0.35 µm/s.
- Interpretation: convection shifts apparent morphological stability thresholds, so Earth process maps should not be copied directly into microgravity process maps.

### Dendrite Tip Kinetics in a Model Transparent Melt

Source: `ReferencePapers/Dendritic Growth tip velocities and radii of curvature in microgravity.pdf`

- Material and method: succinonitrile dendritic growth, Isothermal Dendritic Growth Experiment / Shuttle flight data.
- Extracted values: supercooling range in the extracted context was about 1.844-1.311 K.
- Earth vs microgravity result: the extracted comparison notes an approximately 10% reduction in growth velocity under microgravity.
- Interpretation: even when convection is reduced, microgravity is not just a visually cleaner 1g experiment; measured dendrite kinetics can shift.

### Immiscible Al-Bi-Sn Alloy Solidification

Sources:

- `ReferencePapers/Effect of microgravity on the solidification of aluminum–bismuth–tin immiscible alloys.pdf`
- `ReferencePapers/Solidification of Al-Bi-Sn immiscible alloy under microgravity conditions of space.pdf`

- Alloy and method: Al-Bi-Sn immiscible alloy solidified under Tiangong-2 / space-lab conditions.
- Earth expectation: density differences promote phase separation, droplet sedimentation, coalescence, and macrosegregation.
- Microgravity result: the paper-level extraction identifies a well-dispersed microstructure under microgravity.
- Interpretation: this is the most relevant branch for liquid-solid or multiphase mixture processing, because gravity directly controls whether dispersed liquid/solid phases remain suspended or separate.

### Refractory Alloy Undercooling and Eutectic Cells

Sources:

- `ReferencePapers/Metastable Liquid Properties and Surface Flow Patterns of Ultrahigh Temperature Alloys Explored In Outer Space.pdf`
- `ReferencePapers/Outer space cultivated regular eutectic cells with anomalous internal microstructures for rapidly solidifying Zr50V50 hypereutectic alloy.pdf`

- Extracted values: Nb82.7Si17.3 droplet superheated to 2338 K with undercooling of 437 K; Zr50V50 space environment around 10^-5 g0; anomalous eutectic transition undercooling estimated at 102-110 K; ultimate undercooling 445 K; eutectic cell radius example about 700 µm.
- Earth limitation: high-temperature container interaction and convection make these metastable regimes difficult to study cleanly on ground.
- Microgravity result: space/containerless conditions enabled large undercooling and regular/anomalous eutectic-cell formation.
- Interpretation: microgravity can be used as a microstructure-design environment, not only as a benchmark for theory.

### Ti64 Thermophysical Properties in ISS-EML

Source: `ReferencePapers/Precise Measurements of Thermophysical Properties of Liquid Ti–6Al–4V (Ti64) Alloy On Board the International Space Station.pdf`

- Alloy and facility: Ti-6Al-4V, ISS electromagnetic levitation.
- Extracted values: sample diameter 6-8 mm; stable and undercooled liquid data extended by about 200 K; viscosity about 5-8 mPa s from 1700-1850 K; surface tension about 1.490 N/m at 1950 K; thermal conductivity about 29.8 W/m/K at 1933 K.
- Interpretation: these data are directly useful for laser powder bed fusion, directed energy deposition, casting, and microgravity melt-pool models.

### Co-Cr-Mo Thermophysical Properties

Source: `ReferencePapers/Thermophysical properties of liquid Co–Cr–Mo alloys measured by electromagnetic levitation in a static magnetic field.pdf`

- Alloy and method: Co-Cr-Mo alloys with low and high carbon content measured by EML under a static magnetic field.
- Extracted values: carbon contents 0.053 and 0.251 mass%; DSC range 873-1823 K at 10 K/min; liquidus temperatures 1691 K and 1681 K; density uncertainty about 0.7-1.1%; surface-tension uncertainty about 4.5-5.1%; heat-capacity uncertainty about 6.1-7.9%.
- Interpretation: useful property input for process modeling, but the force environment is not equivalent to passive microgravity because levitation/static magnetic fields can change internal flow.

## Synthesis By Experimental Family

### Directional Solidification and CET

The strongest Earth-vs-microgravity comparison set is directional solidification of Al-based alloys and transparent model alloys. The recurring outcome is that 1g changes both the liquid and solid transport fields: solute-rich or solute-poor liquid moves by buoyancy, detached grains drift, dendrite fragments relocate, and the front shape becomes non-planar or localized. Microgravity cases are therefore not merely "slower" or "cleaner" versions of Earth experiments; they can cross different morphological thresholds because the advective solute field is absent or much weaker.

For the literature review, organize CET around three separate mechanisms:

- Nucleation: grain refiners and constitutional undercooling define where equiaxed grains can appear.
- Growth competition: columnar dendrites can continue advancing unless equiaxed grains block the front.
- Transport: in 1g, grains/fragments are moved by buoyancy and convection; in microgravity, shrinkage and residual flows are relatively more visible.

### Dendritic Growth and Spacing Selection

The Al-Ni, SCN-camphor, and IDGE papers are useful for fundamentals because they discuss tip velocity, radius, primary spacing, and the limits of diffusion-controlled theory. The important review point is that primary spacing is not uniquely selected by `G` and `V`; gravity changes the solutal field around the array and therefore the accessible spacing band. Microgravity is valuable because it makes comparisons to phase-field, Warren-Langer, Lu-Hunt, solvability, and array-stability models more defensible.

### Macrosegregation and Interdendritic Flow

The macrosegregation papers support a simple argument: Earth casting inherits multiple fluid-flow sources that are difficult to separate experimentally. Buoyancy, shrinkage, permeability, thermal gradients, and solid movement all contribute. Microgravity suppresses the largest buoyancy term, so residual macrosegregation becomes a sharper diagnostic of shrinkage feeding, wall heat transfer, and local interface kinetics.

### Immiscible and Monotectic Alloys

The Al-Bi-Sn and immiscible-alloy papers are central for a liquid-solid mixture processing pathway. Earth gravity promotes sedimentation, coalescence, and phase separation in systems with large density contrast. Microgravity can preserve dispersed morphologies, but surface energy, collision/coalescence, Marangoni flow, and cooling path still matter. This literature is a useful bridge from fundamental microgravity science to in-space manufacturing concepts that avoid handling fully molten homogeneous pools.

### Containerless Levitation and Thermophysical Properties

EML/ESL and space-station levitation papers provide property data rather than direct solidification microstructure comparisons. They matter because process simulations for LPBF, DED, casting, and liquid-solid mixture processing depend on accurate density, viscosity, surface tension, emissivity, heat capacity, thermal conductivity, and undercooling data. On Earth, levitation requires stronger fields to oppose weight; in microgravity, positioning and heating can be decoupled more cleanly, reducing forced convection and improving undercooled-liquid access.

## Methodology Matrix

| Method | Typical papers in this folder | What it reveals | Main limitation |
|---|---|---|---|
| In situ X-radiography | Al-Cu CET, Al-Si, XRMON, overview papers | Real-time front motion, dendrite fragmentation, grain transport, CET | Thin samples and X-ray contrast can make geometry non-bulk-like. |
| ISS directional solidification | MSL, DECLIC, SUBSA, Al-Cu, SCN-camphor | Long-duration microgravity benchmark data | Limited sample count and expensive parameter sweeps. |
| Sounding rocket | MASER-14 XRMON-GF2 | Short-duration, high-value in situ tests | About minutes of microgravity, so timeline design dominates. |
| Drop tube / drop tower | Al-Si/Al-Cu rapid tests, undercooling studies | Rapid solidification, short microgravity comparison | Seconds of microgravity; thermal histories are steep and transient. |
| EML/ESL | Ti64, Co-Cr-Mo, refractory alloys, pure metals | Thermophysical properties, undercooling, nucleation, containerless solidification | Field-induced flow and optical-property assumptions must be handled. |
| Transparent organic alloys | SCN-camphor, DECLIC-DSI | Direct visualization and phase-field validation | Analog material properties differ from metallic melts. |
| Computational modeling | phase-field, Bridgman, interdendritic-flow papers | Mechanistic separation and parameter sweeps | Boundary conditions often dominate comparison with flight experiments. |

## How To Use This In The Literature Review

Recommended section structure:

1. Start with [[Why Gravity Matters in Alloy Solidification]]: buoyancy-driven convection, solid transport, and macrosegregation.
2. Introduce [[Microgravity as a Diffusion-Controlled Benchmark]]: not zero flow, but suppressed buoyancy.
3. Compare [[Directional Solidification]] results: Al-Cu, Al-Si, Al-Ni, SCN-camphor.
4. Develop [[Columnar-to-Equiaxed Transition]] as the main case study for Earth-vs-space differences.
5. Add [[Containerless Processing]] and [[Thermophysical Properties]] as enabling data for in-space manufacturing models.
6. Add [[Immiscible Alloy Solidification]] as the bridge to liquid-solid mixture processing and semi-solid manufacturing.
7. Close with [[Implications for In-Space Additive Manufacturing]]: melt-pool convection, powder/particle motion, porosity, wetting, free surfaces, and process maps.

## Open Questions For The PhD

- How much residual flow is acceptable before a microgravity experiment is no longer a diffusion-controlled benchmark?
- Which in-space manufacturing route is most sensitive to the absence of buoyancy: casting, LPBF, DED, wire-fed melting, or liquid-solid mixture deposition?
- Can liquid-solid mixture processing reduce the hazards of free molten metal handling while still achieving acceptable bonding and final density?
- How should Earth-based EML measurements be corrected for field-induced flow before being used in microgravity or lunar/Mars process models?
- What is the minimum set of thermophysical properties needed to predict microgravity solidification microstructure for Al, Ti, Ni, and refractory alloys?
- How do Marangoni flow, shrinkage flow, and residual acceleration rank for small melt pools in orbital, lunar, and Martian gravity?
- What experimental alloy system gives the best compromise between space-manufacturing relevance and interpretable solidification physics?

## High-Priority Papers To Read First

1. `Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation.pdf` - best overview-style comparison across transparent alloys and metallic examples.
2. `Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth_Thomas.pdf` - direct ISS/ground benchmark with clear grain-structure contrast.
3. `In situ investigation of the Columnar-to-Equiaxed Transition during directional solidification of Al–20wt%Cu alloys on Earth and in microgravity.pdf` - strongest CET-focused in situ comparison.
4. `Comparative study of directional solidification of Al-7 wt% Si alloys in Space and on Earth- Effects of gravity on dendrite growth and Columnar-to-equiaxed transition.pdf` - useful Al-Si manufacturing-relevant case with quantitative DAS/grain-size data.
5. `Directional solidification of Al-1.5 wt% Ni alloys under diffusion transport in space_Thi.pdf` - valuable for diffusion transport, spacing selection, and macrosegregation theory.
6. `Precise Measurements of Thermophysical Properties of Liquid Ti–6Al–4V (Ti64) Alloy On Board the International Space Station.pdf` - directly relevant to additive manufacturing modeling.
7. `Effect of microgravity on the solidification of aluminum–bismuth–tin immiscible alloys.pdf` - important for liquid-solid or multiphase mixture processing.

## Source Map

The extraction found 63 local PDFs, 4,859 numerical snippets after stricter filtering, and 1,579 comparison-relevant snippets after filtering to gravity-related contexts. Papers with the densest direct Earth-vs-microgravity numerical snippets include:

- `Melt Growth of Semiconductor Crystals Under Microgravity.pdf`
- `Detached_Solidification_in_Microgravity_A_Review.pdf`
- `Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation.pdf`
- `Comparative study of gravity effects in directional solidification of Al-3.5 wt.% Si and Al-10 wt.% Cu alloys_GUIYUAN 2.pdf`
- `Solidification of Containerless Undercooled Melts - 2012 - Herlach.pdf`
- `Metastable Liquid Properties and Surface Flow Patterns of Ultrahigh Temperature Alloys Explored In Outer Space.pdf`
- `Outer space cultivated regular eutectic cells with anomalous internal microstructures for rapidly solidifying Zr50V50 hypereutectic alloy.pdf`
- `Solidification of Al-Bi-Sn immiscible alloy under microgravity conditions of space.pdf`
- `Dendritic Growth tip velocities and radii of curvature in microgravity.pdf`
- `Effect of microgravity on the solidification of aluminum–bismuth–tin immiscible alloys.pdf`

## Related Notes To Create

- [[Columnar-to-Equiaxed Transition]]
- [[Constitutional Undercooling]]
- [[Microgravity Thermophysical Property Measurement]]
- [[Interdendritic Flow and Macrosegregation]]
- [[Containerless Electromagnetic Levitation]]
- [[Immiscible Alloy Solidification]]
- [[Liquid-Solid Mixture Processing]]
- [[In-Space Additive Manufacturing]]
- [[Marangoni Convection in Melt Pools]]
