#!/usr/bin/env python3
"""Paper watcher for 3D semantic segmentation.

Queries the Hugging Face Papers API (and optionally arXiv) for recent papers
on 3D semantic segmentation (point clouds / LiDAR / voxels / range images),
excludes papers already listed in the repo, and emits a markdown candidate
list.

Note: the arXiv API rate-limits complex boolean queries (HTTP 429) from data
center IPs, so the HF Papers API is the default source. The HF index lags
arXiv by ~1–1.5 months, so use a look-back window of ~60 days for weekly runs.

Intended to run inside a GitHub Actions workflow (paper-watch.yml), but can
also be run locally:

    python3 scripts/arxiv_paper_finder.py --days 60 --output new_papers.md

Requires only the Python standard library.
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

HF_PAPERS_API = "https://huggingface.co/api/papers/search"
ARXIV_API = "https://export.arxiv.org/api/query"
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}
UA = "awesome-3d-semantic-segmentation-watcher/1.0"

# Multiple search queries to widen recall; results are merged and de-duplicated.
HF_QUERIES = [
    "point cloud semantic segmentation",
    "lidar semantic segmentation",
    "3d semantic segmentation",
    "3d scene segmentation point cloud",
    "voxel semantic segmentation",
]

# arXiv query (kept as an optional source; complex queries are often 429-limited).
ARXIV_QUERY = (
    'cat:cs.CV AND '
    '(abs:"semantic segmentation" OR abs:"semantic scene segmentation") AND '
    '(abs:"point cloud" OR abs:"point clouds" OR abs:"lidar" OR abs:"LiDAR" '
    'OR abs:"3D scene" OR abs:"voxel" OR abs:"range image" OR abs:"range-view")'
)

# Rough 2D-only signals that indicate the paper is probably not 3D segmentation.
TWO_D_SIGNALS = [
    "2d semantic", "rgb semantic", "image semantic segmentation",
    "medical image", "ct scan", "mri", "fundus", "endoscopic",
    "whole slide", "histopathology",
]

ARXIV_ID_RE = re.compile(r"arxiv:(\d{4}\.\d{4,5})", re.IGNORECASE)


def _request_json(url: str, retries: int = 3) -> list:
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except Exception as e:
            last_err = e
            wait = 5 * attempt  # 5s, 10s, 15s backoff
            print(f"[warn] API attempt {attempt}/{retries} failed ({e}); retrying in {wait}s…", file=sys.stderr)
            time.sleep(wait)
    raise last_err


def fetch_hf_papers(max_per_query: int = 60, retries: int = 3) -> dict:
    """Fetch recent papers from the HF Papers API; returns {arxiv_id: paper}."""
    merged: dict = {}
    for q in HF_QUERIES:
        params = {"q": q, "limit": max_per_query, "sort": "publishedAt", "order": "desc"}
        url = HF_PAPERS_API + "?" + urllib.parse.urlencode(params)
        try:
            data = _request_json(url, retries=retries)
        except Exception as e:
            print(f"[warn] HF query {q!r} failed: {e}", file=sys.stderr)
            continue
        for item in data:
            paper = item.get("paper") or {}
            pid = paper.get("id")
            if pid:
                merged.setdefault(pid, paper)
        time.sleep(1)  # be polite between queries
    return merged


def fetch_arxiv(max_results: int, sort_by: str = "submittedDate", retries: int = 3, api_url: str = ARXIV_API) -> ET.Element:
    params = {
        "search_query": ARXIV_QUERY,
        "start": 0,
        "max_results": max_results,
        "sortBy": sort_by,
        "sortOrder": "descending",
    }
    url = api_url + "?" + urllib.parse.urlencode(params)
    last_err = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read()
            return ET.fromstring(data)
        except Exception as e:
            last_err = e
            wait = 10 * attempt  # 10s, 20s, 30s backoff
            print(f"[warn] arXiv API attempt {attempt}/{retries} failed ({e}); retrying in {wait}s…", file=sys.stderr)
            time.sleep(wait)
    raise last_err


def parse_hf_paper(paper: dict) -> dict:
    """Normalize an HF Papers API entry to the internal dict format."""
    pid = (paper.get("id") or "").lower()
    authors = [a.get("name", "") for a in (paper.get("authors") or []) if a.get("name")]
    published = paper.get("publishedAt") or ""
    return {
        "title": re.sub(r"\s+", " ", paper.get("title") or ""),
        "authors": authors,
        "arxiv_id": pid,
        "link": f"https://arxiv.org/abs/{pid}" if pid else "",
        "published": published,
        "summary": re.sub(r"\s+", " ", paper.get("summary") or ""),
        "primary_category": "cs.CV (HF)",
    }


def parse_entry(entry: ET.Element) -> dict:
    def text(tag: str) -> str:
        node = entry.find(f"atom:{tag}", NS)
        return node.text.strip() if node is not None and node.text else ""

    authors = [
        a.find("atom:name", NS).text
        for a in entry.findall("atom:author", NS)
        if a.find("atom:name", NS) is not None and a.find("atom:name", NS).text
    ]
    published = text("published")
    raw_id = text("id").rsplit("/", 1)[-1]
    # Prefer the abs page link; fall back to the PDF link.
    link = ""
    for l in entry.findall("atom:link", NS):
        href = l.get("href", "")
        if l.get("rel") == "alternate" and "abs" in href:
            link = href
            break
    if not link:
        for l in entry.findall("atom:link", NS):
            if l.get("title") == "pdf":
                link = l.get("href", "")
                break
    return {
        "title": re.sub(r"\s+", " ", text("title")),
        "authors": authors,
        # Strip version suffix (e.g. "2312.10035v2" -> "2312.10035") so that
        # de-duplication against papers.md works reliably.
        "arxiv_id": re.sub(r"v\d+$", "", raw_id).lower(),
        "link": link or f"https://arxiv.org/abs/{raw_id}",
        "published": published,
        "summary": re.sub(r"\s+", " ", text("summary")),
        "primary_category": entry.find("arxiv:primary_category", NS).get("term", "") if entry.find("arxiv:primary_category", NS) is not None else "",
    }


def is_2d_only(title: str, abstract: str) -> bool:
    text = (title + " " + abstract).lower()
    return any(sig in text for sig in TWO_D_SIGNALS)


def collect_known_ids(exclude_files) -> set:
    """Collect arXiv ids already present in the given markdown files."""
    known = set()
    for path in exclude_files:
        try:
            with open(path, encoding="utf-8") as f:
                content = f.read()
        except OSError:
            continue
        for m in ARXIV_ID_RE.finditer(content):
            known.add(m.group(1).lower())
    return known


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--days", type=int, default=60, help="look-back window in days (HF index lags arXiv by ~1.5 months)")
    parser.add_argument("--max", type=int, default=60, help="max results per query")
    parser.add_argument("--exclude", nargs="*", default=["papers.md"], help="markdown files to de-duplicate against")
    parser.add_argument("--output", default="new_papers.md", help="output markdown path")
    parser.add_argument("--source", choices=["hf", "arxiv"], default="hf", help="paper source API")
    parser.add_argument("--api-url", default=ARXIV_API, help="arXiv API endpoint (mainly for testing)")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)
    known = collect_known_ids(args.exclude)

    if args.source == "hf":
        raw = fetch_hf_papers(max_per_query=args.max)
        papers = [parse_hf_paper(p) for p in raw.values()]
        print(f"[info] fetched {len(papers)} unique papers from HF Papers API", file=sys.stderr)
    else:
        root = fetch_arxiv(args.max, api_url=args.api_url)
        entries = root.findall("atom:entry", NS)
        papers = [parse_entry(e) for e in entries]
        print(f"[info] fetched {len(papers)} entries from arXiv API", file=sys.stderr)

    candidates = []
    for paper in papers:
        if not paper["arxiv_id"]:
            continue
        try:
            published_dt = datetime.fromisoformat(paper["published"].replace("Z", "+00:00"))
        except ValueError:
            continue
        if published_dt < cutoff:
            continue
        if paper["arxiv_id"] in known:
            continue
        if is_2d_only(paper["title"], paper["summary"]):
            continue
        candidates.append(paper)

    candidates.sort(key=lambda p: p["published"], reverse=True)

    if not candidates:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("")  # empty file -> workflow skips the issue
        print(f"No new papers in the last {args.days} days (checked {len(papers)} fetched papers).")
        return 0

    lines = [
        "# 📚 New 3D semantic segmentation papers (auto-detected)",
        "",
        f"Fetched {len(papers)} papers; **{len(candidates)} new candidate(s)** in the last {args.days} days.",
        "",
        "> 🤖 Auto-generated by `scripts/arxiv_paper_finder.py`. Review each entry before adding it to `papers.md` — verify title, venue, and numbers (see CONTRIBUTING.md).",
        "",
    ]
    for i, p in enumerate(candidates, 1):
        authors = ", ".join(p["authors"][:3]) + (" et al." if len(p["authors"]) > 3 else "")
        lines += [
            f"### {i}. {p['title']}",
            "",
            f"- **Authors**: {authors}",
            f"- **arXiv**: [{p['arxiv_id']}]({p['link']}) · submitted {p['published'][:10]} · {p['primary_category']}",
            f"- **Abstract**: {p['summary'][:400]}{'…' if len(p['summary']) > 400 else ''}",
            "",
        ]
    lines.append("---\n\nAdd verified entries to `papers.md` and close this issue. 🤖")
    with open(args.output, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Wrote {len(candidates)} candidates to {args.output}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
