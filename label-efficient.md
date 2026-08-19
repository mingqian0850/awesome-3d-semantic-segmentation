# 🏷️ Label-Efficient 3D Semantic Segmentation

Research on **efficient data labeling / annotation** for 3D semantic
segmentation — getting good models with *less* annotation effort:
semi- and weakly-supervised learning, active learning, self-supervised
pre-training, zero-shot / open-vocabulary learning, cross-modal distillation,
SAM-assisted auto-labeling, plus the annotation tools themselves.

> All entries were verified against arXiv / dblp / CVF / official pages
> (verified snapshot: 2026-08). Entries marked *in main list* are already
> covered in [papers.md](papers.md) and only referenced here. Facts that could
> not be confirmed are listed in [⚠️ Could not verify](#-could-not-verify).

---

## 1. Semi-supervised LiDAR / point-cloud segmentation

**Foundations**
- **LaserMix for Semi-Supervised LiDAR Semantic Segmentation** — Kong *et al.*, CVPR 2023 (Highlight). Mixes laser beams of different LiDAR scans with consistency/confidence regularization; representation-agnostic (range view / voxel); introduces the **ScribbleKITTI** scribble-label benchmark. [arXiv:2207.00026](https://arxiv.org/abs/2207.00026) · [Code](https://github.com/ldkong1205/LaserMix). **+10.8% avg mIoU** over the supervised baseline; reaches fully-supervised parity with **2–5× fewer labels**.

- **Towards Semi-supervised Dual-modal Semantic Segmentation (PD-Net)** — Dong *et al.*, IEEE TMM 2025. 2D-3D dual-modal semi-supervision: point-cloud + image dual streams, pseudo-label self-training, dual-modal fusion. [arXiv:2409.13325](https://arxiv.org/abs/2409.13325).

**2024–2026**
- **Learning from Spatio-temporal Correlation for Semi-Supervised LiDAR Semantic Segmentation (PLE)** — Lee *et al.*, IROS 2024. Temporal neighbor-label estimation + progressive pseudo-label expansion. [arXiv:2410.06893](https://arxiv.org/abs/2410.06893). With only **20% labels exceeds the previous SOTA's 75.2 mIoU at 100% labels** (SemanticKITTI).

- **Beyond the Label Itself: Latent Labels Enhance Semi-supervised Point Cloud Panoptic Segmentation** — Chen *et al.*, AAAI 2024. Latent labels from LiDAR (Cylinder-Mix) and image (instance position-scale learning) branches. [arXiv:2312.08234](https://arxiv.org/abs/2312.08234).

- **Multi-modal NeRF Self-Supervision for LiDAR Semantic Segmentation** — Timoneda *et al.*, IROS 2024. NeRF multimodal reconstruction as self-supervision for LiDAR segmentation. [arXiv:2411.02969](https://arxiv.org/abs/2411.02969).

- **Exploring Scene Affinity for Semi-Supervised LiDAR Semantic Segmentation (AIScene)** — Liu *et al.*, CVPR 2025. Scene-intra consistency + scene-inter association in a teacher–student framework; erasing unlabeled points prevents label leakage. [arXiv:2408.11280](https://arxiv.org/abs/2408.11280) (retitled from "Exploring Scene Coherence…").

- **Collaborative Learning for Semi-Supervised LiDAR Semantic Segmentation (CoLLiS)** — Yang *et al.*, ICML 2026. Collaborative learning over multiple supervision sources to break confirmation bias of single-distillation pseudo labels. [arXiv:2605.17135](https://arxiv.org/abs/2605.17135).

- **RePL: Pseudo-label Refinement for Semi-supervised LiDAR Semantic Segmentation** — Kwon *et al.*, arXiv 2026. Masked reconstruction detects and corrects pseudo-label errors, with theory; SOTA on nuScenes-lidarseg / SemanticKITTI. [arXiv:2604.06825](https://arxiv.org/abs/2604.06825).

- **UniLiPs: Unified LiDAR Pseudo-Labeling with Geometry-Grounded Dynamic Scene Decomposition** — Ghilotti *et al.*, arXiv 2026. Geometry-grounded temporal consistency drives unsupervised multimodal (text + 2D foundation models) LiDAR pseudo-labeling — semantics, 3D boxes, and dense scans, no human input. [arXiv:2601.05105](https://arxiv.org/abs/2601.05105). Depth MAE improved **51.5% / 22.0%** at 80–150 m / 150–250 m.

- **Joint Global and Dynamic Pseudo Labeling for Semi-Supervised Point Cloud Sequence Segmentation** — Liu *et al.*, IEEE TCSVT 2023. Global + dynamic pseudo labels for LiDAR sequence segmentation. [DOI:10.1109/TCSVT.2023.3253210](https://doi.org/10.1109/TCSVT.2023.3253210) · [dblp](https://dblp.uni-trier.de/rec/journals/tcsv/LiuCNY23.html).

## 2. Weakly-supervised point-cloud segmentation (scene-level / sparse / scribble)

- **3D Spatial Recognition without Spatially Labeled 3D (WyPR)** — Ren *et al.*, CVPR 2021. Scene-level labels only; self/cross-task consistency losses + multiple-instance learning for joint segmentation and detection. [arXiv:2105.06461](https://arxiv.org/abs/2105.06461) · [Project](https://facebookresearch.github.io/WyPR/). **>6% mIoU** over prior weakly-supervised SOTA on ScanNet / S3DIS.

- **2D-3D Interlaced Transformer for Point Cloud Segmentation with Scene-Level Supervision** — Yang *et al.*, ICCV 2023. Interlaced 2D-3D transformer propagates supervision under scene-level labels. [arXiv:2310.12817](https://arxiv.org/abs/2310.12817).

- **Densify Your Labels: Unsupervised Clustering with Bipartite Matching for Weakly Supervised Point Cloud Segmentation** — Xia *et al.*, arXiv 2023. Dataset-level unsupervised clustering + bipartite matching propagates scene-level labels to dense per-point pseudo-labels. [arXiv:2312.06799](https://arxiv.org/abs/2312.06799) · [Project](https://densify-your-labels.github.io/).

- **Multi-modality Affinity Inference for Weakly Supervised 3D Semantic Segmentation** — Li *et al.*, AAAI 2024. Geometry + RGB affinity inference generates supervision for weakly supervised 3D segmentation. [arXiv:2312.16578](https://arxiv.org/abs/2312.16578).

- **Dense Supervision Propagation for Weakly Supervised Semantic Segmentation on 3D Point Clouds** — Wei *et al.*, IEEE TCSVT 2024. Dense supervision propagation from sparse/weak labels. [arXiv:2107.11267](https://arxiv.org/abs/2107.11267).

- **Weakly Supervised LiDAR Semantic Segmentation via Scatter Image Annotation** — Chen *et al.*, arXiv 2024. Scatter-image labeling assisted by pretrained optical flow + SAM, coupling efficient annotation with training. [arXiv:2404.12861](https://arxiv.org/abs/2404.12861).

- **3D Weakly Supervised Semantic Segmentation via Class-Aware and Geometry-Guided Pseudo-Label Refinement** — Xu *et al.*, arXiv 2025. Class-aware + geometry-prior pseudo-label refinement for 3D WSSS. [arXiv:2510.17875](https://arxiv.org/abs/2510.17875).

## 3. Active learning for 3D segmentation

- **LiDAL: Inter-frame Uncertainty Based Active Learning for 3D LiDAR Semantic Segmentation** — Hu *et al.*, ECCV 2022. Inter-frame prediction divergence as uncertainty to select frames, combined with pseudo-label usage. [arXiv:2211.05997](https://arxiv.org/abs/2211.05997).

- **Active Learning for Point Cloud Semantic Segmentation via Spatial-Structural Diversity Reasoning** — Shao *et al.*, ACM MM 2022. Spatial-structural diversity-driven sample selection. [arXiv:2202.12588](https://arxiv.org/abs/2202.12588).

- **Hierarchical Point-based Active Learning for Semi-supervised Point Cloud Semantic Segmentation** — Xu *et al.*, ICCV 2023. Hierarchical point-level AL + semi-supervised training. [arXiv:2308.11166](https://arxiv.org/abs/2308.11166).

- **SELECT: A Submodular Approach for Active LiDAR Semantic Segmentation** — Mao *et al.*, arXiv 2025. Voxel-level submodular subset selection + MC-Dropout uncertainty + class-balanced submodular maximization; validated on SemanticPOSS / SemanticKITTI / nuScenes. [arXiv:2505.11516](https://arxiv.org/abs/2505.11516).

- **LLM-Guided Taxonomy and Hierarchical Uncertainty for 3D Point Cloud Active Learning** — Li *et al.*, arXiv 2025. LLM-guided class taxonomy + hierarchical uncertainty. [arXiv:2505.18924](https://arxiv.org/abs/2505.18924).

- **Label-Efficient Point Cloud Segmentation with Active Learning** — Meyer *et al.*, arXiv 2025. Label-efficient AL framework for point-cloud segmentation. [arXiv:2512.05759](https://arxiv.org/abs/2512.05759).

- **MILAN: Milli-Annotations for Lidar Semantic Segmentation** — Samet *et al.*, arXiv 2024. Self-supervised representations select the most informative scans, then single-click cluster annotation. [arXiv:2407.15797](https://arxiv.org/abs/2407.15797). Approaches full-supervision performance with only **1/1000** of the point-level labels.

## 4. Self-supervised pre-training (label-free)

*In main list:* Point-M2AE (NeurIPS 2022, [2205.14401](https://arxiv.org/abs/2205.14401)), PointGPT (NeurIPS 2023, [2305.11487](https://arxiv.org/abs/2305.11487)), PonderV2 (CVPR 2024, [2310.08586](https://arxiv.org/abs/2310.08586)) — see [papers.md §5](papers.md).

- **LiMoE: Mixture of LiDAR Representation Learners from Automotive Scenes** — Xu *et al.*, CVPR 2025. MoE over range-image / sparse-voxel / raw-point representations with image-to-LiDAR pre-training; reduces dependence on dense labels. [arXiv:2501.04004](https://arxiv.org/abs/2501.04004) · [Project](https://ldkong.com/LiMoE).

- **Multi-Scale Neighborhood Occupancy Masked Autoencoder for Self-Supervised Learning in LiDAR Point Clouds (NOMAE)** — Abdelsamad *et al.*, arXiv 2025. Masked occupancy reconstruction over non-masked voxel neighborhoods avoids LiDAR-MAE information leakage. [arXiv:2502.20316](https://arxiv.org/abs/2502.20316).

- **GeoMask3D: Geometrically Informed Mask Selection for Self-Supervised Point Cloud Learning in 3D** — Bahri *et al.*, TMLR 2025. Geometry-aware mask selection for self-supervised point-cloud learning. [arXiv:2405.12419](https://arxiv.org/abs/2405.12419).

## 5. Zero-shot / open-vocabulary (label-efficient focus)

*In main list:* OpenScene, CLIP2Scene, PLA, RegionPLC — see [papers.md §5](papers.md).

- **OpenIns3D: Snap and Lookup for 3D Open-vocabulary Instance Segmentation** — Huang *et al.*, ECCV 2024. Two-stage "snap & lookup": 2D open-vocab mask proposals lifted to 3D, matched in 3D feature space — **no 3D training**. [arXiv:2309.00616](https://arxiv.org/abs/2309.00616).

- **3D-AVS: LiDAR-based 3D Auto-Vocabulary Segmentation** — Wei *et al.*, CVPR 2025. **Auto-vocabulary**: generates class vocabularies at runtime without human/text-defined categories; segments all points. [arXiv:2406.09126](https://arxiv.org/abs/2406.09126).

- **OpenUrban3D: Annotation-Free Open-Vocabulary Semantic Segmentation of Large-Scale Urban Point Clouds** — Wang *et al.*, arXiv 2025. Annotation-free open-vocabulary segmentation for large-scale urban scenes without multi-view image alignment. [arXiv:2509.10842](https://arxiv.org/abs/2509.10842).

- **FreeMask3D: Zero-Shot Point Cloud Instance Segmentation Without 3D Training** — Zhou *et al.*, IEEE RA-L 2025. Zero-shot point-cloud instance segmentation without 3D training. [DOI:10.1109/LRA.2025.3621977](https://doi.org/10.1109/LRA.2025.3621977).

- **Affinity3D: Propagating Instance-Level Semantic Affinity for Zero-Shot Point Cloud Segmentation** — ACM MM 2024. Propagates instance-level semantic affinity from 2D foundation models for zero-shot point-cloud segmentation. [DOI:10.1145/3664647.3680651](https://doi.org/10.1145/3664647.3680651).

## 6. Cross-modal distillation (2D/vision → 3D)

*In main list:* 2DPASS (ECCV 2022, [2207.04397](https://arxiv.org/abs/2207.04397)) — see [papers.md §4](papers.md).

- **Fine-grained Image-to-LiDAR Contrastive Distillation with Visual Foundation Models (OLIVINE)** — Zhang *et al.*, NeurIPS 2024. VFM (SAM etc.)-generated labels enable weakly-supervised pixel-point contrastive distillation with von Mises-Fisher losses. [arXiv:2405.14271](https://arxiv.org/abs/2405.14271) · [Code](https://github.com/Eaphan/OLIVINE).

- **Image-to-Lidar Relational Distillation for Autonomous Driving Data** — Mahmoud *et al.*, ECCV 2024. Relational distillation (intra-/cross-modal constraints) aligned to self-similarity, class imbalance, and sparsity of driving data; boosts zero-/few-shot 3D segmentation. [arXiv:2409.00845](https://arxiv.org/abs/2409.00845).

- **2D Feature Distillation for Weakly- and Semi-Supervised 3D Semantic Segmentation** — Unal *et al.*, WACV 2024. Distills pretrained 2D features into 3D segmentation models, cutting 3D labeling needs under weak/semi supervision. [arXiv:2311.15605](https://arxiv.org/abs/2311.15605).

## 7. SAM in 3D (auto-labeling acceleration & 3D segmentation)

- **SA3D: Segment Anything in 3D with Radiance Fields** — Cen *et al.*, NeurIPS 2023. Projects SAM 2D masks into NeRF and iteratively refines 3D masks. [arXiv:2304.12308](https://arxiv.org/abs/2304.12308) · [Project](https://jumpat.github.io/SA3D/).

- **SAM3D: Segment Anything in 3D Scenes** — Yang *et al.*, arXiv 2023. Training-free: SAM masks → 3D projection → bidirectional bottom-up merging across frames. [arXiv:2306.03908](https://arxiv.org/abs/2306.03908). *Note: often mis-cited as CVPR 2024 — that is actually **SAI3D**; SAM3D itself is arXiv-only.*

- **SAGD (a.k.a. "SAM-Gaussians"): Boundary-Enhanced Segment Anything in 3D Gaussian via Gaussian Decomposition** — Hu *et al.*, IEEE TIP 2026 (arXiv 2024). Gaussian decomposition improves boundary segmentation in 3DGS. [arXiv:2401.17857](https://arxiv.org/abs/2401.17857). *Early title was "Segment Anything in 3D Gaussians".*

- **Gaussian Grouping: Segment and Edit Anything in 3D Scenes** — Ye *et al.*, ECCV 2024. Learns grouping features in 3DGS with SAM guidance for open-world 3D segmentation and editing. [arXiv:2312.00732](https://arxiv.org/abs/2312.00732).

- **EgoLifter: Open-world 3D Segmentation for Egocentric Perception** — Gu *et al.*, ECCV 2024. Training-free lifting of SAM masks to 3D for egocentric large scenes. [arXiv:2403.18118](https://arxiv.org/abs/2403.18118).

- **SAGA: Segment Any 3D Gaussians** — Cen *et al.*, AAAI 2025. SAM-based segmentation on 3DGS. [arXiv:2312.00860](https://arxiv.org/abs/2312.00860).

- **SAM4D: Segment Anything in Camera and LiDAR Streams** — Xu *et al.*, ICCV 2025. Zero-shot segmentation on camera + LiDAR streams (autonomous driving, auto-labeling friendly). [arXiv:2506.21547](https://arxiv.org/abs/2506.21547).

- **SAGOnline: Segment Any Gaussians Online** — Sun *et al.*, arXiv 2025. Online Gaussian segmentation for dynamic scenes. [arXiv:2508.08219](https://arxiv.org/abs/2508.08219).

## 8. Auto-labeling & pseudo-labeling

- **Autolabeling 3D Objects with Differentiable Rendering of SDF Shape Priors (SDFLabel)** — Zakharov *et al.*, CVPR 2020. Classic auto-labeling: SDF shape priors + differentiable rendering generate 3D object labels. [arXiv:1911.11288](https://arxiv.org/abs/1911.11288).

- **Segment, Lift and Fit: Automatic 3D Shape Labeling from 2D Prompts (SLF)** — Li *et al.*, ECCV 2024. SAM 2D masks → lifted 3D shapes (not boxes); training-free, cross-dataset generalization for driving auto-labeling. [arXiv:2407.11382](https://arxiv.org/abs/2407.11382).

- **VESPA: Towards un(Human)supervised Open-World Pointcloud Labeling for Autonomous Driving** — Tempfli *et al.*, arXiv 2025. LiDAR geometry + VLM semantics multimodal auto-labeling with open-vocabulary novel-class discovery, no GT/HD map. [arXiv:2507.20397](https://arxiv.org/abs/2507.20397). nuScenes object discovery AP **52.95%**.

- **COARSE: Collaborative Pseudo-Labeling with Coarse Real Labels for Off-Road Semantic Segmentation** — Noca *et al.*, arXiv 2025. Coarse real labels + dense out-of-domain labels via collaborative pseudo-labeling for off-road semi-supervised domain adaptation. [arXiv:2503.03947](https://arxiv.org/abs/2503.03947).

- *Cross-references:* UniLiPs & RePL (§1), MILAN (§3).

## 9. Surveys

- **A Survey of Label-Efficient Deep Learning for 3D Point Clouds** — Xiao *et al.*, IEEE TPAMI 2024. Systematic survey of label-efficient 3D point-cloud learning (weak/semi/self-supervision, active learning, few-shot). [arXiv:2305.19812](https://arxiv.org/abs/2305.19812) · [Resources](https://github.com/xiaoaoran/3D_label_efficient_learning).

- **LiDAR Remote Sensing Meets Weak Supervision: Concepts, Methods, and Perspectives** — Gao *et al.*, arXiv 2025. Weak supervision (sparse point labels etc.) for LiDAR remote sensing. [arXiv:2503.18384](https://arxiv.org/abs/2503.18384).

- **A Review and A Robust Framework of Data-Efficient 3D Scene Parsing with Traditional/Learned 3D Descriptors** — Liu, arXiv 2023. Data-efficient 3D scene parsing survey + robust framework. [arXiv:2312.01262](https://arxiv.org/abs/2312.01262).

## 10. Annotation tools

### Open-source, point-level semantic/instance segmentation

| Tool | Repository | Lang | ~Stars | Notes | Status |
| --- | --- | --- | --- | --- | --- |
| Semantic Segmentation Editor (Hitachi) | [Hitachi-Automotive-And-Industry-Lab/semantic-segmentation-editor](https://github.com/Hitachi-Automotive-And-Industry-Lab/semantic-segmentation-editor) | JavaScript | 2,000 | Web-based (Meteor/React/three.js); **point-level semantic segmentation** on images & `.pcd` point clouds | slowing |
| Xtreme1 | [xtreme1-io/xtreme1](https://github.com/xtreme1-io/xtreme1) | TypeScript | 1,200 | Full-stack multimodal labeling platform (LF AI & Data); 2D/3D **semantic & instance segmentation**, LiDAR-camera fusion, built-in AI pre-labeling (OpenPCDet/AB3DMOT) | active |
| point_labeler (SemanticKITTI) | [jbehley/point_labeler](https://github.com/jbehley/point_labeler) | C++ | 750 | Jens Behley's point-level semantic labeling tool (PCL/Qt); used to annotate **SemanticKITTI itself** | slow |
| interSeg3D-Studio | [zh-plus/interSeg3D-Studio](https://github.com/zh-plus/interSeg3D-Studio) | Python | 10 | Web interactive 3D segmentation labeling; AGILE3D/PinPoint3D click-based segmentation + Gemini recognition | active |
| antsy3d | [alvinwan/antsy3d](https://github.com/alvinwan/antsy3d) | JavaScript | 36 | Browser point-cloud labeling with "fat markers" for instance segmentation | stale |
| L-CAS cloud_annotation_tool | [yzrobot/cloud_annotation_tool](https://github.com/yzrobot/cloud_annotation_tool) | C++ | 290 | Semi-automatic: point clouds pre-clustered into candidates, annotate by cluster id/class/visibility (L-CAS 3D dataset; ROS/PCL) | stale |

### Open-source, bbox-oriented (detection, not segmentation)

| Tool | Repository | Lang | ~Stars | Notes | Status |
| --- | --- | --- | --- | --- | --- |
| SUSTechPOINTS | [naurril/SUSTechPOINTS](https://github.com/naurril/SUSTechPOINTS) | JavaScript | 1,100 | 3D bbox labeling with camera-LiDAR fusion, semi-automatic boxes | active |
| 3D-BAT | [walzimmer/3d-bat](https://github.com/walzimmer/3d-bat) | TypeScript | 800 | 3D bbox + image labeling, tracking, AI-assisted labeling; v2: [walzimmer/bat-3d](https://github.com/walzimmer/bat-3d) | slowing |
| labelCloud | [ch-sa/labelCloud](https://github.com/ch-sa/labelCloud) | Python | 800 | Lightweight 3D bbox labeling with UI & data management | active |
| point-cloud-annotation-tool | [springzfx/point-cloud-annotation-tool](https://github.com/springzfx/point-cloud-annotation-tool) | C++ | 500 | Classic 3D bbox labeling (PCL/Qt) | stale |
| LATTE | [bernwang/latte](https://github.com/bernwang/latte) | Python | 450 | Camera-LiDAR fusion, one-click 3D boxes + tracking ([arXiv:1904.09085](https://arxiv.org/abs/1904.09085)) | stale |
| SAnE | [hasanari/sane](https://github.com/hasanari/sane) | Python | 85 | Smart Annotation and Evaluation (IEEE Access 2020); PointCNN denoising + guided tracking, 4.44× faster | stale |
| ReBound | [ajedgley/ReBound](https://github.com/ajedgley/ReBound) | Python | 30 | LiDAR visualization/labeling designed for **active-learning** sample selection | stale |
| Earthwings/annotate | [Earthwings/annotate](https://github.com/Earthwings/annotate) | C++ | 180 | Creates 3D label boxes (KITTI style) inside RViz | stale |
| rviz_cloud_annotation | [RMonica/rviz_cloud_annotation](https://github.com/RMonica/rviz_cloud_annotation) | C++ | 160 | RViz-based point-cloud annotation plugin | stale |
| caliperai-gt | [caliperai-ai/caliperai-gt](https://github.com/caliperai-ai/caliperai-gt) | TypeScript | 10 | New open-source sensor-fusion labeling platform: LiDAR + camera 3D cuboids | active |

### General platforms with point-cloud support

| Tool | Repository | Lang | ~Stars | Notes |
| --- | --- | --- | --- | --- |
| CloudCompare | [CloudCompare/CloudCompare](https://github.com/CloudCompare/CloudCompare) | C++ | 4,700 | General point-cloud processing; coarse manual segmentation possible, no dedicated labeling pipeline |
| CVAT | [cvat-ai/cvat](https://github.com/cvat-ai/cvat) | Python | 16,500 | General CV annotation platform with 3D cuboids / point annotation |
| Label Studio | [HumanSignal/label-studio](https://github.com/HumanSignal/label-studio) | TypeScript | 28,000 | Multi-type labeling platform with LiDAR 3D cuboid templates |
| OpenLabeling | [Cartucho/OpenLabeling](https://github.com/Cartucho/OpenLabeling) | Python | 960 | ⚠️ 2D only — often mis-listed as 3D; not for point clouds |

### AI-assisted / semi-automatic labeling

- **LabelMaker** — [cvg/LabelMaker](https://github.com/cvg/LabelMaker) — CVPR 2023. SAM + rendered 2D segments **automatically generate 3D semantic labels** for indoor scenes; humans only review/correct.
- **OpenMask3D** — [OpenMask3D/openmask3d](https://github.com/OpenMask3D/openmask3d) — NeurIPS 2023. Open-vocabulary 3D instance masks for pseudo-labeling (ETH Zurich). (Paper also in [papers.md §5](papers.md).)
- **AGILE3D** — [ywyue/AGILE3D](https://github.com/ywyue/AGILE3D) — ICLR 2024. Attention-guided interactive multi-object 3D segmentation via click positive/negative points; core algorithm for semi-automatic labeling.
- **ActiveAnno3D** — [walzimmer/active-anno-3d](https://github.com/walzimmer/active-anno-3d) — IV 2024. Active-learning framework for multimodal 3D detection (entropy-based sample selection; nuScenes / TUM Traffic Intersection).

### Commercial platforms (point-cloud / LiDAR support confirmed)

| Platform | URL | Point-cloud support |
| --- | --- | --- |
| Scale AI | [scale.com](https://scale.com) | ✅ LiDAR & sensor-fusion labeling |
| Segments.ai | [segments.ai](https://segments.ai) | ✅ 3D point-cloud platform, LiDAR semantic segmentation |
| Supervisely | [supervisely.com](https://supervisely.com) | ✅ 3D point-cloud toolbox (episodes, 3D interpolation; open-source core) |
| Labelbox | [labelbox.com](https://labelbox.com) | ✅ 3D point-cloud annotation product |
| Playment | [playment.io](https://playment.io) | ✅ 3D labeling; acquired by TELUS International (2021) |
| Lionbridge | [lionbridge.com](https://www.lionbridge.com) | ✅ Automotive AI data incl. 3D LiDAR labeling |
| Kognic | [kognic.com](https://www.kognic.com) | ✅ Multimodal AD labeling (LiDAR + camera) |
| Lightly | [lightly.ai](https://www.lightly.ai) | 🟡 Active-learning/data curation for images & video; point clouds not confirmed |

### Active-learning frameworks (general)

- **Lightly** — [lightly-ai/lightly](https://github.com/lightly-ai/lightly) — Python, ~3.8k★, active. Self-supervised + active-learning scoring (2D data).
- **modAL** — [modAL-python/modAL](https://github.com/modAL-python/modAL) — Python, ~2.4k★. Modular active-learning framework with rich query strategies.
- **baal** — [baal-org/baal](https://github.com/baal-org/baal) — Python, ~940★, active. Bayesian active learning (MC-Dropout etc.).
- ~~lightning-flash~~ — [Lightning-Universe/lightning-flash](https://github.com/Lightning-Universe/lightning-flash) — **archived** (was PyTorch Lightning's "AI factory" with AL callbacks).

---

## ⚠️ Could not verify

- **WAP (Weakly-supervised Affinity Propagation)** — no matching 3D point-cloud segmentation paper found after multiple search rounds. Closest actual works: *Densify Your Labels* and *Multi-modality Affinity Inference* (AAAI 2024). Do not list "WAP" as-is.
- **ScribbleSup3D** — no such paper; the 3D scribble benchmark is **ScribbleKITTI** (introduced in LaserMix, CVPR 2023).
- **GP-S3Net** — verified as a **fully-supervised** panoptic network (ICCV 2021, [arXiv:2108.08401](https://arxiv.org/abs/2108.08401)), not semi-supervised — excluded from §1.
- **SAM3D venue** — arXiv 2023 only (dblp: CoRR); the CVPR 2024 paper with a similar name is **SAI3D** ("Segment Any Instance in 3D Scenes").
- **SAM-Gaussians** — renamed to **SAGD** (IEEE TIP 2026); listed under §7 as SAGD.
- **ReWiS3D** — verified to be 2D image segmentation (sparse-label WSSS aided by 3D reconstruction), not 3D point-cloud segmentation — excluded.
- **Ant3D / AntLiDAR** — GitHub org `Ant-ML` does not exist; no matching labeling tool.
- **SegAnnot (point-cloud)** — paper widely cited (ICIP 2017) but no public code; the GitHub "segannot" repo is an unrelated R package.
- **LATTE** — the commonly cited `bernii/latte` link is wrong; correct repo is [bernwang/latte](https://github.com/bernwang/latte).
- **Spatial-SAM** — paper claims SAM2-driven 3D labeling but code is "being prepared for release" — not listed.

---

> 🚧 Missing something? Open a PR — see [CONTRIBUTING.md](CONTRIBUTING.md).
