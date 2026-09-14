# 🧊 3D Representations

The latest and most exciting **3D representations** — how 3D data is
parameterized for learning — with a focus on 2023–2026 breakthroughs
(Neural fields → 3D Gaussian Splatting → …) and their use in 3D semantic
segmentation.

> Entries were verified against arXiv / official pages (snapshot: 2026-08).
> *In main list* = already covered in [papers.md](papers.md) / [label-efficient.md](label-efficient.md),
> referenced here without duplication. We prefer fewer, verified entries over
> more, wrong ones.

---

## 1. Point representations

Foundations already in [papers.md](papers.md): **PointNet++** (Qi *et al.*, NeurIPS 2017,
[arXiv:1706.02413](https://arxiv.org/abs/1706.02413)) — hierarchical metric-space
point feature learning; and **Point Transformer V3** (Wu *et al.*, CVPR 2024,
[arXiv:2312.10035](https://arxiv.org/abs/2312.10035)) — serialized grouping
(Z-order/Hilbert) made point transformers as efficient as sparse convs, the
de-facto strongest point backbone since 2024.

- **PointMamba: A Simple State Space Model for Point Cloud Analysis** — Liang *et al.*, NeurIPS 2024. Replaces attention with selective state-space (Mamba) blocks over point sequences; linear complexity with transformer-level point classification / part & scene segmentation. [arXiv:2402.10739](https://arxiv.org/abs/2402.10739) · [Code](https://github.com/LMD0311/PointMamba).
- **MICAS: Multi-grained In-Context Adaptive Sampling for 3D Point Cloud Processing** — Shao *et al.*, CVPR 2025. Dual point-level + prompt-level adaptive sampling for in-context learning on point clouds; better few-shot segmentation / classification with fewer sampled points. [arXiv:2411.16773](https://arxiv.org/abs/2411.16773) · [CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Shao_MICAS_Multi-grained_In-Context_Adaptive_Sampling_for_3D_Point_Cloud_Processing_CVPR_2025_paper.html).

## 2. Voxel / sparse-convolution representations

Foundations already in [papers.md](papers.md): **SparseConvNet** (Graham *et al.*, CVPR 2018,
[arXiv:1711.10275](https://arxiv.org/abs/1711.10275)) and **MinkowskiEngine / 4D Spatio-Temporal
ConvNets** (Choy *et al.*, CVPR 2019, [arXiv:1904.08755](https://arxiv.org/abs/1904.08755)) —
the sparse-voxel-conv engines behind most LiDAR / indoor segmentation baselines.
Point Transformer V3's serialized grouping (see §1) also acts as a sparse-voxel-style
representation for efficiency.

- **SpaCeFormer: Fast Proposal-Free Open-Vocabulary 3D Instance Segmentation** — Lee *et al.*, ICML 2026. Proposal-free open-vocabulary 3D instance segmentation on NVIDIA's next-gen WarpConvNet engine (Warp/TaO-based sparse convolutions replacing the MinkowskiEngine/SparseConvNet stack). [arXiv:2604.20395](https://arxiv.org/abs/2604.20395) · [Project](https://nvlabs.github.io/SpaCeFormer/) · [WarpConvNet](https://github.com/NVlabs/WarpConvNet).

## 3. Mesh representations

- **MeshCNN: A Network with an Edge** — Hanocka *et al.*, ICCV 2019. Edge-based convolution with learned mesh pooling; the foundational learning-on-mesh representation (classification / segmentation on mesh graphs). [arXiv:1809.05910](https://arxiv.org/abs/1809.05910) · [Code](https://github.com/ranahanocka/MeshCNN).
- **MeshAnything: Artist-Created Mesh Generation with Autoregressive Transformers** — Chen *et al.*, ICLR 2025. VQ-VAE mesh tokenization + autoregressive transformer that regenerates any 3D asset as clean, artist-like meshes; a parametric mesh representation for generation. [arXiv:2406.10163](https://arxiv.org/abs/2406.10163) · [Code](https://github.com/buaacyw/MeshAnything).
- **MeshAnything V2: Artist-Created Mesh Generation with Adjacent Mesh Tokenization** — Chen *et al.*, ICCV 2025. Adjacent mesh tokenization (AMT) halves token count, scaling mesh generation past 1,600 faces with artist-preferred topology. [arXiv:2408.02555](https://arxiv.org/abs/2408.02555) · [Code](https://github.com/buaacyw/MeshAnythingV2).

## 4. Implicit neural fields / NeRF

- **NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis** — Mildenhall *et al.*, ECCV 2020. The implicit-field representation: MLP mapping (x, d) → (color, density) with volume rendering. [arXiv:2003.08934](https://arxiv.org/abs/2003.08934) · [Project](https://www.matthewtancik.com/nerf).
- **Instant Neural Graphics Primitives with a Multiresolution Hash Encoding** — Müller *et al.*, ACM TOG (SIGGRAPH) 2022. Multiresolution hash encoding makes implicit fields trainable/renderable in real time. [arXiv:2201.05989](https://arxiv.org/abs/2201.05989) · [Code](https://github.com/NVlabs/instant-ngp).
- **Semantic-NeRF: In-Place Scene Labelling and Understanding with Implicit Scene Representation** — Zhi *et al.*, ICCV 2021 (Oral). Adds a semantic head to NeRF for in-place semantic / instance labelling; the foundational NeRF-for-segmentation work. [arXiv:2103.15875](https://arxiv.org/abs/2103.15875) · [Code](https://github.com/Harry-Zhi/semantic_nerf).
- **OpenObj: Open-Vocabulary Object-Level Neural Radiance Fields with Fine-Grained Understanding** — Deng *et al.*, IEEE RA-L 2025. Distills open-vocabulary 2D features into object-level radiance fields for fine-grained 3D grounding / segmentation queries. [arXiv:2406.08009](https://arxiv.org/abs/2406.08009).
- Note: since 2023–2024 the segmentation-oriented NeRF line has largely been superseded by 3D Gaussian Splatting (SA3D, SAGD etc. are listed in [label-efficient.md](label-efficient.md)); NeRF remains central for generative / geometry-focused implicit fields.

## 5. 3D Gaussian Splatting (the hottest direction)

- **3D Gaussian Splatting for Real-Time Radiance Field Rendering** — Kerbl *et al.*, ACM TOG 42(4) (SIGGRAPH) 2023. Explicit anisotropic 3D Gaussians + tile-based rasterization; the explicit representation that displaced NeRF for reconstruction, and the base of most 2024–2026 segmentation / editing / understanding work. [arXiv:2308.04079](https://arxiv.org/abs/2308.04079) · [Project](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/).
- **4D Gaussian Splatting for Real-Time Dynamic Scene Rendering** — Wu *et al.*, CVPR 2024. Deformation field on top of 3DGS → real-time dynamic-scene (4D) representation. [arXiv:2310.08528](https://arxiv.org/abs/2310.08528) · [Code](https://github.com/hustvl/4DGaussians). (Concurrent line: **Real-time Photorealistic Dynamic Scene Representation with 4D Gaussian Splatting**, Yang *et al.*, ICLR 2024, [arXiv:2310.10642](https://arxiv.org/abs/2310.10642).)
- **Compact 3D Scene Representation via Self-Organizing Gaussian Grids** — Morgenstern *et al.*, ECCV 2024. Self-organizing 2D grid + index maps compress 3DGS parameters >10× with marginal quality loss; a compact Gaussian representation. [arXiv:2312.13299](https://arxiv.org/abs/2312.13299) · [Code](https://github.com/fraunhoferhhi/Self-Organizing-Gaussians).
- **Gaussian Grouping: Segment and Edit Anything in 3D Scenes** — Ye *et al.*, ECCV 2024. *In label-efficient list* — SAM-guided grouping features on Gaussians for open-world segmentation and editing. [arXiv:2312.00732](https://arxiv.org/abs/2312.00732).
- **SAGA: Segment Any 3D Gaussians** — Cen *et al.*, AAAI 2025. *In label-efficient list* — SAM-based zero-shot segmentation of 3DGS scenes. [arXiv:2312.00860](https://arxiv.org/abs/2312.00860).
- **GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting** — Chen *et al.*, CVPR 2024 (note: *not* SIGGRAPH 2024 as sometimes cited). Gaussian semantic tracing + hierarchical attention for controllable 3D editing. [arXiv:2311.14521](https://arxiv.org/abs/2311.14521) · [Code](https://github.com/buaacyw/GaussianEditor).
- **LangSplat: 3D Language Gaussian Splatting** — Qin *et al.*, CVPR 2024 (Highlight). SAM-filtered CLIP language features bound to Gaussians for open-vocabulary 3D queries, ~199× faster than LERF. [arXiv:2312.16084](https://arxiv.org/abs/2312.16084) · [Project](https://langsplat.github.io/).
- **Feature 3DGS: Supercharging 3D Gaussian Splatting to Enable Distilled Feature Fields** — Zhou *et al.*, CVPR 2024 (Highlight). Distills 2D (SAM/CLIP) feature fields into Gaussians without resolution limits, enabling open-vocab / segmentation features on 3DGS. [arXiv:2312.03203](https://arxiv.org/abs/2312.03203) · [Code](https://github.com/ShijieZhou-UCLA/feature-3dgs).
- **OpenGaussian: Towards Point-Level 3D Gaussian-based Open Vocabulary Understanding** — Wu *et al.*, NeurIPS 2024. Point-level SAM features per Gaussian + 2D–3D feature aggregation for point-level open-vocabulary 3D understanding. [arXiv:2406.02058](https://arxiv.org/abs/2406.02058) · [Code](https://github.com/yanmin-wu/OpenGaussian).
- **GARField: Group Anything with Radiance Fields** — Kim *et al.*, CVPR 2024. Learns a scale-conditional affinity field that yields hierarchy-aware 3D groupings (objects ↔ parts) from multi-view images; widely used as a 3DGS grouping / segmentation module. [arXiv:2401.09419](https://arxiv.org/abs/2401.09419) · [Project](https://www.garfield.studio/).
- **Segment then Splat: Unified 3D Open-Vocabulary Segmentation via Gaussian Splatting** — Lu *et al.*, NeurIPS 2025. Feed-forward segment-then-splat pipeline unifying 3D semantic / instance / panoptic open-vocabulary segmentation on 3DGS. [arXiv:2503.22204](https://arxiv.org/abs/2503.22204) · [Code](https://github.com/vulab-AI/Segment-then-Splat).
- **PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting** — Song *et al.*, CVPR 2026. Latest 3DGS-based segmentation: lifts SAM 2D knowledge through 3DGS rendering with semantic consistency, removing the need for dense point-level labels. [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Song_PointGS_Semantic-Consistent_Unsupervised_3D_Point_Cloud_Segmentation_with_3D_Gaussian_CVPR_2026_paper.html).
- **REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting** — Shi *et al.*, CVPR 2026. An MLLM agent grounds reasoning-heavy instructions into 3DGS objects for open-world segmentation + editing. [CVF](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.html) · [arXiv:2510.16410](https://arxiv.org/abs/2510.16410).
- Also in [label-efficient.md](label-efficient.md): **SAGD** (IEEE TIP 2026, arXiv:2401.17857) and **SAGOnline** (arXiv:2508.08219).

## 6. Triplane & hybrid representations

- **EG3D: Efficient Geometry-aware 3D Generative Adversarial Networks** — Chan *et al.*, CVPR 2022. Introduced the triplane representation — three orthogonal 2D feature planes decoded by a lightweight MLP — enabling 3D-consistent GAN generation at 2D-GAN cost. [arXiv:2112.07945](https://arxiv.org/abs/2112.07945) · [Code](https://github.com/NVlabs/eg3d).
- **Triplane Meets Gaussian Splatting: Fast and Generalizable Single-View 3D Reconstruction with Transformers** — Zou *et al.*, CVPR 2024. Hybrid triplane → Gaussian mapping: a transformer turns a single image's triplane into 3D Gaussians for fast generalizable reconstruction. [arXiv:2312.09147](https://arxiv.org/abs/2312.09147) · [Code](https://github.com/VAST-AI-Research/TriplaneGaussian).
- **DirectTriGS: Triplane-based Gaussian Splatting Field Representation for 3D Generation** — Ju *et al.*, CVPR 2025. Direct triplane-parameterized Gaussian-splatting field with a triplane-aware geometry decoder for efficient 3D generation. [arXiv:2503.06900](https://arxiv.org/abs/2503.06900).
- **Hyper3D: Efficient 3D Representation via Hybrid Triplane and Octree Feature** — Guo *et al.*, arXiv 2025. Hybrid triplane + octree feature representation for 3D shape variational auto-encoders (efficient, compact 3D latent). [arXiv:2503.10403](https://arxiv.org/abs/2503.10403).

## 7. Octree / tree-structured representations

- **OctFormer: Octree-based Transformers for 3D Point Clouds** — Wang *et al.*, IEEE TPAMI 2023. Transformer attention defined on octree nodes with ~O(n log n) complexity; scales to large point clouds / multi-resolution features. [arXiv:2305.03045](https://arxiv.org/abs/2305.03045) · [Project](https://wang-ps.github.io/octformer).
- **Octree-GS: Towards Consistent Real-time Rendering with LOD-Structured 3D Gaussians** — Ren *et al.*, IEEE TPAMI 2025 (arXiv 2024). Octree LOD structure guides Gaussian allocation, giving level-of-detail-consistent, memory-friendly real-time rendering with a Gaussian representation. [arXiv:2403.17898](https://arxiv.org/abs/2403.17898) · [Code](https://github.com/city-super/Octree-GS).

## 8. Occupancy representations

Already in [papers.md](papers.md): **Occ3D** (Tian *et al.*, NeurIPS 2023 D&B, [arXiv:2304.14365](https://arxiv.org/abs/2304.14365)) — first large-scale occupancy benchmark (nuScenes-Occ3D) and its metric stack.

- **Scene as Occupancy (OccNet)** — Tong *et al.*, ICCV 2023. Unifies detection / tracking / segmentation into one occupancy representation ("occupancy is all you need"), the basis of the 2023–2025 semantic-occupancy boom. [arXiv:2306.02851](https://arxiv.org/abs/2306.02851) · [Project](https://tsinghua-mars-lab.github.io/OccNet/).
- **FlashOcc: Fast and Memory-Efficient Occupancy Prediction via Channel-to-Height Plugin** — Yu *et al.*, arXiv 2023 (venue unconfirmed — see ⚠️ below). Replaces costly 2D→3D transformer decoders with a channel-to-height plugin; ~2× faster and ~50% less memory than concurrent SOTA with plug-and-play accuracy. [arXiv:2311.12058](https://arxiv.org/abs/2311.12058).
- **Cam4DOcc: Benchmark for Camera-Only 4D Occupancy Forecasting in Autonomous Driving Applications** — Ma *et al.*, CVPR 2024. Extends occupancy to camera-only 4D *forecasting* (current + future frames) with a new benchmark and baselines. [arXiv:2311.17663](https://arxiv.org/abs/2311.17663) · [Code](https://github.com/haomo-ai/Cam4DOcc).
- **GaussianOcc: Fully Self-supervised and Efficient 3D Occupancy Estimation with Gaussian Splatting** — Gan *et al.*, ICCV 2025. Replaces per-scene NeRF optimization with 3DGS rendering supervision for fully self-supervised occupancy from surround cameras. [arXiv:2408.11447](https://arxiv.org/abs/2408.11447) · [Code](https://github.com/GANWANSHUI/GaussianOcc).
- See also **GaussianWorld** (CVPR 2025) in [papers.md](papers.md) for the Gaussian-as-world-model line of occupancy.

## 9. Multi-representation fusion

- **Point-Voxel CNN for Efficient 3D Deep Learning** — Liu *et al.*, NeurIPS 2019 (Spotlight; *not* AAAI 2019 as sometimes cited). PVCNN fuses a voxel-conv branch (efficient) with a point branch (accurate) — the canonical point-voxel hybrid. [arXiv:1907.03739](https://arxiv.org/abs/1907.03739) · [Project](https://hanlab.mit.edu/projects/pvcnn).
- **Searching Efficient 3D Architectures with Sparse Point-Voxel Convolution (SPVNAS)** — Tang *et al.*, ECCV 2020. *In main list* — sparse point-voxel conv + 3D-NAS for efficient LiDAR segmentation. [arXiv:2007.16100](https://arxiv.org/abs/2007.16100).
- **Point Transformer V3** — Wu *et al.*, CVPR 2024. *In main list* — unifies point / voxel / range pipelines behind one serialized-grouping representation; also serves as a multi-representation fusion backbone. [arXiv:2312.10035](https://arxiv.org/abs/2312.10035).
- **LiMoE: Mixture of LiDAR Representation Learners from Automotive Scenes** — Shuai *et al.*, CVPR 2025. Mixture-of-experts routing across multiple LiDAR representation learners (e.g., range/BEV/voxel-style views) improves downstream segmentation. [arXiv:2501.04004](https://arxiv.org/abs/2501.04004).
- Note: the most active 2024–2026 hybrid front is neural-field / Gaussian hybrids — triplane+Gaussian (Triplane Meets GS, DirectTriGS), octree+Gaussian (Octree-GS), triplane+octree (Hyper3D), Gaussian+occupancy (GaussianOcc) — see §5–§8.

## 10. Universal / foundation representations

- **Uni3D: Exploring Unified 3D Representation at Scale** — Zhou *et al.*, ICLR 2024 (Spotlight). A 2D-prompt-encoder + point-encoder trained at 1B-parameter scale yields a universal 3D representation transferring to classification, retrieval and segmentation. [arXiv:2310.06773](https://arxiv.org/abs/2310.06773) · [Code](https://github.com/baaivision/Uni3D).
- **GaussianAnything: Interactive Point Cloud Latent Diffusion for 3D Generation** — Lan *et al.*, ICLR 2025. Surfel-3D-Gaussian representation with native 3D flow-matching / latent diffusion — a candidate *unified Gaussian representation* for generation and downstream tasks. [arXiv:2411.08033](https://arxiv.org/abs/2411.08033).
- **UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting** — Wang *et al.*, CVPR 2025. *In main list* — cross-modal 3DGS-based unified point-cloud pre-training with strong zero-/few-shot transfer. [arXiv:2506.09952](https://arxiv.org/abs/2506.09952).

---

## ⚠️ Could not verify

- **FlashOcc** formal venue (CVPR 2024 claim circulating but no proceedings page found); cited here as arXiv 2023.
- **Segment then Splat** first author given name (surname "Lu" verified via Semantic Scholar / NeurIPS 2025).
- **GARField** underlying representation (3DGS vs NeRF) is not stated unambiguously in public abstracts; contribution phrased representation-agnostically.
- **SpaCeFormer** exact first-author affiliation (POSTECH/NVIDIA); venue ICML 2026 verified via ICML virtual site.
- **MeshAnything V1** venue: ICLR 2025 (verified via OpenReview / GitHub); some indexes still list it as NeurIPS 2024.
