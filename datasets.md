# 🗂️ Datasets

Datasets for 3D semantic segmentation, grouped by acquisition modality.
Each entry: **name** — year · modality · scale · classes · one-liner · official
link · license (when known).

> Entries were verified against official pages / papers. Facts that could not
> be confirmed are marked *unconfirmed* rather than guessed.

---

## Indoor (RGB-D / LiDAR scans)

- **ScanNet** — 2017. RGB-D video (depth camera + surface reconstruction); 1,513 scans / ~2.5M views; 20 classes (semantic segmentation benchmark). Large-scale RGB-D indoor dataset with camera poses, reconstructions, and instance-level semantic labels. [Official](https://www.scan-net.org/) · Paper: Dai *et al.*, CVPR 2017 ([arXiv](https://arxiv.org/abs/1702.04405)). License: ScanNet Terms of Use (data).

- **ScanNet++** — 2023. LiDAR + 33MP DSLR + iPhone RGB-D (multimodal); 460 scenes in paper (v2 site shows 1,000+); 100 classes (top-100 benchmark). Sub-millimeter high-fidelity indoor scans with long-tailed semantic labels. [Site](https://kaldir.vc.in.tum.de/scannetpp/) · [GitHub](https://github.com/scannetpp/scannetpp) · Paper: Yeshwanth *et al.*, ICCV 2023 ([arXiv](https://arxiv.org/abs/2308.11417)). License: ScanNet++ Terms of Use.

- **S3DIS (Stanford Large-Scale 3D Indoor Spaces)** — 2016. RGB-D (Matterport panoramas; per-point labeled point clouds/meshes); 6 areas (3 buildings), 271 rooms; 13 classes. The classic large-scale indoor point-wise parsing dataset. [Official](http://buildingparser.stanford.edu/dataset.html) · Paper: Armeni *et al.*, CVPR 2016 ([open access](https://openaccess.thecvf.com/content_cvpr_2016/html/Armeni_3D_Semantic_Parsing_CVPR_2016_paper.html)). License: Stanford data license agreement.

- **Matterport3D** — 2017. RGB-D panoramas (Matterport camera); 10,800 panoramas / 194,400 RGB-D images / 90 building-scale scenes; 40 classes. [Official](https://niessner.github.io/Matterport/) · Paper: Chang *et al.*, 3DV 2017 ([arXiv](https://arxiv.org/abs/1709.06158)). License: Terms of Use (non-commercial research).

- **2D-3D-S (Stanford 2D-3D-Semantics)** — 2017. Multi-view RGB-D (Matterport; aligned 2D/2.5D/3D); 6 areas (>6,000 m²) / 70,496 RGB + 1,413 panoramas / ~696M points; 13 classes. Multimodal alignment of RGB, depth, normals, XYZ, and semantics. [Project](http://3Dsemantics.stanford.edu) · [GitHub](https://github.com/alexsax/2D-3D-Semantics) · Paper: Armeni *et al.*, CVPR 2017 ([arXiv](https://arxiv.org/abs/1702.01105)). License: Stanford data license agreement.

- **3RScan** — 2019. RGB-D (Tango device; repeated scans over time); 1,482 scans / 478 changing indoor environments; instance-level semantic labels (class count *unconfirmed*). For long-term SLAM, scene change detection, and object re-localization. [GitHub](https://github.com/WaldJohannaU/3RScan) · Paper: Wald *et al.*, ICCV 2019 ([arXiv](https://arxiv.org/abs/1908.06109)).

- **Structured3D** — 2020. Synthetic (professional interior designs rendered to panoramas/perspectives); 3,500 scenes / 21,835 rooms / 196,515 images; 40 classes (NYU40). Photo-realistic synthetic indoor dataset with rich 3D structural annotations. [Official](https://structured3d-dataset.org/) · Paper: Zheng *et al.*, ECCV 2020 ([arXiv](https://arxiv.org/abs/1908.00222)). License: Terms of Use (research only).

- **ARKitScenes** — 2021. Mobile RGB-D (iPad Pro LiDAR) + static laser scans; 5,047 captures / 1,661 unique scenes; 17 classes (oriented 3D boxes of furniture). First mobile RGB-D indoor dataset from widely available consumer LiDAR. [GitHub](https://github.com/apple/ARKitScenes) · Paper: Baruch *et al.*, NeurIPS 2021 D&B ([arXiv](https://arxiv.org/abs/2111.08897)). License: Apple custom (non-commercial).

---

## Outdoor LiDAR (autonomous driving)

- **SemanticKITTI** — 2019. 64-beam LiDAR (Velodyne HDL-64E); 22 sequences (~43.5k frames; 23,201 train / 20,351 test); ~4.5B points; 28 labeled classes (19 used for the benchmark). Per-point labeled 360° LiDAR sequences — *the* de-facto outdoor LiDAR benchmark. [Official](https://www.semantic-kitti.org) · Paper: Behley *et al.*, ICCV 2019 (extended IJRR 2021). License: CC BY-NC-SA.

- **KITTI-360** — 2022. HDL-64E + SICK LMS-200 pushbroom + fisheye/stereo cameras + IMU/GPS; 9 sequences / 73.7 km / 100k laser scans / 320k+ images; 19 classes for evaluation. KITTI successor with 2D/3D semantic & instance labels. [Official](https://www.cvlibs.net/datasets/kitti-360/) · Paper: Liao, Xie & Geiger, TPAMI 2022 ([arXiv:2109.13410](https://arxiv.org/abs/2109.13410)). License: CC BY-NC-SA 3.0.

- **nuScenes / nuScenes-lidarseg** — 2019 / 2020 (lidarseg). 32-beam LiDAR + 6 cameras + 5 radars; 1,000 scenes (20 s each; 700/150/150); lidarseg covers all scenes with 1.4B+ labeled points; 32 classes. One of the largest open LiDAR segmentation datasets. [Official](https://www.nuscenes.org) · Paper: Caesar *et al.*, CVPR 2020 ([arXiv:1903.11027](https://arxiv.org/abs/1903.11027)); lidarseg: Fong *et al.*, RA-L 2022 ([arXiv:2109.03805](https://arxiv.org/abs/2109.03805)). License: CC BY-NC-SA 4.0 (free for academic).

- **Waymo Open Dataset** — 2019 (3D semantic labels + challenge since 2022). 5 LiDARs + 5 cameras; 1,150 segments (20 s each; 798 train / 150 val / 202 test, ~230k frames); 23 classes for segmentation. [Official](https://waymo.com/open) · Paper: Sun *et al.*, CVPR 2020 ([arXiv:1912.04838](https://arxiv.org/abs/1912.04838)). License: non-commercial (code Apache-2.0). *Note: some community conversions use the 798/202/150 split (e.g., SphereFormer).*

- **SemanticPOSS** — 2020. Hesai Pandora 40-beam LiDAR + 4 wide-angle cameras; 2,988 frames / 216M points; 14 classes. Campus scenes (PKU) with many dynamic instances; SemanticKITTI-compatible format. [Official](http://www.poss.pku.edu.cn/semanticposs.html) · Paper: Pan *et al.*, IEEE IV 2020 ([arXiv:2002.09147](https://arxiv.org/abs/2002.09147)). License: CC BY-NC-SA 3.0.

- **Paris-Lille-3D** — 2018. Velodyne HDL-32E mobile laser scanning; ~2 km / 2,479 frames / ~143M labeled points; 50 annotated classes (10 commonly used). Urban MLS point clouds of Paris & Lille for large-scene segmentation. [Official](https://npm3d.fr/paris-lille-3d) · Paper: Roynard *et al.*, IJRR 2018 ([arXiv:1712.00032](https://arxiv.org/abs/1712.00032)). License: CC-BY-NC-ND-3.0.

- **Toronto-3D** — 2020. Vehicle-mounted MLS; ~1 km / 78.3M points; 8 classes (+unclassified). Toronto urban road MLS data with RGB & intensity. [GitHub](https://github.com/WeikaiTan/Toronto-3D) · Paper: Tan *et al.*, CVPRW 2020 ([Open Access](https://openaccess.thecvf.com/content_CVPRW_2020/html/w11/Tan_Toronto-3D_A_Large-Scale_Mobile_LiDAR_Dataset_for_Semantic_Segmentation_of_CVPRW_2020_paper.html)).

- **PandaSet** — 2020. Pandar64 + PandarGT + 6 cameras + GPS/IMU; 100+ scenes (8 s each) / 16,000+ LiDAR frames; 28 classes (boxes) / 37 classes (segmentation). Hesai & Scale AI open dataset. [Official](https://pandaset.org) · Paper: Xiao *et al.*, IEEE ITSC 2021 ([arXiv:2112.12610](https://arxiv.org/abs/2112.12610)). License: free for academic & commercial use.

- **HELIXNet** — 2022. Stereopolis II MLS LiDAR sequences (per-point timestamps, sensor rotation); 20 sequences / 78k rotations / 8.85B labeled points; 9 classes; 6 cities. Built for online (real-time) LiDAR semantic segmentation evaluation. [Official](https://romainloiseau.fr/helixnet/) · [GitHub](https://github.com/romainloiseau/HelixNet) · [Zenodo](https://zenodo.org/record/6519817) · Paper: Loiseau *et al.*, ECCV 2022 ([arXiv:2206.08194](https://arxiv.org/abs/2206.08194)). License: CC BY 4.0.

- **Argoverse 2** — 2021. **Not suitable for 3D semantic segmentation**: the Sensor dataset has only 3D bounding boxes; the Lidar dataset (20k × 30 s) has no labels. Verified and deliberately excluded.

---

## Aerial / urban mobile mapping

- **Semantic3D** — 2017. Terrestrial laser scanning (TLS); 4B+ manually labeled points; 8 classes. Outdoor large-scene point-cloud classification/segmentation benchmark (churches, streets, rail, squares, villages, soccer fields, castles). [Official](https://www.semantic3d.net/) (site currently offline) · Paper: Hackel *et al.*, ISPRS Annals 2017 ([arXiv:1704.03847](https://arxiv.org/abs/1704.03847)).

- **SensatUrban** — 2021 (CVPR) / 2022 (IJCV). Aerial photogrammetric (UAV multi-view dense reconstruction) point clouds; ~3B points, 3 UK cities, ~7.6 km²; 13 classes. City-scale photogrammetric segmentation. [GitHub](https://github.com/QingyongHu/SensatUrban) · Paper: Hu *et al.*, CVPR 2021 ([arXiv:2009.03137](https://arxiv.org/abs/2009.03137); IJCV [arXiv:2201.04494](https://arxiv.org/abs/2201.04494)). *Note: README says ~3B points / 2 cities / ~6 km² vs paper's 3 cities / 7.6 km².*

- **DALES (Dayton Annotated LiDAR Earth Scan)** — 2020. Aerial LiDAR (Dayton, Ohio); ~505M points, 10 km², 40 scenes; 8 classes (ground/vegetation/cars/trucks/powerlines/fences/poles/buildings). [Paper (CVPRW)](https://www.openaccess.thecvf.com/content_CVPRW_2020/html/w11/Varney_DALES_A_Large-Scale_Aerial_LiDAR_Data_Set_for_Semantic_Segmentation_CVPRW_2020_paper.html) · [arXiv:2004.11985](https://arxiv.org/abs/2004.11985).

- **Hessigheim 3D (H3D)** — 2021. UAV LiDAR + Multi-View-Stereo point clouds and textured meshes; 4 epochs (2016/2018/2019), ~800 pts/m²; 11 classes. Multi-temporal high-res urban benchmark (Hessigheim, Germany). [Benchmark](https://ifpwww.ifp.uni-stuttgart.de/benchmark/hessigheim/Default.aspx) · Paper: Kölle *et al.*, ISPRS Open Journal 2021 ([arXiv:2102.05346](https://arxiv.org/abs/2102.05346)).

- **DublinCity** — 2019. Aerial LiDAR (ALS); 260M+ points of Dublin city center; 13 classes (hierarchical: building/vegetation/ground → window/door/tree). First city-scale dense aerial LiDAR semantic benchmark. [V-SENSE](https://v-sense.scss.tcd.ie/dublincity/) · Paper: Zolanvari *et al.*, BMVC 2019 ([arXiv:1909.03613](https://arxiv.org/abs/1909.03613)).

---

## RGB-D

- **NYUv2 (NYU Depth V2)** — 2012. RGB-D (Kinect v1); 1,449 densely labeled pairs / 464 scenes / 407k unlabeled frames; 40 classes (NYU40). The classic indoor RGB-D dataset. [Official](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html) · Paper: Silberman *et al.*, ECCV 2012.

- **SUN RGB-D** — 2015. RGB-D (4 sensors: Kinect v1/v2, RealSense, Xtion); 10,335 RGB-D images; 37 classes (+unknown). Multi-task RGB-D benchmark suite (segmentation, detection, layout). [Official](https://3dvision.princeton.edu/projects/2015/SUNrgbd/) · Paper: Song *et al.*, CVPR 2015 ([open access](https://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Song_SUN_RGB-D_A_2015_CVPR_paper.html)).

---

## Synthetic

- **Structured3D** — 2020. Synthetic indoor (see Indoor section). [Official](https://structured3d-dataset.org/) · [GitHub](https://github.com/manycore-research/Structured3D) · Paper: Zheng *et al.*, ECCV 2020 ([arXiv:1908.00222](https://arxiv.org/abs/1908.00222)). License: Terms of Use (research only).

- **BlenderProc** — 2019. Procedural synthetic-data generation pipeline (not a fixed-size dataset); outputs semantic/instance segmentation, depth, normals. [GitHub](https://github.com/DLR-RM/BlenderProc) · Paper: Denninger *et al.*, 2019 ([arXiv:1911.01911](https://arxiv.org/abs/1911.01911)). *Note: "BlenderProc4BGL" does not exist; the official companion dataset is BlenderProc4BOP (6D pose estimation, not segmentation).*

- **SYNTHIA** — 2016. Synthetic virtual city (Unity); RAND-CITYSCAPES subset (~9,400 frames, *partially confirmed*); 13 classes (Cityscapes-aligned). Street-scene synthetic imagery with semantic + depth labels. [Official](https://synthia-dataset.net/) · Paper: Ros *et al.*, CVPR 2016 ([CVF](https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Ros_The_SYNTHIA_Dataset_CVPR_2016_paper.html)).

- **SUNCG** — 2017 (note). 3D semantic annotations for 45,622 indoor scenes (per-object semantic categories); distribution stopped after 2019 (legal dispute). [CVF](https://www.openaccess.thecvf.com/content_cvpr_2017/html/Song_Semantic_Scene_Completion_CVPR_2017_paper.html).

- **SceneNet RGB-D** — 2017 (note). 5M synthetic indoor images with rendered depth and per-pixel semantic labels ("perfect ground truth"). [Project](https://robotvault.bitbucket.io/scenenet-rgbd.html) · Paper: McCormac *et al.*, ICCV 2017 ([CVF](https://openaccess.thecvf.com/content_iccv_2017/html/McCormac_SceneNet_RGB-D_Can_ICCV_2017_paper.html)).

---

> 🚧 Missing a dataset? Open a PR — see [CONTRIBUTING.md](CONTRIBUTING.md).
