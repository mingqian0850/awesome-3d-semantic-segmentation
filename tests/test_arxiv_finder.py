#!/usr/bin/env python3
"""Unit tests for scripts/arxiv_paper_finder.py using local fixtures.

Run: python3 -m unittest discover -s tests -v
"""

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import arxiv_paper_finder as apf  # noqa: E402

HF_FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "hf_papers_sample.json")


def load_hf_fixture() -> dict:
    with open(HF_FIXTURE, encoding="utf-8") as f:
        data = json.load(f)
    return {item["paper"]["id"]: item["paper"] for item in data}


class TestPaperFinder(unittest.TestCase):
    def test_parse_hf_paper(self):
        raw = load_hf_fixture()
        paper = apf.parse_hf_paper(raw["2608.12345"])
        self.assertEqual(paper["arxiv_id"], "2608.12345")
        self.assertEqual(paper["link"], "https://arxiv.org/abs/2608.12345")
        self.assertIn("Alice Example", paper["authors"])
        self.assertIn("Transformers", paper["title"])

    def test_parse_entry_strips_version(self):
        xml = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2608.12345v2</id>
    <published>2026-08-18T10:00:00Z</published>
    <title>Some Point Cloud Segmentation</title>
    <summary>Point cloud semantic segmentation with voxels and lidar.</summary>
    <author><name>Alice Example</name></author>
    <arxiv:primary_category term="cs.CV"/>
    <link href="http://arxiv.org/abs/2608.12345v2" rel="alternate"/>
  </entry>
</feed>"""
        root = apf.ET.fromstring(xml)
        paper = apf.parse_entry(root.find("atom:entry", apf.NS))
        self.assertEqual(paper["arxiv_id"], "2608.12345")
        self.assertEqual(paper["link"], "http://arxiv.org/abs/2608.12345v2")

    def test_versioned_id_dedup(self):
        # "2312.10035v3" must de-duplicate against a known "2312.10035".
        self.assertEqual(apf.re.sub(r"v\d+$", "", "2312.10035v3"), "2312.10035")
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write("See [arXiv:2312.10035](https://arxiv.org/abs/2312.10035).")
            path = f.name
        try:
            known = apf.collect_known_ids([path])
            self.assertIn("2312.10035", known)
        finally:
            os.unlink(path)

    def test_2d_filter(self):
        self.assertTrue(apf.is_2d_only("Medical Image Semantic Segmentation of CT Scans", "mri and whole slide"))
        self.assertFalse(apf.is_2d_only("LiDAR Semantic Segmentation", "point clouds and voxels"))

    def test_full_pipeline_filters_and_dedups(self):
        # entry 1: relevant, new -> kept
        # entry 2: medical/2D -> filtered
        # entry 3: known id (PTv3) -> deduped
        # entry 4: older than window -> filtered
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
            f.write("PTv3 [arXiv:2312.10035](https://arxiv.org/abs/2312.10035).")
            path = f.name
        out = tempfile.mktemp(suffix=".md")
        original_fetch = apf.fetch_hf_papers
        apf.fetch_hf_papers = lambda max_per_query=60, retries=3: load_hf_fixture()
        old_argv = sys.argv
        sys.argv = ["arxiv_paper_finder.py", "--days", "7", "--exclude", path, "--output", out, "--source", "hf"]
        try:
            rc = apf.main()
        finally:
            sys.argv = old_argv
            apf.fetch_hf_papers = original_fetch
        self.assertEqual(rc, 0)
        with open(out, encoding="utf-8") as f:
            content = f.read()
        self.assertIn("2608.12345", content)          # kept
        self.assertNotIn("54321", content)            # 2D/medical filtered
        self.assertNotIn("2312.10035", content)       # deduped
        self.assertNotIn("2501.00001", content)       # outside window


if __name__ == "__main__":
    unittest.main()
