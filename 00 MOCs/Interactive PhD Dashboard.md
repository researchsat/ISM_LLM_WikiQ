---
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
| Notes | 380 |
| Reference PDFs | 63 |
| Paper digests | 186 |
| Archive paper notes | 54 |
| Chart images | 12 |
| Legacy link cleanup examples | 153 |

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
