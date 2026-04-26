---
type: synthesis
title: "Deep Research: Metal Alloy Processing for In-Space Manufacturing"
topic: "Investigating Solidification Behaviour Under Microgravity"
status: draft
created: 2026-04-26
tags:
  - phd
  - literature-review
  - in-space-manufacturing
  - microgravity
  - solidification
  - metal-alloys
---

# Deep Research: Metal Alloy Processing for In-Space Manufacturing

Research question: **How does microgravity alter metal-alloy solidification behaviour, and how can that knowledge be converted into process rules for in-space manufacturing of reliable metallic parts?**

## 1. Thesis-Level Framing

This topic sits at the junction of three literatures that are still only partially integrated:

1. **Classical and microgravity solidification science**: directional solidification, dendritic growth, columnar-to-equiaxed transition (CET), macrosegregation, shrinkage flow, nucleation, phase selection.
2. **Space materials-science experiments**: ISS Materials Science Laboratory (CETSOL/MICAST), sounding rockets, parabolic flights, ISS-EML, ISS-ELF, China Space Station electrostatic levitation, transparent-alloy analogues.
3. **In-space manufacturing and metal additive manufacturing**: wire-fed laser deposition, powder-bed or powder-assisted approaches, bound-metal routes, melt-pool control, defect formation, process monitoring, autonomy.

The central PhD opportunity is not just to ask whether microgravity changes solidification. That is already established. The stronger thesis is:

> Microgravity removes buoyancy-driven transport, but it does not create a flow-free melt. Instead, it exposes a hierarchy of residual transport mechanisms, including Marangoni convection, shrinkage feeding, electromagnetic stirring, surface-pore-driven flows, g-jitter, recoil/vapour effects and melt-bridge instabilities. These residual mechanisms determine whether space-made alloys become cleaner, more homogeneous and more controllable than terrestrial analogues.

For in-space manufacturing, this means that "microgravity" should be treated as a **process parameter and model-validation environment**, not as a simple off switch for convection.

## 2. Framework

I used a technology/applied-science decomposition rather than PICO, because this is not a clinical intervention question.

| Component | How it maps to the PhD topic | Key sub-area to explore |
|---|---|---|
| Core mechanism | Gravity changes momentum, heat and solute transport during solidification | Buoyancy suppression, diffusion-controlled growth, residual convection |
| Materials system | Alloy behaviour depends strongly on solute density, partitioning, nucleants and phase diagram | Al-Cu, Al-Si, Al-Ni, Ti alloys, Ni superalloys, refractory alloys, metallic glasses |
| Process route | In-space manufacturing will use melt pools, wire/powder feedstock, remelting and rapid solidification | Link Bridgman/levitation benchmarks to AM thermal histories |
| Measurement platform | Different platforms give different duration, sample size and diagnostics | ISS MSL, sounding rockets, parabolic flights, ISS-EML/ELF, China Space Station, drop tubes |
| Outcome | The useful outputs are not just micrographs but process rules | CET maps, segregation metrics, porosity/shrinkage behaviour, property databases, validated simulation inputs |

## 3. What The Literature Shows

### 3.1 Microgravity gives benchmark diffusion-controlled data, but only in carefully constrained configurations

The strongest directional-solidification evidence comes from Al-based ISS/sounding-rocket experiments. CETSOL/MICAST studies show that microgravity suppresses buoyancy-driven melt convection and solid-grain sedimentation/floatation, allowing cleaner tests of CET theory and macrosegregation models [1-7]. Grain-refined Al-Cu experiments on the ISS reported negligible axial macrosegregation and no radial effects, supporting an assumption of nearly diffusive solidification in those cases [1]. Al-7Si and Al-20Cu experiments show that gravity changes dendrite growth, grain transport and CET progression [3,4,6].

The important caveat is that microgravity samples are not always simple or ideal. Surface pores, shrinkage feeding and Marangoni effects can create local flow even in nominally microgravity experiments [8-10]. This is directly relevant to additive manufacturing, where free surfaces, pores, steep thermal gradients and melt-pool curvature are unavoidable.

### 3.2 Gravity effects are alloy-specific, not universal

Recent comparative work on Al-3.5wt.%Si and Al-10wt.%Cu argues that gravity effects depend on solute redistribution, solute density and crystallization mode [11]. This is important for your PhD because it pushes the research away from generic claims such as "microgravity reduces convection" and toward alloy-specific process windows.

Examples:

- **Al-Cu**: strong benchmark system for CET, equiaxed growth, macrosegregation and model validation [1,4,5,7].
- **Al-Si**: relevant to castable/lightweight aerospace alloys and MICAST/CETSOL; shows gravity-sensitive dendrite/CET behaviour [3,6,8].
- **Al-Ni**: useful for cell-dendrite transition and diffusion-versus-flow comparisons [12].
- **Ti64/TiAl/Ni superalloys**: important for space hardware, but direct microgravity solidification datasets are more commonly thermophysical-property oriented than full AM-build oriented [13-16].
- **Refractory alloys and metallic glasses**: China Space Station and ISS-EML/space-AM work shows deep undercooling, phase selection and containerless processing opportunities [14,17-20].

### 3.3 In-space metal AM has crossed the demonstration threshold, but not the qualification threshold

ESA and Airbus launched the first metal 3D printer to the ISS in January 2024, produced first metal printing lines by June 2024, and printed the first full metal part in August 2024, publicly announced on 6 September 2024 [21-23]. By November 2025, ESA reported returned part analysis at ESTEC, focused on understanding how microgravity affected the printing process [24].

This is a major inflection point for the field. However, it is still a technology demonstration. The published academic AM literature says metal AM in space remains underdeveloped relative to polymer AM and ground-based aerospace AM [25-28]. The knowledge gap is now: **what solidification and defect mechanisms control quality when a real metal melt pool is processed in microgravity, vacuum/controlled atmosphere and constrained spacecraft safety conditions?**

## 4. Mechanism Map

| Mechanism | 1g behaviour | Microgravity behaviour | Why it matters for in-space manufacturing |
|---|---|---|---|
| Buoyancy-driven thermal/solutal convection | Strong flow can redistribute heat/solute and distort growth fronts | Strongly reduced when residual acceleration is low | Cleaner benchmark for diffusion models; less macrosegregation |
| Grain sedimentation/floatation | Equiaxed grains move relative to liquid depending on density | Suppressed, so grain motion more likely from shrinkage/contact/forced flow | CET maps from Earth may not transfer directly |
| Interdendritic/shrinkage flow | Couples with gravity and permeability to form inverse segregation | Still present because feeding is driven by solidification shrinkage | Microgravity does not eliminate all segregation |
| Marangoni convection | Often masked by buoyancy | Can become dominant around bubbles, pores and free surfaces | Critical for melt pools, pores and wire-fed AM |
| Electromagnetic stirring | Used intentionally or introduced by levitation/heating fields | Can be isolated from buoyancy and tuned | Useful for property measurement but may bias "diffusive" assumptions |
| Surface tension and wetting | Crucible/contact effects plus gravity affect shape/contact | Detached/free-surface states become more accessible | Relevance to droplet processing, powder fixation and melt-pool stability |
| Undercooling and nucleation | Limited by contamination/contact and convection | Deeper undercooling possible in containerless processing | Enables phase-selection studies and metallic-glass formation |
| Rapid solidification | Present in AM/welding; hard to isolate gravity effects | AM-like cooling with altered flow/particle behaviour remains underexplored | Core PhD gap |

## 5. Priority Reading Order

Read these in this order to get oriented quickly:

1. **Nguyen-Thi, Reinhart and Billia (2017), "On the interest of microgravity experimentation for studying convective effects during the directional solidification of metal alloys"** [2]. Start here for the conceptual justification of microgravity alloy-solidification experiments.
2. **Bergeon et al. (2021), "Analysis of gravity effects during binary alloy directional solidification..."** [5]. Read for how in situ observation plus microgravity isolates gravity effects.
3. **Zimmermann et al. (2024), "Structures in grain-refined directionally solidified hypoeutectic Al-Cu alloys..."** [1]. This is a high-priority benchmark for Al-Cu CET under ISS conditions.
4. **Ngomesse et al. (2021), "In situ investigation of the Columnar-to-Equiaxed Transition..."** [4]. Read for direct X-radiography and the distinction between mechanical and solutal blocking.
5. **Williams and Beckermann (2022), "Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth"** [7]. Read for modelling-relevant data and density-driven solid transport contrasts.
6. **Mohr et al. (2023), "Electromagnetic levitation containerless processing... thermophysical properties"** [13]. Use this to connect solidification behaviour to property-data requirements for simulations.
7. **Matson et al. (2023), "Electromagnetic levitation containerless processing... rapid solidification"** [14]. Read for undercooling, nucleation and rapid-solidification framing.
8. **Taghizadeh and Zhu (2024), "A comprehensive review on metal laser additive manufacturing in space"** [25]. Use this to connect the solidification literature to in-space metal AM.
9. **Neumann et al. (2023), "Additive manufacturing of metallic glass from powder in space"** [26]. Read for the best current example of powder-based metal AM in microgravity.
10. **ESA Metal 3D Printer reports (2024-2025)** [21-24]. Use these to anchor the PhD in the current state of orbital metal printing.

## 6. Research Gaps Worth Owning

### Gap 1: Bridgman and levitation data are not yet converted into AM melt-pool process maps

Directional solidification gives controlled temperature gradients and velocities. AM gives steep gradients, high cooling rates, remelting, free surfaces, layer-wise thermal cycling and moving heat sources. The literature has many CET models for casting and AM [29-35], but there is not yet a mature, validated map for **microgravity AM melt-pool solidification**.

PhD angle:

> Build a transfer framework from microgravity benchmark variables (temperature gradient G, interface velocity R, cooling rate, undercooling, solute profile) to AM variables (laser power, scan speed, wire/powder feed, bead geometry, melt-pool lifetime, remelting depth).

### Gap 2: "No buoyancy" leaves residual flow mechanisms that are AM-critical

ISS and China Space Station experiments show Marangoni, pore, bubble, electromagnetic and shrinkage effects can reshape dendrites, produce spurious grains, drive spiral eutectics and create surface dendritic patterns [8-10,17-20]. These are exactly the mechanisms expected around AM melt pools.

PhD angle:

> Treat microgravity as a way to rank residual transport mechanisms by dominance: Marangoni number, Peclet number, capillary number, recoil pressure, shrinkage feeding and residual acceleration.

### Gap 3: Alloy selection for in-space metal AM lacks a microgravity-specific basis

Current metal AM alloy-design work focuses on printability under terrestrial conditions: cracking, grain morphology, hot tearing, solute trapping, oxidation and processability [27,29-35]. Space changes powder/wire handling, heat transfer, surface stability and flow. Alloy systems that look poor on Earth may behave differently in microgravity, and alloys designed for terrestrial AM may not be optimal for orbital manufacturing.

PhD angle:

> Compare candidate alloy families by gravity sensitivity, not only by conventional AM printability: Al-Si, Al-Cu, Ti64, TiAl, Inconel/Ni superalloys, stainless steel/wire feed, Zr-based metallic glasses and refractory eutectics.

### Gap 4: Diagnostics for space metal processing are not yet enough for qualification

ISS MSL and sounding-rocket X-radiography have shown the power of in situ observation [4,5,36]. ESA's metal printer has sensors/cameras and ground-controlled operation, but returned sample analysis is still central [21-24]. For future autonomous manufacturing, the field needs correlations between in situ process signatures and final microstructure/properties.

PhD angle:

> Develop a process-monitoring feature set: melt-pool geometry, thermal history, bead height/width, spatter/particle escape, pore signatures, cooling rate proxies and post-build EBSD/SEM/XCT validation.

### Gap 5: Reduced gravity beyond microgravity is underused

Lunar and Martian manufacturing will not occur in perfect microgravity. They will occur at partial gravity, with dust/regolith contamination, vacuum or low-pressure atmospheres and limited thermal management. Hypergravity/partial-gravity studies can help separate gravity-level scaling from platform artefacts.

PhD angle:

> Use gravity level as a continuous variable: microgravity, lunar-g, Mars-g, 1g and hypergravity. This enables scaling laws rather than binary Earth/space comparisons.

## 7. Candidate PhD Research Questions

1. **RQ1: Which solidification mechanisms are genuinely suppressed by microgravity, and which residual mechanisms dominate instead?**
   - Hypothesis: buoyancy-driven convection and grain sedimentation are suppressed, but Marangoni, shrinkage and free-surface effects dominate in AM-relevant geometries.

2. **RQ2: How do microgravity solidification conditions shift CET boundaries in AM-relevant alloys?**
   - Hypothesis: CET maps built for terrestrial AM overpredict/underpredict equiaxed growth depending on whether terrestrial buoyancy aided grain transport or solute removal.

3. **RQ3: Can microgravity benchmark data be used to calibrate melt-pool simulations for in-space metal AM?**
   - Hypothesis: ISS/rocket/EML data can constrain thermophysical properties, nucleation undercooling and diffusion-controlled growth laws, reducing uncertainty in AM models.

4. **RQ4: Which alloy families are most promising for early in-space metal manufacturing?**
   - Hypothesis: early success favours wire-fed stainless steels for demonstrator simplicity, metallic glasses for reduced crystallization constraints, and Al/Ti alloys for structural relevance, but each fails for different solidification-control reasons.

5. **RQ5: What post-build microstructural signatures distinguish microgravity processing from terrestrial processing?**
   - Candidate outputs: grain morphology, texture, dendrite arm spacing, eutectic fraction, porosity distribution, segregation profile, intermetallic distribution, residual stress, hardness/strength anisotropy.

## 8. Proposed PhD Methodology

### Track A: Evidence synthesis and data extraction

Build a structured matrix across alloy, platform, gravity level, thermal gradient, velocity/cooling rate, undercooling, microstructure and reported defects. Your vault already has the foundations in `06 Data/Literature Review Extraction/`.

Minimum fields:

- Alloy and composition
- Platform: ISS MSL, ISS-EML, ISS-ELF, China Space Station, sounding rocket, parabolic flight, drop tube, terrestrial control
- Gravity level and duration
- Process: directional solidification, isothermal equiaxed solidification, levitation, AM/welding/deposition
- G, R, cooling rate, undercooling, melt temperature
- Grain morphology, CET type, dendrite arm spacing, eutectic fraction, segregation, porosity
- Evidence quality: in situ, post-mortem, simulation-only, benchmark dataset

### Track B: Modelling and scaling

Use the literature to define a reduced mechanism model before choosing a heavy numerical method.

Candidate modelling stack:

- **Thermal model**: moving heat source or Bridgman-style gradient to compute G, R and cooling rate.
- **Transport model**: compare diffusion-only, buoyancy, Marangoni and shrinkage-flow terms.
- **Microstructure model**: CET map, KGT/LGK dendrite growth, CA-FE/CA-FVM, phase-field for selected local cases.
- **AM bridge**: convert process parameters to local solidification variables and compare with terrestrial AM CET models.

Key dimensionless groups:

- Rayleigh/Grashof: buoyancy relevance.
- Marangoni number: surface-tension-driven flow.
- Peclet number: advection versus diffusion.
- Stefan number: latent heat effect.
- Capillary number/Bond number: free-surface and droplet shape control.

### Track C: Experimental or quasi-experimental design

Depending on access, the PhD can be designed at three levels.

**Level 1: Ground-only with validated microgravity benchmarks**

- Use existing ISS/sounding-rocket data for validation.
- Perform terrestrial directional solidification or laser/wire single-track experiments.
- Vary orientation, thermal gradient, scan speed and shielding atmosphere.
- Compare against diffusion-only and flow-enabled simulations.

**Level 2: Reduced-gravity campaign**

- Use drop tower/parabolic flight/sounding rocket for short-duration single-track or remelting experiments.
- Focus on one alloy and one mechanism: e.g. Marangoni versus buoyancy in an Al-Si or stainless-steel melt pool.

**Level 3: Space-platform experiment proposal**

- Design a small, high-value experiment for ISS or commercial microgravity platform.
- Keep the question narrow: single-track wire-fed melt pool, controlled remelting of a preplaced alloy coupon, or containerless droplet solidification with AM-like thermal cycling.

## 9. Candidate Chapter Structure

1. **Introduction**: why metal in-space manufacturing needs solidification science, not just printer hardware.
2. **Gravity-sensitive alloy solidification**: buoyancy, solute transport, CET, dendrites, macrosegregation.
3. **Microgravity evidence base**: ISS MSL, sounding rockets, parabolic flights, levitation facilities, China Space Station.
4. **From benchmark solidification to AM melt pools**: process-variable translation and limits.
5. **Modelling framework**: diffusion-only baseline plus residual-flow extensions.
6. **Experiment/simulation results**: alloy-specific solidification behaviour under selected conditions.
7. **Implications for in-space manufacturing**: process maps, alloy selection, monitoring and qualification.
8. **Conclusions and future work**: lunar/Mars gravity, ISRU feedstocks, autonomous quality control.

## 10. Search Strings To Keep Using

### Broad field

```text
("microgravity" OR "reduced gravity" OR "space") AND ("solidification" OR "directional solidification") AND ("metallic alloy" OR "aluminium alloy" OR "Al-Cu" OR "Al-Si")
```

### CET and benchmark experiments

```text
("columnar-to-equiaxed transition" OR CET) AND ("microgravity" OR "International Space Station" OR "sounding rocket") AND ("Al-Cu" OR "Al-Si" OR "metal alloy")
```

### Residual convection

```text
("Marangoni convection" OR "shrinkage flow" OR "surface pore" OR "g-jitter") AND ("microgravity solidification" OR "space solidification") AND (dendrite OR eutectic OR "spurious grain")
```

### Thermophysical properties

```text
("ISS-EML" OR "electromagnetic levitation" OR "electrostatic levitation") AND ("thermophysical properties" OR viscosity OR "surface tension" OR density) AND (Ti64 OR "Ni-based superalloy" OR "Al-Cu" OR "metallic glass")
```

### In-space metal AM

```text
("in-space manufacturing" OR "space additive manufacturing" OR "microgravity additive manufacturing") AND ("metal" OR "metallic") AND ("laser" OR "wire feed" OR "powder bed fusion" OR "directed energy deposition")
```

### AM solidification bridge

```text
("metal additive manufacturing" OR LPBF OR DED OR WAAM) AND ("columnar-to-equiaxed transition" OR "grain morphology" OR "dendritic growth") AND ("solidification map" OR "constitutional undercooling")
```

## 11. Ninety-Day Work Plan

### Days 1-30: Build the evidence map

- Convert the existing literature notes into a single spreadsheet with alloy, platform, process, gravity level and measured outcomes.
- Identify 10 "anchor" papers and extract all numerical values into the matrix.
- Write one 2-page synthesis on **what microgravity suppresses** and another on **what microgravity reveals**.

### Days 31-60: Define the thesis mechanism

- Pick one primary alloy family and one comparator. A strong pair is Al-Cu/Al-Si for evidence depth; Ti64/stainless steel for manufacturing relevance.
- Build a process-variable translation table: Bridgman G/R versus AM laser power/scan speed/feed.
- Draft a mechanism hierarchy: buoyancy, Marangoni, shrinkage, electromagnetic, residual acceleration.

### Days 61-90: Produce the first publishable review outline

- Draft a review paper section titled: "From diffusion-controlled benchmarks to in-space melt pools."
- Build three figures:
  - Timeline of microgravity metal-solidification platforms.
  - Mechanism map of gravity-sensitive transport.
  - Gap map linking alloy systems to process routes and diagnostics.
- Decide whether the PhD's original contribution will be experimental, modelling-heavy, or synthesis-plus-model validation.

## 12. Key References And Sources

### Academic papers surfaced in this search

[1] [Structures in grain-refined directionally solidified hypoeutectic Al-Cu alloys: Benchmark experiments under microgravity on-board the International Space Station](https://consensus.app/papers/details/754e5e4fce435e0e9d1fa4ccacf492e3/?utm_source=chatgpt) - G. Zimmermann et al., 2024, *Materialia*, citations: 4.

[2] [On the interest of microgravity experimentation for studying convective effects during the directional solidification of metal alloys](https://consensus.app/papers/details/f71b805c13b052b2b0a4e1c20b919899/?utm_source=chatgpt) - H. Nguyen-Thi, G. Reinhart, B. Billia, 2017, *Comptes Rendus Mecanique*, citations: 25.

[3] [Comparative study of directional solidification of Al-7 wt% Si alloys in Space and on Earth](https://consensus.app/papers/details/0914f0efd7285a7886ae64923bb2789a/?utm_source=chatgpt) - Y. Li et al., 2019, *Journal of Crystal Growth*, citations: 28.

[4] [In situ investigation of the Columnar-to-Equiaxed Transition during directional solidification of Al-20wt.%Cu alloys on Earth and in microgravity](https://consensus.app/papers/details/a51ccc5265b5519c863ee509157bf305/?utm_source=chatgpt) - F. Ngomesse et al., 2021, *Acta Materialia*, citations: 32.

[5] [Analysis of gravity effects during binary alloy directional solidification by comparison of microgravity and Earth experiments with in situ observation](https://consensus.app/papers/details/f61034bfc4ac59fa907d3f0b72b68be5/?utm_source=chatgpt) - N. Bergeon et al., 2021, *European Physical Journal E*, citations: 9.

[6] [Influence of gravity level on Columnar-to-Equiaxed Transition during directional solidification of Al-20 wt.% Cu alloys](https://consensus.app/papers/details/34c7a788f55c56099cabf14525dd5abc/?utm_source=chatgpt) - L. Abou-Khalil et al., 2016, *Acta Materialia*, citations: 53.

[7] [Benchmark Al-Cu Solidification Experiments in Microgravity and on Earth](https://consensus.app/papers/details/75afad1eb6d85ca78e25ddf4870248b9/?utm_source=chatgpt) - T. Williams and C. Beckermann, 2022, *Metallurgical and Materials Transactions A*, citations: 12.

[8] [Effect of solidification conditions and surface pores on the microstructure and columnar-to-equiaxed transition in solidification under microgravity](https://consensus.app/papers/details/070e619459035c2f9523e8d2cea2a268/?utm_source=chatgpt) - Y. Li et al., 2018, *Journal of Alloys and Compounds*, citations: 21.

[9] [Spurious grain formation due to Marangoni convection during directional solidification of alloys in microgravity environment of International Space Station](https://consensus.app/papers/details/a50fd0a371965dd5957f9fa024d7d6f1/?utm_source=chatgpt) - S. A. Nabavizadeh et al., 2021, *Journal of Crystal Growth*, citations: 2.

[10] [The Marangoni convection effects on directional dendritic solidification](https://consensus.app/papers/details/b8195622cdf05eb49d9559848f0d5ca6/?utm_source=chatgpt) - S. A. Nabavizadeh et al., 2019, *Heat and Mass Transfer*, citations: 12.

[11] [Comparative study of gravity effects in directional solidification of Al-3.5 wt.% Si and Al-10 wt.% Cu alloys](https://consensus.app/papers/details/5a00c2d228965b9b9a75539256440487/?utm_source=chatgpt) - G. Zhang et al., 2024, *npj Microgravity*, citations: 3.

[12] [Directional solidification of Al-1.5 wt% Ni alloys under diffusion transport in space and fluid-flow localisation on earth](https://consensus.app/papers/details/c3edb1e8bf4b5a51a95a48488698bc89/?utm_source=chatgpt) - H. N. Thi et al., 2005, *Journal of Crystal Growth*, citations: 70.

[13] [Electromagnetic levitation containerless processing of metallic materials in microgravity: thermophysical properties](https://consensus.app/papers/details/dea025c28dc6581f863277dd3ffc1428/?utm_source=chatgpt) - M. Mohr et al., 2023, *npj Microgravity*, citations: 11.

[14] [Electromagnetic levitation containerless processing of metallic materials in microgravity: rapid solidification](https://consensus.app/papers/details/008c35a55d9a525c81309cbd4e024f2c/?utm_source=chatgpt) - D. Matson et al., 2023, *npj Microgravity*, citations: 18.

[15] [Precise Measurements of Thermophysical Properties of Liquid Ti-6Al-4V (Ti64) Alloy On Board the International Space Station](https://consensus.app/papers/details/23ae80de1a905b83bd0ee15be2058397/?utm_source=chatgpt) - M. Mohr et al., 2020, *Advanced Engineering Materials*, citations: 46.

[16] [Thermophysical Properties of Advanced Ni-Based Superalloys in the Liquid State Measured on Board the International Space Station](https://consensus.app/papers/details/8d1a6f244da7563b9d65957661b90f56/?utm_source=chatgpt) - M. Mohr et al., 2019, *Advanced Engineering Materials*, citations: 13.

[17] [Spiral eutectic growth dynamics facilitated by space Marangoni convection and liquid surface wave](https://consensus.app/papers/details/3c42f890525f544fbdabc25649d901c5/?utm_source=chatgpt) - H. Wang et al., 2024, *Physics of Fluids*, citations: 19.

[18] [Freezing Shrinkage Dynamics and Surface Dendritic Growth of Floating Refractory Alloy Droplets in Outer Space](https://consensus.app/papers/details/1dfdd69019fd53f994a5038ca92db57f/?utm_source=chatgpt) - H. Wang et al., 2024, *Advanced Materials*, citations: 35.

[19] [Remarkable undercooling capability and metastable thermophysical properties of liquid Nb84.1Si15.9 alloy revealed by electrostatic levitation in outer space](https://consensus.app/papers/details/e10783b8697f54fdbd67971e7bd683aa/?utm_source=chatgpt) - J. Chang et al., 2024, *Review of Scientific Instruments*, citations: 11.

[20] [Thermophysical properties of liquid Zr52.5Cu17.9Ni14.6Al10Ti5 - prospects for bulk metallic glass manufacturing in space](https://consensus.app/papers/details/020287dd9da35303842ca0e3ffc35132/?utm_source=chatgpt) - M. Mohr et al., 2019, *npj Microgravity*, citations: 19.

[25] [A comprehensive review on metal laser additive manufacturing in space: Modeling and perspectives](https://consensus.app/papers/details/6cc2f39d52965b7486821bffde5cfe70/?utm_source=chatgpt) - M. Taghizadeh and Z. Zhu, 2024, *Acta Astronautica*, citations: 27.

[26] [Additive manufacturing of metallic glass from powder in space](https://consensus.app/papers/details/9e1e0a50e5b15e23a5ba5465811f0737/?utm_source=chatgpt) - C. Neumann et al., 2023, *npj Microgravity*, citations: 7.

[27] [In-Space Additive Manufacturing: A Review](https://consensus.app/papers/details/af30c32c81185956b65e9e9c3770efac/?utm_source=chatgpt) - M. Hoffmann and A. Elwany, 2022, *Journal of Manufacturing Science and Engineering*, citations: 55.

[28] [CFD-Based Feasibility Study of Laser-Directed Energy Deposition With a Metal Wire for On-Orbit Manufacturing](https://consensus.app/papers/details/4e3cd42a1c225b639f5f0568ccf25d31/?utm_source=chatgpt) - S. N. R. Noori Rahim Abadi et al., 2022, citations: 7.

[29] [Columnar to equiaxed transition in solidification processing](https://consensus.app/papers/details/cb7793b2c7ef56dba015e0591f910a64/?utm_source=chatgpt) - W. Kurz, C. Bezencon, M. Gaumann, 2001, *Science and Technology of Advanced Materials*, citations: 410.

[30] [A solutal interaction mechanism for the columnar-to-equiaxed transition in alloy solidification](https://consensus.app/papers/details/3996a1ad300a54fb8562c2469f07b7b5/?utm_source=chatgpt) - M. Martorano, C. Beckermann, C. Gandin, 2003, *Metallurgical and Materials Transactions A*, citations: 248.

[31] [Columnar to equiaxed grain transition in as solidified alloys](https://consensus.app/papers/details/df595b9aadad5a55a04837c4cd86ca84/?utm_source=chatgpt) - J. A. Spittle, 2006, *International Materials Reviews*, citations: 234.

[32] [Simulation of the columnar-to-equiaxed transition in directionally solidified Al-Cu alloys](https://consensus.app/papers/details/ad82092c8d6f52c2975805012400e07c/?utm_source=chatgpt) - H. Dong and P. Lee, 2005, *Acta Materialia*, citations: 279.

[33] [Insight into the mechanisms of columnar to equiaxed grain transition during metallic additive manufacturing](https://consensus.app/papers/details/3118b11007f0560a8ac45c2cd66c58ec/?utm_source=chatgpt) - P. Liu et al., 2019, *Additive Manufacturing*, citations: 210.

[34] [Modelling columnar-to-equiaxed transition during fusion-based metal additive manufacturing](https://consensus.app/papers/details/f3ab8296a105554da888f6669bff589e/?utm_source=chatgpt) - A. Durga and G. Lindwall, 2023, *Additive Manufacturing*, citations: 14.

[35] [Compositional criteria to predict columnar to equiaxed transitions in metal additive manufacturing](https://consensus.app/papers/details/7f36b287c5fc5bc7bc415f2acef10f93/?utm_source=chatgpt) - R. Brooke et al., 2025, *Nature Communications*, citations: 3.

[36] [Analysis of preparatory directional solidification experiments for a new X-ray facility for the International Space Station](https://consensus.app/papers/details/3a5b08e9ae25539585eea9b95f2b586b/?utm_source=chatgpt) - G. Reinhart et al., 2025, *IOP Conference Series: Materials Science and Engineering*, citations: 0.

### Official and web sources

[21] [ESA launches first metal 3D printer to ISS](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/ESA_launches_first_metal_3D_printer_to_ISS) - ESA, 31 January 2024.

[22] [First metal 3D printing on Space Station](https://www.esa.int/ESA_Multimedia/Images/2024/06/First_metal_3D_printing_on_Space_Station) - ESA, 3 June 2024.

[23] [ESA 3D prints first metal part on the International Space Station](https://www.esa.int/Newsroom/Press_Releases/ESA_3D_prints_first_metal_part_on_the_International_Space_Station) - ESA, 6 September 2024.

[24] [A close-up look at the first metal part made in space](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/A_close-up_look_br_at_the_first_metal_br_part_made_in_space) - ESA, 13 November 2025.

[37] [3D Printing: Saving Weight and Space at Launch](https://www.nasa.gov/missions/station/iss-research/3d-printing-saving-weight-and-space-at-launch/) - NASA, 21 March 2025.

[38] [Adaptation of Metal Additive Manufacturing Processes for the International Space Station](https://ntrs.nasa.gov/citations/20205011519) - NASA NTRS, Prater et al.

[39] [Metal alloy research](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Research/Metal_alloy_research) - ESA overview of MICAST/MSL metal-alloy research.

[40] [Materials Science Laboratory - CETSOL and MICAST](https://ntrs.nasa.gov/citations/20090014815) - NASA NTRS.

## 13. Search Audit

- Research date: 2026-04-26.
- Local sources consulted: existing PhD vault notes, paper digests, extraction CSV files and synthesis pages.
- Consensus searches run: 5.
- Consensus tier detected: Pro, 20 papers per search.
- Consensus result ceiling: approximately 100 paper records before deduplication.
- Web searches run: 3 groups, focused on ESA/NASA current status and official programme context.
- Main coverage limitation: this is a strong launch-pad synthesis, not a complete systematic review. The next step is to deduplicate the returned papers, add DOI metadata, and extract numerical values into the existing literature matrix.
