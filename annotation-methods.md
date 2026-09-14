# ✍️ 3D Data Annotation Methods

The latest and most exciting **methods for annotating 3D data** — how to label
point clouds / LiDAR scenes faster, cheaper, and more automatically
(interactive segmentation, SAM/LLM-assisted auto-labeling, auto-labeling
pipelines, active-learning annotation, labeling protocols).

> Entries were verified against arXiv / dblp / Crossref / CVF (snapshot:
> 2026-08). This file focuses on *labeling itself*; learning algorithms that
> need fewer labels (semi/weakly-supervised, distillation) live in
> [label-efficient.md](label-efficient.md). Entries *in other list* are
> referenced without duplication. We prefer fewer, verified entries over more,
> wrong ones.

---

## 1. Interactive point-cloud segmentation labeling

**Foundations**
- **AGILE3D: Attention Guided Interactive Multi-object 3D Segmentation** — Yue *et al.*, ICLR 2024. Attention-based model for *simultaneous* interactive segmentation of multiple 3D objects from positive/negative clicks — one click can correct several objects at once, making it a ready semi-automatic labeling engine. [arXiv:2306.00977](https://arxiv.org/abs/2306.00977) · [Project](https://ywyue.github.io/AGILE3D/) · [Code](https://github.com/ywyue/AGILE3D). *Also listed as a tool in [label-efficient.md §10](label-efficient.md).*

- **iSeg: Interactive 3D Segmentation via Interactive Attention** — Lang *et al.*, SIGGRAPH Asia 2024. Interactive-attention network for click-driven 3D segmentation, applicable to meshes, point clouds and scans. [arXiv:2404.03219](https://arxiv.org/abs/2404.03219) · [Project](https://threedle.github.io/iSeg/).

**2024–2026**
- **S²AM3D: Scale-controllable Part Segmentation of 3D Point Clouds** — Su *et al.*, CVPR 2026 (Oral). One prompt point plus a **continuous slider** controls segmentation granularity (whole object ↔ fine parts), trained with 2D-3D hybrid supervision — a scale-controllable interactive labeling primitive. [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Su_S2AM3D_Scale-controllable_Part_Segmentation_of_3D_Point_Clouds_CVPR_2026_paper.html). *Also in [papers.md §9](papers.md).*

- **PinPoint3D: Fine-Grained 3D Part Segmentation from a Few Clicks** — Zhang *et al.*, arXiv 2025. Two-level forward mask-prediction architecture that outputs object-level *and* part-level masks from a few user clicks — fine-grained interactive part labeling. [arXiv:2509.25970](https://arxiv.org/abs/2509.25970).

- **ClickSeg3D: Few-Click Interactive Segmentation via Semantic Embeddings** — Kang *et al.*, arXiv 2026. Few-click interactive 3D segmentation guided by semantic embeddings to propagate click information. [arXiv:2605.08925](https://arxiv.org/abs/2605.08925).

- **iClickSeg: Interactive Click Segmentation for Zero-Shot Cross-Category 3D Part Segmentation** — Yi *et al.*, Pattern Recognition 2026. Zero-shot cross-category click-based part labeling, generalizing categories never seen during training. [DOI:10.1016/j.patcog.2025.112816](https://doi.org/10.1016/j.patcog.2025.112816).

---

## 2. SAM / foundation-model-driven 3D auto-labeling

*Cross-referenced from [label-efficient.md §7](label-efficient.md) (no duplication):* **LabelMaker** (CVPR 2023), **SA3D** (NeurIPS 2023), **SAM3D** (arXiv 2023), **SAGD / SAM-Gaussians** (IEEE TIP 2026), **Gaussian Grouping** (ECCV 2024), **EgoLifter** (ECCV 2024), **SAGA** (AAAI 2025), **SAM4D** (ICCV 2025, camera+LiDAR streams — the video/stream-driven entry), **SAGOnline** (arXiv 2025).

**2024–2026**
- **Segment3D: Learning Fine-Grained Class-Agnostic 3D Segmentation without Manual Labels** — Huang *et al.*, ECCV 2024. Uses 2D image-segmentation foundation models (SAM) to automatically generate 3D training labels and builds a large auto-annotated class-agnostic dataset — no manual 3D labels required. [arXiv:2312.17232](https://arxiv.org/abs/2312.17232) · [Project](https://segment3d.github.io/).

- **Better Call SAL: Towards Learning to Segment Anything in Lidar** — Ošep *et al.*, arXiv 2024 (NVIDIA). Foundation model for LiDAR instance segmentation trained from automatically generated labels (2D foundation-model masks + temporal aggregation) — an auto-labeling loop for LiDAR. [arXiv:2403.13129](https://arxiv.org/abs/2403.13129).

- **SAM2Point: Segment Any 3D as Videos in Zero-shot and Promptable Manners** — Guo *et al.*, arXiv 2024. Treats point clouds / 3DGS scenes as videos and runs SAM 2 in a promptable, zero-shot way — a reusable promptable auto-labeling backbone. [arXiv:2408.16768](https://arxiv.org/abs/2408.16768).

- **Zero-Shot 4D Lidar Panoptic Segmentation** — Zhang *et al.*, CVPR 2025. Zero-shot 4D LiDAR panoptic segmentation via vision foundation models plus temporal clustering — label-free annotation of LiDAR streams. [arXiv:2504.00848](https://arxiv.org/abs/2504.00848).

- **RangeSAM: On the Potential of Visual Foundation Models for Range-View represented LiDAR segmentation** — Kühn *et al.*, WACV 2026 Workshops (FoMoV). Systematic study of applying SAM/SAM2-style visual foundation models directly to range-view LiDAR — evidence for foundation-model reuse in LiDAR labeling. [arXiv:2509.15886](https://arxiv.org/abs/2509.15886).

- **Leveraging Foundation Models for Labeling Custom Object Masks in LiDAR Point Cloud Sequences** — Prutsch *et al.*, ECMR 2025. Foundation-model-driven labeling of user-defined (custom) object masks across LiDAR sequences. [DOI:10.1109/ECMR65884.2025.11163318](https://doi.org/10.1109/ECMR65884.2025.11163318).

---

## 3. LLM / MLLM-assisted 3D labeling

- **AutoOcc: Automatic Open-Ended Semantic Occupancy Annotation via Vision-Language Guided Gaussian Splatting** — Zhou *et al.*, ICCV 2025. Vision-language guidance plus 3DGS to automatically generate *open-ended* (class-agnostic, expandable vocabulary) semantic occupancy labels for driving scenes. [arXiv:2502.04981](https://arxiv.org/abs/2502.04981).

- **LPL3D: LVLM-Driven Pseudo-Labeling for 3D Object Detection** — Li *et al.*, IEEE TCSVT 2026. Large vision-language model generates and refines pseudo-labels for 3D object detection. [DOI:10.1109/TCSVT.2025.3616500](https://doi.org/10.1109/TCSVT.2025.3616500).

- *Cross-references:* **VESPA** (VLM + LiDAR geometry open-world auto-labeling, [label-efficient.md §8](label-efficient.md)); **LLM-Guided Taxonomy and Hierarchical Uncertainty for 3D Point Cloud Active Learning** (LLM-guided sampling, [label-efficient.md §3](label-efficient.md)).

---

## 4. Auto-labeling pipelines

*Cross-referenced from [label-efficient.md §8](label-efficient.md) (no duplication):* **SDFLabel** (CVPR 2020, SDF shape priors + differentiable rendering), **SLF** (ECCV 2024, SAM 2D masks → lifted 3D shapes), **VESPA** (arXiv 2025), **COARSE** (arXiv 2025).

**2024–2026**
- **OpenBox: Annotate Any Bounding Boxes in 3D** — Lee *et al.*, NeurIPS 2025. Two-stage automatic 3D bounding-box annotation pipeline built on a 2D vision foundation model: unsupervised, open-vocabulary 3D box labeling with instance association — detection-grade auto-labeling for driving data. [arXiv:2512.01352](https://arxiv.org/abs/2512.01352).

---

## 5. Active-learning annotation frameworks

*Cross-referenced from [label-efficient.md §3](label-efficient.md) (no duplication):* **LiDAL** (ECCV 2022), **Spatial-Structural Diversity Reasoning** (ACM MM 2022), **Hierarchical Point-based AL** (ICCV 2023), **MILAN** (arXiv 2024), **SELECT** (arXiv 2025, submodular/diversity), **LLM-Guided Taxonomy and Hierarchical Uncertainty** (arXiv 2025), **Label-Efficient Point Cloud Segmentation with Active Learning** (arXiv 2025), plus the **ActiveAnno3D** tool ([label-efficient.md §10](label-efficient.md)).

**2024–2026**
- **BUMP: A Boundary-Aware Active Learning Framework for Point Cloud Semantic Segmentation** — Zhang *et al.*, ICDIP 2025 (SPIE). Boundary-aware sampling that prioritizes points near class boundaries where errors concentrate. [DOI:10.1117/12.3073283](https://doi.org/10.1117/12.3073283).

- **Inconsistency-Aware Active Learning for Semi-supervised 3D Point Cloud Semantic Segmentation** — Xu *et al.*, IEEE TMM 2026. Selects samples by prediction inconsistency within a semi-supervised active-learning framework. [DOI:10.1109/TMM.2026.3687738](https://doi.org/10.1109/TMM.2026.3687738).

---

## 6. Labeling protocols & granularity studies

- **Scribble-Supervised LiDAR Semantic Segmentation (ScribbleKITTI)** — Unal *et al.*, CVPR 2022 (Oral). Introduces **ScribbleKITTI**, the first scribble-annotated LiDAR benchmark: scribble strokes reach up to **95.7% of fully-supervised performance with only 8% labeled points** on SemanticKITTI. [arXiv:2203.08537](https://arxiv.org/abs/2203.08537) · [Code](https://github.com/LeonRuddat/scribblekitti). *Note: ScribbleKITTI was introduced here — see the ⚠️ correction below about [label-efficient.md](label-efficient.md).*

- **One Class One Click: Quasi Scene-level Weakly Supervised Point Cloud Semantic Segmentation with Active Learning** — Wang *et al.*, arXiv 2022. One click per class per scene — a quasi-scene-level protocol combined with active learning, quantifying the annotation budget of scene-level vs. dense labels. [arXiv:2211.12657](https://arxiv.org/abs/2211.12657).

- **Rewis3d: Reconstruction Improves Weakly-Supervised Semantic Segmentation** — Ernst *et al.*, CVPR 2026. Uses 3D reconstruction to densify and improve weak supervision (scribbles / scene-level / sparse labels) for segmentation. [arXiv:2603.06374](https://arxiv.org/abs/2603.06374).

- **Weakly Supervised Segmentation on Outdoor 4D Point Clouds With Progressive 4D Grouping** — Shi *et al.*, IEEE TPAMI 2025. Progressive 4D grouping lets sparse weak labels supervise dense outdoor LiDAR sequences. [DOI:10.1109/TPAMI.2025.3532284](https://doi.org/10.1109/TPAMI.2025.3532284).

---

## 7. Reconstruction-assisted labeling (NeRF / 3DGS)

*Cross-referenced from [label-efficient.md §7](label-efficient.md) (no duplication):* **SAGA** (AAAI 2025), **Gaussian Grouping** (ECCV 2024), **SAGOnline** (arXiv 2025); **AutoOcc** (ICCV 2025) lives in §3 above.

**2024–2026**
- **GaussianCut: Interactive Segmentation via Graph Cut for 3D Gaussian Splatting** — Jain *et al.*, NeurIPS 2024. A few user clicks + graph cut over 3DGS yields interactive multiview object segmentation — segmentation labels propagated across views. [arXiv:2411.07555](https://arxiv.org/abs/2411.07555).

- **iSegMan: Interactive Segment-and-Manipulate 3D Gaussians** — Zhao *et al.*, CVPR 2025. Click/text-driven interactive segmentation of 3DGS scenes, then manipulation — interactive object-level labeling in reconstructed scenes. [arXiv:2505.11934](https://arxiv.org/abs/2505.11934).

- **PanopticNeRF-360: Panoramic 3D-to-2D Label Transfer in Urban Scenes** — Fu *et al.*, IEEE TPAMI 2025. NeRF-based panoramic 3D-to-2D label transfer: annotate once in 3D, propagate dense labels to all views. [arXiv:2309.10815](https://arxiv.org/abs/2309.10815) · [DOI:10.1109/TPAMI.2025.3581608](https://doi.org/10.1109/TPAMI.2025.3581608).

---

## 8. Data engines & large-scale auto-labeling

- **SALT: A Flexible Semi-Automatic Labeling Tool for General LiDAR Point Clouds with Cross-Scene Adaptability and 4D Consistency** — Wang *et al.*, arXiv 2025. Semi-automatic LiDAR labeling tool with cross-scene adaptability and 4D (spatio-temporal) label consistency. [arXiv:2503.23980](https://arxiv.org/abs/2503.23980).

- **From Binary to Semantic: Utilizing Large-Scale Binary Occupancy Data for 3D Semantic Occupancy Prediction** — Noguchi *et al.*, ICCV 2025 Workshops (ECLR). Reuses automatically produced large-scale *binary* occupancy as a label engine to train *semantic* occupancy prediction. [arXiv:2507.13387](https://arxiv.org/abs/2507.13387).

- **An Auto-Labeling Tool for Occupancy Grid and BEV in Autonomous Driving Dataset** — Bea *et al.*, IEEE SMC 2025. Automated tooling for occupancy-grid and BEV labels in AV datasets. [DOI:10.1109/SMC58881.2025.11343566](https://doi.org/10.1109/SMC58881.2025.11343566).

- **Semi-Automated Data Annotation in Multisensor Datasets for Autonomous Vehicle Testing** — Gamalii *et al.*, arXiv 2025. Semi-automated annotation workflows across camera + LiDAR multisensor AV datasets. [arXiv:2512.24896](https://arxiv.org/abs/2512.24896).

- *Cross-references:* **Segment3D**'s auto-annotated class-agnostic dataset (§2 above); **OpenBox** (NeurIPS 2025) in §4.

---

## ⚠️ Could not verify

- **GaussianLabeler** — searched multiple rounds (arXiv / ICLR); no paper with this exact title/venue could be confirmed. Closest verified MLLM+3DGS annotation work is **AutoOcc** (ICCV 2025, §3); **LabelGS** (arXiv:2508.19699) exists but is label-aware GS *segmentation*, not annotation. Likely a misremembered title.
- **GS-Annotator** — could not locate any paper, tool, or project with this name.
- **Interactive3D: Segment Anything in 3D with Gaussians** — could not confirm; the CVPR 2024 **Interactive3D** is an unrelated 3D *generation* paper (arXiv:2404.16510).
- **Correction for [label-efficient.md](label-efficient.md) §1**: its LaserMix (CVPR 2023) entry says it "introduces the ScribbleKITTI scribble-label benchmark" — ScribbleKITTI was actually introduced by **Unal *et al.*, CVPR 2022** ([arXiv:2203.08537](https://arxiv.org/abs/2203.08537)); LaserMix only reuses it as a benchmark.
