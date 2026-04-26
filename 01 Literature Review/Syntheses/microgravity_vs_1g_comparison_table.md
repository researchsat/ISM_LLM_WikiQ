# 1g vs. Microgravity (µg) Solidification — Comparison Table by Phenomenon

**Companion to:** `microgravity_solidification_deep_research_2026.md`
**Date:** 22 April 2026
**Structure:** One row per phenomenon. Columns give Flemings chapter anchor, 1g prediction or observation, µg observation, magnitude of the gravity effect, and the 2–3 most diagnostic references (prioritizing 2024–2026 where available).

Chapter codes follow Flemings, *Solidification Processing* (1974): **Ch. 1** Heat Flow, **Ch. 2** Plane Front, **Ch. 3** Cellular/Dendritic, **Ch. 4** Polyphase/Eutectic, **Ch. 5** Cast Structure, **Ch. 6** Cast Structure Variants, **Ch. 7** Interdendritic Flow & Macrosegregation, **Ch. 8** Thermodynamics, **Ch. 9** Nucleation & Growth Morphology, **Ch. 10** Processing–Structure–Property.

---

## A. Fluid Flow, Convection, and Macrosegregation (Flemings Ch. 7)

| # | Phenomenon | Flemings Ch. | 1g prediction / observation | µg observation | Magnitude of gravity effect | Key references |
|---|---|---|---|---|---|---|
| A1 | Axial macrosegregation (Al-Si columnar) | 7 | Si enriches **upward** to +20–30% due to solutal buoyancy (ρ_liquid decreases with Si) | ±5% flat diffusive profile | ~4–6× reduction in segregation amplitude | Zhang 2024 *npj Microgravity* [doi 10.1038/s41526-024-00454-9]; Mehrabian/Keane/Flemings 1970 |
| A2 | Axial macrosegregation (Al-Cu equiaxed) | 7 | Cu enriches **downward** (dense Cu sinks in melt) | "Almost disappears" — uniform | Qualitative change (directional sign lost) | Zhang 2024; Chen 2025 *JOM* [doi 10.1007/s11837-025-07956-1] |
| A3 | Radial macrosegregation (Al-20Cu, Bridgman) | 7 | ~15–20% radial | <5% | ~3–4× reduction | Spinella 2024 *Materialia*; Williams 2022 *MMTA* |
| A4 | Inverse (shrinkage-driven) segregation | 7 | Present at chill face | **Still present** — gravity-independent | Equivalent (both regimes) | Zhang 2024; Mirihanage 2023 *npj Microgravity* |
| A5 | Channel/freckle segregation | 7 | Present above Ra_cr ≈ 0.25–46 (geometry/anisotropy dependent) | Not observed in any µg Ni-superalloy or Al-Cu trial | Critical Rayleigh number effectively → ∞ | Mehrabian/Flemings 1970; CETSOL/MICAST dataset; Zhang 2024 |
| A6 | Interdendritic flow driver | 7 | Buoyancy + shrinkage | **Shrinkage only** | Buoyancy term eliminated | Simpson & Kou 1984; Ganesan & Poirier 1990 |
| A7 | Solute redistribution mechanism | 7 | Convective (bulk mixing) | Purely diffusive (BPS/Tiller) | Transport mode switch | Thi 2005; Stelian 2005 |
| A8 | Surface cavity / freezing-shrinkage morphology | 2, 7 | Masked by buoyancy-driven flow | Wrinkled & spiral patterns visible (refractory droplets) | New morphology accessible | Wang 2024 *Adv. Mater.* [doi 10.1002/adma.202313162]; Liu 2024 *Adv. Funct. Mater.* |

---

## B. Dendritic and Cellular Solidification (Flemings Ch. 3, 5)

| # | Phenomenon | Flemings Ch. | 1g prediction / observation | µg observation | Magnitude | Key references |
|---|---|---|---|---|---|---|
| B1 | Secondary dendrite arm spacing SDAS (Al-7Si, matched pair) | 3 | 150–250 µm | 120–180 µm | ~30% finer in µg | Zhang 2024; Roósz 2022 *Crystals* |
| B2 | Primary dendrite arm spacing PDAS | 3 | Convection-broadened; scatter | Narrower distribution | Histogram tightening | Williams 2022; Ngomesse 2021 *Acta Mat.* |
| B3 | Equiaxed grain size (Al-Cu, grain-refined) | 5 | 200–500 µm | 100–300 µm (3× smaller vs. non-refined µg) | ~2–3× finer | Zimmermann 2024 *Materialia*; Williams 2022 |
| B4 | Columnar-to-equiaxed transition (CET) position (Al-7Si, non-refined) | 5 | ~30% solidified | Absent or >90% solidified | CET largely suppressed | Mirihanage 2023 *npj Microgravity*; Ngomesse 2021 |
| B5 | CET blocking mechanism | 5 | Solutal blocking (dominant) | Mechanical/shrinkage-flow blocking | Mechanism shift | Ngomesse 2021 (MASER-14 X-ray) |
| B6 | CET onset acceleration under g-jitter | 5 | N/A (g is fixed) | Negligible up to ≤±0.04 g (parabolic flight) | First empirical threshold bound | Geng 2025 *IOP Conf. Ser.* |
| B7 | Dendrite tip velocity V(ΔT) in SCN | 3, 9 | Convection-enhanced; scatter hides theory | LGK + non-paraboloid tip + integration limit 0.2R₁ → agrees within scatter | IDGE historical 20% gap resolved | Glicksman 1994–99; Alexandrov 2026 *Acta Mat.* |
| B8 | Equiaxed nucleation dynamics | 5, 9 | Continuous, spatially scattered (convection sampling) | **Burst-like, simultaneous** (uniform solute field) | Qualitative change | Becker 2023 *MMTA* [doi 10.1007/s11661-023-07092-0] |
| B9 | Dendritic growth velocity (isothermal, Al-Cu/Ge at same ΔT) | 3 | ≈ 8 µm/s | ≈ 8 µm/s — identical | No effect | Becker 2023 |
| B10 | Fragment density (Al-7Si 3D) | 5 | Sedimentation-dependent | Misorientation-driven only (no sedimentation) | Mechanism change | Abou-Khalil 2023 *Acta Mat.* |
| B11 | Phase-field vs. experiment (primary spacing) | 3 | >30% discrepancy pre-2020 | 5–10% with GPU PF vs. DECLIC-DSI | Quantitative closure | Tian 2026; Medjkoune 2025 *Acta Mat.* |
| B12 | Dendrite array packing (3D stability) | 3 | Largely untested (2D proxies) | 3D benchmark established | New quantitative regime | Medjkoune 2025 |

---

## C. Eutectic, Peritectic, and Polyphase / Immiscible (Flemings Ch. 4, 6)

| # | Phenomenon | Flemings Ch. | 1g prediction / observation | µg observation | Magnitude | Key references |
|---|---|---|---|---|---|---|
| C1 | Jackson-Hunt λ²V = K (2D lamellar) | 4 | Exponent n ≈ 0.5 (ideal) | n = 0.484 (Al₀.₉CoCrNi₂.₁); 3 µm → 0.4 µm across 0.1–2000 µm/s for Ni-Sn | 2D J-H confirmed in µg | Xu 2024 *Intermetallics*; Cao 2025 *Materials* |
| C2 | 3D anisotropy-driven grain morphology | 4, 6 | Isotropic J-H in 2D doesn't predict | *Laminated Matrix with Rods* (LMR) — new type | New morphology accessible | Mohagheghi 2024 *MMTA* |
| C3 | Oscillatory / locked eutectic colonies | 4 | Damped by weak convection (~1 µm/s is enough) | Persistent, observable | Instability revealed | Akamatsu 2023 *npj Microgravity* |
| C4 | Peritectic coupled growth | 4 | Qualitatively reported (TRIS-NPG) | Phase-field matches µg; lamellar↔rod via composition | Mechanistic wavelength selection now predictable | Rátkai 2024 *Acta Mat.*; Ludwig 2022 ISS |
| C5 | Coupled vs. divorced eutectic (Fe-19Si) | 4 | **Divorced** (convection redistributes solute) | **Coupled** (diffusion-limited) | Morphology switch | Hu 2025 *Rev. Mater. Res.* |
| C6 | Eutectic undercooling achieved (Zr-V) | 4, 9 | Ground ~30–80 K typical | 253 K with spiral eutectic (CSS) | ~3–8× deeper | Wang 2024 *Phys. Fluids* 36, 042110 |
| C7 | Spiral / Marangoni-wave coupled growth | 4, 6 | Not observed | Present in CSS refractory droplets | New pattern class | Wang 2024; Liao 2025 *Adv. Mater.* |
| C8 | Monotectic droplet separation (Al-Bi, Fe-Cu) | 6 | Stokes sedimentation dominates — gross phase separation | Marangoni-only residue — dispersed droplets 1–2 µm | Sedimentation eliminated | Jiang 2020; Uporov 2024 *Intermetallics* |
| C9 | Core-shell immiscible microsphere formation | 6 | Requires forced stabilization | Natural outcome (Marangoni-driven) | Mechanism isolated | Chen 2024 *JMPT*; Wang Li 2019 |
| C10 | Anomalous eutectic at velocity transitions | 4 | Transient, often obscured by convection | Clearly resolved in µg (Ni-Sn) | Transient state observable | Cao 2025 |

---

## D. Nucleation, Undercooling, and Interface Kinetics (Flemings Ch. 9)

| # | Phenomenon | Flemings Ch. | 1g prediction / observation | µg observation | Magnitude | Key references |
|---|---|---|---|---|---|---|
| D1 | Max undercooling (Nb-Si eutectic) | 9 | Ground levitator ~100–180 K | **437 K** (CSS-ESL) | ~2.5× deeper; approaches 0.2 T_L homogeneous limit | Wang 2024 *Angew. Chem.* [doi 10.1002/ange.202313165] |
| D2 | Max undercooling (Nb₈₄.₁Si₁₅.₉) | 9 | ~100 K | **421 K** (0.18 T_L) | ~4× deeper | Chang 2024 *Rev. Sci. Instr.* 95, 095103 |
| D3 | Max undercooling (Zr-Ni-Al-Nb BMG) | 9 | Ground-limited | 274 K → 83% amorphous phase | Metastable amorphization accessible | 2025 *MMTA* [doi 10.1007/s11661-025-07887-1] |
| D4 | Undercooling record (Zr₆₄V₃₆) | 9 | N/A (refractory) | 253 K + spiral eutectic | Previously inaccessible | Wang 2024 *Phys. Fluids* |
| D5 | Nucleation under stirring | 9 | Faster on ground (convection samples activation sites) | **Slower** with RF stirring (CFM confirmed) — first µg evidence | Direct CFM validation | Gangopadhyay 2025 *J. Chem. Phys.* 162, 134502 |
| D6 | Metastable phase selection (Fe-Cr-Ni) | 9 | FCC dominant | BCC selected under deep undercooling | Phase-selection pathway altered | Herlach 1997 (revived 2024 ISS-EML); Hasan & Choudhuri 2025 |
| D7 | Recalescence velocity V(ΔT) | 9 | Often unresolved at high ΔT | U-shaped curve resolved (Zr-Ni-Al; Al-Ni ISS-EML) | Kinetics quantifiable | Alexandrov 2025 *Math. Methods Appl. Sci.*; Al-Ni ISS-EML 2021 |
| D8 | Interface response function | 9 | Rarely measured in deep undercooling | Becoming quantifiable on CSS | Methodology advance | Jin 2024 *Acta Phys. Sin.*; Wang 2024 *Adv. Mater.* |
| D9 | Container-wall nucleation | 9 | Dominant in 1g crucibles (limits ΔT) | Eliminated (containerless) | Qualitative removal | Herlach 1993, 2010 |
| D10 | Burst-vs-continuous nucleation geometry | 9 | Continuous, scattered | Burst, simultaneous | Qualitative change | Becker 2023 |

---

## E. Thermophysical Properties, Heat Flow, Plane-Front (Flemings Ch. 1, 2, 8)

| # | Phenomenon | Flemings Ch. | 1g prediction / observation | µg observation | Magnitude | Key references |
|---|---|---|---|---|---|---|
| E1 | BPS solute boundary layer (Al-1.5Ni plane front) | 2 | Convection-reduced boundary layer | Full BPS analytic profile | Analytical theory validated | Thi 2005 *J. Crystal Growth* |
| E2 | g-jitter effect on BPS boundary layer | 2 | N/A (steady g) | Sensitive below 10⁻² Hz | Periodic boundary-layer destabilization | Stelian 2005 *J. Cryst. Growth* |
| E3 | Liquid density uncertainty | 1, 8 | 5–10% ground EML | **±0.4–1% ISS-EML/ELF** | ~5–10× improvement | Au study 2023; rare-earth titanate 2024; Vit106a 2026 *npj Microgravity* |
| E4 | Liquid surface tension uncertainty | 8 | 3–8% | **±0.6–2%** | ~3–10× improvement | Au uncertainty 2023; Mohr ISS-EML III |
| E5 | Liquid viscosity uncertainty | 8 | 5–15% | **±1.9%** (Au); Vogel-Fulcher fit for BMGs | ~3–5× improvement | Au 2023; Vit106a 2026 |
| E6 | Cross-platform cross-validation (ISS vs. CSS) | 8 | Not applicable | **Not yet performed** — open gap | Systematic comparison missing | CSS dataset Liu 2025/26 *Sci. Data*; Brillo 2024 (ground EML/ESL only) |
| E7 | Evaporation mass loss during EML | 1, 8 | Modeled with wide uncertainty | Validated via post-flight SEM-EDX in three labs (FeCrNi) | Mass-loss model confirmed | *npj Microgravity* 2024 [doi 10.1038/s41526-024-00416-1] |
| E8 | Specific heat / emissivity of BMGs | 1, 8 | Ground-limited by container | Vit106a full dataset now available | New benchmark class | Vit106a 2026 |

---

## F. Detached Bridgman and Semiconductor Crystal Quality (Flemings Ch. 2, 9)

| # | Phenomenon | Flemings Ch. | 1g prediction / observation | µg observation | Magnitude | Key references |
|---|---|---|---|---|---|---|
| F1 | Detachment from crucible wall | 2 | Rare (suppressed by hydrostatic P) | Natural outcome; 10–100 µm gap | Qualitative change | Duffar 1990 *J. Cryst. Growth* 76 cits.; Regel & Wilcox 1998 |
| F2 | Dewetting angle criterion | 2 | Ground-workable only with rough crucibles or applied gas Δp | Capillary-only (contact + growth angle > 180°) | Mechanism isolated | Duffar 1990; Cröll 2009 *MRS Bulletin* |
| F3 | Dislocation density (GeSi, GaSb) | 2, 9 | Baseline | ~10×–50× lower in detached-grown crystal | 1–1.5 orders of magnitude | Regel & Wilcox 1998; Volz ISS GeSi |
| F4 | **Dislocation density (InAsSb CSS 2026)** | 2, 9 | Baseline | **10× lower** | 1 order of magnitude | *npj Microgravity* 2026 [InAsSb CSS] |
| F5 | Compositional uniformity (InAsSb CSS) | 2 | Variable across wafer | ±0.5 mol% Sb over 11 mm × 2.5 mm | Near-uniform | *npj Microgravity* 2026 |
| F6 | Stacking-fault elimination (InSe CSS) | 9 | Present; masks intrinsic properties | **Eliminated** — activates intrinsic sliding ferroelectricity | Qualitative property unlock | *Nature Communications* 2026 |
| F7 | Semiconductor quality meta-baseline (160 crystals, 1973–2016) | 10 | Baseline | **86% improved on ≥1 metric** | Quantitative meta-answer | Vincent 2024 *npj Microgravity* |
| F8 | Ground-analog: high magnetic field (10 T) Bridgman | 2 | Partial µg-emulation | ~35% dislocation reduction | Ground approximation (not commercial) | 2026 *AIP Scilight* [unverified in peer-reviewed form] |

---

## G. Gas Porosity, Bubble Behaviour, and AM Bridge (Flemings Ch. 10; cross to AM literature)

| # | Phenomenon | Flemings Ch. | 1g prediction / observation | µg observation | Magnitude | Key references |
|---|---|---|---|---|---|---|
| G1 | Gas bubble buoyant escape | 10 | Rise under g; most bubbles vent | Bubbles trapped (no buoyancy) — Marangoni-only escape | Mechanism change | µg porosity literature; *Nat. Comm.* 2024 pore evolution (AM) |
| G2 | AM DED pore retention | — | Lower than µg (buoyant venting helps) | 49.7% → 53.9% volume fraction (metallic glass AM 1g vs µg) | Modestly higher retention in µg | *Progress in Additive Manufacturing* 2025 (metallic glass) |
| G3 | Marangoni-driven bubble motion | 10 | Masked by buoyancy | Isolated & quantifiable in µg / AM | Quantitative mechanism now explicit | *Nat. Comm.* 2024 [doi 10.1038/s41467-024-45913-9] |
| G4 | µg → AM defect-mitigation bridge | 10 | — | Emerging; no full cross-validation yet | Open linkage | *Adv. Eng. Materials* 2025 review adem.202501082 |

---

## H. Processing–Structure–Property and Mechanical Data (Flemings Ch. 10) — The Persistent Gap

| # | Phenomenon | Flemings Ch. | 1g prediction / observation | µg observation | Magnitude | Key references |
|---|---|---|---|---|---|---|
| H1 | Tensile strength of ISS/CSS-solidified metallic alloys | 10 | Baseline | **No published open-literature data** as of April 2026 | Gap remains | — (open gap) |
| H2 | Fatigue / creep of µg-solidified alloys | 10 | Baseline | **No published data** | Gap remains | — |
| H3 | Hardness / microindentation | 10 | Baseline | Ruan 2017 AlAgGe: finer grain → higher H, but very limited dataset | Under-populated | Ruan 2017 *Acta Mat.*; Hu 2025 Fe-19Si |
| H4 | Semiconductor carrier mobility (µg vs 1g) | 10 | Baseline | Improved in 86% of 160 crystals (meta-analysis) | Consistent but aggregate | Vincent 2024 *npj Microgravity* |
| H5 | InSe piezo/ferroelectric response (CSS) | 10 | Suppressed by stacking faults | High-performance ferroelectric activated | Qualitative property unlock | *Nat. Comm.* 2026 |
| H6 | Grain-size vs. cooling-rate anomaly (Fe-19Si) | 10 | Finer grain expected without convection | **Larger grain in µg** (lower effective cooling rate) | Counter-intuitive; unresolved | Hu 2025 |

---

## Reference Key (full citations)

**2024–2026 (primary new additions):**
- Alexandrov, D. V. et al. (2026). Ice crystals under terrestrial and microgravity conditions… *Acta Materialia*. doi:10.1016/j.actamat.2026.000650
- Alexandrov, D. V. et al. (2025). Mathematical modeling of measured recalescence velocities. *Math. Methods Appl. Sci.*
- Akamatsu, S. et al. (2023). Microgravity studies of solidification patterns in model transparent alloys onboard the ISS. *npj Microgravity* 9, 61. doi:10.1038/s41526-023-00326-8
- Brillo, J. et al. (2024). Transport property measurement of liquid metals and alloys using EML and ESL. *Int. J. Thermophysics.*
- Cao, S. et al. (2025). Unraveling anomalous eutectic formation in Ni-Sn… *Materials.*
- Chang, J. et al. (2024). Remarkable undercooling capability and metastable thermophysical properties of Nb₈₄.₁Si₁₅.₉. *Rev. Sci. Instrum.* 95, 095103. doi:10.1063/5.0219739
- Chen, Q. et al. (2025). Effects of gravity and process factors on dendrite growth, CET, and compositional segregation in Al-Si / Al-Cu. *JOM.* doi:10.1007/s11837-025-07956-1
- Chen et al. (2024). An improved preparation method of core-shell Al@Sn-Bi microspheres. *J. Mater. Proc. Technol.*
- De Albuquerque et al. (2024, 2025). Al-Cu-Sn immiscible X-radiography series. *Mater. Today Commun.* / *Metals.*
- Galenko, P. et al. (2024). Dendrite growth under a forced convective flow: A review. *Physics Reports.*
- Gangopadhyay, A. et al. (2025). Slower nucleation kinetics with stirring in a supercooled Zr₈₀Pt₂₀ liquid — ISS-EML. *J. Chem. Phys.* 162, 134502.
- Geng et al. (2025). G-jitter thresholds in Al-20Cu under parabolic flight. *IOP Conf. Ser.*
- Gu, Y. et al. (2024). Recent progress in space science on CSS 2022–2024. *Chin. J. Space Sci.*
- Hasan, M. M. & Choudhuri, D. (2025). Metastable states assisted homogeneous nucleation in supercooled liquid aluminum alloys. *J. Chem. Phys.* 162, 084501.
- He, Z. et al. (2024). Pressure effects on SDAS and columnar dendrite growth rate via PF. *MMTB.*
- Hu, L. et al. (2025). Fe-19%Si on CSS: thermophysical properties and solidification mechanisms. *Rev. Mater. Res.*
- Jiang, H. et al. (2023). In-situ X-ray monitoring of solidification (XRMON-GF review). *npj Microgravity* 9, 63. doi:10.1038/s41526-023-00321-z
- Jin, Y.-J. et al. (2024). Thermophysical properties and rapid solidification of Zr₆₀Ni₂₅Al₁₅ under ESL. *Acta Phys. Sin.*
- Liao et al. (2025). Dynamic localization of dendritic & eutectic growth patterns under space fluid flow (CSS). *Advanced Materials.*
- Liu, Y. et al. (2025/2026). Materials dataset from microgravity levitation experiments on the China Space Station. *Scientific Data.* doi:10.1038/s41597-025-06428-0
- Mancias, J. et al. (2025). Mapping microstructure transitions during rapid alloy solidification with Bayesian-guided PF. *Acta Materialia.*
- Medjkoune, M. et al. (2025). Benchmark µg experiments and computations for 3D dendritic-array stability. *Acta Materialia.*
- Mohagheghi, M. et al. (2024). Interphase boundary energy anisotropy and "Laminated Matrix with Rods" grain. *MMTA.*
- Murphy, A. et al. (2025). Mesoscale front-tracking simulation of µg equiaxed Al-20Cu (MASER-13). *IOP Conf. Ser.*
- Rátkai, L. et al. (2024). PF modeling of peritectic coupled growth in TRIS-NPG. *Acta Materialia.*
- *npj Microgravity* special issue (2024). A meta-analysis of semiconductor materials fabricated in microgravity. doi:10.1038/s41526-024-00410-7
- *npj Microgravity* (2024). Thermodynamic assessment of evaporation during molten steel testing onboard ISS. doi:10.1038/s41526-024-00416-1
- *npj Microgravity* (2024). Microgravity effects on non-equilibrium melt processing of neodymium titanate. doi:10.1038/s41526-024-00371-x
- *npj Microgravity* (2025). Glass-forming ability of La₂O₃–Nb₂O₅ under µg. doi:10.1038/s41526-025-00520-w
- *npj Microgravity* (2026). Thermophysical properties and solidification of Vit106a. doi:10.1038/s41526-026-00572-6
- *npj Microgravity* (2026). Microgravity-enabled growth of uniform InAsSb bulk single crystal. doi:10.1038/s41526-026-00581-5
- *Nature Communications* (2026). Microgravity-activated high-performance vdW InSe ferroelectric semiconductor. doi:10.1038/s41467-026-70520-1
- *Nature Communications* (2024). Pore evolution mechanisms during DED AM. doi:10.1038/s41467-024-45913-9
- Spinella, I. et al. (2024). Grain-refined directionally solidified hypoeutectic Al-Cu — ISS benchmark. *Materialia.*
- Tian, J. et al. (2026). Benchmarking of massively parallel phase-field codes for directional solidification.
- Tourret, D. et al. (2023). Morphological stability of solid–liquid interfaces under AM conditions. *Acta Materialia.*
- Uporov et al. (2024). Monotectic composites with YGdTbDyHo HEA particles. *Intermetallics.*
- Viardin, A. et al. (2025). Automatic detection of dendritic microstructure with CV/DL. *Integr. Mater. Manuf. Innov.*
- Wang, H. et al. (2024). Metastable liquid properties and surface flow patterns of UHT alloys in outer space. *Angew. Chem.* doi:10.1002/ange.202313165
- Wang, H. et al. (2024). Freezing shrinkage dynamics and surface dendritic growth of floating refractory droplets. *Adv. Mater.* doi:10.1002/adma.202313162
- Wang, H. et al. (2024). Spiral eutectic growth dynamics facilitated by space Marangoni convection and liquid surface wave. *Phys. Fluids* 36, 042110.
- Xu et al. (2024). Directional Al₀.₉CoCrNi₂.₁ HEA: lamellar eutectic formation. *Intermetallics.*
- Zhang, G. et al. (2024). Comparative study of gravity effects in Al-3.5Si and Al-10Cu directional solidification. *npj Microgravity.* doi:10.1038/s41526-024-00454-9
- Zhang et al. (2024). In-situ analysis of solute and flow fields in immiscible Al-Bi directional solidification. *AIP Advances.*
- Zimmermann, G. et al. (2024). Structures in grain-refined directionally solidified hypoeutectic Al-Cu — CETSOL ISS benchmark. *Materialia.*

**Foundational / pre-2024 anchors (cited inline above):**
- Mehrabian, R., Keane, M. & Flemings, M. C. (1970). Interdendritic fluid flow and macrosegregation; influence of gravity. *Met. Trans. B.*
- Simpson, J. E. & Kou, S. (1984). Effects of gravity on interdendritic flow. *Met. Trans. A.*
- Ganesan, S. & Poirier, D. R. (1990). Conservation of mass and momentum for the flow of interdendritic liquid. *Met. Trans. B.*
- Thi, H. N. et al. (2005). Directional solidification of Al-1.5 wt% Ni alloys under diffusion transport in space. *J. Crystal Growth.*
- Stelian, C. et al. (2005). Modeling of a space experiment on Bridgman solidification — g-jitter effects. *J. Crystal Growth.*
- Duffar, T. et al. (1990). Crucible de-wetting during Bridgman growth of semiconductors in µg. *J. Crystal Growth.*
- Regel, L. L. & Wilcox, W. R. (1998). Detached solidification in microgravity: a review. *Microgravity Sci. Technol.*
- Cröll, A. et al. (2009). Detached Bridgman growth — a standard crystal growth method with a new twist. *MRS Bulletin.*
- Glicksman, M. E. et al. (1994–1999). IDGE — A test of dendritic growth theory using space flight. (series)
- Williams, T. et al. (2022). Benchmark Al-Cu solidification experiments in µg and on Earth. *MMTA.*
- Ngomesse, M. et al. (2021). In-situ investigation of CET during directional solidification (MASER-14). *Acta Materialia.*
- Roósz, A. et al. (2022). Al-7Si microstructure under microgravity. *Crystals.*
- Mirihanage, W. U. et al. (2023). Microgravity studies of solidification patterns onboard ISS. *npj Microgravity.*
- Becker, M. et al. (2023). Nucleation and growth of equiaxed dendrites in thin Al-Cu/Ge samples in µg and on Earth. *MMTA.* doi:10.1007/s11661-023-07092-0
- Herlach, D. M. et al. (1993, 2007, 2010). Containerless undercooling/solidification series.
- Ruan, Y. et al. (2017). AlAgGe ternary solidification under microgravity. *Acta Materialia.*
- Jiang, W. et al. (2020). Progress in monotectic alloy solidification under microgravity. (review)
- Ludwig, A. et al. (2022). Peritectic TRIS-NPG on ISS.
- Mohr, M. et al. (2020, 2022). Properties and solidification of metallic melts under microgravity; ISS-EML Part III.
- Vincent, L. et al. (2024). Meta-analysis of semiconductor materials fabricated in microgravity. *npj Microgravity.*

---

## Usage notes

- The table is organized so that each section (A–H) maps onto a Flemings chapter or chapter cluster. When writing your thesis chapters, you can pull rows directly.
- For each row, the "Magnitude" column gives the practical size of the gravity effect — use this to decide which phenomena are worth proposing a dedicated benchmark experiment around.
- Section H (mechanical properties) intentionally shows empty cells — that is the actual gap in the field and therefore your strongest PhD-thesis lever.

*End of comparison table.*
