---
title: Literature Review Extraction Validation Report
tags:
  - phd
  - literature-review
  - validation
status: validated
validated_on: 2026-04-26
---

# Literature Review Extraction Validation Report

Validated outputs:

- `01 Literature Review/Earth 1g vs Microgravity Solidification Processing.md`
- `06 Data/Literature Review Extraction/paper-extraction-matrix.csv`
- `06 Data/Literature Review Extraction/numerical-data-extract.csv`
- `06 Data/Literature Review Extraction/comparison-data-earth-vs-microgravity.csv`
- `06 Data/Literature Review Extraction/comparison-data-summary-by-paper.csv`
- `scripts/extract_pdf_evidence.py`

## Checks Performed

| Check | Result |
|---|---|
| Local PDFs discovered | 63 |
| PDFs parsed successfully | 63 |
| PDF parsing failures | 0 |
| Numerical snippets extracted | 4,859 |
| Gravity-relevant comparison snippets | 1,579 |
| Exact PDF references in review note | 31 |
| Missing PDF references in review note | 0 |
| Shortened `...` PDF references remaining | 0 |
| `deg C` placeholder units remaining in review note | 0 |
| Thermal gradients `K/cm` and `K/mm` classified as thermal condition | 117 / 117 |

## Comparison Snippet Contexts

| Gravity context | Snippet count |
|---|---:|
| Microgravity / space | 1,063 |
| Earth / 1g | 252 |
| Direct Earth-vs-microgravity comparison | 264 |

## Dominant Method Tags In Parsed Library

| Method tag | Paper count |
|---|---:|
| Thermophysical properties | 60 |
| Dendritic growth | 50 |
| Nucleation / undercooling | 50 |
| Macrosegregation / interdendritic flow | 44 |
| Eutectic / peritectic | 41 |
| X-ray radiography | 35 |
| Directional solidification | 32 |
| Containerless levitation | 25 |
| Transparent model alloy | 19 |
| Immiscible / monotectic | 16 |

## Quality Assessment

The first version was usable as a scaffold but had two quality problems:

- A few source filenames were shortened in the prose with `...`, which weakened traceability.
- Thermal-gradient units such as `K/cm` and `K/mm` were initially categorized as length-scale snippets in the raw extractor.

Both were corrected. The review note now uses exact source filenames, and the extraction script now classifies `K/cm` and `K/mm` as thermal conditions.

## Remaining Limitations

- PDF text extraction can misread symbols, ligatures, and equation formatting. The CSVs are evidence-discovery artifacts, not final thesis citations.
- Some numerical snippets are figure-caption values rather than table values. These should be checked visually in the PDFs before being used in final prose.
- The review note intentionally uses curated values from the extraction rather than every extracted number, because the raw numerical table contains equation terms and contextual values that are not always experimental results.
