#!/usr/bin/env python3
"""Extract compact evidence tables from local PDF reference papers.

The script deliberately writes snippets and metadata rather than full paper text.
It is intended for literature-review triage: finding numerical values, methods,
gravity condition comparisons, and page-level evidence to inspect manually.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from pypdf import PdfReader


PDF_DIR = Path("ReferencePapers")
OUT_DIR = Path("06 Data") / "Literature Review Extraction"
SNIPPET_RADIUS = 220

MICRO_TERMS = [
    "microgravity",
    "micro-gravity",
    "µg",
    "μg",
    "0g",
    "0 g",
    "zero-g",
    "zero gravity",
    "space",
    "spacelab",
    "space shuttle",
    "iss",
    "international space station",
    "sounding rocket",
    "parabolic",
    "drop tower",
    "drop tube",
    "sj-10",
    "maser",
    "texus",
    "tempus",
    "msl",
    "declIC".lower(),
    "electrostatic levitation",
]

EARTH_TERMS = [
    "earth",
    "earth gravity",
    "1g",
    "1 g",
    "normal gravity",
    "terrestrial",
    "ground",
    "ground-based",
    "ground based",
]

METHOD_PATTERNS = {
    "directional solidification": r"directional solidification|bridgman|gradient furnace|pull(?:ing)? rate",
    "containerless levitation": r"electromagnetic levitation|electrostatic levitation|containerless|eml|tempus",
    "x-ray radiography": r"x[- ]ray|radiograph|radiography|tomograph",
    "transparent model alloy": r"succinonitrile|scn|transparent alloy|declIC|cch4|neopentyl glycol|tris",
    "dendritic growth": r"dendrit(?:e|ic)|tip velocity|tip radius|columnar-to-equiaxed|cet",
    "eutectic/peritectic": r"eutectic|peritectic|lamellar|rod transition",
    "immiscible/monotectic": r"immiscible|monotectic|al-bi|aluminum-bismuth|al-bi-sn",
    "thermophysical properties": r"thermophysical|surface tension|viscosity|density|specific heat|thermal conductivity|emissivity",
    "macrosegregation/interdendritic flow": r"macrosegregation|interdendritic|freckle|natural convection|buoyancy",
    "nucleation/undercooling": r"undercool|nucleation|recalescence|metastable",
}

UNIT_RE = re.compile(
    r"""
    (?P<value>
        [<>~≈±]?\s*
        (?:
            \d+(?:\.\d+)?(?:\s*[x×]\s*10\s*[-−]?\s*\d+|[eE][-+]?\d+)?
            (?:\s*[-–]\s*\d+(?:\.\d+)?)?
            |
            \d+/\d+
        )
    )
    \s*
    (?P<unit>
        wt\.?\s*%|at\.?\s*%|vol\.?\s*%|mass\s*%|mol\s*%|%
        |K\s*/\s*mm|K/mm|K\s*mm-1|K\s*/\s*cm|K/cm|K\s*cm-1
        |K\s*/\s*s|K\s*s-1|K/s|K\s*min-1|K/min|°C\s*/\s*s|°C/s
        |mm\s*/\s*s|mm/s|cm\s*/\s*s|cm/s|m\s*/\s*s|m/s|µm\s*/\s*s|μm/s|um/s
        |g\s*cm-3|g/cm3|kg\s*m-3|kg/m3
        |µm|μm|um|mm|cm|nm
        |K|°C
        |sec|seconds|ms|min|hr|hours
        |mT|kW|Hz
        |Pa\s*s|mPa\s*s|Pa|kPa|MPa|GPa
        |µg|μg|mg|kg
        |W\s*m-1\s*K-1|W/mK|W\s*/\s*m\s*/\s*K
        |mN\s*m-1|mN/m|N\s*m-1|N/m
    )
    """,
    re.IGNORECASE | re.VERBOSE,
)

BARE_SCI_RE = re.compile(r"\b\d+(?:\.\d+)?\s*[x×]\s*10\s*[-−]?\s*\d+\b")


@dataclass
class PageText:
    page: int
    text: str


def clean_text(text: str) -> str:
    text = text.replace("\x00", " ")
    text = text.replace("\u00ad", "")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def compact_context(text: str, start: int, end: int, radius: int = SNIPPET_RADIUS) -> str:
    lo = max(0, start - radius)
    hi = min(len(text), end + radius)
    snippet = text[lo:hi]
    snippet = re.sub(r"\s+", " ", snippet).strip()
    return snippet


def extract_pdf(path: Path) -> tuple[dict, list[PageText]]:
    reader = PdfReader(str(path))
    metadata = reader.metadata or {}
    pages: list[PageText] = []
    for idx, page in enumerate(reader.pages, start=1):
        try:
            txt = page.extract_text() or ""
        except Exception as exc:  # noqa: BLE001 - keep batch extraction moving.
            txt = f"[TEXT EXTRACTION ERROR: {exc}]"
        pages.append(PageText(idx, clean_text(txt)))
    info = {
        "file": str(path),
        "paper_key": path.stem,
        "pdf_title": clean_text(str(metadata.get("/Title", "") or "")),
        "pdf_author": clean_text(str(metadata.get("/Author", "") or "")),
        "pages": len(pages),
        "text_chars": sum(len(p.text) for p in pages),
        "low_text_pages": sum(1 for p in pages if len(p.text) < 200),
    }
    return info, pages


def detect_terms(text: str, terms: Iterable[str]) -> list[str]:
    lower = text.lower()
    return sorted({term for term in terms if term in lower})


def detect_methods(text: str) -> list[str]:
    lower = text.lower()
    methods = []
    for label, pattern in METHOD_PATTERNS.items():
        if re.search(pattern, lower, re.IGNORECASE):
            methods.append(label)
    return methods


def get_abstract(all_text: str) -> str:
    match = re.search(
        r"\babstract\b(.{200,2500}?)(?:\bkeywords?\b|\b1\.?\s+introduction\b|\bintroduction\b)",
        all_text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return ""
    return re.sub(r"\s+", " ", match.group(1)).strip()[:1600]


def extract_section_snippets(pages: list[PageText]) -> dict[str, str]:
    buckets = {
        "method_snippet": r"experiment|experimental|apparatus|facility|sample|specimen|method|setup|procedure",
        "outcome_snippet": r"result|discussion|conclusion|observed|showed|found|microstructure|segregation",
        "gravity_comparison_snippet": r"microgravity|normal gravity|1g|1 g|earth|terrestrial|ground",
    }
    out: dict[str, str] = {k: "" for k in buckets}
    for page in pages:
        for key, pat in buckets.items():
            if out[key]:
                continue
            match = re.search(pat, page.text, re.IGNORECASE)
            if match:
                out[key] = f"p. {page.page}: {compact_context(page.text, match.start(), match.end(), 360)}"
    return out


def gravity_context(snippet: str) -> str:
    lower = snippet.lower()
    has_micro = any(t in lower for t in MICRO_TERMS)
    has_earth = any(t in lower for t in EARTH_TERMS)
    if has_micro and has_earth:
        return "earth-vs-microgravity comparison"
    if has_micro:
        return "microgravity/space"
    if has_earth:
        return "earth/1g"
    return "unspecified"


def numeric_topic(snippet: str, unit: str = "") -> str:
    lower = snippet.lower()
    unit_lower = unit.lower().replace(" ", "")
    if "%" in unit_lower or unit_lower in {"wt%", "wt.%", "at%", "at.%", "vol%"}:
        return "alloy composition"
    if any(token in unit_lower for token in ["k/mm", "k/cm", "kmm-1", "kcm-1"]):
        return "thermal condition"
    if any(token in unit_lower for token in ["µm/s", "μm/s", "um/s", "mm/s", "cm/s", "m/s"]):
        return "growth/velocity"
    if any(token in unit_lower for token in ["k/s", "kmin-1", "k/min", "°c/s"]):
        return "thermal condition"
    if any(token in unit_lower for token in ["µm", "μm", "um", "nm", "mm", "cm"]):
        return "length scale/microstructure"
    if unit_lower in {"k", "°c"}:
        return "thermal condition"
    if unit_lower in {"sec", "seconds", "ms", "min", "hr", "hours"}:
        return "gravity/time/facility"
    if any(token in unit_lower for token in ["pa", "mpa", "gpa", "mn/m", "n/m", "kg/m3", "g/cm3", "pa*s"]):
        return "thermophysical/mechanical property"
    if unit_lower in {"mt", "kw", "hz"}:
        return "field/power"
    if unit_lower in {"µg", "μg"}:
        return "gravity/time/facility"
    topic_rules = [
        ("thermal condition", r"temperature|undercool|cooling|gradient|heating|kelvin|°c|melting"),
        ("growth/velocity", r"velocity|speed|pull|growth rate|tip|front|interface"),
        ("length scale/microstructure", r"spacing|radius|diameter|length|grain|dendrite|lamellar|cell|microstructure"),
        ("gravity/time/facility", r"microgravity|gravity|1g|drop|rocket|iss|space|flight|second|minute|hour|duration"),
        ("thermophysical/mechanical property", r"density|viscosity|surface tension|conductivity|emissivity|specific heat"),
        ("mechanical property", r"hardness|modulus|strength|gpa|mpa"),
        ("field/power", r"magnetic|field|power|laser|current|voltage|frequency"),
        ("alloy composition", r"wt|at\.|mass|mol|composition|alloy|al-|cu|si|ni|bi|sn|ti|zr|co|cr|mo"),
    ]
    for label, pat in topic_rules:
        if re.search(pat, lower):
            return label
    return "other numerical value"


def extract_numbers(info: dict, pages: list[PageText]) -> list[dict]:
    rows: list[dict] = []
    seen: set[tuple[str, int, str, str]] = set()
    for page in pages:
        for match in UNIT_RE.finditer(page.text):
            snippet = compact_context(page.text, match.start(), match.end())
            key = (info["paper_key"], page.page, match.group("value"), match.group("unit").lower())
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                {
                    "paper_key": info["paper_key"],
                    "file": info["file"],
                    "page": page.page,
                    "value": re.sub(r"\s+", " ", match.group("value")).strip(),
                    "unit": re.sub(r"\s+", " ", match.group("unit")).strip(),
                    "topic": numeric_topic(snippet, match.group("unit")),
                    "gravity_context": gravity_context(snippet),
                    "snippet": snippet,
                }
            )
        for match in BARE_SCI_RE.finditer(page.text):
            snippet = compact_context(page.text, match.start(), match.end())
            if gravity_context(snippet) == "unspecified" and numeric_topic(snippet) == "other numerical value":
                continue
            key = (info["paper_key"], page.page, match.group(0), "")
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                {
                    "paper_key": info["paper_key"],
                    "file": info["file"],
                    "page": page.page,
                    "value": re.sub(r"\s+", " ", match.group(0)).strip(),
                    "unit": "",
                    "topic": numeric_topic(snippet),
                    "gravity_context": gravity_context(snippet),
                    "snippet": snippet,
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    if not PDF_DIR.exists():
        print(f"Missing {PDF_DIR}", file=sys.stderr)
        return 2
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    papers: list[dict] = []
    numbers: list[dict] = []
    failures: list[dict] = []

    for pdf in sorted(PDF_DIR.glob("*.pdf")):
        try:
            info, pages = extract_pdf(pdf)
            all_text = "\n".join(p.text for p in pages)
            info["abstract_or_opening"] = get_abstract(all_text) or re.sub(r"\s+", " ", all_text[:1400]).strip()
            info["microgravity_terms"] = "; ".join(detect_terms(all_text, MICRO_TERMS))
            info["earth_terms"] = "; ".join(detect_terms(all_text, EARTH_TERMS))
            info["method_tags"] = "; ".join(detect_methods(all_text))
            info.update(extract_section_snippets(pages))
            paper_numbers = extract_numbers(info, pages)
            info["numeric_snippets_count"] = len(paper_numbers)
            papers.append(info)
            numbers.extend(paper_numbers)
        except Exception as exc:  # noqa: BLE001 - batch extraction should continue.
            failures.append({"file": str(pdf), "error": repr(exc)})

    write_csv(
        OUT_DIR / "paper-extraction-matrix.csv",
        papers,
        [
            "paper_key",
            "file",
            "pdf_title",
            "pdf_author",
            "pages",
            "text_chars",
            "low_text_pages",
            "method_tags",
            "microgravity_terms",
            "earth_terms",
            "numeric_snippets_count",
            "abstract_or_opening",
            "method_snippet",
            "gravity_comparison_snippet",
            "outcome_snippet",
        ],
    )
    write_csv(
        OUT_DIR / "numerical-data-extract.csv",
        numbers,
        ["paper_key", "file", "page", "value", "unit", "topic", "gravity_context", "snippet"],
    )
    with (OUT_DIR / "extraction-summary.json").open("w", encoding="utf-8") as fh:
        json.dump(
            {
                "pdf_count": len(list(PDF_DIR.glob("*.pdf"))),
                "papers_extracted": len(papers),
                "failures": failures,
                "numeric_snippets": len(numbers),
                "output_files": [
                    str(OUT_DIR / "paper-extraction-matrix.csv"),
                    str(OUT_DIR / "numerical-data-extract.csv"),
                ],
            },
            fh,
            indent=2,
        )
    print(json.dumps({"papers": len(papers), "numeric_snippets": len(numbers), "failures": failures}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
