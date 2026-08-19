<p align="center">
  <img src="https://img.shields.io/badge/3D%20Semantic%20Segmentation-Awesome-blueviolet" alt="Awesome">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs Welcome">
</p>

# Awesome 3D Semantic Segmentation

A curated list of **state-of-the-art research, open-source projects, benchmarks,
and datasets** for **3D semantic segmentation** — the task of assigning a
semantic label (e.g., *road*, *wall*, *chair*, *car*) to every 3D point, voxel,
or pixel in a 3D scene.

Covers indoor & outdoor scenes, point-cloud / voxel / range-image / hybrid
representations, transformer & foundation models, zero-shot / open-vocabulary
segmentation, and the adjacent tasks of 3D occupancy prediction and LLM-based
3D understanding.

> **Status**: actively maintained research snapshot (last verified 2026-08).
> Leaderboards move fast — verify numbers before citing them in papers.

---

## 📑 Contents

- [🏆 SOTA at a Glance](#-sota-at-a-glance)
- [📄 Papers](papers.md)
  - Point-based methods · Voxel / sparse-conv methods · Projection methods ·
    Transformers & hybrids · Zero-shot / foundation models · 3D occupancy
- [🏷️ Label-Efficient Learning](label-efficient.md)
  - Semi/weakly-supervised · Active learning · Self-supervised · Zero-shot ·
    Distillation · SAM in 3D · Auto-labeling · Annotation tools
- [🗂️ Datasets](datasets.md)
  - Indoor · Outdoor LiDAR · Aerial / urban MLS · Synthetic · RGB-D
- [📊 Benchmarks & Leaderboards](benchmarks.md)
  - SemanticKITTI · nuScenes · Waymo · ScanNet · S3DIS · Semantic3D · Occ3D …
- [🛠️ Open-Source Projects](projects.md)
  - Frameworks & toolkits · Official implementations · Foundation-model projects
- [🤝 Contributing](CONTRIBUTING.md)

---

## 🏆 SOTA at a Glance

*Representative state-of-the-art results (verified snapshot: 2026-08). Full
details, caveats, and per-paper numbers live in [benchmarks.md](benchmarks.md).*

| Task / Dataset | Metric | Best method | Reported result |
| --- | --- | --- | --- |
| SemanticKITTI (test, single-scan) | mIoU | LSK3DNet | **75.6** |
| SemanticKITTI (test, multi-scan) | mIoU | MemorySeg | **58.3** |
| SemanticKITTI (val) | mIoU | PTv3 + PPT | **72.3** |
| ScanNet (val) | mIoU | DITR | **80.5** |
| ScanNet (test) | mIoU | Volt | **80.5** |
| S3DIS (Area 5) | mIoU | Sonata + PTv3 | **76.0** |
| nuScenes lidarseg (test) | mIoU | DITR | **85.1** |
| Waymo 2024 challenge | 1st place | PTv3 Extreme | — |

---

## 🧭 How to navigate this repo

| File | Contents |
| --- | --- |
| [`papers.md`](papers.md) | Research papers, grouped by methodological family and year |
| [`label-efficient.md`](label-efficient.md) | Label-efficient learning & efficient annotation (semi/weak supervision, active learning, SAM-assisted labeling, tools) |
| [`datasets.md`](datasets.md) | Datasets with modality, scale, classes, and links |
| [`benchmarks.md`](benchmarks.md) | Leaderboards, evaluation metrics, and official toolkits |
| [`projects.md`](projects.md) | Open-source frameworks and codebases |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to add entries |

---

## 🤖 Automation

The repo ships with a **paper watcher** ([`.github/workflows/paper-watch.yml`](.github/workflows/paper-watch.yml)):

- **Every Monday 01:00 UTC** (and manually via *Actions → paper-watch → Run workflow*),
  it queries the [Hugging Face Papers API](https://huggingface.co/papers) for new
  3D semantic segmentation papers (point clouds / LiDAR / voxels / range images).
- Papers already listed in [`papers.md`](papers.md) are excluded automatically;
  obviously 2D/medical papers are filtered out.
- If new candidates are found, a digest **issue** is opened (or the existing
  open digest is updated) with titles, arXiv links, and abstracts — review,
  verify, then add the good ones to `papers.md` and close the issue.
- Run locally: `python3 scripts/arxiv_paper_finder.py --days 60` (unit tests:
  `python3 -m unittest discover -s tests`).

---

## ✨ Related awesome lists

- [awesome-point-cloud-analysis](https://github.com/Yochengliu/awesome-point-cloud-analysis)
- [awesome-3d-detection](https://github.com/zhulf0804/3D-PointCloud) — point cloud papers & code
- [awesome-3d-vision](https://github.com/qiuye-git/Awesome-3D-Vision)
- [awesome-3d-dataset](https://github.com/viagea/awesome-3d-dataset)

---

## 📜 License

[MIT](LICENSE) © Mingqian Chen. The list itself is free to reuse; links and
descriptions point to their respective owners' work.
