---
title: "Review Queue and Gaps"
type: dashboard
---

# Action Required: Review Queue

The following papers have been ingested as a foundational draft but remain marked as `review_status: "draft"`.

```dataview
TABLE year, source_status, confidence
FROM "wiki/papers"
WHERE type = "paper" AND review_status = "draft"
SORT file.name ASC
```

# Missing Datapoints (Governance)

The following papers are missing crucial relevance scoring or confidence metrics.

```dataview
TABLE review_status, confidence, relevance_to_in_space_manufacturing AS "ISM Relevance"
FROM "wiki/papers"
WHERE type = "paper" AND (!confidence OR !relevance_to_in_space_manufacturing)
SORT file.name ASC
```

<!-- STATIC_TABLE_START -->
### Static Render (For Quartz)
| Title | Review Status | Last Reviewed |
|-------|---------------|---------------|
| [[wiki/papers/Elke__gravity_on_liquid_diffusion\|gravity on liquid diffusion]] | draft |  |
| [[wiki/papers/Haipeng_2024_refractory_droplet_freezing_in_space\|refractory droplet freezing in space]] | draft |  |
| [[wiki/papers/Viardin__mesoscopic_hypergravity\|mesoscopic hypergravity]] | draft |  |
| [[wiki/papers/Thomas_2023_Al-Cu_benchmark_g1g\|Al-Cu benchmark µg+1g]] | draft |  |
| [[wiki/papers/Gangopadhyay_2022_ISS-EML_stirring__nucleation\|ISS-EML stirring & nucleation]] | draft |  |
| [[wiki/papers/Neumann_2023_BMG_powder_AM_in_space\|BMG powder AM in space]] | draft |  |
| [[wiki/papers/Zhang_2024_ESL_control_on_CSS\|ESL control on CSS]] | draft |  |
| [[wiki/papers/Matson__ISS-EML_rapid_solidification\|ISS-EML rapid solidification]] | draft |  |
| [[wiki/papers/Yidong_2024_CSS_space-science_progress\|CSS space-science progress]] | draft |  |
| [[wiki/papers/Bergeon_2022_g_vs_1g_DS_in-situ\|µg vs 1g DS in-situ]] | draft |  |
| [[wiki/papers/QiuZhong_2024_CSS_ESL_thermophysics\|CSS ESL thermophysics]] | draft |  |
| [[wiki/papers/Fredriksson__g_solidification_analysis\|µg solidification analysis]] | draft |  |
| [[wiki/papers/Jiuzhou__immiscible_alloy_in_space\|immiscible alloy in space]] | draft |  |
| [[wiki/papers/Rakibul_2024_reduced-g_laser_welding\|reduced-g laser welding]] | draft |  |
| [[wiki/papers/Yanan_2024_CSS_materials_dataset\|CSS materials dataset]] | draft |  |
| [[wiki/papers/Seyed__Marangoni-driven_spurious_grains_ISS\|Marangoni-driven spurious grains ISS]] | draft |  |
| [[wiki/papers/Reitz_2021_AM_under_lunar-g__g\|AM under lunar-g / µg]] | draft |  |
| [[wiki/papers/Galenko_2022_Al-Ni_rapid_solidification\|Al-Ni rapid solidification]] | draft |  |
| [[wiki/papers/Reinhart_2022_XRMON-ISS_prep\|XRMON-ISS prep]] | draft |  |
| [[wiki/papers/Chang_2024_Nb-Si_ESL_undercooling\|Nb-Si ESL undercooling]] | draft |  |
| [[wiki/papers/Xunzuo_2024_metal_AM_in_space_review\|metal AM in space review]] | draft |  |
| [[wiki/papers/Wang__UHT_alloys__Marangoni_in_space\|UHT alloys & Marangoni in space]] | draft |  |
| [[wiki/papers/Guiyuan__Al-Si_vs_Al-Cu_DS\|Al-Si vs Al-Cu DS]] | draft |  |
| [[wiki/papers/Haipeng__spiral_eutectic_via_Marangoni\|spiral eutectic via Marangoni]] | draft |  |
| [[wiki/papers/Liao_2024_space_flow_on_dendriticeutectic_growth\|space flow on dendritic/eutectic growth]] | draft |  |
| [[wiki/papers/Yuze__RMF_on_Al-7Si_g\|RMF on Al-7Si µg]] | draft |  |
| [[wiki/papers/Kargl__XRISE-M_sounding_rocket\|XRISE-M sounding rocket]] | draft |  |
| [[wiki/papers/Francisco__ISRU_lunar_plant_analysis\|ISRU lunar plant analysis]] | draft |  |
| [[wiki/papers/Aboukhalil__Al-7Si_3D_fragment_g\|Al-7Si 3D fragment µg]] | draft |  |
| [[wiki/papers/Akamatsu__lamellar-to-rod_in_g\|lamellar-to-rod in µg]] | draft |  |
| [[wiki/papers/Mohr__ISS-EML_thermophysical_properties\|ISS-EML thermophysical properties]] | draft |  |
| [[wiki/papers/Ngomesse_2023_Al-20Cu_CET_in-situ\|Al-20Cu CET in-situ]] | draft |  |
| [[wiki/papers/Hrjer__Al-20Cu_in-situ_X-radiography\|Al-20Cu in-situ X-radiography]] | draft |  |
| [[wiki/papers/Fangjie_2023_hypergravity_review\|hypergravity review]] | draft |  |
| [[wiki/papers/Geng_2023_acoustic_levitation_solidification\|acoustic levitation solidification]] | draft |  |
| [[wiki/papers/Geng__g-jitter_on_Al-20Cu\|g-jitter on Al-20Cu]] | draft |  |
| [[wiki/papers/Mohr__thermophysical_g_review\|thermophysical µg review]] | draft |  |
| [[wiki/papers/Ludwig__peritectic_couple_growth_g\|peritectic couple growth µg]] | draft |  |
| [[wiki/papers/Lhu__Fe-19Si_on_CSS\|Fe-19Si on CSS]] | draft |  |
| [[wiki/papers/Robin_2023_sharpprogressive_CET_model\|sharp/progressive CET model]] | draft |  |
| [[wiki/papers/Andrew_2023_Al-Ni_ISS-EML_kinetics\|Al-Ni ISS-EML kinetics]] | draft |  |
| [[wiki/papers/Becker_2023_Al-Cu__Al-Ge_equiaxed_g\|Al-Cu / Al-Ge equiaxed µg]] | draft |  |
| [[wiki/papers/Roosz__Al-7Si_eutectic__2_in_g\|Al-7Si eutectic & λ2 in µg]] | draft |  |
| [[wiki/papers/Mohr__Ti-6Al-4V_ISS-EML\|Ti-6Al-4V ISS-EML]] | draft |  |
| [[wiki/papers/Huang_2024_Ti-46Al-8Nb_CA-FVM_centrifugal\|Ti-46Al-8Nb CA-FVM centrifugal]] | draft |  |
| [[wiki/papers/Haipeng__Zr50V50_hypereutectic_in_space\|Zr50V50 hypereutectic in space]] | draft |  |
| [[wiki/papers/Viardin_2023_CVDL_on_phase-field_dendrites\|CV/DL on phase-field dendrites]] | draft |  |
| [[wiki/papers/Blake_2024_ISRU_ductile_iron\|ISRU ductile iron]] | draft |  |
| [[wiki/papers/Zimmermann__grain-refined_Al-Cu_ISS\|grain-refined Al-Cu ISS]] | draft |  |
| [[wiki/papers/Akamatsu__SCN_transparent_g\|SCN transparent µg]] | draft |  |
| [[wiki/papers/Mitra_2024_laser_AM_in_space_review\|laser AM in space review]] | draft |  |
| [[wiki/papers/Murphy__MASER-13_front-tracking_Al-20Cu\|MASER-13 front-tracking Al-20Cu]] | draft |  |
| [[wiki/papers/Apurba__Al-Cu_nanostructure_MD\|Al-Cu nanostructure MD]] | draft |  |
| [[wiki/papers/Reinhart__in-situ_X-ray_review\|in-situ X-ray review]] | draft |  |
<!-- STATIC_TABLE_END -->