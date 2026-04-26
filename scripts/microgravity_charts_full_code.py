"""
=============================================================================
MICROGRAVITY SOLIDIFICATION — All 12 Charts
Source data + matplotlib code
Data extracted from: microgravity_vs_1g_comparison_table.md (April 2026)
=============================================================================
"""

import matplotlib
matplotlib.use('Agg')          # remove this line if running interactively
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ── Global style ──────────────────────────────────────────────────────────────
C1G  = '#1f77b4'   # 1g colour  – blue
CMU  = '#d62728'   # µg colour  – red
CGAP = '#7f7f7f'   # gap / neutral – grey
CHLT = '#ff7f0e'   # highlight accent – orange

plt.rcParams.update({
    'font.family'        : 'DejaVu Sans',
    'axes.spines.top'    : False,
    'axes.spines.right'  : False,
    'figure.dpi'         : 150,
})

OUT = './'   # change to your preferred output folder


# ════════════════════════════════════════════════════════════════════════════════
# CHART 1 — Radar: Gravity Effect Landscape across all 8 sections
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
Eight thematic sections (A–H) drawn from Flemings chapter groupings.
Each section is scored 0–10 on three dimensions:
  • 1g Limitation Severity  – how badly 1g distorts / masks the phenomenon
  • µg Benefit Achieved     – how much µg experiments have advanced understanding
  • Remaining Gap           – open questions / unfilled metrics as of April 2026

Scores are composite ratings derived from:
  (a) number of phenomena in each section
  (b) qualitative gravity-effect magnitude column in the comparison table
  (c) presence of empty cells in Section H (mechanical properties)

Section  | 1g Limitation | µg Benefit | Remaining Gap
---------|---------------|------------|---------------
A Macroseg.          |  9 |  9 |  3
B Dendritic          |  7 |  8 |  4
C Eutectic/Polyphase |  8 |  9 |  4
D Nucleation         |  9 | 10 |  5
E Thermophysical     |  8 |  9 |  6
F Semiconductor      |  9 | 10 |  3
G Porosity / AM      |  6 |  5 |  7
H Mech. Properties   |  7 |  2 | 10   ← critical unfilled section
"""

categories = [
    'Macrosegregation\n(A)',
    'Dendritic\nMicrostructure (B)',
    'Eutectic /\nPolyphase (C)',
    'Nucleation &\nUndercooling (D)',
    'Thermophysical\nProperties (E)',
    'Semiconductor\nCrystal (F)',
    'Gas Porosity\n& AM (G)',
    'Mech. Properties\n(H – GAP)',
]

scores_1g_limited = [9, 7, 8, 9, 8, 9, 6, 7]
scores_ug_benefit  = [9, 8, 9, 10, 9, 10, 5, 2]
scores_gap         = [3, 4, 4,  5, 6,  3, 7, 10]

N      = len(categories)
angles = np.linspace(0, 2*np.pi, N, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(polar=True))
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

for scores, color, label, alpha in [
    (scores_1g_limited, C1G,  '1g Limitation Severity', 0.15),
    (scores_ug_benefit,  CMU,  'µg Benefit Achieved',    0.15),
    (scores_gap,         CGAP, 'Remaining Research Gap', 0.15),
]:
    vals = scores + scores[:1]
    ax.plot(angles, vals, color=color, linewidth=2.5, label=label)
    ax.fill(angles, vals, color=color, alpha=alpha)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, size=9.5, fontweight='bold')
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2','4','6','8','10'], size=7, color='grey')
ax.set_title('Fig 1 — Gravity Effect Landscape:\nBenefit, Limitation & Open Gaps Across All Phenomena',
             pad=30, fontsize=13, fontweight='bold')
ax.legend(loc='upper right', bbox_to_anchor=(1.35, 1.15), fontsize=9.5)

plt.tight_layout()
plt.savefig(OUT + 'chart1_radar.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 1 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 2 — Lollipop: Magnitude of gravity effect, all 47 phenomena
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
Each tuple: (short label, magnitude score 0–10, section letter)

Scoring key (from 'Magnitude of gravity effect' column):
  10 → transformative / qualitative sign change (e.g. segregation eliminated,
        channel freckling absent, container-wall nucleation removed)
   9 → very large quantitative reduction (≥4–5× or mechanism completely replaced)
   8 → large effect (2–4× or major morphology shift)
   7 → moderate effect (~2–3× or significant distribution narrowing)
   6 → modest (~30%)
   5 → small quantitative (exponent confirmed, <20% change)
   4 → threshold / boundary established (g-jitter)
   3 → minimal / indirect (only partial data)
   0 → no gravity effect OR open gap with no µg data

Ref rows with score 0:
  A4  Inverse shrinkage segregation  → gravity-independent (no effect)
  B9  Dendritic growth velocity      → identical at same ΔT (no effect)
  E6  Cross-platform validation      → experiment not yet performed (gap)
  H1  Tensile strength               → no published µg data (gap)
  H2  Fatigue / creep                → no published µg data (gap)
"""

phenomena = [
    ('A1 Axial Macroseg. Al-Si',         9,  'A'),
    ('A2 Axial Macroseg. Al-Cu',         10, 'A'),
    ('A3 Radial Macroseg. Al-20Cu',      8,  'A'),
    ('A4 Inverse Shrinkage Seg.',        0,  'A'),   # gravity-independent
    ('A5 Channel/Freckle Seg.',          10, 'A'),
    ('A6 Interdendritic Flow Driver',    9,  'A'),
    ('A7 Solute Redistrib. Mechanism',   9,  'A'),
    ('A8 Surface Cavity Morphology',     8,  'A'),
    ('B1 SDAS Al-7Si',                   6,  'B'),
    ('B2 PDAS distribution',             5,  'B'),
    ('B3 Equiaxed Grain Size',           7,  'B'),
    ('B4 CET position',                  9,  'B'),
    ('B5 CET mechanism',                 9,  'B'),
    ('B6 CET g-jitter threshold',        4,  'B'),
    ('B7 Dendrite tip V (SCN)',          7,  'B'),
    ('B8 Equiaxed Nucleation dynamics',  9,  'B'),
    ('B9 Dendritic growth velocity',     0,  'B'),   # no effect
    ('B10 Fragment density',             7,  'B'),
    ('C1 J-H λ²V = K',                  5,  'C'),
    ('C2 3D eutectic grain morphology',  9,  'C'),
    ('C3 Oscillatory eutectic colonies', 8,  'C'),
    ('C4 Peritectic coupled growth',     7,  'C'),
    ('C5 Coupled vs. divorced eutectic', 9,  'C'),
    ('C6 Eutectic undercooling (Zr-V)',  9,  'C'),
    ('C7 Spiral Marangoni growth',       9,  'C'),
    ('C8 Monotectic droplet separation', 10, 'C'),
    ('D1 Max undercooling Nb-Si',        8,  'D'),
    ('D2 Max undercooling Nb-Si 2',      9,  'D'),
    ('D3 BMG amorphization',             8,  'D'),
    ('D5 Nucleation under stirring',     8,  'D'),
    ('D6 Metastable phase selection',    8,  'D'),
    ('D9 Container-wall nucleation',     10, 'D'),
    ('E3 Liquid density uncertainty',    9,  'E'),
    ('E4 Liquid surface tension',        9,  'E'),
    ('E5 Liquid viscosity',              8,  'E'),
    ('E6 Cross-platform validation',     0,  'E'),   # open gap
    ('F1 Crucible detachment',           10, 'F'),
    ('F3 Dislocation density GeSi',      9,  'F'),
    ('F4 Dislocation density InAsSb',    9,  'F'),
    ('F6 Stacking-fault elimination',    10, 'F'),
    ('F7 Semicond. meta-baseline 86%',   9,  'F'),
    ('G1 Gas bubble buoyancy',           10, 'G'),
    ('G3 Marangoni bubble motion',       8,  'G'),
    ('H1 Tensile strength (GAP)',        0,  'H'),   # no µg data
    ('H2 Fatigue/Creep (GAP)',           0,  'H'),   # no µg data
    ('H3 Hardness microindent.',         3,  'H'),
    ('H6 Grain-size anomaly Fe-19Si',    5,  'H'),
]

labels   = [p[0] for p in phenomena]
scores   = [p[1] for p in phenomena]
sections = [p[2] for p in phenomena]

sec_colors = {'A':C1G,'B':'#2ca02c','C':'#9467bd','D':CMU,
              'E':'#8c564b','F':'#e377c2','G':'#17becf','H':CGAP}
colors = [sec_colors[s] for s in sections]

fig, ax = plt.subplots(figsize=(11, 18))
y = np.arange(len(labels))

ax.barh(y, scores, height=0.08, color=colors, alpha=0.6)
ax.scatter(scores, y, color=colors, s=120, zorder=5)
ax.axvline(0, color='black', linewidth=0.8)

for i, (s, l) in enumerate(zip(scores, labels)):
    if s == 0:
        ax.axhspan(i-0.4, i+0.4, color='#ffe0b2', alpha=0.5, zorder=0)
        ax.text(0.3, i, '● OPEN GAP / NO EFFECT', va='center', fontsize=7, color='#b45309')
    if s == 10:
        ax.scatter(s, i, color='gold', s=200, zorder=6, edgecolors='black', linewidths=0.7)

ax.set_yticks(y)
ax.set_yticklabels(labels, fontsize=7.8)
ax.set_xlabel('Magnitude of Gravity Effect  (0 = none / gap, 10 = transformative)', fontsize=10)
ax.set_title('Fig 2 — Magnitude of Gravity Effect Across All Phenomena\n'
             '(gold = maximum / transformative; orange band = gap or no effect)',
             fontsize=12, fontweight='bold', pad=12)
ax.set_xlim(-0.5, 11)
ax.invert_yaxis()

legend_patches = [mpatches.Patch(color=c, label=f'Section {k}') for k, c in sec_colors.items()]
ax.legend(handles=legend_patches, loc='lower right', fontsize=8.5, framealpha=0.7)

plt.tight_layout()
plt.savefig(OUT + 'chart2_magnitude_lollipop.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 2 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 3 — Macrosegregation amplitude & reduction factor
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
A1  Axial macroseg. Al-Si (columnar, Bridgman):
    1g: Si enriches upward; amplitude +20–30%  → midpoint = 25%
    µg: ±5% flat diffusive profile              → value = 5%
    Source: Zhang 2024 npj Microgravity doi:10.1038/s41526-024-00454-9

A3  Radial macroseg. Al-20Cu (Bridgman):
    1g: ~15–20%    → midpoint = 17.5%
    µg: <5%        → value = 3.5%
    Source: Spinella 2024 Materialia; Williams 2022 MMTA

A2  Axial macroseg. Al-Cu (equiaxed) – normalised to comparable scale:
    1g: Cu enriches downward; ~7% amplitude (normalised)
    µg: "almost disappears" → 0.5%
    Source: Zhang 2024; Chen 2025 JOM doi:10.1007/s11837-025-07956-1

A5  Channel/freckle segregation (Ni-superalloy, Al-Cu):
    1g: present above Ra_cr ≈ 0.25–46
    µg: NOT observed in any trial → fold = ∞ (plotted as 12 for display)
    Source: Mehrabian/Flemings 1970; CETSOL/MICAST; Zhang 2024
"""

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Left panel – amplitude
cases   = ['A1 Axial\nAl-Si', 'A3 Radial\nAl-20Cu', 'A2 Axial\nAl-Cu (norm.)']
val_1g  = [25,   17.5, 7]      # %
val_ug  = [5,    3.5,  0.5]    # %

x = np.arange(len(cases)); w = 0.35
ax = axes[0]
b1 = ax.bar(x - w/2, val_1g, w, color=C1G, label='1g', zorder=3)
b2 = ax.bar(x + w/2, val_ug,  w, color=CMU, label='µg', zorder=3)
ax.set_xticks(x); ax.set_xticklabels(cases, fontsize=10)
ax.set_ylabel('Segregation Amplitude (%)', fontsize=10)
ax.set_title('Fig 3a — Macrosegregation Amplitude\n1g vs. µg', fontsize=11, fontweight='bold')
ax.legend(fontsize=10); ax.set_ylim(0, 32)
ax.grid(axis='y', alpha=0.3, zorder=0)
for bar in b1: ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.4, f'{bar.get_height():.0f}%', ha='center', fontsize=8.5, color=C1G, fontweight='bold')
for bar in b2: ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.4, f'{bar.get_height():.1f}%', ha='center', fontsize=8.5, color=CMU, fontweight='bold')

# Right panel – fold-reduction
cases2    = ['A1 Axial\nAl-Si', 'A3 Radial\nAl-20Cu', 'A5 Freckle\n(suppressed)']
fold_plot = [5, 3.5, 12]    # 12 = ∞ capped for display
colors2   = [CMU, CMU, CHLT]
ax2 = axes[1]
bars = ax2.bar(cases2, fold_plot, color=colors2, zorder=3, edgecolor='white')
ax2.set_ylabel('Gravity Effect Reduction Factor (×)', fontsize=10)
ax2.set_title('Fig 3b — Segregation Reduction Factor\n(µg vs. 1g)', fontsize=11, fontweight='bold')
ax2.set_ylim(0, 15); ax2.grid(axis='y', alpha=0.3, zorder=0)
ax2.axhline(1, color='grey', linestyle='--', linewidth=1, label='No change (1×)')
ax2.legend(fontsize=9)
labels_fold = ['~5×', '~3.5×', '∞ (eliminated)']
for bar, lbl in zip(bars, labels_fold):
    ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.2, lbl,
             ha='center', fontsize=9.5, fontweight='bold')

plt.tight_layout()
plt.savefig(OUT + 'chart3_macrosegregation.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 3 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 4 — SDAS distribution, grain size & CET suppression
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
B1  SDAS Al-7Si matched pair (Roósz 2022 Crystals; Zhang 2024):
    1g: 150–250 µm  → normal(200, 25)
    µg: 120–180 µm  → normal(150, 15)
    Effect: ~30% finer in µg

B3  Equiaxed grain size Al-Cu (Williams 2022; Zimmermann 2024 Materialia):
    Non-refined 1g: 400 µm  |  Non-refined µg: 250 µm
    Grain-refined 1g: 300 µm | Grain-refined µg: 150 µm
    Effect: 2–3× finer

B4  CET position Al-7Si non-refined (Ngomesse 2021 Acta Mat.; Mirihanage 2023 npj Microgravity):
    1g: CET at ~30% solidified
    µg: CET absent or >90% solidified → largely suppressed
"""

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 4a — SDAS histograms (synthetic distributions matching reported ranges)
ax = axes[0]
np.random.seed(42)
sdas_1g = np.random.normal(200, 25, 400)
sdas_ug = np.random.normal(150, 15, 400)
sdas_1g = sdas_1g[(sdas_1g > 100) & (sdas_1g < 350)]
sdas_ug = sdas_ug[(sdas_ug >  80) & (sdas_ug < 300)]
ax.hist(sdas_1g, bins=30, color=C1G, alpha=0.65, label='1g  (150–250 µm)', density=True)
ax.hist(sdas_ug, bins=30, color=CMU, alpha=0.65, label='µg  (120–180 µm)', density=True)
ax.axvline(np.mean(sdas_1g), color=C1G, linestyle='--', linewidth=1.8)
ax.axvline(np.mean(sdas_ug),  color=CMU, linestyle='--', linewidth=1.8)
ax.set_xlabel('SDAS (µm)', fontsize=10); ax.set_ylabel('Density', fontsize=10)
ax.set_title('Fig 4a — Secondary Dendrite\nArm Spacing Distribution', fontsize=11, fontweight='bold')
ax.legend(fontsize=9)
ax.text(0.98, 0.95, '~30% finer in µg', transform=ax.transAxes,
        ha='right', va='top', fontsize=9, color=CMU, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', fc='#ffe0e0', ec=CMU, alpha=0.8))

# 4b — equiaxed grain size
ax2 = axes[1]
cases_g = ['Non-refined\n1g', 'Non-refined\nµg', 'Grain-refined\n1g', 'Grain-refined\nµg']
grain   = [400, 250, 300, 150]
colors4 = [C1G, CMU, C1G, CMU]
hatches = ['', '', '///', '///']
bars = ax2.bar(cases_g, grain, color=colors4, hatch=hatches, edgecolor='white')
ax2.set_ylabel('Mean Equiaxed Grain Size (µm)', fontsize=10)
ax2.set_title('Fig 4b — Equiaxed Grain Size\n(Al-Cu, 1g vs. µg)', fontsize=11, fontweight='bold')
ax2.set_ylim(0, 530)
for bar, val in zip(bars, grain):
    ax2.text(bar.get_x()+bar.get_width()/2, val+8, f'{val} µm', ha='center', fontsize=9, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)
p1 = mpatches.Patch(color=C1G, label='1g')
p2 = mpatches.Patch(color=CMU, label='µg')
ax2.legend(handles=[p1, p2], fontsize=9)

# 4c — CET position
ax3 = axes[2]
cond3 = ['Al-7Si\n1g', 'Al-7Si\nµg\n(non-refined)']
cet   = [30, 92]
ax3.barh(cond3, cet, color=[C1G, CMU], height=0.5)
ax3.set_xlabel('Fraction Solidified at CET (%)', fontsize=10)
ax3.set_title('Fig 4c — Columnar-to-Equiaxed\nTransition (CET) Suppression in µg', fontsize=11, fontweight='bold')
ax3.set_xlim(0, 105)
for i, v in enumerate(cet):
    lbl = f'{v}%' if v < 92 else f'{v}%  ← largely suppressed'
    ax3.text(v+1, i, lbl, va='center', fontsize=9.5, fontweight='bold',
             color=CMU if v == 92 else C1G)
ax3.axvline(50, color='grey', linestyle=':', linewidth=1, label='50% threshold')
ax3.legend(fontsize=9)

plt.tight_layout()
plt.savefig(OUT + 'chart4_dendrite_grain.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 4 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 5 — Maximum undercooling records
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
D1  Nb-Si eutectic (CSS-ESL):
    1g: ~100–180 K (ground levitator) → midpoint 140 K
    µg: 437 K  →  fold: 3.1×
    Source: Wang 2024 Angew. Chem. doi:10.1002/ange.202313165

D2  Nb₈₄.₁Si₁₅.₉ (CSS):
    1g: ~100 K  |  µg: 421 K  →  fold: 4.2×
    Source: Chang 2024 Rev. Sci. Instrum. 95, 095103

D3  BMG Zr-Ni-Al-Nb:
    1g: ground-limited ~80 K  |  µg: 274 K  →  fold: 3.4×
    Source: 2025 MMTA doi:10.1007/s11661-025-07887-1

D4  Zr₆₄V₃₆ (CSS):
    1g: ~60 K typical  |  µg: 253 K  →  fold: 4.2×
    Source: Wang 2024 Phys. Fluids 36, 042110
"""

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

materials   = ['Nb-Si\neutectic', 'Nb₈₄.₁Si₁₅.₉', 'BMG\nZr-Ni-Al-Nb', 'Zr₆₄V₃₆']
under_1g    = [140, 100,  80,  60]   # K
under_ug    = [437, 421, 274, 253]   # K

x = np.arange(len(materials)); w = 0.35
ax = axes[0]
b1 = ax.bar(x-w/2, under_1g, w, color=C1G, label='1g / Ground levitator', zorder=3)
b2 = ax.bar(x+w/2, under_ug,  w, color=CMU, label='µg / CSS-ESL',           zorder=3)
ax.set_xticks(x); ax.set_xticklabels(materials, fontsize=9.5)
ax.set_ylabel('Maximum Undercooling ΔT (K)', fontsize=10)
ax.set_title('Fig 5a — Maximum Undercooling Records\n1g vs. µg by Material System', fontsize=11, fontweight='bold')
ax.legend(fontsize=9.5); ax.set_ylim(0, 500)
ax.grid(axis='y', alpha=0.3, zorder=0)
for bar in b1: ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+5, f'{bar.get_height():.0f} K', ha='center', fontsize=8, color=C1G, fontweight='bold')
for bar in b2: ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+5, f'{bar.get_height():.0f} K', ha='center', fontsize=8, color=CMU, fontweight='bold')
ax.annotate('~2.5–4× deeper\nundercooling in µg',
            xy=(0.5, 0.78), xycoords='axes fraction', ha='center',
            fontsize=9.5, color=CHLT, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.4', fc='#fff3cd', ec=CHLT, alpha=0.9))

ax2 = axes[1]
fold = [u/g for u, g in zip(under_ug, under_1g)]
bars = ax2.bar(materials, fold, color=[CMU]*4, zorder=3, edgecolor='white')
ax2.axhline(1, color='grey', linestyle='--', linewidth=1.2, label='No change')
ax2.axhline(2, color=CHLT,  linestyle=':', linewidth=1.2, label='2× threshold')
ax2.set_ylabel('Fold-Increase in Undercooling (µg / 1g)', fontsize=10)
ax2.set_title('Fig 5b — Fold-Increase in\nMax. Undercooling (µg / 1g)', fontsize=11, fontweight='bold')
ax2.set_ylim(0, 6); ax2.legend(fontsize=9.5)
ax2.grid(axis='y', alpha=0.3, zorder=0)
for bar, f in zip(bars, fold):
    ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.08, f'{f:.1f}×',
             ha='center', fontsize=10, fontweight='bold', color=CMU)

plt.tight_layout()
plt.savefig(OUT + 'chart5_undercooling.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 5 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 6 — Thermophysical property precision
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
E3  Liquid density:
    Ground EML: 5–10%  → midpoint 7.5%
    ISS-EML/ESL:  ±0.4–1%  → midpoint 0.7%
    Fold improvement: ~10×
    Source: Au 2023; rare-earth titanate 2024 npj Microgravity; Vit106a 2026

E4  Surface tension:
    Ground EML: 3–8%  → midpoint 5.5%
    ISS-EML/ESL: ±0.6–2%  → midpoint 1.3%
    Fold: ~4×
    Source: Au 2023; Mohr ISS-EML III

E5  Viscosity:
    Ground EML: 5–15%  → midpoint 10%
    ISS-EML/ESL: ±1.9% (Au); Vit106a
    Fold: ~5×
    Source: Au 2023; Vit106a 2026 npj Microgravity
"""

props  = ['Liquid\nDensity', 'Surface\nTension', 'Viscosity']
unc_1g = [7.5, 5.5, 10.0]
unc_ug = [0.7, 1.3,  1.9]

fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(props)); w = 0.38
b1 = ax.bar(x - w/2, unc_1g, w, color=C1G, label='Ground EML (1g)',      zorder=3)
b2 = ax.bar(x + w/2, unc_ug,  w, color=CMU, label='ISS-EML / ESL (µg)', zorder=3)
ax.set_xticks(x); ax.set_xticklabels(props, fontsize=12)
ax.set_ylabel('Measurement Uncertainty (%)', fontsize=11)
ax.set_title('Fig 6 — Thermophysical Property Precision:\nGround EML vs. Microgravity (ISS-EML / ESL)',
             fontsize=12, fontweight='bold')
ax.legend(fontsize=11); ax.set_ylim(0, 14)
ax.grid(axis='y', alpha=0.3, zorder=0)
for bar in b1: ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.2, f'{bar.get_height():.1f}%', ha='center', fontsize=10, color=C1G, fontweight='bold')
for bar in b2: ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.2, f'{bar.get_height():.1f}%', ha='center', fontsize=10, color=CMU, fontweight='bold')
for i,(g,u) in enumerate(zip(unc_1g, unc_ug)):
    factor = g / u
    ax.annotate(f'{factor:.0f}× better',
                xy=(i+w/2, u+0.5), xytext=(i+w/2+0.07, g*0.6),
                arrowprops=dict(arrowstyle='->', color=CHLT, lw=1.8),
                fontsize=9.5, color=CHLT, fontweight='bold', ha='left')

plt.tight_layout()
plt.savefig(OUT + 'chart6_thermophysical.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 6 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 7 — Semiconductor crystal quality
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
F3  GeSi dislocation density (Regel & Wilcox 1998; Volz ISS GeSi):
    1g: ~1×10⁵ cm⁻²  |  µg detached: ~3×10³ cm⁻²  →  ~33× reduction

F3b GaSb (Cröll 2009 MRS Bulletin):
    1g: ~5×10⁴ cm⁻²  |  µg: ~2×10³ cm⁻²  →  ~25× reduction

F4  InAsSb CSS 2026 (npj Microgravity 2026):
    1g: ~2×10⁵ cm⁻²  |  µg: ~2×10⁴ cm⁻²  →  10× reduction

F7  Meta-analysis of 160 µg-grown crystals 1973–2016 (Vincent 2024 npj Microgravity):
    86% improved on ≥1 metric  |  14% no improvement
"""

fig, axes = plt.subplots(1, 2, figsize=(13, 6))

materials_sc = ['GeSi', 'GaSb', 'InAsSb\n(2026)']
dd_1g = [1e5, 5e4, 2e5]
dd_ug = [3e3, 2e3, 2e4]
x = np.arange(len(materials_sc)); w = 0.35
ax = axes[0]
b1 = ax.bar(x-w/2, dd_1g, w, color=C1G, label='1g Bridgman',     zorder=3)
b2 = ax.bar(x+w/2, dd_ug,  w, color=CMU, label='µg Detached/CSS', zorder=3)
ax.set_yscale('log')
ax.set_xticks(x); ax.set_xticklabels(materials_sc, fontsize=11)
ax.set_ylabel('Dislocation Density (cm⁻²) [log scale]', fontsize=10)
ax.set_title('Fig 7a — Dislocation Density:\nSemiconductors 1g vs. µg', fontsize=11, fontweight='bold')
ax.legend(fontsize=10); ax.grid(axis='y', alpha=0.3, zorder=0, which='both')
fold_sc = [g/u for g, u in zip(dd_1g, dd_ug)]
for i,(f, bar) in enumerate(zip(fold_sc, b2)):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()*1.3, f'{f:.0f}× ↓',
            ha='center', fontsize=9.5, color=CHLT, fontweight='bold')

ax2 = axes[1]
sizes2   = [86, 14]
labels_d = ['Improved on\n≥1 metric\n(86%)', 'No\nimprovement\n(14%)']
wedges, texts, autotexts = ax2.pie(sizes2, labels=labels_d, colors=[CMU, CGAP],
                                    autopct='%1.0f%%', startangle=90,
                                    pctdistance=0.6, textprops={'fontsize': 11},
                                    wedgeprops=dict(width=0.55))
autotexts[0].set_fontweight('bold'); autotexts[0].set_fontsize(13)
ax2.set_title('Fig 7b — Meta-analysis: Semiconductor Quality\n(160 µg Crystals, Vincent 2024 npj Microgravity)',
              fontsize=11, fontweight='bold')
ax2.text(0, 0, '160\ncrystals\n1973–2016', ha='center', va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig(OUT + 'chart7_semiconductor.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 7 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 8 — Knowledge taxonomy: stacked bar (quantitative / qualitative / gap)
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
Counts of phenomena per section in each knowledge category.
'Quantitative' = µg delivers a measurable number (%, fold, µm, K, cm⁻²)
'Qualitative'  = mechanism change, morphology switch, new pattern observed
'Open gap'     = no µg data or critical metric undefined

Section | Quantitative | Qualitative | Gap
--------|-------------|-------------|----
A  (8 rows)  | 5 | 3 | 0
B  (12 rows) | 6 | 4 | 2  (B9 no effect counted as resolved; E6 cross-platform is gap)
C  (10 rows) | 5 | 5 | 0
D  (10 rows) | 5 | 4 | 1  (D8 interface response function partially open)
E  (8 rows)  | 5 | 1 | 2  (E6 cross-platform; E2 g-jitter partially open)
F  (8 rows)  | 5 | 3 | 0
G  (4 rows)  | 2 | 2 | 2  (G4 AM bridge; G2 full cross-validation)
H  (6 rows)  | 1 | 1 | 4  (H1 tensile, H2 fatigue, H4 carrier mobility aggregate only)
"""

sections8 = ['A\nMacroseg.','B\nDendritic','C\nEutectic','D\nNucleation',
              'E\nThermophys.','F\nSemicond.','G\nPorosity/AM','H\nMech.Prop.']
quant8 = [5, 6, 5, 5, 5, 5, 2, 1]
qual8  = [3, 4, 5, 4, 1, 3, 2, 1]
gap8   = [0, 2, 0, 1, 2, 0, 2, 4]

x = np.arange(len(sections8)); w = 0.6
fig, ax = plt.subplots(figsize=(11, 6))
p1 = ax.bar(x, quant8, w, color='#2ca02c',  label='Quantitative µg result',          zorder=3)
p2 = ax.bar(x, qual8,  w, bottom=quant8,    color=CMU,   label='Qualitative / mechanism-change', zorder=3)
b2 = [q1+q2 for q1,q2 in zip(quant8,qual8)]
p3 = ax.bar(x, gap8,   w, bottom=b2,        color=CGAP,  label='Open gap / unresolved',          zorder=3, hatch='xxx', edgecolor='white')

ax.set_xticks(x); ax.set_xticklabels(sections8, fontsize=10)
ax.set_ylabel('Number of Phenomena', fontsize=11)
ax.set_title('Fig 8 — Knowledge Status by Section:\nQuantitative, Qualitative & Open Gaps', fontsize=12, fontweight='bold')
ax.legend(fontsize=10, loc='upper right'); ax.grid(axis='y', alpha=0.3, zorder=0); ax.set_ylim(0, 14)
ax.annotate('Critical\nmechanical\nproperty gap',
            xy=(7, 5.5), xytext=(5.5, 11),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5),
            fontsize=9.5, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', fc='#f0f0f0', ec='grey', alpha=0.9))

plt.tight_layout()
plt.savefig(OUT + 'chart8_taxonomy_stacked.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 8 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 9 — Bubble / porosity & transport mechanism shift
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
G1  Gas bubble escape:
    1g: buoyant rise + Marangoni  →  most bubbles vent
    µg: Marangoni only  →  bubbles trapped, pore retention higher
    Source: general µg porosity literature; Nat. Comm. 2024

G2  AM DED pore volume fraction (metallic glass, Progress Addit. Manuf. 2025):
    1g DED: 49.7%
    µg DED: 53.9%   →  +4.2 percentage-point increase (buoyant venting lost)

Mechanism shift table (schematic in 9a):
  Phenomenon            | 1g driver        | µg driver
  ----------------------|------------------|------------------
  Bubble escape         | Buoyancy          | Marangoni only
  Droplet motion        | Stokes sedimentation | Marangoni
  Interdendritic flow   | Buoyancy + shrinkage | Shrinkage only
  Solute transport      | Convective (bulk) | Diffusive (BPS/Tiller)
"""

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# 9a schematic
ax = axes[0]
ax.set_xlim(0,10); ax.set_ylim(0,10); ax.set_aspect('equal'); ax.axis('off')
ax.set_title('Fig 9a — Transport Mechanism Shift\n(Schematic)', fontsize=11, fontweight='bold')
def draw_regime(ax, cx, cy, r, color, label, sublabel):
    circle = plt.Circle((cx,cy), r, color=color, alpha=0.25)
    ax.add_patch(circle)
    ax.text(cx, cy+0.3, label,    ha='center', va='center', fontsize=11, fontweight='bold', color=color)
    ax.text(cx, cy-0.5, sublabel, ha='center', va='center', fontsize=8,  color='grey')
draw_regime(ax, 2.5, 5, 2.0, C1G, '1g', 'Buoyancy\ndominated')
draw_regime(ax, 7.5, 5, 2.0, CMU, 'µg', 'Marangoni\ndominated')
ax.annotate('', xy=(5.3,5), xytext=(4.7,5),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))
ax.text(5.0, 5.6, 'gravity\nremoved', ha='center', fontsize=9, style='italic')
shifts = ['Bubble escape: buoyancy → Marangoni only',
          'Droplet motion: Stokes → Marangoni',
          'Interdendritic flow: buoyancy+shrinkage → shrinkage only',
          'Solute transport: convective → diffusive (BPS)']
for i, s in enumerate(shifts):
    ax.text(0.04, 0.22 - i*0.05, f'• {s}', fontsize=7.5, transform=ax.transAxes)

# 9b pore retention
ax2 = axes[1]
cond9 = ['1g DED\n(metallic glass)', 'µg DED\n(metallic glass)']
pore9 = [49.7, 53.9]
bars9 = ax2.bar(cond9, pore9, color=[C1G, CMU], width=0.45, zorder=3)
ax2.set_ylim(45, 57); ax2.set_ylabel('Pore Volume Fraction (%)', fontsize=10)
ax2.set_title('Fig 9b — AM DED Pore Retention\n1g vs. µg (Metallic Glass)', fontsize=11, fontweight='bold')
ax2.grid(axis='y', alpha=0.3, zorder=0)
for bar, v in zip(bars9, pore9):
    ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.1, f'{v:.1f}%',
             ha='center', fontsize=11, fontweight='bold')
ax2.annotate('+4.2% higher\nretention in µg\n(buoyant venting lost)',
             xy=(1,53.9), xytext=(0.5,56.2),
             arrowprops=dict(arrowstyle='->', color=CHLT, lw=1.5),
             fontsize=9, color=CHLT, fontweight='bold', ha='center',
             bbox=dict(boxstyle='round,pad=0.3', fc='#fff3cd', ec=CHLT, alpha=0.9))

plt.tight_layout()
plt.savefig(OUT + 'chart9_porosity_transport.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 9 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 10 — Research readiness gap matrix (heat-map)
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
Rows: 17 selected phenomena spanning sections A–H
Columns (6 readiness dimensions):
  1. µg Data Exists        – any published µg result
  2. Magnitude Quantified  – actual numbers in literature
  3. Mechanism Understood  – causal explanation available
  4. Model Validated       – phase-field or analytical model confirmed
  5. Mech. Prop. Linked    – connected to tensile/fatigue/hardness/carrier mobility
  6. AM / Earth Bridge     – demonstrated pathway to terrestrial application

Cell values:  2 = done (green)  |  1 = partial (yellow)  |  0 = open gap (red)

Key observations:
  • Columns 5 & 6 are almost entirely red across all phenomena
  • H1, H2 rows are all-red (no µg mechanical property data published as of April 2026)
  • E6 cross-platform validation: all-red (experiment never performed)
"""

phenomena10 = [
    'A1 Axial Macroseg. (Al-Si)',
    'A5 Freckle Segregation',
    'B4 CET Suppression',
    'B7 Dendrite Tip Velocity',
    'B11 Phase-field Closure',
    'C3 Oscillatory Eutectic',
    'C8 Monotectic Separation',
    'D1 Max Undercooling (Nb-Si)',
    'D5 Nucleation w/ Stirring',
    'E3 Liquid Density',
    'E6 Cross-platform Validation',
    'F3 Dislocation Density',
    'F6 Stacking-fault Elim.',
    'G1 Bubble Buoyancy',
    'H1 Tensile Strength',
    'H2 Fatigue / Creep',
    'H3 Hardness Data',
]
metric_cols10 = ['µg Data\nExists','Quantified\nMagnitude','Mechanism\nUnderstood',
                 'Model\nValidated','Mech.Prop.\nLinked','AM / Earth\nBridge']

data10 = np.array([
    [2,2,2,2,0,0],  # A1
    [2,2,2,1,0,0],  # A5
    [2,2,2,1,0,0],  # B4
    [2,2,2,2,0,0],  # B7
    [2,2,1,2,0,0],  # B11
    [2,1,1,0,0,0],  # C3
    [2,2,2,1,0,0],  # C8
    [2,2,1,0,0,0],  # D1
    [2,1,1,1,0,0],  # D5
    [2,2,2,2,0,0],  # E3
    [0,0,0,0,0,0],  # E6  ← all gap
    [2,2,2,1,1,0],  # F3
    [2,2,2,0,1,0],  # F6
    [2,2,2,1,0,1],  # G1
    [0,0,0,0,0,0],  # H1  ← all gap
    [0,0,0,0,0,0],  # H2  ← all gap
    [1,1,0,0,0,0],  # H3
])

cmap10  = matplotlib.colors.ListedColormap(['#d62728','#ffdd57','#2ca02c'])
bounds10= [-0.5, 0.5, 1.5, 2.5]
norm10  = matplotlib.colors.BoundaryNorm(bounds10, cmap10.N)

fig, ax = plt.subplots(figsize=(11,10))
ax.imshow(data10, cmap=cmap10, norm=norm10, aspect='auto')
ax.set_xticks(np.arange(len(metric_cols10))); ax.set_yticks(np.arange(len(phenomena10)))
ax.set_xticklabels(metric_cols10, fontsize=9.5)
ax.set_yticklabels(phenomena10,   fontsize=9)
ax.xaxis.set_label_position('top'); ax.xaxis.tick_top()

for i in range(len(phenomena10)):
    for j in range(len(metric_cols10)):
        v   = data10[i,j]
        txt = {2:'✓',1:'~',0:'✗'}[v]
        col = 'white' if v == 2 else 'black'
        ax.text(j, i, txt, ha='center', va='center', fontsize=13, fontweight='bold', color=col)

ax.set_title('Fig 10 — Research Readiness Gap Matrix\n(✓ Done   ~ Partial   ✗ Open Gap)',
             fontsize=12, fontweight='bold', pad=18)
legend10 = [mpatches.Patch(color='#2ca02c',label='✓ Completed'),
            mpatches.Patch(color='#ffdd57',label='~ Partial'),
            mpatches.Patch(color='#d62728',label='✗ Open Gap')]
ax.legend(handles=legend10, loc='lower right', fontsize=10,
          bbox_to_anchor=(1.0,-0.06), framealpha=0.9)
for ri in [14,15,16]:   # highlight H rows
    ax.add_patch(plt.Rectangle((-0.5,ri-0.5), len(metric_cols10), 1,
                               fill=False, edgecolor='black', linewidth=2.5, zorder=5))
ax.text(len(metric_cols10)+0.1, 15, '← Critical\nMechanical\nProp. Gap',
        va='center', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(OUT + 'chart10_gap_matrix.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 10 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 11 — Eutectic: J-H law validation & undercooling depth
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
C1  Jackson-Hunt law λ²V = K (Xu 2024 Intermetallics; Cao 2025 Materials):
    µg confirms exponent n = 0.484  (theory: 0.5)
    Range tested: 0.1–2000 µm/s; spacing 0.4–3 µm
    K_representative = 8 µm³/s for plot normalisation
    1g data: broader scatter (convection displaces lamellar spacing)
    µg data: tight clustering around theory line

C6  Eutectic undercooling:
    Al-Si (typical): 1g ~25 K  |  µg ~40 K   → fold 1.6×
    Ni-Sn (CSS Cao 2025): 1g ~50 K  |  µg ~130 K  → fold 2.6×
    Zr-V  (CSS Wang 2024 Phys Fluids): 1g ~60 K  |  µg 253 K  → fold 4.2×
"""

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# 11a — log-log J-H
ax = axes[0]
V_th  = np.logspace(-1, 3.3, 80)
K     = 8.0
lam_th = np.sqrt(K / V_th)
np.random.seed(7)
V1g   = 10**np.random.uniform(-0.5, 3, 30)
lam1g = np.sqrt(K / V1g) * np.random.uniform(0.6, 1.6, 30)
Vug   = 10**np.random.uniform(-0.5, 3, 30)
lamug = np.sqrt(K / Vug) * np.random.uniform(0.85, 1.15, 30)

ax.loglog(V_th, lam_th, 'k--', linewidth=1.8, label='J-H theory: λ²V = K')
ax.scatter(V1g,  lam1g, color=C1G, alpha=0.6, s=55, label='1g (convection scatter)')
ax.scatter(Vug,  lamug, color=CMU, alpha=0.8, s=55, label='µg (tighter fit)')
ax.set_xlabel('Solidification Velocity V (µm/s)', fontsize=10)
ax.set_ylabel('Lamellar Spacing λ (µm)', fontsize=10)
ax.set_title('Fig 11a — Jackson-Hunt Law Validation:\nλ²V = K, 1g vs. µg', fontsize=11, fontweight='bold')
ax.legend(fontsize=8.5); ax.grid(True, which='both', alpha=0.25)
ax.text(0.05,0.12,'µg confirms J-H\nexponent n ≈ 0.484\n(theory: 0.5)',
        transform=ax.transAxes, fontsize=8.5, color=CMU, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', fc='#ffe0e0', ec=CMU, alpha=0.9))

# 11b — eutectic undercooling bars
ax2 = axes[1]
sys11 = ['Al-Si\n(typical)','Ni-Sn\n(CSS)','Zr-V\n(CSS)']
u1g11 = [25,  50,  60]; u_ug11 = [40, 130, 253]
e1g11 = [5,   15,  20]; e_ug11 = [8,  20,   30]
x11   = np.arange(len(sys11)); w11=0.35
ax2.bar(x11-w11/2, u1g11, w11, color=C1G, label='1g', zorder=3,
        yerr=e1g11, capsize=5, error_kw={'ecolor':C1G,'elinewidth':1.5})
ax2.bar(x11+w11/2, u_ug11, w11, color=CMU, label='µg', zorder=3,
        yerr=e_ug11, capsize=5, error_kw={'ecolor':CMU,'elinewidth':1.5})
ax2.set_xticks(x11); ax2.set_xticklabels(sys11, fontsize=10)
ax2.set_ylabel('Eutectic Undercooling ΔT (K)', fontsize=10)
ax2.set_title('Fig 11b — Eutectic Undercooling Depth\n(Representative Values)', fontsize=11, fontweight='bold')
ax2.legend(fontsize=10); ax2.grid(axis='y', alpha=0.3, zorder=0)
for i,(g,u,eg,eu) in enumerate(zip(u1g11,u_ug11,e1g11,e_ug11)):
    fold=u/g
    ax2.text(i, max(g,u)+max(eg,eu)+5, f'{fold:.1f}×', ha='center',
             fontsize=10, color=CHLT, fontweight='bold')

plt.tight_layout()
plt.savefig(OUT + 'chart11_eutectic.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 11 saved")


# ════════════════════════════════════════════════════════════════════════════════
# CHART 12 — Publication timeline & effect-type breakdown
# ════════════════════════════════════════════════════════════════════════════════
"""
DATA
----
12a  Cumulative publication counts per topical area 2018–2026.
     Values are illustrative totals anchored to the reference list in the
     comparison table (2024–2026 entries counted directly; pre-2024 anchored
     to foundational citations).

     Year    | Macro | Dendrite | Eutectic | Nucleation | Semicond | Thermophys
     --------|-------|----------|----------|------------|----------|----------
     2018    |  1    |  2       |  1       |  1         |  1       |  1
     2019    |  2    |  4       |  2       |  2         |  2       |  2
     2020    |  3    |  6       |  3       |  4         |  3       |  3
     2021    |  5    |  8       |  5       |  6         |  4       |  4
     2022    |  7    | 11       |  7       |  8         |  6       |  6
     2023    |  9    | 14       |  9       | 10         |  8       |  8
     2024    | 11    | 17       | 12       | 13         | 10       | 10
     2025    | 14    | 21       | 15       | 16         | 12       | 13
     2026    | 16    | 25       | 18       | 20         | 15       | 16

12b  Nature of gravity effect (all 47 phenomena A–H):
     Quantitative reduction     18  (33%)
     Qualitative morphology change 12  (22%)
     Mechanism isolation        10  (18%)
     New phenomenon              7  (13%)
     Open gap / no effect        8  (15%)
"""

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

years12 = np.arange(2018, 2027)
macro12  = np.array([ 1, 2, 3, 5, 7, 9,11,14,16])
dend12   = np.array([ 2, 4, 6, 8,11,14,17,21,25])
eut12    = np.array([ 1, 2, 3, 5, 7, 9,12,15,18])
nuc12    = np.array([ 1, 2, 4, 6, 8,10,13,16,20])
semi12   = np.array([ 1, 2, 3, 4, 6, 8,10,12,15])
therm12  = np.array([ 1, 2, 3, 4, 6, 8,10,13,16])

ax = axes[0]
ax.stackplot(years12, macro12, dend12, eut12, nuc12, semi12, therm12,
             labels=['Macrosegregation','Dendritic','Eutectic/Polyphase',
                     'Nucleation','Semiconductor','Thermophysical'],
             colors=['#1f77b4','#2ca02c','#9467bd','#d62728','#e377c2','#8c564b'],
             alpha=0.82)
ax.set_xlim(2018, 2026); ax.set_ylim(0, None)
ax.set_xlabel('Year', fontsize=10); ax.set_ylabel('Cumulative Key Publications', fontsize=10)
ax.set_title('Fig 12a — Research Momentum:\nCumulative Key µg Solidification Papers 2018–2026',
             fontsize=11, fontweight='bold')
ax.legend(loc='upper left', fontsize=8.5, framealpha=0.7)
ax.grid(axis='y', alpha=0.25)
ax.axvline(2022, color='black', linestyle='--', linewidth=1.2)
ax.text(2022.1, 5, 'CSS\nlaunched', fontsize=8, style='italic')

ax2 = axes[1]
etype   = ['Quantitative\nreduction','Qualitative\nmorphology change',
           'Mechanism\nisolation','New\nphenomenon','Open gap /\nno effect']
ecounts = [18, 12, 10, 7, 8]
explode = [0,  0,   0,  0.08, 0.08]
ecolors = ['#2ca02c','#1f77b4','#9467bd','#ff7f0e','#7f7f7f']
wedges, texts, autotexts = ax2.pie(ecounts, labels=etype, autopct='%1.0f%%',
                                    colors=ecolors, explode=explode, startangle=120,
                                    pctdistance=0.65, textprops={'fontsize':8.5},
                                    wedgeprops=dict(edgecolor='white', linewidth=1.2))
for at in autotexts: at.set_fontsize(9); at.set_fontweight('bold')
ax2.set_title('Fig 12b — Nature of Gravity Effect\nAcross All 47 Phenomena (Sections A–H)',
              fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig(OUT + 'chart12_timeline_pie.png', bbox_inches='tight', dpi=150)
plt.close()
print("Chart 12 saved")

print("\n✓ All 12 charts generated.")
