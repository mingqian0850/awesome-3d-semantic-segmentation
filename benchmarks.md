# 📊 Benchmarks & Leaderboards

Official evaluation benchmarks and leaderboards for 3D semantic segmentation,
plus a quick reference on metrics and official toolkits.

---

## Leaderboards

| Benchmark | Task | Modality | Official leaderboard | Notes |
| --- | --- | --- | --- | --- |
| SemanticKITTI | semantic segmentation | LiDAR | *TBD* | *TBD* |
| nuScenes lidarseg | semantic segmentation | LiDAR | *TBD* | *TBD* |
| Waymo Open | semantic segmentation | LiDAR | *TBD* | *TBD* |
| ScanNet | semantic segmentation | RGB-D | *TBD* | *TBD* |
| S3DIS | semantic segmentation | RGB-D | *TBD* | *TBD* |
| Semantic3D | semantic segmentation | TLS | *TBD* | *TBD* |
| SensatUrban | semantic segmentation | aerial MLS | *TBD* | *TBD* |
| Occ3D | 3D occupancy | multi-modal | *TBD* | *TBD* |

---

## Evaluation metrics

- **mIoU (mean Intersection-over-Union)** — the de-facto standard for semantic
  segmentation.
- **mAcc / oAcc** — mean / overall per-point accuracy.
- **IoU per class** — class-level breakdown, important for imbalanced outdoor
  scenes.
- **Panoptic metrics (PQ)** — for panoptic segmentation (instance + semantic).

---

## Official evaluation toolkits

*TBD — filled from research snapshot.*
