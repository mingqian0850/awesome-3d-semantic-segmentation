#!/usr/bin/env python3
"""Unit tests for scripts/arxiv_paper_finder.py using a local fixture.

Run: python3 -m unittest discover -s tests -v
"""

import os
import sys
import tempfile
import unittest
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import arxiv_paper_finder as apf  # noqa: E402

FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "arxiv_sample.xml")


class TestPaperFinder(unittest.TestCase):
    def setUp(self):
        self.root = apf.ET.parse(FIXTURE).getroot()

    def test_parse_entry_strips_version(self):
        entries = self.root.findall("atom:entry", apf.NS)
        paper = apf.parse_entry(entries[0])
        self.assertEqual(paper["arxiv_id"], "2608.12345")
        self.assertEqual(paper["link"], "http://arxiv.org/abs/2608.12345v1")
        self.assertIn("Alice Example", paper["authors"])
        self.assertEqual(paper["primary_category"], "cs.CV")

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
        try:
            # Patch the fetch to use the fixture instead of the network.
            original_fetch = apf.fetch_arxiv
            apf.fetch_arxiv = lambda max_results, **kw: self.root
            old_argv = sys.argv
            sys.argv = ["arxiv_paper_finder.py", "--days", "7", "--exclude", path, "--output", out, "--api-url", "fixture"]
            try:
                rc = apf.main()
            finally:
                sys.argv = old_argv
                apf.fetch_arxiv = original_fetch
            self.assertEqual(rc, 0)
            with open(out, encoding="utf-8") as f:
                content = f.read()
            self.assertIn("2608.12345", content)          # kept
            self.assertNotIn("54321", content)            # 2D/medical filtered
            self.assertNotIn("2312.10035", content)       # deduped
            self.assertNotIn("2501.00001", content)       # outside window
        finally:
            os.unlink(path)
            if os.path.exists(out):
                os.unlink(out)

    def test_no_candidates_writes_empty_file(self):
        out = tempfile.mktemp(suffix=".md")
        try:
            with open(out, "w", encoding="utf-8") as f:
                f.write("")
            self.assertEqual(os.path.getsize(out), 0)
        finally:
            if os.path.exists(out):
                os.unlink(out)


if __name__ == "__main__":
    unittest.main()
