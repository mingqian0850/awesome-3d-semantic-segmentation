# 📄 Papers

A curated list of papers on **3D semantic segmentation**, grouped by
methodological family. Every entry was verified against its arXiv / official
page (title, first author, venue, year, links, representative metrics).

> **Legend.** Metrics are reported as **mIoU** on the dataset and split named
> in the entry (val/test, Area 5 / 6-fold). Official-leaderboard numbers and
> paper-reported numbers are distinguished where it matters. Leaderboard
> snapshots move fast — re-check before citing.

---

## 1. Point-based methods

- **PointNet: Deep Learning on Point Sets for 3D Classification and Segmentation** — Qi *et al.*, CVPR 2017. Shared MLPs + symmetric max-pooling over unordered point sets; the foundation of modern point-cloud learning. [arXiv:1612.00593](https://arxiv.org/abs/1612.00593) · [Project](https://web.stanford.edu/~rqi/pointnet/). S3DIS 6-fold mIoU 47.71.

- **PointNet++: Deep Hierarchical Feature Learning on Point Sets in a Metric Space** — Qi *et al.*, NeurIPS 2017. Hierarchical feature learning via nested metric-space partitioning + recursive PointNet. [arXiv:1706.02413](https://arxiv.org/abs/1706.02413) · [Project](https://stanford.edu/~rqi/pointnet2/).

- **PointCNN: Convolution On X-Transformed Points** — Li *et al.*, NeurIPS 2018. Learned X-Transform re-weights/re-orders neighbor points before convolution. [arXiv:1801.07791](https://arxiv.org/abs/1801.07791). S3DIS 6-fold 65.39; Area-5 57.26.

- **Dynamic Graph CNN for Learning on Point Clouds** — Wang *et al.*, ACM TOG 2019 (38(4):139). EdgeConv: dynamic k-NN graphs rebuilt in feature space each layer. [arXiv:1801.07829](https://arxiv.org/abs/1801.07829) · [Project](https://liuziwei7.github.io/projects/DGCNN). S3DIS 6-fold 56.1.

- **PointConv: Deep Convolutional Networks on 3D Point Clouds** — Wu *et al.*, CVPR 2019. Kernel-density-corrected continuous convolution kernels over non-uniform point clouds. [arXiv:1811.07246](https://arxiv.org/abs/1811.07246). ScanNet benchmark mIoU 55.6.

- **KPConv: Flexible and Deformable Convolution for Point Clouds** — Thomas *et al.*, ICCV 2019. Convolution weights placed directly on kernel points in Euclidean space (deformable variant included). [arXiv:1904.08889](https://arxiv.org/abs/1904.08889) · [Code](https://github.com/HuguesTHOMAS/KPConv). S3DIS Area-5 67.1 (deformable); ScanNet benchmark 68.4.

- **RandLA-Net: Efficient Semantic Segmentation of Large-Scale Point Clouds** — Hu *et al.*, CVPR 2020 (Oral). Random sampling + local feature aggregation (LocSE / attentive pooling / dilated residual blocks); processes millions of points in one forward pass. [arXiv:1911.11236](https://arxiv.org/abs/1911.11236) · [Code](https://github.com/QingyongHu/RandLA-Net). SemanticKITTI 53.9 (online single-scan test track); S3DIS 6-fold 70.0.

- **Point Transformer** — Zhao *et al.*, ICCV 2021. Vector self-attention with position encoding for point clouds. [arXiv:2012.09164](https://arxiv.org/abs/2012.09164). S3DIS Area-5 70.4 / 6-fold 73.5.

- **Point Transformer V2: Grouped Vector Attention and Partition-based Pooling** — Wu *et al.*, NeurIPS 2022. Grouped vector attention + lightweight partition-based pooling for accuracy *and* efficiency. [arXiv:2210.05666](https://arxiv.org/abs/2210.05666) · [Code](https://github.com/Gofinge/PointTransformerV2). ScanNet val 75.4; S3DIS Area-5 71.6.

## 2. Voxel / sparse-convolution methods

- **VoxNet: A 3D Convolutional Neural Network for Real-Time Object Recognition** — Maturana *et al.*, IROS 2015. Early 3D-CNN on voxelized occupancy grids (kept as historical anchor). [CMU page](https://www.ri.cmu.edu/publications/voxnet-a-3d-convolutional-neural-network-for-real-time-object-recognition/).

- **3D Semantic Segmentation with Submanifold Sparse Convolutional Networks** — Graham *et al.*, CVPR 2018. Submanifold sparse convolutions fix the "submanifold dilation" problem of sparse 3D convs. [arXiv:1711.10275](https://arxiv.org/abs/1711.10275) · [Code](https://github.com/facebookresearch/SparseConvNet). ScanNet v2 benchmark (test) 72.5 avg IoU.

- **4D Spatio-Temporal ConvNets: Minkowski Convolutional Neural Networks** — Choy *et al.*, CVPR 2019. The MinkowskiEngine sparse-conv engine + 4D spatio-temporal convs. [arXiv:1904.08755](https://arxiv.org/abs/1904.08755) · [Code](https://github.com/StanfordVL/MinkowskiEngine). ScanNet benchmark (test) 67.9; S3DIS Area 5 65.35 (MinkowskiNet32).

- **Searching Efficient 3D Architectures with Sparse Point-Voxel Convolution** — Tang *et al.*, ECCV 2020. SPVConv (sparse voxel conv + point branch) + 3D-NAS → efficient SPVNAS. [arXiv:2007.16100](https://arxiv.org/abs/2007.16100) · [Project](https://hanlab.mit.edu/projects/spvnas). SemanticKITTI test 66.4 (leaderboard-topping at publication) / val 64.7.

- **Cylindrical and Asymmetrical 3D Convolution Networks for LiDAR Segmentation** — Zhu *et al.*, CVPR 2021 (Oral). Cylinder partition + asymmetric 3D conv + point-wise refinement. [arXiv:2011.10033](https://arxiv.org/abs/2011.10033) · [Code](https://github.com/xinge008/Cylinder3D). SemanticKITTI test 67.8 (TTA) / val 65.9; topped both single/multi-scan leaderboards at publication.

## 3. Projection methods (range image / BEV)

- **RangeNet++: Fast and Accurate LiDAR Semantic Segmentation** — Milioto *et al.*, IROS 2019. Range-image projection + fully-conv net + kNN-based post-processing; the real-time baseline of the range-image line. [Official PDF](https://www.ipb.uni-bonn.de/wp-content/papercite-data/pdf/milioto2019iros.pdf) · [Code](https://github.com/PRBonn/lidar-bonnetal). SemanticKITTI test single-scan 52.2 (with kNN).

- **SqueezeSegV3: Spatially-Adaptive Convolution for Efficient Point-Cloud Segmentation** — Xu *et al.*, ECCV 2020. Spatially-adaptive convolution (SAC) for range-image features. [arXiv:2004.01803](https://arxiv.org/abs/2004.01803) · [Code](https://github.com/chenfengxu714/SqueezeSegV3). SemanticKITTI test single-scan 55.9 (SSGV3-53, kNN) / 52.9 (no kNN).

- **SalsaNext: Fast, Uncertainty-Aware Semantic Segmentation of LiDAR Point Clouds** — Cortinhal *et al.*, ISVC 2020 (Springer LNCS 12509). Dilated-conv residual + pixel-shuffle + Lovász-Softmax + Bayesian uncertainty. [arXiv:2003.03653](https://arxiv.org/abs/2003.03653) · [Code](https://github.com/TiagoCortinhal/SalsaNext). SemanticKITTI test single-scan 59.5 (kNN) / 56.6 (no kNN).

- **CENet: Toward Concise and Efficient LiDAR Semantic Segmentation for Autonomous Driving** — Cheng *et al.*, ICME 2022. Real-time range-image network: large-kernel attention + multi auxiliary heads. [arXiv:2207.12691](https://arxiv.org/abs/2207.12691) · [Code](https://github.com/3DSS-Project/ce_net_ros). SemanticKITTI test 64.7 (64×2048 input, 37.8 FPS); SemanticPOSS val 50.3.

## 4. Transformers & hybrid methods

- **RPVNet: A Deep and Efficient Range-Point-Voxel Fusion Network for LiDAR Point Cloud Segmentation** — Xu *et al.*, ICCV 2021. Range/point/voxel triple-view interaction + gated fusion. [arXiv:2103.12978](https://arxiv.org/abs/2103.12978). SemanticKITTI test 70.3; nuScenes val 77.6.

- **Stratified Transformer for 3D Point Cloud Segmentation** — Lai *et al.*, CVPR 2022. Stratified grouping attention for non-uniform point density. [arXiv:2203.14508](https://arxiv.org/abs/2203.14508) · [Code](https://github.com/dvlab-research/Stratified-Transformer). ScanNet val 74.3 / test 73.7; S3DIS Area-5 72.0.

- **2DPASS: 2D Priors Assisted Semantic Segmentation on LiDAR Point Clouds** — Yan *et al.*, ECCV 2022. Multi-scale knowledge distillation from 2D image priors; point-cloud-only at inference. [arXiv:2207.04397](https://arxiv.org/abs/2207.04397) · [Code](https://github.com/yanx27/2DPASS). SemanticKITTI test 72.9 (val 69.3); nuScenes test 80.8 / val 79.4.

- **Spherical Transformer for LiDAR-based 3D Recognition** (a.k.a. "SphereFormer") — Lai *et al.*, CVPR 2023. Radial window attention in spherical coordinates aggregates distant sparse points directly. [arXiv:2303.12766](https://arxiv.org/abs/2303.12766) · [Code](https://github.com/dvlab-research/SphereFormer). SemanticKITTI test 74.8; nuScenes val 78.4 / test 81.9.

- **Point Transformer V3: Simpler, Faster, Stronger** — Wu *et al.*, CVPR 2024 (Oral). Serialized grouping (Z-order/Hilbert) + neighbor attention makes point transformers as efficient as sparse convs; the de-facto strongest backbone for indoor & outdoor segmentation since 2024. [arXiv:2312.10035](https://arxiv.org/abs/2312.10035) · [Code](https://github.com/Pointcept/PointTransformerV3). Single-dataset from scratch: ScanNet val 77.5 / test 77.9; S3DIS Area-5 73.4 (6-fold 77.7); SemanticKITTI val 70.8 / test 74.2; nuScenes val 80.4 / test 82.7. With multi-dataset Point Prompt Training (PPT): ScanNet 78.6 / 79.4; S3DIS Area-5 74.7 (6-fold 80.8); SemanticKITTI 72.3 / 75.5; nuScenes 81.2 / 83.0.

- **Towards Large-scale 3D Representation Learning with Multi-dataset Point Prompt Training (PPT)** — Wu *et al.*, CVPR 2024. Cross-dataset / cross-task universal point-cloud representations via prompt training (official PTv3 companion). [CVF OpenAccess](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_Towards_Large-scale_3D_Representation_Learning_with_Multi-dataset_Point_Prompt_Training_CVPR_2024_paper.html). PTv3+PPT: ScanNet val 78.5 (8-frame).

- **OneFormer3D: One Transformer for Unified Point Cloud Segmentation** — Kolodiazhnyi *et al.*, CVPR 2024. A single transformer unifying semantic / instance / panoptic segmentation. [CVPR page](https://mlanthology.org/cvpr/2024/kolodiazhnyi2024cvpr-oneformer3d/) · [Poster](https://cvpr.thecvf.com/virtual/2024/poster/30040).

- **Multi-Space Alignments Towards Universal LiDAR Segmentation (MSA)** — Liu *et al.*, CVPR 2024. Cross-dataset universal LiDAR segmentation via multi-space (BEV/range/view) alignment. [CVPR page](https://mlanthology.org/cvpr/2024/liu2024cvpr-multispace/).

- **RAPiD-Seg: Range-Aware Pointwise Distance Distribution Networks for 3D LiDAR Segmentation** — ECCV 2024. Range-aware pointwise distance distributions reduce sensitivity to point density. [Poster](https://eccv2024.ecva.net/virtual/2024/poster/887) · [arXiv:2407.10159](https://arxiv.org/abs/2407.10159).

- **CamPoint: Boosting Point Cloud Segmentation with Virtual Camera** — Zhang *et al.*, CVPR 2025. Learnable "virtual camera" as point-grouping parameterization; better accuracy and training efficiency. [CVF OpenAccess](https://openaccess.thecvf.com//content/CVPR2025/html/Zhang_CamPoint_Boosting_Point_Cloud_Segmentation_with_Virtual_Camera_CVPR_2025_paper.html).

## 5. Self-supervised, zero-shot & open-vocabulary methods, foundation models

- **Point-M2AE: Multi-scale Masked Autoencoders for Hierarchical Point Cloud Pre-training** — Zhang *et al.*, NeurIPS 2022. Masked-autoencoder pre-training on a hierarchical point transformer. [arXiv:2205.14401](https://arxiv.org/abs/2205.14401). Evaluated on classification / few-shot.

- **OpenScene: 3D Scene Understanding with Open Vocabularies** — Peng *et al.*, CVPR 2023. Distills 2D CLIP features into 3D points for zero-shot open-vocabulary scene understanding. [arXiv:2211.15654](https://arxiv.org/abs/2211.15654) · [Project](https://pengsongyou.github.io/openscene) · [Code](https://github.com/pengsongyou/openscene). Zero-shot mIoU: ScanNet val 47.5, nuScenes val 42.1, Matterport3D test 42.6.

- **PLA: Language-Driven Open-Vocabulary 3D Scene Understanding** — Ding *et al.*, CVPR 2023. Region-level point-language association with dense-caption prompts for open-vocabulary 3D semantic/instance segmentation. [arXiv:2211.16312](https://arxiv.org/abs/2211.16312) · [Code](https://github.com/CVMI-Lab/PLA). ScanNet val (zero-shot): hIoU 65.3, novel-class mIoU 62.4.

- **ULIP: Learning a Unified Representation of Language, Images, and Point Clouds for 3D Understanding** — Xue *et al.*, CVPR 2023. Image-bridged tri-modal contrastive pre-training (language–image–point). [arXiv:2212.05171](https://arxiv.org/abs/2212.05171) · [Code](https://github.com/salesforce/ULIP). Zero-/few-shot classification benchmarks.

- **CLIP2Scene: Towards Label-efficient 3D Scene Understanding by CLIP** — Chen *et al.*, CVPR 2023. CLIP knowledge distilled into 3D networks with cross-modal & spatio-temporal consistency + self-training. [arXiv:2301.04926](https://arxiv.org/abs/2301.04926). nuScenes val: 1% labels 56.3 / 100% 71.5; SemanticKITTI val: 1% 42.6 / 100% 55.0; zero-shot nuScenes 20.8.

- **ConceptFusion: Open-set Multimodal 3D Mapping** — Jatavallabhula *et al.*, RSS 2023. Open-set 3D semantic maps from pre-trained vision-language features. [arXiv:2302.07241](https://arxiv.org/abs/2302.07241) · [Code](https://github.com/concept-fusion/concept-fusion). Replica open-vocab f-mIoU 38.70 (w/ SAM).

- **PointGPT: Auto-regressively Generative Pre-training from Point Clouds** — Chen *et al.*, NeurIPS 2023. Point clouds as token sequences for autoregressive generative pre-training. [arXiv:2305.11487](https://arxiv.org/abs/2305.11487). Classification / few-shot.

- **OpenMask3D: Open-Vocabulary 3D Instance Segmentation** — Takmaz *et al.*, NeurIPS 2023. Class-agnostic 3D instance masks + multi-view fused CLIP features. [arXiv:2306.13631](https://arxiv.org/abs/2306.13631). ScanNet200 val: AP 15.4 / AP50 19.9 / AP25 23.1.

- **RegionPLC: Regional Point-Language Contrastive Learning for Open-World 3D Scene Understanding** — Yang *et al.*, CVPR 2024 (arXiv 2023). Regional point-language contrastive learning + open-vocabulary expansion. [arXiv:2304.00962](https://arxiv.org/abs/2304.00962). ScanNet val zero-shot: hIoU 69.4, novel-class mIoU 70.7.

- **SegPoint: Segment Any Point Cloud via Large Language Model** — He *et al.*, ECCV 2024. LLM-unified instruction/reference-driven point-cloud segmentation. [arXiv:2407.13761](https://arxiv.org/abs/2407.13761) · [Code](https://github.com/heshuting555/SegPoint).

- **Point-GCC: Universal Self-supervised 3D Scene Pre-training via Geometry-Color Contrast** — Fan *et al.*, ACM MM 2024. Geometry–color contrastive pre-training generalizing to segmentation/detection/classification. [arXiv:2305.19623](https://arxiv.org/abs/2305.19623) · [ACM DL](https://dl.acm.org/doi/10.1145/3664647.3681343).

- **PonderV2: Pave the Way for 3D Foundation Model with A Universal Pre-training Paradigm** — Yang *et al.*, arXiv 2023/24 (preprint). 3D-occupancy-prediction-based universal pre-training boosting 20+ downstream datasets. [arXiv:2310.08586](https://arxiv.org/abs/2310.08586) · [Weights](https://huggingface.co/HaoyiZhu/PonderV2).

- **Point-MoE: Large-Scale Multi-Dataset Training with Mixture-of-Experts for 3D Semantic Segmentation** — UvA CV Lab, arXiv 2025. MoE training across datasets for cross-domain generalization at scale. [arXiv:2505.23926](https://arxiv.org/abs/2505.23926) · [Project](https://uva-computer-vision-lab.github.io/point-moe/).

- **SAS: Segment Any 3D Scene with Integrated 2D Priors** — arXiv 2025. Zero-shot 3D scene segmentation with integrated 2D priors; competitive vs fully-supervised & zero-shot methods on ScanNet/Matterport/nuScenes. [arXiv:2503.08512](https://arxiv.org/abs/2503.08512).

- **UniPre3D: Unified Pre-training of 3D Point Cloud Models with Cross-Modal Gaussian Splatting** — Wang *et al.*, CVPR 2025. Cross-modal 3DGS-based unified point-cloud pre-training; strong zero-/few-shot transfer. [arXiv:2506.09952](https://arxiv.org/abs/2506.09952) · [CVF](https://openaccess.thecvf.com//content/CVPR2025/html/Wang_UniPre3D_Unified_Pre-training_of_3D_Point_Cloud_Models_with_Cross-Modal_CVPR_2025_paper.html).

- **AIDE: Improving 3D Open-Vocabulary Semantic Segmentation by Aligned Vision-Language Learning** — Wang *et al.*, WACV 2025. Aligned vision-language learning for open-vocabulary 3D semantic segmentation (2D-3D distillation). [CVF](https://www.openaccess.thecvf.com/content/WACV2025/html/Wang_AIDE_Improving_3D_Open-Vocabulary_Semantic_Segmentation_by_Aligned_Vision-Language_Learning_WACV_2025_paper.html).

- **Masked Point-Entity Contrast for Open-Vocabulary 3D Scene Understanding** — Wang *et al.*, CVPR 2025. Masked point-entity contrastive learning (BIGAI). [CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Masked_Point-Entity_Contrast_for_Open-Vocabulary_3D_Scene_Understanding_CVPR_2025_paper.html).

- **HB-Mamba: Hierarchical Bi-directional State Space Modeling for LiDAR Semantic Segmentation in Autonomous Driving** — ACM MM 2025. Mamba-based bidirectional hierarchical modeling; surpasses PTv3 (82.7) on the official nuScenes test leaderboard. [ACM DL](https://dl.acm.org/doi/10.1145/3805622.3810584).

## 6. LLM + 3D understanding (adjacent topic)

- **3D-LLM: Injecting the 3D World into Large Language Models** — Hong *et al.*, NeurIPS 2023 (Spotlight). Injects 3D scenes (multi-view + point clouds + 3D features) into LLMs for unified 3D QA / grounding / description. [arXiv:2307.12981](https://arxiv.org/abs/2307.12981) · [Code](https://github.com/Km3888/3D-LLM).

- **PointLLM: Empowering Large Language Models to Understand Point Clouds** — Xu *et al.*, ECCV 2024 (arXiv 2023). First point-cloud + multi-view 3D dialogue model. [arXiv:2308.16911](https://arxiv.org/abs/2308.16911) · [Code](https://github.com/InternRobotics/PointLLM).

- **LL3DA: Visual Interactive Instruction Tuning for Omni-3D Understanding, Reasoning, and Planning** — Chen *et al.*, CVPR 2024. Omni-3D instruction-tuned model with point/box "visual interaction" prompts. [CVF](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_LL3DA_Visual_Interactive_Instruction_Tuning_for_Omni-3D_Understanding_Reasoning_and_CVPR_2024_paper.html) · [arXiv:2311.18651](https://arxiv.org/abs/2311.18651).

- **Chat-Scene: Bridging 3D Scene and Large Language Models with Object Identifiers** — Zhu *et al.*, NeurIPS 2024. Object identifiers bridge 3D scenes and LLMs for object-level referring & dialogue. [NeurIPS 2024](https://papers.nips.cc/paper_files/paper/2024/hash/cebbd24f1e50bcb63d015611fe0fe767-Abstract-Conference.html).

- **SceneVerse: Scaling 3D Vision-Language Learning for Grounded Scene Understanding** — Jia *et al.*, ECCV 2024. Million-scale 3D scene-language pre-training data + baselines (BIGAI). [Code](https://github.com/bigai-ai/SceneVerse) · [ECVA](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1407_ECCV_2024_paper.php).

- **GPT4Scene: Understand 3D Scenes from Videos with Vision-Language Models** — Zhang *et al.*, arXiv 2025. Reconstructs 3D scene graphs from video and injects them into VLMs; improves ScanNet/Matterport scene understanding & QA. [arXiv:2501.01428](https://arxiv.org/abs/2501.01428).

## 7. 3D occupancy prediction (adjacent topic)

- **Occ3D: A Large-Scale 3D Occupancy Prediction Benchmark for Autonomous Driving** — Tian *et al.*, NeurIPS 2023 (Datasets & Benchmarks). First large-scale multimodal 3D occupancy benchmark (nuScenes-Occ3D) with metrics. [arXiv:2304.14365](https://arxiv.org/abs/2304.14365) · [Code](https://github.com/Tsinghua-MARS-Lab/Occ3D).

- **OpenOccupancy: A Large Scale Benchmark for Surrounding Semantic Occupancy Perception** — Wang *et al.*, ICCV 2023. Dense 3D semantic-occupancy annotations + efficient SSC baselines. [arXiv:2303.03991](https://arxiv.org/abs/2303.03991) · [Code](https://github.com/lzhbrian/OpenOccupancy).

- **SurroundOcc: Multi-Camera 3D Occupancy Prediction for Autonomous Driving** — Wei *et al.*, ICCV 2023. Dense multi-camera 3D occupancy prediction with multi-frame aggregation. [arXiv:2303.09551](https://arxiv.org/abs/2303.09551).

- **OccNet: Scene as Occupancy** — Ma *et al.*, ICCV 2023. Unifies reconstruction / segmentation / motion prediction through a 3D-occupancy representation. [arXiv:2306.02851](https://arxiv.org/abs/2306.02851) · [Code](https://github.com/collector-m/OccNet).

- **OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving** — Zheng *et al.*, ECCV 2024. Occupancy world model that autoregressively predicts future occupancy & trajectories. [Code](https://github.com/wzzheng/OccWorld) · [ECCV](https://mlanthology.org/eccv/2024/zheng2024eccv-occworld/).

- **OccSora: 4D Occupancy Generation Models as World Simulators for Autonomous Driving** — Zheng *et al.*, arXiv 2024. Occupancy tokenizer + diffusion transformer generating 4D occupancy. [arXiv:2405.20337](https://arxiv.org/abs/2405.20337).

- **GaussianWorld: Gaussian World Model for Streaming 3D Occupancy Prediction** — Zuo *et al.*, CVPR 2025. 3D Gaussian Splatting world model for streaming occupancy prediction + reconstruction. [CVF](https://openaccess.thecvf.com//content/CVPR2025/html/Zuo_GaussianWorld_Gaussian_World_Model_for_Streaming_3D_Occupancy_Prediction_CVPR_2025_paper.html) · [Code](https://github.com/zuosc19/GaussianWorld).

- **COME: Adding Scene-Centric Forecasting Control to Occupancy World Model** — Shi *et al.*, NeurIPS 2025. Adds scene-centric forecasting control (intervenable occupancy prediction) to occupancy world models. [NeurIPS 2025](https://neurips.cc/virtual/2025/loc/san-diego/poster/119126).

- **A Survey on Occupancy Perception for Autonomous Driving: The Information Fusion Perspective** — Xu *et al.*, Information Fusion 2025. Occupancy-perception survey from the information-fusion perspective + resource list. [Resources](https://github.com/HuaiyuanXu/3D-Occupancy-Perception).

## 8. Notable challenge winners

- **Point Transformer V3 Extreme: 1st Place Solution for 2024 Waymo Open Dataset Challenge in Semantic Segmentation** — Wu *et al.*, arXiv 2024. Ultra-large-scale PTv3 training variant; **1st place** in the 2024 Waymo semantic-segmentation challenge. [arXiv:2407.15282](https://arxiv.org/abs/2407.15282) · [Challenge](https://waymo.com/open/challenges/2024/3d-semantic-segmentation/).

- **vFusedSeg3D: 3rd Place Solution for 2024 Waymo Open Dataset Challenge in Semantic Segmentation** — arXiv 2024. View-based fusion of LiDAR and camera (vision) features for 3D semantic segmentation. [arXiv:2408.15254](https://arxiv.org/abs/2408.15254).

---

## Verification notes

- **PTv3 is CVPR 2024 (Oral)** — often mis-cited as NeurIPS 2023.
- **RPVNet is ICCV 2021** (arXiv:2103.12978), **2DPASS is ECCV 2022**, **CENet is ICME 2022**, **SalsaNext is ISVC 2020** (not IEEE IV).
- **"SphereFormer"** official title is *Spherical Transformer for LiDAR-based 3D Recognition* (CVPR 2023, arXiv:2303.12766).
- **SPVNAS** official title is *Searching Efficient 3D Architectures with Sparse Point-Voxel Convolution* (arXiv:2007.16100).
- **"SEAL"**: we could not verify a matching 3D segmentation paper named "SEAL" (the only hit is a self-supervised *embodied active learning* work, NeurIPS 2021 — different direction) — deliberately excluded. Verify before adding.
- **"SegFormer3D"** (point-cloud version) and **"Point Transformer V4"** could not be verified to exist — not included.
- **OccWorld is ECCV 2024** (not CVPR); **Occ3D is NeurIPS 2023 D&B**.
- Point Transformer (ICCV'21) official repo is no longer accessible; maintained implementations: [POSTECH-CVLab/point-transformer](https://github.com/POSTECH-CVLab/point-transformer) and [lucidrains/point-transformer-pytorch](https://github.com/lucidrains/point-transformer-pytorch).

> 🚧 Missing something? Open a PR — see [CONTRIBUTING.md](CONTRIBUTING.md). We prefer *fewer, but verified* entries over *more, but wrong* ones.
