# 📊 Benchmarks & Leaderboards

Official evaluation benchmarks and leaderboards for 3D semantic segmentation,
plus a state-of-the-art reference table and a quick metrics primer.

---

## Leaderboards

| Benchmark | Task | Modality | Official leaderboard | Notes |
| --- | --- | --- | --- | --- |
| SemanticKITTI | LiDAR semantic segmentation | LiDAR | [semantic-kitti.org/tasks.html](http://semantic-kitti.org/tasks.html) · CodaLab: [competitions/6280](https://codalab.lisn.upsaclay.fr/competitions/6280) | 19 classes, mIoU. CodaLab 7097/24025 are the *panoptic* tasks — don't mix them up. |
| nuScenes lidarseg | LiDAR semantic segmentation | LiDAR | [nuscenes.org/lidar-segmentation](https://www.nuscenes.org/lidar-segmentation) · submission via [HF evaluation server](https://huggingface.co/spaces/nuscenes/nuscenes-lidarseg-challenge) | 32 classes. |
| Waymo Open Dataset | 3D semantic segmentation | LiDAR | [waymo.com/open/challenges/3d-semantic-segmentation/](https://waymo.com/open/challenges/3d-semantic-segmentation/) | Annual challenge page; 23 classes. |
| ScanNet | Indoor 3D semantic segmentation | RGB-D | [kaldir.vc.in.tum.de/scannet_benchmark/](https://kaldir.vc.in.tum.de/scannet_benchmark/) · 3D results: [semantic_label_3d](https://kaldir.vc.in.tum.de/scannet_benchmark/semantic_label_3d) | Hosted by TUM; sortable by metric. |
| S3DIS | Indoor 3D semantic segmentation | RGB-D | **No official leaderboard** | Community convention: report Area-5 or 6-fold mIoU (protocols differ — always state which). |
| Semantic3D | Large-scene point-cloud segmentation | TLS | **Official site offline** (301→401) | Benchmark definition in [arXiv:1704.03847](https://arxiv.org/abs/1704.03847). |
| SensatUrban | City-scale point-cloud segmentation | aerial photogrammetry | CodaLab: [competitions/31519](https://competitions.codalab.org/competitions/31519) | ECCV 2022 challenge. |
| Occ3D | 3D semantic occupancy prediction | multi-modal | [tsinghua-mars-lab.github.io/Occ3D/](https://tsinghua-mars-lab.github.io/Occ3D/) · [GitHub](https://github.com/Tsinghua-MARS-Lab/Occ3D) | The older AD23Challenge online leaderboard is defunct. |

---

## State-of-the-art reference (verified snapshot)

> SemanticKITTI and ScanNet **test** numbers are official-leaderboard data; all
> **val** numbers and S3DIS Area-5 are paper-reported (no official val boards).
> Cross-paper comparison is tricky: training configs differ (TTA, extra
> pre-training such as PPT/Sonata). Re-verify before citing.

| Task | Dataset | Metric | Best method | Result | Source |
| --- | --- | --- | --- | --- | --- |
| LiDAR segmentation (single-scan) | SemanticKITTI | mIoU | LSK3DNet (CVPR 2024) | **75.6 (test)** | [Official board](http://semantic-kitti.org/tasks.html) / [semantic_single.json](http://semantic-kitti.org/data/semantic_single.json) · [Paper](https://arxiv.org/abs/2403.15173) |
| LiDAR segmentation (multi-scan) | SemanticKITTI | mIoU | MemorySeg (ICCV 2023) | **58.3 (test)** | [Official board](http://semantic-kitti.org/tasks.html) / [semantic_multi.json](http://semantic-kitti.org/data/semantic_multi.json) · [Paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Li_MemorySeg_Online_LiDAR_Semantic_Segmentation_with_a_Latent_Memory_ICCV_2023_paper.pdf) |
| LiDAR segmentation (val) | SemanticKITTI | mIoU | PTv3 + PPT | **72.3 (val)** | [PTv3 paper, Table 21](https://arxiv.org/abs/2312.10035) |
| Indoor segmentation (val) | ScanNet v2 | mIoU | DITR: DINO in the Room (3DV 2026) | **80.5 (val)** | [Paper, Table 1](https://arxiv.org/abs/2503.18944) |
| Indoor segmentation (test) | ScanNet v2 | mIoU | Volt: Volume Transformer | **80.5 (test)** | [ScanNet official benchmark](https://kaldir.vc.in.tum.de/scannet_benchmark/semantic_label_3d) (2nd: PTv3-PPT-ALC 79.8; PTv3+PPT submission [#1719](https://kaldir.vc.in.tum.de/scannet_benchmark/result_details?id=1719)) |
| Indoor segmentation | S3DIS Area 5 | mIoU | Sonata + PTv3 (CVPR 2025) | **76.0 (Area 5)** | [Sonata paper, Table 6](https://arxiv.org/abs/2503.16429) (6-fold 82.3) |
| LiDAR segmentation (lidarseg) | nuScenes | mIoU | DITR: DINO in the Room | **85.1 (test)** | [Paper, Table 2](https://arxiv.org/abs/2503.18944) (val 84.2; PTv3+PPT 83.0 official test) |

**Caveats**
- The SemanticKITTI official board only lists *submitted* methods; paper-reported
  numbers (SphereFormer test 74.8, PTv3+PPT test 75.5, UniSeg 75.2) are not on
  the official board.
- S3DIS: distinguish **Area 5** from **6-fold** (Papers-with-Code defaults to 6-fold).
- ScanNet val-leader DITR (80.5) and test-leader Volt (80.5) coincidentally match
  but belong to different splits.
- nuScenes official board requires login; PTv3 holds the top official-test spot
  (82.7) until 2025 methods such as [HB-Mamba](https://dl.acm.org/doi/10.1145/3805622.3810584) surpassed it.

---

## Evaluation metrics

- **mIoU (mean Intersection-over-Union)** — the de-facto standard for semantic segmentation.
- **mAcc / oAcc** — mean / overall per-point accuracy.
- **Per-class IoU** — class-level breakdown, essential for imbalanced outdoor scenes.
- **Panoptic quality (PQ)** — for panoptic segmentation (instance + semantic).
- **Occupancy metrics** — IoU / mIoU over voxel grids (Occ3D-style benchmarks).

---

## Official evaluation toolkits

| Toolkit | URL | Purpose |
| --- | --- | --- |
| SemanticKITTI API | [PRBonn/semantic-kitti-api](https://github.com/PRBonn/semantic-kitti-api) | Visualization, data processing, and evaluation for SemanticKITTI |
| nuScenes devkit | [nutonomy/nuscenes-devkit](https://github.com/nutonomy/nuscenes-devkit) | Official nuScenes devkit (incl. lidarseg) |
| waymo-open-dataset | [waymo-research/waymo-open-dataset](https://github.com/waymo-research/waymo-open-dataset) | Official Waymo Open Dataset tools (incl. semantic segmentation labels) |
| ScanNet benchmark | [kaldir.vc.in.tum.de/scannet_benchmark](https://kaldir.vc.in.tum.de/scannet_benchmark/) | Submission + evaluation for ScanNet tasks |

---

> 🚧 Spot a stale leaderboard number? Open a PR — see [CONTRIBUTING.md](CONTRIBUTING.md).
