# 🛠️ Open-Source Projects

Frameworks, toolkits, and official implementations for 3D semantic
segmentation. Star counts are **approximate** (verified via GitHub); check the
repositories for current status.

---

## Frameworks & general-purpose toolkits

| Name | Repository | Lang | ~Stars | One-liner | Status |
| --- | --- | --- | --- | --- | --- |
| Open3D-ML | [isl-org/Open3D-ML](https://github.com/isl-org/Open3D-ML) | Python | 2,300 | Official Open3D ML extension with RandLA-Net, KPConv, and SemanticKITTI/S3DIS support | active |
| Pointcept | [Pointcept/Pointcept](https://github.com/Pointcept/Pointcept) | Python | 3,200 | Point-cloud perception research codebase integrating PTv1/v2/v3, SphereFormer, and many SOTA models | very active |
| mmdetection3d | [open-mmlab/mmdetection3d](https://github.com/open-mmlab/mmdetection3d) | Python | 6,500 | OpenMMLab 3D perception platform (detection-first; includes PointNet++/MinkUNet segmentation) | slowing |
| OpenPCDet | [open-mmlab/OpenPCDet](https://github.com/open-mmlab/OpenPCDet) | Python | 5,700 | LiDAR 3D detection toolbox (*adjacent* — detection, not segmentation) | active |
| Paddle3D | [PaddlePaddle/Paddle3D](https://github.com/PaddlePaddle/Paddle3D) | Python | 640 | Baidu PaddlePaddle 3D vision toolkit (point-cloud detection & segmentation) | active |
| MinkowskiEngine | [NVIDIA/MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine) | Python | 3,000 | High-dimensional sparse-tensor autodiff library; basis of MinkUNet & sparse-conv segmentation | slowing |
| SparseConvNet | [facebookresearch/SparseConvNet](https://github.com/facebookresearch/SparseConvNet) | C++ | 2,100 | Submanifold sparse convolutional networks (classic implementation) | archived |
| spconv | [traveller59/spconv](https://github.com/traveller59/spconv) | Python | 2,300 | Sparse convolution library powering many LiDAR detection/segmentation models | active |
| torchsparse (TorchSparse / TorchSparse++) | [mit-han-lab/torchsparse](https://github.com/mit-han-lab/torchsparse) | Cuda | 1,500 | TorchSparse (MLSys'22) + TorchSparse++ (MICRO'23); *no separate "torchsparse2" repo exists* | active |
| Open3D | [isl-org/Open3D](https://github.com/isl-org/Open3D) | C++ | 13,900 | Modern 3D data processing library (point clouds, geometry, visualization) | very active |
| PDAL | [PDAL/PDAL](https://github.com/PDAL/PDAL) | C++ | 1,400 | Point-cloud data abstraction library ("the GDAL of point clouds") | very active |
| CloudCompare | [CloudCompare/CloudCompare](https://github.com/CloudCompare/CloudCompare) | C++ | 4,700 | 3D point-cloud viewer / processing / annotation desktop software | very active |

## Official implementations of landmark papers

| Name | Repository | Lang | ~Stars | One-liner | Status |
| --- | --- | --- | --- | --- | --- |
| PointNet++ | [charlesq34/pointnet2](https://github.com/charlesq34/pointnet2) | Python | 3,700 | Official PointNet++ implementation; the classic baseline | stale |
| KPConv | [HuguesTHOMAS/KPConv](https://github.com/HuguesTHOMAS/KPConv) | Python | 780 | Official Kernel Point Convolutions implementation | stale |
| RandLA-Net | [QingyongHu/RandLA-Net](https://github.com/QingyongHu/RandLA-Net) | Python (TF) | 1,600 | Official RandLA-Net (CVPR'20 Oral / TPAMI) | stale |
| Point Transformer V2 | [Pointcept/PointTransformerV2](https://github.com/Pointcept/PointTransformerV2) | Python | 440 | Official PTv2 (NeurIPS'22) | stale |
| Point Transformer V3 | [Pointcept/PointTransformerV3](https://github.com/Pointcept/PointTransformerV3) | Python | 1,900 | Official PTv3 (CVPR'24 Oral); also integrated in Pointcept | active |
| Cylinder3D | [xinge008/Cylinder3D](https://github.com/xinge008/Cylinder3D) | Python | 960 | Official Cylinder3D (CVPR'21 Oral; once #1 on SemanticKITTI) | stale |
| SphereFormer | [JIA-Lab-research/SphereFormer](https://github.com/JIA-Lab-research/SphereFormer) | Python | 370 | Official SphereFormer (CVPR'23; redirected from dvlab-research) | stale |
| 2DPASS | [yanx27/2DPASS](https://github.com/yanx27/2DPASS) | Python | 470 | Official 2DPASS (ECCV'22; 2D-prior-assisted LiDAR segmentation). *Ignore the 0-star [callzhang/2DPASS](https://github.com/callzhang/2DPASS) placeholder* | stale |
| OpenScene | [pengsongyou/openscene](https://github.com/pengsongyou/openscene) | Python | 850 | Official OpenScene (CVPR'23; open-vocabulary 3D scene understanding) | stale |
| PLA / RegionPLC | [CVMI-Lab/PLA](https://github.com/CVMI-Lab/PLA) | Python | 300 | Official PLA (CVPR'23) + RegionPLC (CVPR'24) | stale |
| SegPoint | [heshuting555/SegPoint](https://github.com/heshuting555/SegPoint) | Python | 40 | Official SegPoint (ECCV'24; LLM-guided point-cloud segmentation) | stale |
| ConceptFusion | [concept-fusion/concept-fusion](https://github.com/concept-fusion/concept-fusion) | Python | 240 | Official ConceptFusion (RSS'23; open-set multimodal 3D mapping) | stale |

> **Note on Point Transformer (ICCV'21)**: the commonly cited official repo
> (`Point-Transformers/Point-Transformers`) is no longer accessible (404).
> Maintained implementations: [POSTECH-CVLab/point-transformer](https://github.com/POSTECH-CVLab/point-transformer) and
> [lucidrains/point-transformer-pytorch](https://github.com/lucidrains/point-transformer-pytorch);
> PTv1 is also integrated in [Pointcept](https://github.com/Pointcept/Pointcept).

## Foundation models & LLM-based projects

| Name | Repository | Lang | ~Stars | One-liner | Status |
| --- | --- | --- | --- | --- | --- |
| PointLLM | [InternRobotics/PointLLM](https://github.com/InternRobotics/PointLLM) | Python | 1,000 | Point-cloud LLM (ECCV'24 Best Paper candidate; TPAMI'25) | active |
| GPT4Point | [Pointcept/GPT4Point](https://github.com/Pointcept/GPT4Point) | Python | 440 | Unified point-language understanding & generation framework (CVPR'24 Highlight) | stale |
| ULIP | [salesforce/ULIP](https://github.com/salesforce/ULIP) | Python | 610 | Language-image-point unified representation pre-training (CVPR'23) | archived |
| Point-M2AE | [ZrrSkywalker/Point-M2AE](https://github.com/ZrrSkywalker/Point-M2AE) | Python | 230 | Multi-scale masked-autoencoder point-cloud pre-training (NeurIPS'22) | stale |
| SOLE | [CVRP-SOLE/SOLE](https://github.com/CVRP-SOLE/SOLE) | Python | — | "Segment any 3D Object with Language" (ICLR'25) | — |

## 3D occupancy

| Name | Repository | Lang | ~Stars | One-liner | Status |
| --- | --- | --- | --- | --- | --- |
| OpenOccupancy | [lzhbrian/OpenOccupancy](https://github.com/lzhbrian/OpenOccupancy) | Python | ~1* | Surrounding semantic-occupancy benchmark (ICCV'23) official code. *Star count looks reset after repo migration — URL/README confirm it's official* | stale |
| Occ3D | [Tsinghua-MARS-Lab/Occ3D](https://github.com/Tsinghua-MARS-Lab/Occ3D) | Python | 570 | Occ3D large-scale 3D occupancy benchmark & toolkit (NeurIPS'23 D&B) | stale |
| OccWorld | [wzzheng/OccWorld](https://github.com/wzzheng/OccWorld) | Python | 580 | 3D occupancy world model (ECCV'24) | stale |

## Data & evaluation toolkits

| Name | Repository | Lang | ~Stars | One-liner | Status |
| --- | --- | --- | --- | --- | --- |
| semantic-kitti-api | [PRBonn/semantic-kitti-api](https://github.com/PRBonn/semantic-kitti-api) | Python | 900 | Official SemanticKITTI API: visualization, processing, evaluation | active |
| waymo-open-dataset | [waymo-research/waymo-open-dataset](https://github.com/waymo-research/waymo-open-dataset) | Python | 3,400 | Official Waymo Open Dataset tools | active |
| nuscenes-devkit | [nutonomy/nuscenes-devkit](https://github.com/nutonomy/nuscenes-devkit) | Python | 2,800 | Official nuScenes devkit | active |

---

> 🚧 Missing a project? Open a PR — see [CONTRIBUTING.md](CONTRIBUTING.md).
