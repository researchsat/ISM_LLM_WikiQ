---
title: "Platforms and Alloys Matrix"
type: dashboard
---

# Experimental Platforms Used

A live map of which microgravity simulation platforms are tied to which papers.

```dataview
TABLE platform, facility, mission
FROM "wiki/papers"
WHERE type = "paper" AND (platform != null OR length(platform) > 0)
SORT file.name ASC
```

# Associated Alloy Systems

Map of literature by alloy composition constraints.

```dataview
TABLE alloy_family, alloy_composition, solidification_mode
FROM "wiki/papers"
WHERE type = "paper" AND (alloy_family != null OR length(alloy_family) > 0)
SORT file.name ASC
```

<!-- STATIC_TABLE_START -->
### Static Render (For Quartz)
| Title | Platform | Alloy Family |
|-------|----------|--------------|
| [[wiki/papers/Elke__gravity_on_liquid_diffusion\|gravity on liquid diffusion]] |  |  |
| [[wiki/papers/Haipeng_2024_refractory_droplet_freezing_in_space\|refractory droplet freezing in space]] |  |  |
| [[wiki/papers/Viardin__mesoscopic_hypergravity\|mesoscopic hypergravity]] |  |  |
| [[wiki/papers/Thomas_2023_Al-Cu_benchmark_g1g\|Al-Cu benchmark µg+1g]] |  |  |
| [[wiki/papers/Gangopadhyay_2022_ISS-EML_stirring__nucleation\|ISS-EML stirring & nucleation]] |  |  |
| [[wiki/papers/Neumann_2023_BMG_powder_AM_in_space\|BMG powder AM in space]] |  |  |
| [[wiki/papers/Zhang_2024_ESL_control_on_CSS\|ESL control on CSS]] |  |  |
| [[wiki/papers/Matson__ISS-EML_rapid_solidification\|ISS-EML rapid solidification]] |  |  |
| [[wiki/papers/Yidong_2024_CSS_space-science_progress\|CSS space-science progress]] |  |  |
| [[wiki/papers/Bergeon_2022_g_vs_1g_DS_in-situ\|µg vs 1g DS in-situ]] |  |  |
| [[wiki/papers/QiuZhong_2024_CSS_ESL_thermophysics\|CSS ESL thermophysics]] |  |  |
| [[wiki/papers/Fredriksson__g_solidification_analysis\|µg solidification analysis]] |  |  |
| [[wiki/papers/Jiuzhou__immiscible_alloy_in_space\|immiscible alloy in space]] |  |  |
| [[wiki/papers/Rakibul_2024_reduced-g_laser_welding\|reduced-g laser welding]] |  |  |
| [[wiki/papers/Yanan_2024_CSS_materials_dataset\|CSS materials dataset]] |  |  |
| [[wiki/papers/Seyed__Marangoni-driven_spurious_grains_ISS\|Marangoni-driven spurious grains ISS]] |  |  |
| [[wiki/papers/Reitz_2021_AM_under_lunar-g__g\|AM under lunar-g / µg]] |  |  |
| [[wiki/papers/Galenko_2022_Al-Ni_rapid_solidification\|Al-Ni rapid solidification]] |  |  |
| [[wiki/papers/Reinhart_2022_XRMON-ISS_prep\|XRMON-ISS prep]] |  |  |
| [[wiki/papers/Chang_2024_Nb-Si_ESL_undercooling\|Nb-Si ESL undercooling]] |  |  |
| [[wiki/papers/Xunzuo_2024_metal_AM_in_space_review\|metal AM in space review]] |  |  |
| [[wiki/papers/Wang__UHT_alloys__Marangoni_in_space\|UHT alloys & Marangoni in space]] |  |  |
| [[wiki/papers/Guiyuan__Al-Si_vs_Al-Cu_DS\|Al-Si vs Al-Cu DS]] |  |  |
| [[wiki/papers/Haipeng__spiral_eutectic_via_Marangoni\|spiral eutectic via Marangoni]] |  |  |
| [[wiki/papers/Liao_2024_space_flow_on_dendriticeutectic_growth\|space flow on dendritic/eutectic growth]] |  |  |
| [[wiki/papers/Yuze__RMF_on_Al-7Si_g\|RMF on Al-7Si µg]] |  |  |
| [[wiki/papers/Kargl__XRISE-M_sounding_rocket\|XRISE-M sounding rocket]] |  |  |
| [[wiki/papers/Francisco__ISRU_lunar_plant_analysis\|ISRU lunar plant analysis]] |  |  |
| [[wiki/papers/Aboukhalil__Al-7Si_3D_fragment_g\|Al-7Si 3D fragment µg]] |  |  |
| [[wiki/papers/Akamatsu__lamellar-to-rod_in_g\|lamellar-to-rod in µg]] |  |  |
| [[wiki/papers/Mohr__ISS-EML_thermophysical_properties\|ISS-EML thermophysical properties]] |  |  |
| [[wiki/papers/Ngomesse_2023_Al-20Cu_CET_in-situ\|Al-20Cu CET in-situ]] |  |  |
| [[wiki/papers/Hrjer__Al-20Cu_in-situ_X-radiography\|Al-20Cu in-situ X-radiography]] |  |  |
| [[wiki/papers/Fangjie_2023_hypergravity_review\|hypergravity review]] |  |  |
| [[wiki/papers/Geng_2023_acoustic_levitation_solidification\|acoustic levitation solidification]] |  |  |
| [[wiki/papers/Geng__g-jitter_on_Al-20Cu\|g-jitter on Al-20Cu]] |  |  |
| [[wiki/papers/Mohr__thermophysical_g_review\|thermophysical µg review]] |  |  |
| [[wiki/papers/Ludwig__peritectic_couple_growth_g\|peritectic couple growth µg]] |  |  |
| [[wiki/papers/Lhu__Fe-19Si_on_CSS\|Fe-19Si on CSS]] |  |  |
| [[wiki/papers/Robin_2023_sharpprogressive_CET_model\|sharp/progressive CET model]] |  |  |
| [[wiki/papers/Andrew_2023_Al-Ni_ISS-EML_kinetics\|Al-Ni ISS-EML kinetics]] |  |  |
| [[wiki/papers/Becker_2023_Al-Cu__Al-Ge_equiaxed_g\|Al-Cu / Al-Ge equiaxed µg]] |  |  |
| [[wiki/papers/Roosz__Al-7Si_eutectic__2_in_g\|Al-7Si eutectic & λ2 in µg]] |  |  |
| [[wiki/papers/Mohr__Ti-6Al-4V_ISS-EML\|Ti-6Al-4V ISS-EML]] |  |  |
| [[wiki/papers/Huang_2024_Ti-46Al-8Nb_CA-FVM_centrifugal\|Ti-46Al-8Nb CA-FVM centrifugal]] |  |  |
| [[wiki/papers/Haipeng__Zr50V50_hypereutectic_in_space\|Zr50V50 hypereutectic in space]] |  |  |
| [[wiki/papers/Viardin_2023_CVDL_on_phase-field_dendrites\|CV/DL on phase-field dendrites]] |  |  |
| [[wiki/papers/Blake_2024_ISRU_ductile_iron\|ISRU ductile iron]] |  |  |
| [[wiki/papers/Zimmermann__grain-refined_Al-Cu_ISS\|grain-refined Al-Cu ISS]] |  |  |
| [[wiki/papers/Akamatsu__SCN_transparent_g\|SCN transparent µg]] |  |  |
| [[wiki/papers/Mitra_2024_laser_AM_in_space_review\|laser AM in space review]] |  |  |
| [[wiki/papers/Murphy__MASER-13_front-tracking_Al-20Cu\|MASER-13 front-tracking Al-20Cu]] |  |  |
| [[wiki/papers/Apurba__Al-Cu_nanostructure_MD\|Al-Cu nanostructure MD]] |  |  |
| [[wiki/papers/Reinhart__in-situ_X-ray_review\|in-situ X-ray review]] |  |  |
<!-- STATIC_TABLE_END -->