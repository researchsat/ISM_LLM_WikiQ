#!/usr/bin/env python3
"""Build a self-contained visual dashboard for the Obsidian PhD vault."""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from html import escape
from pathlib import Path


ROOT = Path(".")
OUT_HTML = Path("00 MOCs") / "Interactive PhD Dashboard.html"
OUT_MD = Path("00 MOCs") / "Interactive PhD Dashboard.md"
OUT_JSON = Path("06 Data") / "dashboard-data.json"

TOP_LEVEL = [
    "00 MOCs",
    "01 Literature Review",
    "02 Concepts",
    "03 Papers",
    "04 Experiments",
    "05 Methods",
    "06 Data",
    "99 Templates",
    "ReferencePapers",
    "scripts",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end].strip()
    body = text[end + 4 :].lstrip()
    data: dict[str, object] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if re.match(r"^[A-Za-z0-9_-]+:", line):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            if value == "":
                data[key] = []
            elif value.startswith("[") and value.endswith("]"):
                items = [v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip()]
                data[key] = items
            else:
                data[key] = value.strip("\"'")
        elif current_key and line.strip().startswith("-"):
            existing = data.setdefault(current_key, [])
            if not isinstance(existing, list):
                existing = [str(existing)]
                data[current_key] = existing
            existing.append(line.strip()[1:].strip().strip("\"'"))
    return data, body


def note_type(path: Path) -> str:
    parts = path.parts
    if len(parts) < 2:
        return "Home"
    if parts[0] == "00 MOCs":
        return "MOC"
    if parts[0] == "01 Literature Review":
        return "Review"
    if parts[0] == "02 Concepts":
        if len(parts) > 2:
            return parts[1]
        return "Concept"
    if parts[0] == "03 Papers":
        if len(parts) > 2:
            return parts[1]
        return "Paper"
    if parts[0] == "04 Experiments":
        return "Experiment"
    if parts[0] == "05 Methods":
        return "Method"
    if parts[0] == "99 Templates":
        return "Template"
    return parts[0]


def normalize_tags(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(v).strip("# ") for v in value if str(v).strip()]
    if isinstance(value, str):
        return [v.strip("# ") for v in re.split(r"[, ]+", value) if v.strip()]
    return []


def collect_data() -> dict:
    markdown_paths = sorted(
        p for p in ROOT.rglob("*.md") if ".obsidian" not in p.parts and not str(p).startswith("./.obsidian")
    )
    records = []
    all_tags: Counter[str] = Counter()
    statuses: Counter[str] = Counter()
    types: Counter[str] = Counter()
    folder_counts: Counter[str] = Counter()
    links: Counter[str] = Counter()

    for path in markdown_paths:
        text = read_text(path)
        fm, body = split_frontmatter(text)
        title = str(fm.get("title") or path.stem)
        tags = normalize_tags(fm.get("tags", []))
        status = str(fm.get("status") or "unspecified")
        kind = note_type(path)
        top = path.parts[0] if path.parts else "."
        wikilinks = re.findall(r"\[\[([^\]|#]+)", text)
        for tag in tags:
            all_tags[tag] += 1
        for link in wikilinks:
            links[link.strip()] += 1
        statuses[status] += 1
        types[kind] += 1
        folder_counts[top] += 1
        preview = re.sub(r"\s+", " ", re.sub(r"---.*?---", "", text, flags=re.DOTALL)).strip()[:260]
        records.append(
            {
                "title": title,
                "path": str(path),
                "type": kind,
                "top": top,
                "status": status,
                "tags": tags,
                "priority": str(fm.get("priority") or ""),
                "system": str(fm.get("system") or ""),
                "method": str(fm.get("method") or ""),
                "relevance": str(fm.get("relevance") or ""),
                "source_pdf": str(fm.get("source_pdf") or ""),
                "links": sorted(set(wikilinks)),
                "preview": preview,
            }
        )

    charts = [
        {"title": p.stem.replace("_", " ").replace("chart", "Chart "), "path": str(p)}
        for p in sorted((ROOT / "06 Data" / "Charts").glob("*.png"))
    ]
    pdf_count = len(list((ROOT / "ReferencePapers").glob("*.pdf")))
    digest_count = len(list((ROOT / "03 Papers" / "Digests").glob("*.md")))
    archive_papers = len(list((ROOT / "03 Papers" / "Archive Paper Notes").glob("*.md")))
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")

    notes_by_stem = {Path(r["path"]).stem for r in records}
    missing_links = sorted(link for link in links if link not in notes_by_stem and not link.endswith(".pdf"))

    data = {
        "generated": generated,
        "counts": {
            "notes": len(records),
            "pdfs": pdf_count,
            "digests": digest_count,
            "archive_papers": archive_papers,
            "charts": len(charts),
            "missing_note_links": len(missing_links),
        },
        "records": records,
        "charts": charts,
        "topTags": all_tags.most_common(30),
        "statuses": statuses.most_common(),
        "types": types.most_common(),
        "folders": folder_counts.most_common(),
        "missingLinks": missing_links[:80],
    }
    return data


def to_rel_from_dashboard(path: str) -> str:
    # Dashboard HTML lives in 00 MOCs.
    return "../" + path.replace("\\", "/").replace(" ", "%20")


def render_html(data: dict) -> str:
    json_blob = json.dumps(data, ensure_ascii=False)
    chart_imgs = "\n".join(
        f'<button class="chartThumb" data-chart="{escape(to_rel_from_dashboard(c["path"]))}">'
        f'<img src="{escape(to_rel_from_dashboard(c["path"]))}" alt="{escape(c["title"])}"><span>{escape(c["title"])}</span></button>'
        for c in data["charts"]
    )
    top_tag_buttons = "\n".join(
        f'<button class="chip tagChip" data-tag="{escape(tag)}">{escape(tag)} <span>{count}</span></button>'
        for tag, count in data["topTags"][:18]
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PhD Wiki Interactive Dashboard</title>
<style>
:root {{
  --bg: #f6f4ef;
  --panel: #ffffff;
  --ink: #1f2933;
  --muted: #667085;
  --line: #d9ded6;
  --green: #2f6f5e;
  --blue: #315f8c;
  --red: #9f4f45;
  --gold: #b5842f;
  --shadow: 0 8px 24px rgba(31, 41, 51, 0.08);
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
}}
a {{ color: inherit; }}
.shell {{ max-width: 1440px; margin: 0 auto; padding: 28px; }}
.hero {{
  display: grid;
  grid-template-columns: 1.4fr 0.9fr;
  gap: 20px;
  align-items: stretch;
  margin-bottom: 20px;
}}
.heroMain, .panel, .metric, .result, .chartStage {{
  background: var(--panel);
  border: 1px solid var(--line);
  box-shadow: var(--shadow);
  border-radius: 8px;
}}
.heroMain {{ padding: 26px; }}
.eyebrow {{ color: var(--green); font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: .08em; }}
h1 {{ margin: 10px 0 12px; font-size: 38px; line-height: 1.05; letter-spacing: 0; }}
.subtitle {{ color: var(--muted); max-width: 820px; line-height: 1.55; }}
.quickLinks {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 22px; }}
.quickLinks a, button {{
  border: 1px solid var(--line);
  background: #fbfbf8;
  border-radius: 6px;
  padding: 9px 12px;
  font-weight: 650;
  text-decoration: none;
  cursor: pointer;
}}
.quickLinks a:hover, button:hover {{ border-color: var(--green); }}
.metrics {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }}
.metric {{ padding: 18px; min-height: 98px; }}
.metric b {{ display: block; font-size: 34px; line-height: 1; }}
.metric span {{ display: block; color: var(--muted); margin-top: 8px; font-size: 13px; }}
.grid {{ display: grid; grid-template-columns: 360px 1fr; gap: 20px; align-items: start; }}
.panel {{ padding: 18px; margin-bottom: 20px; }}
.panel h2 {{ margin: 0 0 14px; font-size: 18px; }}
.search {{ width: 100%; padding: 12px 14px; border: 1px solid var(--line); border-radius: 6px; font-size: 15px; }}
.chips {{ display: flex; flex-wrap: wrap; gap: 8px; }}
.chip {{ font-size: 13px; padding: 7px 9px; }}
.chip.active {{ background: var(--green); color: white; border-color: var(--green); }}
.chip span {{ color: var(--muted); margin-left: 4px; }}
.chip.active span {{ color: rgba(255,255,255,.75); }}
.barRow {{ display: grid; grid-template-columns: 115px 1fr 42px; gap: 10px; align-items: center; margin: 9px 0; font-size: 13px; }}
.barLabel {{ white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: var(--muted); }}
.barTrack {{ height: 10px; background: #edf0eb; border-radius: 999px; overflow: hidden; }}
.bar {{ height: 100%; background: var(--blue); border-radius: 999px; }}
.resultGrid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }}
.result {{ padding: 15px; min-height: 160px; display: flex; flex-direction: column; gap: 10px; }}
.result h3 {{ margin: 0; font-size: 16px; line-height: 1.25; }}
.meta {{ display: flex; gap: 8px; flex-wrap: wrap; color: var(--muted); font-size: 12px; }}
.pill {{ border: 1px solid var(--line); border-radius: 999px; padding: 3px 7px; background: #fafafa; }}
.preview {{ color: var(--muted); line-height: 1.45; font-size: 13px; flex: 1; }}
.openLink {{ color: var(--green); font-weight: 700; text-decoration: none; }}
.sectionHeader {{ display: flex; justify-content: space-between; align-items: baseline; gap: 14px; margin-bottom: 12px; }}
.sectionHeader h2 {{ margin: 0; font-size: 22px; }}
.count {{ color: var(--muted); font-size: 13px; }}
.chartLayout {{ display: grid; grid-template-columns: 260px 1fr; gap: 16px; }}
.chartList {{ display: grid; gap: 8px; max-height: 620px; overflow: auto; padding-right: 4px; }}
.chartThumb {{ display: grid; grid-template-columns: 52px 1fr; gap: 10px; text-align: left; align-items: center; width: 100%; }}
.chartThumb img {{ width: 52px; height: 38px; object-fit: cover; border: 1px solid var(--line); border-radius: 4px; background: white; }}
.chartStage {{ min-height: 420px; display: grid; place-items: center; padding: 16px; }}
.chartStage img {{ max-width: 100%; max-height: 660px; border-radius: 6px; }}
.table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
.table th, .table td {{ border-bottom: 1px solid var(--line); padding: 8px; text-align: left; vertical-align: top; }}
.table th {{ color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .05em; }}
.footer {{ color: var(--muted); font-size: 12px; padding: 24px 0; }}
@media (max-width: 980px) {{
  .hero, .grid, .chartLayout {{ grid-template-columns: 1fr; }}
  .resultGrid {{ grid-template-columns: 1fr; }}
  h1 {{ font-size: 30px; }}
}}
</style>
</head>
<body>
<div class="shell">
  <section class="hero">
    <div class="heroMain">
      <div class="eyebrow">Metal alloy processing for in-space manufacturing</div>
      <h1>PhD Wiki Interactive Dashboard</h1>
      <p class="subtitle">A visual index of the current Obsidian vault: concept notes, paper notes, digests, charts, extraction data, and review workflow. Use the filters to move between the literature-review map, mechanisms, alloy systems, platforms, and paper evidence.</p>
      <div class="quickLinks">
        <a href="../START%20HERE.md">Start Here</a>
        <a href="Metal%20Alloy%20Processing%20for%20In-Space%20Manufacturing%20MOC.md">Main MOC</a>
        <a href="../01%20Literature%20Review/Earth%201g%20vs%20Microgravity%20Solidification%20Processing.md">1g vs Microgravity Review</a>
        <a href="../05%20Methods/Literature%20Review%20Workflow.md">Workflow</a>
      </div>
    </div>
    <div class="metrics" id="metrics"></div>
  </section>

  <section class="grid">
    <aside>
      <div class="panel">
        <h2>Search</h2>
        <input id="search" class="search" placeholder="Search notes, tags, methods, systems">
      </div>
      <div class="panel">
        <h2>Type Filter</h2>
        <div class="chips" id="typeChips"></div>
      </div>
      <div class="panel">
        <h2>Status Filter</h2>
        <div class="chips" id="statusChips"></div>
      </div>
      <div class="panel">
        <h2>Top Tags</h2>
        <div class="chips">{top_tag_buttons}</div>
      </div>
      <div class="panel">
        <h2>Vault Composition</h2>
        <div id="folderBars"></div>
      </div>
    </aside>
    <main>
      <div class="panel">
        <div class="sectionHeader">
          <h2>Filtered Notes</h2>
          <span class="count" id="resultCount"></span>
        </div>
        <div id="results" class="resultGrid"></div>
      </div>
      <div class="panel">
        <div class="sectionHeader">
          <h2>Evidence Charts</h2>
          <span class="count">Click a chart to inspect it</span>
        </div>
        <div class="chartLayout">
          <div class="chartList">{chart_imgs}</div>
          <div class="chartStage"><img id="activeChart" src="{escape(to_rel_from_dashboard(data["charts"][0]["path"]) if data["charts"] else "")}" alt="Selected chart"></div>
        </div>
      </div>
      <div class="panel">
        <div class="sectionHeader">
          <h2>Review Priorities</h2>
          <span class="count">Paper notes with priority metadata</span>
        </div>
        <table class="table" id="priorityTable"></table>
      </div>
      <div class="panel">
        <div class="sectionHeader">
          <h2>Legacy Link Cleanup</h2>
          <span class="count" id="missingCount"></span>
        </div>
        <p class="preview">Imported archive notes include legacy links to historical PDF filenames. These should be cleaned when each paper is read, not bulk-mapped.</p>
        <table class="table" id="missingTable"></table>
      </div>
    </main>
  </section>
  <div class="footer">Generated {escape(data["generated"])} from local vault files. No external network assets.</div>
</div>

<script id="dashboard-data" type="application/json">{json_blob}</script>
<script>
const data = JSON.parse(document.getElementById('dashboard-data').textContent);
const state = {{ q: '', type: '', status: '', tag: '' }};
const metrics = [
  ['Notes', data.counts.notes],
  ['Reference PDFs', data.counts.pdfs],
  ['Paper Digests', data.counts.digests],
  ['Charts', data.counts.charts],
  ['Archive Paper Notes', data.counts.archive_papers],
  ['Legacy Link Tasks', data.counts.missing_note_links]
];
document.getElementById('metrics').innerHTML = metrics.map(([label, value]) => `<div class="metric"><b>${{value}}</b><span>${{label}}</span></div>`).join('');

function chip(container, label, count, key) {{
  const btn = document.createElement('button');
  btn.className = 'chip';
  btn.innerHTML = `${{label}} <span>${{count}}</span>`;
  btn.onclick = () => {{
    state[key] = state[key] === label ? '' : label;
    render();
  }};
  btn.dataset.value = label;
  container.appendChild(btn);
}}

const typeBox = document.getElementById('typeChips');
data.types.forEach(([label, count]) => chip(typeBox, label, count, 'type'));
const statusBox = document.getElementById('statusChips');
data.statuses.forEach(([label, count]) => chip(statusBox, label, count, 'status'));

document.querySelectorAll('.tagChip').forEach(btn => {{
  btn.onclick = () => {{
    state.tag = state.tag === btn.dataset.tag ? '' : btn.dataset.tag;
    render();
  }};
}});

document.getElementById('search').addEventListener('input', e => {{
  state.q = e.target.value.toLowerCase();
  render();
}});

function renderBars() {{
  const max = Math.max(...data.folders.map(x => x[1]));
  document.getElementById('folderBars').innerHTML = data.folders.map(([name, count]) => {{
    const w = Math.round(count / max * 100);
    return `<div class="barRow"><div class="barLabel" title="${{name}}">${{name}}</div><div class="barTrack"><div class="bar" style="width:${{w}}%"></div></div><div>${{count}}</div></div>`;
  }}).join('');
}}

function matches(r) {{
  const blob = [r.title, r.path, r.type, r.status, r.tags.join(' '), r.system, r.method, r.relevance, r.preview].join(' ').toLowerCase();
  if (state.q && !blob.includes(state.q)) return false;
  if (state.type && r.type !== state.type) return false;
  if (state.status && r.status !== state.status) return false;
  if (state.tag && !r.tags.includes(state.tag)) return false;
  return true;
}}

function fileHref(path) {{
  return '../' + encodeURI(path);
}}

function renderResults() {{
  const rows = data.records.filter(matches).slice(0, 80);
  document.getElementById('resultCount').textContent = `${{rows.length}} shown`;
  document.getElementById('results').innerHTML = rows.map(r => {{
    const tags = r.tags.slice(0, 4).map(t => `<span class="pill">#${{t}}</span>`).join('');
    return `<article class="result">
      <h3>${{r.title}}</h3>
      <div class="meta"><span class="pill">${{r.type}}</span><span class="pill">${{r.status}}</span>${{tags}}</div>
      <div class="preview">${{r.preview || r.relevance || r.path}}</div>
      <a class="openLink" href="${{fileHref(r.path)}}">Open note</a>
    </article>`;
  }}).join('');
}}

function renderPriority() {{
  const rows = data.records
    .filter(r => r.priority && r.type === 'Paper')
    .sort((a,b) => Number(a.priority || 999) - Number(b.priority || 999));
  document.getElementById('priorityTable').innerHTML = `<tr><th>Priority</th><th>Paper</th><th>System</th><th>Method</th></tr>` +
    rows.map(r => `<tr><td>${{r.priority}}</td><td><a href="${{fileHref(r.path)}}">${{r.title}}</a></td><td>${{r.system}}</td><td>${{r.method}}</td></tr>`).join('');
}}

function renderMissing() {{
  document.getElementById('missingCount').textContent = `${{data.missingLinks.length}} examples shown`;
  document.getElementById('missingTable').innerHTML = `<tr><th>Legacy unresolved target</th></tr>` +
    data.missingLinks.slice(0, 24).map(x => `<tr><td>${{x}}</td></tr>`).join('');
}}

function updateActiveChips() {{
  document.querySelectorAll('.chip').forEach(btn => {{
    const val = btn.dataset.value || btn.dataset.tag;
    btn.classList.toggle('active', val && (val === state.type || val === state.status || val === state.tag));
  }});
}}

function render() {{
  updateActiveChips();
  renderResults();
}}

document.querySelectorAll('.chartThumb').forEach(btn => {{
  btn.onclick = () => {{
    document.getElementById('activeChart').src = btn.dataset.chart;
  }};
}});

renderBars();
renderPriority();
renderMissing();
render();
</script>
</body>
</html>
"""


def render_markdown(data: dict) -> str:
    return f"""---
title: Interactive PhD Dashboard
tags:
  - dashboard
  - moc
  - phd
status: active
---

# Interactive PhD Dashboard

Open the full visual dashboard:

- [Interactive PhD Dashboard.html](Interactive%20PhD%20Dashboard.html)

The HTML dashboard is self-contained and generated from the current vault files. It includes search, type/status/tag filters, review-priority tables, chart inspection, and archive link-cleanup tracking.

## Key Links

- [[START HERE]]
- [[Metal Alloy Processing for In-Space Manufacturing MOC]]
- [[Earth 1g vs Microgravity Solidification Processing]]
- [[Archive Import Map]]
- [[Literature Review Workflow]]

## Current Counts

| Metric | Count |
|---|---:|
| Notes | {data["counts"]["notes"]} |
| Reference PDFs | {data["counts"]["pdfs"]} |
| Paper digests | {data["counts"]["digests"]} |
| Archive paper notes | {data["counts"]["archive_papers"]} |
| Chart images | {data["counts"]["charts"]} |
| Legacy link cleanup examples | {data["counts"]["missing_note_links"]} |

## Dataview: Active Paper Notes

```dataview
TABLE priority, status, system, method, relevance
FROM "03 Papers"
WHERE priority
SORT priority ASC
```

## Dataview: Active Concept Notes

```dataview
TABLE status, related
FROM "02 Concepts"
WHERE status
SORT file.name ASC
```
"""


def main() -> int:
    data = collect_data()
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    OUT_HTML.write_text(render_html(data), encoding="utf-8")
    OUT_MD.write_text(render_markdown(data), encoding="utf-8")
    print(json.dumps({"html": str(OUT_HTML), "markdown": str(OUT_MD), "json": str(OUT_JSON), "counts": data["counts"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
