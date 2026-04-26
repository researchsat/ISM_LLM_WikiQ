#!/usr/bin/env python3
"""
==============================================================================
  Solidification Literature PDF Digest Generator
  PhD Research Tool — Space Solidification (µg vs 1g) Literature Review
==============================================================================
  Generates three Markdown files per paper in RefPapers/:

    <stem>_digest.md   — Full structured digest (classification, phenomena,
                         Flemings chapter mapping, findings, comparisons)
    <stem>_metrics.md  — Quantitative metrics table (values + context snippets)
    <stem>_summary.md  — Concise 1-page overview + quick-reference table

  Usage:
    python pdf_digest_generator.py                  # process all PDFs
    python pdf_digest_generator.py --paper FILE.pdf # single paper
    python pdf_digest_generator.py --folder PATH    # custom folder
    python pdf_digest_generator.py --output PATH    # custom output dir

  Dependencies:
    pip install pdfplumber --break-system-packages

  Reference skeleton : Solidification_Flemings_Contents.md
  Reference tables   : 1g vs µg Comparison Table, Metrics Table
==============================================================================
"""

import os
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict


# ══════════════════════════════════════════════════════════════════════════════
# STEP 1 ── KEYWORD / VARIABLE MASTER DICTIONARY
# ══════════════════════════════════════════════════════════════════════════════

# ── 1a. ALLOY SYSTEMS ─────────────────────────────────────────────────────────
ALLOY_PATTERNS = [
    r'Al[‐\-–]?\s*(?:Cu|Ni|Si|Ag|Bi|Sn|Zn|Mg|In)',
    r'Fe[‐\-–]?\s*(?:Cu|Ni|Co|Si|Cr)',
    r'Ti[‐\-–]?\s*(?:6Al[‐\-–]?4V|6Al|4V|Al|Ni)',
    r'Nb\s*\d+[\.\d]*\s*Si\s*\d+[\.\d]*',
    r'Zr\s*\d+[\.\d]*\s*(?:Pt|V|Cu|Al)\s*\d+[\.\d]*',
    r'Cu\s*\d+[\.\d]*\s*(?:Zr|Al|Ag|Sn)\s*\d+[\.\d]*',
    r'Co[‐\-–]?\s*(?:Cr|Ni|Fe)',
    r'succinonitrile|SCN\b',
    r'InSb|GaSb|GeSi|InAsSb|InSe|GaAs|InP|InGaAs',
    r'TRIS[‐\-–]?NPG|TRIS\b|NPG\b',
    r'(?:Al|Cu|Fe|Ni|Ti|Zr|Nb)\s*\d+[\.\d]*\s*(?:wt|at|mol)[\.\s]*(?:pct|%)',
    r'\d+[\.\d]*\s*(?:wt|at|mol)[\.\s]*(?:pct|%)\s*(?:Cu|Ni|Si|Al|Ag|Bi|Sn|Zn)',
    r'(?:binary|ternary|multicomponent|eutectic|peritectic|monotectic)\s+alloy',
    r'hypereutectic|hypoeutectic',
    r'Sn[‐\-–]?\s*(?:Bi|Pb|In|Ag)',
    r'Pb[‐\-–]?\s*(?:Sn|Bi)',
]

# ── 1b. EXPERIMENTAL FACILITIES / PROGRAMS ────────────────────────────────────
FACILITY_KEYWORDS = {
    'ISS': [
        'international space station', r'\bISS\b', 'material science laboratory', r'\bMSL\b',
        'low gradient furnace', r'\bLGF\b', 'gradient heating facility', r'\bGHF\b',
    ],
    'DECLIC-DSI': [
        r'\bDECLIC\b', 'declic-dsi', r'\bDSI\b', 'directional solidification insert',
    ],
    'CETSOL': [r'\bCETSOL\b', 'cetsol'],
    'MICAST': [r'\bMICASTb', r'\bMICAST\b', 'micast'],
    'IDGE': [
        r'\bIDGE\b', 'isothermal dendritic growth experiment',
        r'\bUSMP\b', 'united states microgravity payload',
    ],
    'ISS-EML': [
        r'\bEML\b', 'electromagnetic levitation', r'\bISS-EML\b', r'\bELF\b',
        'electro-magnetic levitation',
    ],
    'ESL': [
        r'\bESL\b', 'electrostatic levitation', r'\bCSS-ESL\b',
    ],
    'Bridgman': [
        r'\bBridgman\b', 'bridgman furnace', 'directional solidification furnace',
        'bridgman-stockbarger',
    ],
    'XRMON': [
        r'\bXRMON\b', r'\bMASER\b', 'sounding rocket', r'\bTEXUS\b', r'\bMAXUS\b',
        'x-ray radiograph', 'in situ x-ray',
    ],
    'China Space Station': [
        'china space station', r'\bCSS\b', 'chinese space station', r'\bTZ-2\b',
    ],
    'Skylab': [r'\bSkylab\b', 'skylab'],
    'Drop tube/tower': [
        'drop tube', 'drop tower', r'\bMLCC\b', 'electromagnetic containerless',
        'free fall',
    ],
    'Containerless/Levitation': [
        'containerless processing', 'acoustic levitation', 'aerodynamic levitation',
        'levitated droplet',
    ],
    'Parabolic flight': ['parabolic flight', 'zero-g aircraft', 'reduced gravity aircraft'],
}

# ── 1c. GRAVITY CONDITIONS ────────────────────────────────────────────────────
GRAVITY_KEYWORDS = {
    'microgravity (µg)': [
        r'microgravity', r'micro-gravity', r'\bµg\b', r'\bμg\b', r'\b0g\b',
        r'weightlessness', r'zero[- ]gravity', r'reduced gravity',
        r'space environment', r'aboard.*station', r'in\s+(?:outer\s+)?space',
        r'low[- ]gravity',
    ],
    'terrestrial (1g)': [
        r'terrestrial', r'\b1g\b', r'\b1-g\b', r'ground[- ]based',
        r'on\s+earth', r'earth[- ]based', r'normal gravity',
        r'under\s+gravity', r'gravity[- ]driven',
    ],
    'sounding rocket': [
        r'sounding rocket', r'\bTEXUS\b', r'\bMASER\b', r'\bMAXUS\b', r'\bRexus\b',
    ],
    'parabolic flight': [r'parabolic flight', r'reduced gravity aircraft'],
    'drop tube/tower': [r'drop tube', r'drop tower', r'free fall', r'microgravity.*drop'],
}

# ── 1d. SOLIDIFICATION PHENOMENA ─────────────────────────────────────────────
PHENOMENA_KEYWORDS = {
    # Transport phenomena
    'convection': [
        'convection', 'convective', 'buoyancy-driven', 'thermosolutal convection',
        'Marangoni convection', 'solutal convection', 'natural convection',
        'forced convection', 'melt convection', 'fluid flow',
    ],
    'diffusion': [
        'purely diffusive', 'diffusion-controlled', 'diffusion-limited',
        'solute diffusion', 'thermal diffusion', 'stagnant melt', 'no convection',
    ],
    'macrosegregation': [
        'macrosegregation', 'macro-segregation', 'freckle', 'channel segregation',
        'inverse segregation', 'axial segregation', 'radial segregation',
        'positive segregation', 'negative segregation',
    ],
    'microsegregation': [
        'microsegregation', 'micro-segregation', 'solute redistribution',
        'solute profile', 'Scheil', 'interdendritic segregation',
    ],
    # Morphological phenomena
    'dendritic growth': [
        'dendrite', 'dendritic', 'dendritic growth', 'dendrite tip',
        'dendrite arm', 'columnar dendrite', 'equiaxed dendrite', 'PDAS', 'SDAS',
        'primary arm', 'secondary arm', 'tertiary arm',
    ],
    'cellular solidification': [
        'cellular solidification', 'cell structure', 'cellular-dendritic',
        'cell spacing', 'cellular front', 'cell formation',
    ],
    'eutectic solidification': [
        'eutectic', 'lamellar eutectic', 'rod eutectic', 'eutectic spacing',
        'eutectic growth', 'lamellar-to-rod', 'eutectic colony',
        'oscillatory instabilities', 'Jackson-Hunt',
    ],
    'peritectic solidification': [
        'peritectic', 'peritectic solidification', 'peritectic reaction',
        'peritectic alloy',
    ],
    'monotectic/immiscible': [
        'monotectic', 'immiscible alloy', 'phase separation', 'Stokes sedimentation',
        'core-shell', 'Marangoni migration', 'immiscible',
    ],
    # Phase transitions
    'CET': [
        'CET', 'columnar-to-equiaxed transition', 'columnar to equiaxed',
        'columnar grain', 'equiaxed grain', 'grain structure', 'grain nucleation',
    ],
    'nucleation': [
        'nucleation', 'nucleate', 'heterogeneous nucleation', 'homogeneous nucleation',
        'grain refinement', 'inoculant', 'undercooling', 'supercooling',
        'nucleation rate',
    ],
    'detached Bridgman': [
        'detached solidification', 'detached Bridgman', 'detached growth',
        'dewetting', 'de-wetting', 'gap formation', 'wetting angle',
        'contact angle', 'capillary',
    ],
    'rapid solidification': [
        'rapid solidification', 'undercooled melt', 'metastable phase',
        'amorphous', 'glass forming', 'recalescence', 'containerless undercooling',
    ],
    'thermophysical properties': [
        'thermophysical', 'surface tension', 'viscosity', 'density measurement',
        'specific heat', 'thermal conductivity', 'thermal diffusivity',
        'emissivity', 'electrical resistivity',
    ],
    'interface stability': [
        'interface stability', 'constitutional supercooling', 'Mullins-Sekerka',
        'planar interface', 'morphological stability', 'perturbation analysis',
    ],
    'g-jitter': [
        'g-jitter', 'g-jitter sensitivity', 'residual gravity',
        'residual acceleration', 'vibration', 'periodic instabilit',
    ],
    'mushy zone': [
        'mushy zone', 'mushy region', 'two-phase zone', 'semi-solid',
        'fraction solid', 'fraction liquid', 'solid fraction',
    ],
}

# ── 1e. QUANTITATIVE PARAMETERS WITH REGEX PATTERNS ──────────────────────────
# Each entry: variable_name → (display_description, [regex_list])
QUANTITATIVE_PATTERNS = {
    'undercooling': (
        'Undercooling ΔT (K)',
        [
            r'undercooling[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:K\b|°C)',
            r'(\d+[\.\d]*)\s*K\s+undercooling',
            r'ΔT\s*[=≈~]\s*(\d+[\.\d]*)\s*(?:K|°C)',
            r'supercooling[^\n.]{0,60}?(\d+[\.\d]*)\s*(?:K|°C)',
            r'undercooled\s+by\s+(\d+[\.\d]*)\s*(?:K|°C)',
        ],
    ),
    'PDAS': (
        'Primary Dendrite Arm Spacing λ₁ (µm)',
        [
            r'primary[^\n.]{0,60}?spacing[^\n.]{0,40}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
            r'\bPDAS\b[^\n.]{0,40}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
            r'λ[₁1][^\n.]{0,40}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
            r'primary arm spacing[^\n.]{0,30}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
        ],
    ),
    'SDAS': (
        'Secondary Dendrite Arm Spacing λ₂ (µm)',
        [
            r'secondary[^\n.]{0,60}?spacing[^\n.]{0,40}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
            r'\bSDAS\b[^\n.]{0,40}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
            r'λ[₂2][^\n.]{0,40}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
        ],
    ),
    'eutectic_spacing': (
        'Eutectic Spacing λₑ (µm)',
        [
            r'eutectic[^\n.]{0,60}?spacing[^\n.]{0,40}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
            r'lamellar[^\n.]{0,60}?spacing[^\n.]{0,40}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
            r'rod[^\n.]{0,30}?spacing[^\n.]{0,30}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
        ],
    ),
    'dendrite_tip_velocity': (
        'Dendrite Tip Velocity V (µm/s)',
        [
            r'tip\s+velocit[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:µm/s|mm/s|cm/s|μm/s)',
            r'growth\s+velocit[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:µm/s|mm/s|cm/s|μm/s)',
            r'solidification\s+velocit[^\n.]{0,60}?(\d+[\.\d]*)\s*(?:µm/s|mm/s)',
            r'\bV\s*=\s*(\d+[\.\d]*)\s*(?:µm/s|mm/s|μm/s)',
        ],
    ),
    'temperature_gradient': (
        'Temperature Gradient G (K/mm)',
        [
            r'temperature\s+gradient[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:K/mm|K/cm|°C/cm|°C/mm)',
            r'thermal\s+gradient[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:K/mm|K/cm)',
            r'\bG\s*=\s*(\d+[\.\d]*)\s*(?:K/mm|K/cm)',
            r'gradient\s+of\s+(\d+[\.\d]*)\s*(?:K/mm|K/cm)',
        ],
    ),
    'pulling_velocity': (
        'Pulling / Withdrawal Velocity V (µm/s)',
        [
            r'pulling\s+velocit[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:µm/s|mm/s|μm/s)',
            r'withdrawal\s+(?:rate|speed|velocit)[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:µm/s|mm/s)',
            r'solidification\s+rate[^\n.]{0,60}?(\d+[\.\d]*)\s*(?:µm/s|mm/s)',
        ],
    ),
    'cooling_rate': (
        'Cooling Rate (K/s)',
        [
            r'cooling\s+rate[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:K/s|°C/s|K/min)',
            r'(\d+[\.\d]*)\s*(?:K/s|°C/s)\s+cooling',
        ],
    ),
    'surface_tension': (
        'Surface Tension γ (mN/m)',
        [
            r'surface\s+tension[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:mN/m|N/m|J/m²)',
            r'(\d{3,4}[\.\d]*)\s*mN/m',
            r'γ\s*[=≈]\s*(\d+[\.\d]*)\s*(?:mN/m|N/m)',
        ],
    ),
    'viscosity': (
        'Viscosity η (mPa·s)',
        [
            r'viscosit[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:mPa|cP|Pa\.s|mPa·s|mPas)',
            r'(\d+[\.\d]*)\s*mPa[·\.]?s',
        ],
    ),
    'density': (
        'Density ρ (kg/m³ or g/cm³)',
        [
            r'densit[^\n.]{0,80}?(\d{3,5}[\.\d]*)\s*(?:kg/m³|kg/m3)',
            r'densit[^\n.]{0,80}?(\d[\.\d]*)\s*(?:g/cm³|g/cc|g/cm3)',
        ],
    ),
    'specific_heat': (
        'Specific Heat Cₚ (J/g·K)',
        [
            r'specific\s+heat[^\n.]{0,80}?(\d[\.\d]*)\s*(?:J/g|J/kg|kJ/kg)',
            r'\bCp\b[^\n.]{0,40}?(\d[\.\d]*)\s*(?:J/g|J/kg)',
        ],
    ),
    'thermal_conductivity': (
        'Thermal Conductivity k (W/m·K)',
        [
            r'thermal\s+conductivit[^\n.]{0,80}?(\d+[\.\d]*)\s*(?:W/m|W/mK)',
        ],
    ),
    'partition_coefficient': (
        'Partition Coefficient k₀',
        [
            r'partition\s+coefficient[^\n.]{0,60}?(\d[\.\d]*)',
            r'distribution\s+coefficient[^\n.]{0,60}?(\d[\.\d]*)',
            r'\bk[e0]?\s*=\s*(\d[\.\d]{1,5})\b',
            r'equilibrium\s+(?:partition|distribution)[^\n.]{0,50}?(\d[\.\d]*)',
        ],
    ),
    'composition': (
        'Alloy Composition (wt/at %)',
        [
            r'(\d+[\.\d]*)\s*(?:wt|at|mol)[\.\s]*(?:pct|%)\s*(?:Cu|Ni|Si|Al|Ag|Bi|Sn)',
        ],
    ),
    'dislocation_density': (
        'Dislocation Density (cm⁻²)',
        [
            r'dislocation\s+densit[^\n.]{0,80}?(\d+[\.\d]*(?:\s*[×x]\s*10[⁰¹²³⁴⁵⁶⁷⁸⁹]+)?)',
            r'(\d+[\.\d]*(?:\s*[×x]\s*10\^\d+)?)\s*(?:cm|m)[⁻-]2',
        ],
    ),
    'tip_radius': (
        'Dendrite Tip Radius ρ (µm)',
        [
            r'tip\s+radius[^\n.]{0,60}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
            r'radius\s+of\s+curvature[^\n.]{0,60}?(\d+[\.\d]*)\s*(?:µm|μm|mm)',
        ],
    ),
}

# ── 1f. THEORETICAL MODELS / THEORIES ────────────────────────────────────────
MODEL_KEYWORDS = {
    'LGK / BCT theory': [
        r'\bLGK\b', r'\bBCT\b', 'Lipton-Glicksman-Kurz',
        'Boettinger-Coriell-Trivedi',
    ],
    'BPS / Tiller model': [
        r'\bBPS\b', 'Burton-Prim-Slichter', 'Tiller model', 'Tiller equation',
        'no-convection analytical',
    ],
    'KGT theory': [r'\bKGT\b', 'Kurz-Giovanola-Trivedi'],
    'Phase-field simulation': [
        r'phase[- ]field', r'\bPFM\b', r'\bPFCOM\b', 'phase field model',
    ],
    'Scheil / Gulliver': [r'\bScheil\b', 'Gulliver-Scheil', r'\bScheil-Gulliver\b'],
    'Jackson-Hunt (eutectic)': [
        'Jackson-Hunt', r'\bJ-H\b', 'eutectic spacing theory',
    ],
    'Mullins-Sekerka (stability)': [
        'Mullins-Sekerka', r'\bMSI\b', 'morphological stability theory',
    ],
    'Flemings (mushy zone)': [
        r'\bFlemings\b', 'interdendritic flow model', 'mushy zone theory',
    ],
    'Butler equation': ['Butler equation', 'surface tension model'],
    'CAFE / volume-averaged': [
        r'\bCAFE\b', 'cellular automaton finite element', 'volume-averaged model',
    ],
}

# ── 1g. FLEMINGS CHAPTER MAPPING ─────────────────────────────────────────────
FLEMINGS_CHAPTERS = {
    'Ch.1: Heat Flow in Solidification': [
        'heat flow', 'heat transfer', 'heat extraction', 'thermal profile',
        'solidification rate', 'cooling curve', 'heat flux', 'ingot casting',
        'casting process', 'thermal resistance', 'mold', 'chilling',
        'directional solidification furnace', 'temperature distribution',
    ],
    'Ch.2: Plane Front Solidification (Single-phase)': [
        'plane front', 'planar front', 'BPS', 'Burton-Prim-Slichter',
        'constitutional supercooling', 'Czochralski', 'zone melting',
        'solute boundary layer', 'effective distribution coefficient',
        'diffusion-limited growth', 'Tiller', 'stagnant melt', 'facet effect',
        'no convection', 'diffusive transport',
    ],
    'Ch.3: Cellular Solidification': [
        'cellular solidification', 'cellular front', 'cell spacing', 'cell formation',
        'cellular-dendritic transition', 'Mullins-Sekerka', 'interface stability',
        'constitutional supercooling cells', 'solute redistribution cellular',
    ],
    'Ch.4: Plane Front Solidification (Polyphase/Eutectic)': [
        'lamellar eutectic', 'rod eutectic', 'eutectic growth', 'eutectic spacing',
        'Jackson-Hunt', 'faceted eutectic', 'two-phase structure', 'lamellar-to-rod',
        'eutectic colony', 'oscillatory', 'eutectic pattern', 'convection eutectic',
        'peritectic', 'ternary eutectic',
    ],
    'Ch.5: Solidification of Castings and Ingots': [
        'grain structure', 'columnar grain', 'equiaxed grain', 'CET',
        'columnar-to-equiaxed', 'PDAS', 'SDAS', 'dendrite arm spacing',
        'grain refinement', 'solidification of castings', 'undercooled melt',
        'metastable', 'equiaxed solidification',
    ],
    'Ch.6: Polyphase Alloys – Castings and Ingots': [
        'peritectic solidification', 'eutectic solidification in castings',
        'cast iron', 'ternary alloy solidification', 'monotectic',
        'immiscible alloy', 'dissolved gas', 'gas porosity', 'primary inclusion',
        'secondary inclusion', 'Bi', 'In',
    ],
    'Ch.7: Fluid Flow': [
        'fluid flow', 'interdendritic flow', 'macrosegregation', 'buoyancy flow',
        'Marangoni flow', 'natural convection flow', 'freckle', 'channel',
        'mushy zone flow', 'thermosolutal', 'risering', 'fluidity',
        'interdendritic liquid', 'forced convection', 'melt convection',
    ],
    'Ch.8: Thermodynamics of Solidification': [
        'thermodynamics', 'phase diagram', 'partition ratio', 'partition coefficient',
        'capillary', 'Gibbs-Thomson', 'liquidus', 'solidus', 'activity coefficient',
        'curvature effect', 'contact angle', 'wetting', 'Butler equation',
        'surface energy', 'liquid-solid surface',
    ],
    'Ch.9: Nucleation and Interface Kinetics': [
        'nucleation', 'heterogeneous nucleation', 'homogeneous nucleation',
        'grain refinement', 'inoculation', 'growth kinetics', 'interface kinetics',
        'undercooling nucleation', 'LGK', 'KGT', 'BCT', 'dendrite growth theory',
        'two-dimensional nucleation', 'screw dislocation', 'twin plane',
        'continuous growth', 'lateral growth', 'recalescence',
    ],
    'Ch.10: Processing and Properties': [
        'mechanical properties', 'dislocation density', 'homogenization',
        'solution treatment', 'aligned composite', 'tensile strength', 'hardness',
        'microhardness', 'crystal quality', 'crystal perfection', 'working',
        'ferritic', 'pearlitic', 'malleable iron',
    ],
}

# ── 1h. 1g vs µg COMPARISON MARKER PHRASES ───────────────────────────────────
# Use [\s\S]{3,120} (not [^\n.]) so patterns match across PDF line-wrap breaks.
UG_1G_MARKERS = [
    r'(?:terrestrial|on Earth|1g|ground[- ]based)[\s\S]{3,120}?(?:microgravity|in space|\bµg\b|\bμg\b|reduced gravity)',
    r'(?:microgravity|in space|\bµg\b|\bμg\b|reduced gravity|aboard the)[\s\S]{3,120}?(?:terrestrial|on Earth|\b1g\b|ground[- ]based)',
    r'compared?\s+(?:to|with)\s+(?:earth|ground|\b1g\b|terrestrial)[\s\S]{5,150}',
    r'(?:in|under)\s+(?:microgravity|space|\bµg\b)[\s\S]{5,150}?(?:while|whereas|compared|unlike|in contrast)',
    r'(?:between microgravity and[\s\S]{3,100}terrestrial|between[\s\S]{3,60}microgravity[\s\S]{3,60}earth)',
    r'(?:suppressed?|eliminated?|reduced?|enhanced?|increased?)\s[\s\S]{3,80}?(?:gravity|convection|buoyancy|segregation)',
    r'(?:purely diffusive|diffusion[- ]controlled|stagnant melt)[\s\S]{5,100}?(?:compared|unlike|instead of)',
    r'macrosegregation[\s\S]{5,80}?(?:eliminated?|suppressed?|reduced?|absent|virtually)',
    r'(?:gravity|1g|terrestrial)[\s\S]{3,80}?(?:effect|influence|role|impact)[\s\S]{3,80}?solidif',
    r'differences?\s+(?:in|between)[\s\S]{5,100}?(?:microgravity|space|µg)[\s\S]{5,80}?(?:terrestrial|earth|1g)',
]

# ── 1i. KEY FINDING DETECTION PHRASES ────────────────────────────────────────
FINDING_MARKERS = [
    r'(?:we|the|our)\s+(?:find|found|show|observe|demonstrate|report|measure|confirm|establish)',
    r'(?:results|data|experiments?)\s+(?:show|indicate|suggest|reveal|demonstrate|confirm)',
    r'(?:significant|clear|notable|important|striking)\s+(?:difference|improvement|reduction|increase|effect)',
    r'compared\s+to\s+(?:earth|ground|terrestrial|1g)',
    r'in\s+(?:microgravity|space|µg)[,\s]+(?:the|we|dendrite|growth|convection|segregation)',
    r'(?:eliminated?|suppressed?|reduced?|enhanced?)\s+(?:by|in|due\s+to)',
    r'(?:first|novel|new)\s+(?:measurement|observation|evidence|demonstration|report)',
    r'(?:good|excellent|quantitative)\s+agreement\s+with\s+(?:theory|model|simulation|prediction)',
    r'(?:validates?|confirms?)\s+(?:the|our)\s+(?:model|theory|prediction|simulation)',
    r'(?:benchmark|reference)\s+data',
    r'(?:clearly|strongly)\s+(?:suggest|indicate|demonstrate|show)',
]

# ── 1j. AUTHOR AFFILIATION / RESEARCH GROUP INDICATORS ───────────────────────
KNOWN_GROUPS = {
    'Glicksman (IDGE/dendrite theory)': [r'Glicksman', r'IDGE', 'succinonitrile.*tip velocity'],
    'Herlach / Fecht (EML thermophysical)': [r'Herlach', r'Fecht', 'electromagnetic levitation.*property'],
    'Nguyen-Thi / Reinhart (XRMON/CETSOL)': [r'Nguyen-Thi', r'Reinhart', r'IM2NP', r'XRMON'],
    'Akamatsu / Bottin-Rousseau (DECLIC)': [r'Akamatsu', r'Bottin-Rousseau', r'DECLIC.*eutectic'],
    'Zimmermann (MICAST/CETSOL)': [r'Zimmermann', r'ACCESS', r'MICAST.*Al-Cu'],
    'Ratke / Steinbach (immiscibles)': [r'Ratke', r'Steinbach', r'immiscible.*microgravity'],
    'Wang / Luo (China Space Station)': [r'Wang.*Luo|Luo.*Wang', r'Xi.an Jiaotong', r'CSS.*refractory'],
    'Trivedi / Kurz (microstructure theory)': [r'Trivedi', r'Kurz', r'KGT|Kurz-Giovanola'],
    'Beckermann (macrosegregation)': [r'Beckermann', r'CET.*benchmark'],
    'Duffar (detached Bridgman)': [r'Duffar', r'detached.*Bridgman', r'dewetting'],
}


# ══════════════════════════════════════════════════════════════════════════════
# STEP 2 ── TEXT EXTRACTION
# ══════════════════════════════════════════════════════════════════════════════

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract full text from PDF using pdfplumber.
    Returns two versions joined by a separator:
      - raw (for section/abstract extraction)
      - linearised (newlines → spaces, for regex matching across line-breaks)
    We return linearised text as the main body so regex patterns work across
    PDF word-wrap breaks, while preserving paragraph breaks.
    """
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            pages = []
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    # Collapse intra-paragraph line breaks but keep paragraph gaps
                    # (two consecutive newlines become a paragraph marker)
                    t = re.sub(r'(?<!\n)\n(?!\n)', ' ', t)
                    pages.append(t)
            return '\n\n'.join(pages)
    except ImportError:
        return '[ERROR: pdfplumber not installed. Run: pip install pdfplumber --break-system-packages]'
    except Exception as e:
        return f'[ERROR extracting {pdf_path}: {e}]'


def get_abstract(full_text: str) -> str:
    """Extract abstract or first substantive paragraph."""
    m = re.search(
        r'abstract[\s\n:.]{1,5}(.{150,2500}?)(?=\n\s*(?:keywords?|I{1,3}\.?\s+[A-Z]|1\.\s+[A-Z]|introduction|\nKeyword))',
        full_text, re.IGNORECASE | re.DOTALL
    )
    if m:
        return m.group(1).strip()
    # Fallback: first 1000 chars of text after removing title-like lines
    lines = [l.strip() for l in full_text.split('\n') if len(l.strip()) > 60]
    return ' '.join(lines[:8])[:1200]


# ══════════════════════════════════════════════════════════════════════════════
# STEP 3 ── DATA EXTRACTION
# ══════════════════════════════════════════════════════════════════════════════

def extract_metadata(full_text: str, filename: str) -> dict:
    """Extract paper metadata."""
    meta = {'filename': filename}

    # DOI
    doi_m = re.search(r'(?:doi|DOI)[:\s/]+(10\.\d{4,}/[^\s\n,)]+)', full_text, re.IGNORECASE)
    if not doi_m:
        doi_m = re.search(r'(10\.\d{4,}/[^\s\n,)]{6,})', full_text)
    meta['doi'] = doi_m.group(1).rstrip('.,)') if doi_m else 'Not found'

    # Year (prefer publication year, four-digit 19xx or 20xx)
    years = re.findall(r'\b(19[7-9]\d|20[0-2]\d)\b', full_text)
    meta['year'] = years[0] if years else 'Unknown'

    # Journal
    journal_patterns = [
        (r'Acta Materialia', 'Acta Materialia'),
        (r'Metallurgical.*(?:Materials )?Transactions', 'Metallurgical & Materials Transactions'),
        (r'Journal of Crystal Growth', 'Journal of Crystal Growth'),
        (r'npj Microgravity', 'npj Microgravity'),
        (r'Nature Communications', 'Nature Communications'),
        (r'Scripta Materialia', 'Scripta Materialia'),
        (r'International Journal.*Heat', 'Int. J. Heat and Mass Transfer'),
        (r'Journal.*Materials Science', 'Journal of Materials Science'),
        (r'Computational Materials', 'Computational Materials Science'),
        (r'Progress.*Materials Science', 'Progress in Materials Science'),
        (r'Materials Science.*Engineering', 'Materials Science & Engineering'),
        (r'Journal.*Alloys.*Compounds', 'Journal of Alloys and Compounds'),
        (r'ISIJ International', 'ISIJ International'),
        (r'Modelling.*Simulation.*Materials', 'Modelling & Simulation in Materials Science'),
        (r'Physical Review', 'Physical Review'),
        (r'Applied Physics', 'Applied Physics'),
    ]
    meta['journal'] = 'Unknown'
    for pattern, name in journal_patterns:
        if re.search(pattern, full_text, re.IGNORECASE):
            meta['journal'] = name
            break

    # Title: use cleaned filename as primary source (most reliable for journal PDFs)
    # Strip trailing author names like "_Thomas", "_MOTA", etc.
    stem = Path(filename).stem
    # Remove trailing _SURNAME or _AUTHORNAME suffix patterns
    stem_clean = re.sub(r'[_\s]+[A-Z][A-Z]+$', '', stem)  # e.g. _REINHART
    stem_clean = re.sub(r'[_\s]+\d$', '', stem_clean)       # trailing digit
    stem_clean = stem_clean.replace('_', ' ').replace('-', '–').strip()
    meta['title_guess'] = stem_clean[:160] if len(stem_clean) > 15 else filename[:160]

    return meta


def _normalise_alloy(s: str) -> str:
    """Normalise alloy string: collapse whitespace, standardise separators."""
    s = re.sub(r'\s+', ' ', s).strip()
    # e.g. "Al- Cu" → "Al-Cu", "10 wt pct Cu" → "10wt%Cu"
    s = re.sub(r'(?<=\d)\s*wt\s*pct\s*', 'wt% ', s, flags=re.IGNORECASE)
    s = re.sub(r'(?<=\d)\s*at\s*pct\s*', 'at% ', s, flags=re.IGNORECASE)
    return s


def extract_alloy_systems(full_text: str) -> list:
    """Find alloy systems mentioned; normalise and de-duplicate."""
    raw = set()
    for pattern in ALLOY_PATTERNS:
        for m in re.finditer(pattern, full_text, re.IGNORECASE):
            hit = m.group(0).strip()
            if len(hit) >= 3:
                raw.add(_normalise_alloy(hit))

    # Prefer longer / more specific matches: suppress substrings of other matches
    raw_list = sorted(raw, key=len, reverse=True)
    kept = []
    for candidate in raw_list:
        c_lower = candidate.lower()
        if not any(c_lower in k.lower() and c_lower != k.lower() for k in kept):
            kept.append(candidate)
    return sorted(kept[:20])


def extract_facilities(full_text: str) -> list:
    """Find experimental facilities/programs (min 2 hits to suppress ref-list noise)."""
    found = []
    for facility, keywords in FACILITY_KEYWORDS.items():
        count = sum(
            len(re.findall(kw, full_text, re.IGNORECASE))
            for kw in keywords
        )
        if count >= 2:
            found.append(facility)
    return sorted(set(found))


def extract_gravity_context(full_text: str) -> list:
    """Determine gravity conditions discussed (min 2 hits to avoid ref noise)."""
    found = []
    for condition, keywords in GRAVITY_KEYWORDS.items():
        count = sum(
            len(re.findall(kw, full_text, re.IGNORECASE))
            for kw in keywords
        )
        if count >= 2:
            found.append(condition)
    return found


def extract_phenomena(full_text: str) -> list:
    """Find solidification phenomena, ranked by keyword frequency."""
    text_lower = full_text.lower()
    ranked = []
    for phenomenon, keywords in PHENOMENA_KEYWORDS.items():
        count = sum(
            len(re.findall(re.escape(kw.lower()), text_lower))
            for kw in keywords
        )
        if count >= 2:
            ranked.append((phenomenon, count))
    ranked.sort(key=lambda x: -x[1])
    return [p for p, _ in ranked]


def extract_quantitative_metrics(full_text: str) -> dict:
    """Extract quantitative measurements with surrounding context."""
    results = {}
    for var_name, (description, patterns) in QUANTITATIVE_PATTERNS.items():
        hits = []
        for pattern in patterns:
            try:
                for m in re.finditer(pattern, full_text, re.IGNORECASE):
                    start = max(0, m.start() - 60)
                    end   = min(len(full_text), m.end() + 60)
                    ctx   = full_text[start:end].replace('\n', ' ').strip()
                    val   = m.group(1) if m.lastindex and m.lastindex >= 1 else m.group(0)
                    hits.append({'value': val.strip(), 'context': ctx})
            except re.error:
                pass
        if hits:
            # Deduplicate by value
            seen, unique = set(), []
            for h in hits:
                if h['value'] not in seen:
                    seen.add(h['value'])
                    unique.append(h)
            results[var_name] = {'description': description, 'hits': unique[:4]}
    return results


def extract_models(full_text: str) -> list:
    """Find theoretical models/theories referenced."""
    found = []
    for model, keywords in MODEL_KEYWORDS.items():
        for kw in keywords:
            if re.search(kw, full_text, re.IGNORECASE):
                found.append(model)
                break
    return found


def map_flemings_chapters(full_text: str) -> list:
    """Map paper to Flemings chapters, ranked by keyword density."""
    text_lower = full_text.lower()
    scores = {}
    for chapter, keywords in FLEMINGS_CHAPTERS.items():
        score = sum(
            len(re.findall(re.escape(kw.lower()), text_lower))
            for kw in keywords
        )
        if score > 0:
            scores[chapter] = score
    return sorted(scores.items(), key=lambda x: -x[1])


def extract_key_findings(full_text: str, n: int = 8) -> list:
    """Extract sentences containing key finding markers."""
    sentences = re.split(r'(?<=[.!?])\s+', full_text)
    findings = []
    for sentence in sentences:
        sentence = sentence.strip()
        if not (40 < len(sentence) < 450):
            continue
        for marker in FINDING_MARKERS:
            if re.search(marker, sentence, re.IGNORECASE):
                findings.append(sentence)
                break
    return findings[:n]


def extract_1g_vs_ug_comparisons(full_text: str) -> list:
    """Extract sentences making explicit 1g vs µg comparisons."""
    comparisons = []
    for pattern in UG_1G_MARKERS:
        try:
            for m in re.finditer(pattern, full_text, re.IGNORECASE | re.DOTALL):
                text = m.group(0).replace('\n', ' ').strip()
                if 40 < len(text) < 400:
                    comparisons.append(text)
        except re.error:
            pass
    # Deduplicate by 60-char prefix
    seen, unique = set(), []
    for c in comparisons:
        key = c[:60].lower()
        if key not in seen:
            seen.add(key)
            unique.append(c)
    return unique[:10]


def identify_research_groups(full_text: str) -> list:
    """Identify known research groups from the paper."""
    found = []
    for group, patterns in KNOWN_GROUPS.items():
        for p in patterns:
            if re.search(p, full_text, re.IGNORECASE):
                found.append(group)
                break
    return found


# ══════════════════════════════════════════════════════════════════════════════
# STEP 4 ── OUTPUT GENERATION
# ══════════════════════════════════════════════════════════════════════════════

def _escape_pipe(s: str) -> str:
    return s.replace('|', '\\|')


def _bar(score: int, max_score: int = 60) -> str:
    filled = min(10, round(10 * score / max(max_score, 1)))
    return '█' * filled + '░' * (10 - filled)


# ── DIGEST ────────────────────────────────────────────────────────────────────
def generate_digest_md(
    meta, alloys, facilities, gravity, phenomena, metrics,
    models, chapters, findings, comparisons, abstract, groups
) -> str:

    ts = datetime.now().strftime('%Y-%m-%d')
    max_score = chapters[0][1] if chapters else 1

    # Flemings chapter table
    ch_rows = []
    for ch, score in chapters[:8]:
        ch_rows.append(
            f'| {ch} | {_bar(score, max_score)} | {score} |'
        )

    # Quantitative metrics table
    met_rows = []
    for var_name, data in metrics.items():
        if data['hits']:
            vals = ', '.join(f'`{h["value"]}`' for h in data['hits'][:3])
            met_rows.append(f'| {data["description"]} | {vals} |')

    comp_items = [f'- {_escape_pipe(c[:200])}' for c in comparisons[:8]]
    finding_items = [f'{i+1}. {_escape_pipe(f)}' for i, f in enumerate(findings)]

    lines = [
        f'# Digest — {_escape_pipe(meta["title_guess"][:100])}',
        '',
        f'| Field | Value |',
        f'|-------|-------|',
        f'| **File** | `{meta["filename"]}` |',
        f'| **Year** | {meta["year"]} |',
        f'| **Journal** | {meta["journal"]} |',
        f'| **DOI** | {meta["doi"]} |',
        f'| **Generated** | {ts} |',
        '',
        '---',
        '',
        '## Abstract / Overview',
        '',
        _escape_pipe(abstract[:900]) + ('…' if len(abstract) > 900 else ''),
        '',
        '---',
        '',
        '## Classification',
        '',
        '| Category | Extracted Content |',
        '|----------|-------------------|',
        f'| **Alloy Systems** | {", ".join(alloys[:12]) if alloys else "—"} |',
        f'| **Experimental Facilities** | {", ".join(facilities[:6]) if facilities else "—"} |',
        f'| **Gravity Conditions** | {", ".join(gravity) if gravity else "—"} |',
        f'| **Key Phenomena** | {", ".join(phenomena[:8]) if phenomena else "—"} |',
        f'| **Models / Theories** | {", ".join(models[:6]) if models else "—"} |',
        f'| **Research Groups** | {", ".join(groups[:4]) if groups else "—"} |',
        '',
        '---',
        '',
        '## Flemings Chapter Relevance',
        '',
        '| Chapter | Relevance | Hits |',
        '|---------|-----------|------|',
    ] + ch_rows + [
        '',
        '---',
        '',
        '## Key Findings Extracted',
        '',
        '\n'.join(finding_items) if finding_items else '_No explicit finding statements detected._',
        '',
        '---',
        '',
        '## 1g vs. µg Comparison Statements',
        '',
    ] + (comp_items if comp_items else ['_No explicit 1g/µg comparisons detected._']) + [
        '',
        '---',
        '',
        '## Quantitative Parameters',
        '',
        '| Parameter | Extracted Values |',
        '|-----------|-----------------|',
    ] + (met_rows if met_rows else ['| — | No quantitative values extracted |'])

    return '\n'.join(lines)


# ── METRICS ───────────────────────────────────────────────────────────────────
def generate_metrics_md(meta, metrics, alloys, facilities, gravity, comparisons) -> str:

    met_rows = []
    for var_name, data in metrics.items():
        if data['hits']:
            for hit in data['hits'][:2]:
                ctx = _escape_pipe(hit['context'][:100])
                met_rows.append(
                    f'| **{data["description"]}** | `{hit["value"]}` | _{ctx}_ |'
                )

    comp_rows = [
        f'| {i+1} | {_escape_pipe(c[:140])} |'
        for i, c in enumerate(comparisons[:10])
    ]

    lines = [
        f'# Metrics & Specifications — {_escape_pipe(meta["title_guess"][:90])}',
        '',
        f'> **File:** `{meta["filename"]}` · **Year:** {meta["year"]} · **DOI:** {meta["doi"]}',
        '',
        '---',
        '',
        '## Experimental Setup',
        '',
        '| Specification | Value |',
        '|--------------|-------|',
        f'| Alloy Systems | {", ".join(alloys[:8]) if alloys else "—"} |',
        f'| Facility / Program | {", ".join(facilities[:5]) if facilities else "—"} |',
        f'| Gravity Environment | {", ".join(gravity) if gravity else "—"} |',
        '',
        '---',
        '',
        '## Quantitative Measurements Extracted',
        '',
        '| Variable | Value | Context (excerpt) |',
        '|----------|-------|-------------------|',
    ] + (met_rows if met_rows else ['| — | — | No quantitative data extracted |']) + [
        '',
        '---',
        '',
        '## 1g vs. µg Comparison Statements',
        '',
        '| # | Extracted Comparison |',
        '|---|----------------------|',
    ] + (comp_rows if comp_rows else ['| — | No explicit comparisons detected |'])

    return '\n'.join(lines)


# ── SUMMARY ───────────────────────────────────────────────────────────────────
def generate_summary_md(
    meta, alloys, facilities, gravity, phenomena, chapters,
    findings, comparisons, abstract, models
) -> str:

    gravity_str   = ' and '.join(gravity)    if gravity    else 'unspecified gravity'
    alloy_str     = ', '.join(alloys[:4])    if alloys     else 'unspecified alloys'
    facility_str  = ', '.join(facilities[:3])if facilities else 'unspecified facility'
    phenomena_str = ', '.join(phenomena[:5]) if phenomena  else 'solidification phenomena'
    top_ch_names  = [ch.split(':')[1].strip() for ch, _ in chapters[:3]] if chapters else []
    chapter_str   = '; '.join(top_ch_names) if top_ch_names else 'solidification fundamentals'
    model_str     = ', '.join(models[:4])   if models     else 'no specific models identified'
    ch_codes      = ', '.join([ch.split(':')[0] for ch, _ in chapters[:3]]) if chapters else '—'

    finding_items = [f'{i+1}. {_escape_pipe(f)}' for i, f in enumerate(findings[:4])]
    comp_items    = [f'- {_escape_pipe(c[:160])}' for c in comparisons[:5]]

    lines = [
        f'# Summary — {_escape_pipe(meta["title_guess"][:100])}',
        '',
        f'> **{meta["year"]}** · {meta["journal"]} · DOI: `{meta["doi"]}`',
        '',
        '---',
        '',
        '## One-Paragraph Overview',
        '',
        (
            f'This paper investigates **{phenomena_str}** in **{alloy_str}** '
            f'under **{gravity_str}** conditions using **{facility_str}**. '
            f'It is primarily relevant to Flemings *{chapter_str}* '
            f'and references models including {model_str}.'
        ),
        '',
        '---',
        '',
        '## Top Findings',
        '',
        '\n'.join(finding_items) if finding_items else '_No explicit finding statements extracted — see full digest._',
        '',
        '---',
        '',
        '## Relevance to µg Solidification Research',
        '',
    ] + (comp_items if comp_items else ['_No explicit 1g/µg comparisons detected._']) + [
        '',
        '---',
        '',
        '## Quick Reference',
        '',
        '| Tag | Value |',
        '|-----|-------|',
        f'| Alloys | {", ".join(alloys[:5]) if alloys else "—"} |',
        f'| Facility | {facility_str} |',
        f'| Gravity | {gravity_str} |',
        f'| Flemings Chapters | {ch_codes} |',
        f'| Models | {model_str} |',
        '',
        '> 📄 See `_digest.md` for full extraction · `_metrics.md` for quantitative data',
    ]

    return '\n'.join(lines)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN PROCESSING PIPELINE
# ══════════════════════════════════════════════════════════════════════════════

def safe_stem(filename: str) -> str:
    stem = Path(filename).stem
    return re.sub(r'[^\w\-]', '_', stem)[:80]


def process_paper(pdf_path: str, output_dir: str) -> bool:
    """Full pipeline for one PDF → three .md files."""
    filename = Path(pdf_path).name
    stem     = safe_stem(filename)

    print(f'  → Extracting text …')
    full_text = extract_text_from_pdf(pdf_path)

    if full_text.startswith('[ERROR'):
        print(f'  ✗ {full_text}')
        return False

    nchars = len(full_text)
    print(f'  → Parsing ({nchars:,} chars) …')

    meta        = extract_metadata(full_text, filename)
    abstract    = get_abstract(full_text)
    alloys      = extract_alloy_systems(full_text)
    facilities  = extract_facilities(full_text)
    gravity     = extract_gravity_context(full_text)
    phenomena   = extract_phenomena(full_text)
    metrics     = extract_quantitative_metrics(full_text)
    models      = extract_models(full_text)
    chapters    = map_flemings_chapters(full_text)
    findings    = extract_key_findings(full_text)
    comparisons = extract_1g_vs_ug_comparisons(full_text)
    groups      = identify_research_groups(full_text)

    print(f'  → Generating .md files …')

    digest_md  = generate_digest_md(
        meta, alloys, facilities, gravity, phenomena, metrics,
        models, chapters, findings, comparisons, abstract, groups
    )
    metrics_md = generate_metrics_md(
        meta, metrics, alloys, facilities, gravity, comparisons
    )
    summary_md = generate_summary_md(
        meta, alloys, facilities, gravity, phenomena, chapters,
        findings, comparisons, abstract, models
    )

    out = Path(output_dir)
    for suffix, content in [
        ('_digest',  digest_md),
        ('_metrics', metrics_md),
        ('_summary', summary_md),
    ]:
        path = out / f'{stem}{suffix}.md'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content if isinstance(content, str) else '\n'.join(content))

    print(f'  ✓ {stem}_[digest|metrics|summary].md')
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Solidification Literature PDF Digest Generator'
    )
    parser.add_argument(
        '--folder',
        default='/sessions/trusting-nifty-heisenberg/mnt/SpSolidLitReview/RefPapers',
        help='Folder containing PDF files',
    )
    parser.add_argument(
        '--paper', default=None,
        help='Process a single PDF (filename only, inside --folder)',
    )
    parser.add_argument(
        '--output', default=None,
        help='Output directory (default: <folder>/digests/)',
    )
    args = parser.parse_args()

    folder     = Path(args.folder)
    output_dir = Path(args.output) if args.output else folder / 'digests'
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.paper:
        pdfs = [folder / args.paper]
    else:
        pdfs = sorted(p for p in folder.glob('*.pdf') if not p.name.startswith('~'))

    print(f'\n{"="*65}')
    print(f'  Solidification Literature Digest Generator')
    print(f'  Input : {folder}')
    print(f'  Output: {output_dir}')
    print(f'  Papers: {len(pdfs)}')
    print(f'{"="*65}\n')

    success = 0
    for i, pdf_path in enumerate(pdfs, 1):
        print(f'[{i:02d}/{len(pdfs):02d}] {pdf_path.name[:65]}')
        if process_paper(str(pdf_path), str(output_dir)):
            success += 1
        print()

    print(f'{"="*65}')
    print(f'  Complete: {success}/{len(pdfs)} papers processed')
    print(f'  Output  : {output_dir}')
    print(f'{"="*65}\n')


if __name__ == '__main__':
    main()
