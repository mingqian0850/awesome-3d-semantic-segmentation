# 3D 点云语义分割的自动化与 Agent 化现状调研笔记

> 调研时间:2026 年(以检索到的资料为准);目的:为"3D 语义分割(3DSS)作为 agent 环境的可行性对比报告"收集素材。
> 方法:web_search 多轮(中英文)+ 直接抓取 GitHub raw README / 官方页面 / arXiv API 验证。
> 原则:**查不到的明确写"未找到公开资料",每条关键信息附来源 URL。**

---

## A. 3D 点云 / LiDAR 语义分割的自动化与 agent 化工作

### A1. LLM agent 驱动的点云模型训练 / 调参 / 架构搜索 —— 未找到直接命中

**核心结论:未找到公开资料表明存在专门针对"点云/LiDAR 语义分割模型训练、调参、架构搜索"的 LLM agent 工作。** 点云领域的 LLM agent 集中在"推理/分析/交互式分割"而非"训练自动化";"训练自动化"侧的 LLM agent 是通用 ML 的,未见 3DSS 落地。

**点云领域已存在的 LLM agent(推理/分析型,非训练型):**

- **LiDARAgent**(pkurelab,北大):面向生态遥感 LiDAR 点云的智能体框架。微调 LLM 作核心推理引擎 + MCP 协议连接外部点云处理工具,实现"知识理解—任务规划—工具调用—结果反馈"流程,支持森林点云结构参数提取、生态指标计算、领域知识问答等。**是"点云分析 agent",不是"训练/调参 agent"。**
  - 来源:https://github.com/pkurelab/LiDARAgent/blob/main/README.md
- **REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting**(CVPR 2026):基于 3DGS 的开放世界 3D 推理分割/编辑的 MLLM-agent 框架(推理期交互,非训练自动化)。
  - 来源:https://www.openaccess.thecvf.com/content/CVPR2026/html/Shi_REALM_An_MLLM-Agent_Framework_for_Open_World_3D_Reasoning_Segmentation_CVPR_2026_paper.html
- **LLM-Supervised Point Cloud Processing: From Unsupervised 3D Scene-Graph Generation to Interactive Scene Manipulation**(ISPRS Annals):用 LLM 监督/驱动无监督 3D 场景图生成与交互式点云操作。
  - 来源:https://isprs-archives.copernicus.org/articles/XLIX-B2-2026/1311/2026/
- 其他 LLM 参与 3D 分割(推理/提示型,非训练自动化):SegPoint(Segment Any Point Cloud via LLM, Mendeley 条目 https://www.mendeley.com/catalogue/921a85f9-2979-3987-8c8a-496548ee014b/)、Point Linguist Model(https://huggingface.co/papers/2509.07825)、Generalized Few-Shot Point Cloud Segmentation via LLM-Assisted Hyper-Relation Matching(https://ieeexplore.ieee.org/document/11445002)。

**通用 LLM agent / AutoML(可迁移到 3D 但未见 3DSS 专用落地):**

- **AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML**(ICML 2025):多 agent LLM 完成数据→模型→训练→评估全流程 AutoML。
  - 来源:https://github.com/deepauto-ai/automl-agent
- **MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation**(ICML 2024,Stanford):LLM agent 自主做 ML 实验(改代码、调参、训练、评估)的基准;任务含 CV 分类/回归等,**未包含 3D 点云分割任务**。
  - 来源:https://arxiv.org/abs/2310.03302 ; https://github.com/snap-stanford/MLAgentBench
- **ML-Bench**(gersteinlab):评估 LLM/agent 在仓库级 ML 任务(读 README/改代码/跑实验)上的能力。
  - 来源:https://github.com/gersteinlab/ML-Bench ; https://arxiv.org/abs/2311.09835
- **MARS: Modular Agent with Reflective Search for Automated AI Research**(论文笔记):模块化反思搜索式 AI 研究 agent。
  - 来源:https://en.papernotes.org/ICML2026/code_intelligence/mars_modular_agent_with_reflective_search_for_automated_ai_research/
- **KompeteAI**(arXiv 2508.10177):多 agent 端到端生成 ML pipeline。
  - 来源:https://ar5iv.labs.arxiv.org/html/2508.10177
- LLM 驱动的 NAS 范式(通用背景):**Graph Neural Architecture Search with GPT-4**(arXiv 2310.01436,https://arxiv.org/abs/2310.01436);**Can GPT-4 Perform Neural Architecture Search?**(arXiv 2402.18443,https://arxiv.org/abs/2402.18443)。**均非点云/3D 专用。**

### A2. 点云 NAS(neural architecture search)

- **Point-NAS: A Novel Neural Architecture Search Framework for Point Cloud Analysis**(IEEE TIP 2023):点云分析的 NAS 框架(面向分类/分割网络的结构搜索)。
  - 来源:https://ieeexplore.ieee.org/document/10318065 ; https://www.semanticscholar.org/paper/3fd5eb3097e2d59c5b5aee1dcae64ae18a5a56b7
- **Auto-Points: Automatic Learning for Point Cloud Analysis With Neural Architecture Search**(IEEE TMM 2023,Wang/Xie):点云分析的自动学习(NAS 自动搜索网络结构)。
  - 来源:https://ieeexplore.ieee.org/document/10223431 ; https://www.semanticscholar.org/paper/e69ceecbe0bc2c24d68e616104df2de183f59a6f
- 要点:点云 NAS 工作数量少、年份偏早(2023),且为传统 NAS(进化/权重共享类),**未发现与 LLM/agent 结合的版本**;后续主流转向"预训练大模型/基础模型"(见 A3),NAS 在 3DSS 领域基本停滞。

### A3. self-supervised + self-training 自动标注闭环(可用于分割模型持续改进)

- **PiSA(Point-Self-Augmented)**:CUHK-SZ 李镇团队联合 CUHK、UCD 发布;**"self-augmented 数据引擎"三阶段闭环**:① 3D MLLM 直接在点云上自动标注(不经过 2D 渲染,保留深度/空间几何)→ ② 2D MLLM(Qwen2-VL-72B)对 12 视角渲染做跨模态校验精修 → ③ 用上一轮生成数据训练下一轮模型,迭代自增强("data-model 共演化"、数据质量随训练提升)。附带 PointLLM-PiSA 模型与 PiSA-Bench 评测基准。**面向 3D MLLM 理解(描述/分类)而非语义分割,但"生成-校验-重训"闭环机制可直接借鉴到 3DSS。**
  - 来源:https://arxiv.org/pdf/2503.10529 ; https://github.com/CG-ops/PiSA ; 官方介绍 https://itso.cuhk.edu.cn/en/article/522
- **One Thing One Click: A Self-Training Approach for Weakly Supervised 3D Semantic Segmentation**(CVPR 2021):每类点一次 + self-training 的弱监督 3D 语义分割,**是 3DSS 上最直接的伪标签自训练工作**。
  - 来源:https://arxiv.org/abs/2104.02246 ; https://openaccess.thecvf.com/content/CVPR2021/html/Liu_One_Thing_One_Click_A_Self-Training_Approach_for_Weakly_Supervised_CVPR_2021_paper.html
- **无监督域自适应(UDA)中的伪标签自训练闭环(LiDAR 分割)**:这类工作用"teacher 预测→伪标签→再训练"闭环提升模型,但面向域迁移而非单域持续改进:
  - LiDAR-UDA: Self-ensembling Through Time for Unsupervised LiDAR Domain Adaptation(arXiv 2309.13523,https://ar5iv.labs.arxiv.org/html/2309.13523)
  - ConUDA: Confidence-Guided Pseudo-Label Sampling for UDA in 3D LiDAR Semantic Segmentation(https://ieeexplore.ieee.org/document/11163385)
  - Domain Adaptive LiDAR Point Cloud Segmentation via Density-Aware Self-Training(IEEE TITS 2024,https://dl.acm.org/doi/abs/10.1109/TITS.2024.3386865)
  - DPGLA: Bridging the Gap between Synthetic and Real Data for UDA in 3D LiDAR Semantic Segmentation(arXiv 2510.23525,https://ar5iv.labs.arxiv.org/html/2510.23525)
- **2D→3D 蒸馏/伪标签(弱监督)**:FeatureDistillation(CVLab UniBo,https://cvlab-unibo.github.io/FeatureDistillation/)、PPDistiller(https://www.sciencedirect.com/science/article/abs/pii/S0950705124012887)。
- **自监督预训练(提升分割性能,但不是"闭环持续改进")**:PointContrast、Contrastive Scene Contexts、MSC(CVPR 2023)、Point-GCC(ACM MM 2024,https://huggingface.co/papers/2305.19623)、Sonata(CVPR 2025,https://arxiv.org/abs/2503.16429)、PPT(CVPR 2024,https://arxiv.org/abs/2308.09718)等,多在 Pointcept 中实现。
- **无标签/自监督分割**:FoundObj: Self-supervised Foundation Models as Rewards for Label-free 3D Object Segmentation(ICML 2026,https://icml.cc/virtual/2026/poster/61637)。

---

## B. Auto3DSeg(MONAI)

- **定位**:面向**医学影像 3D 体素分割**的自动化解决方案,不是点云/LiDAR。输入为 CT/MRI/PET 等医学图像体素(带 spacing/intensity 元数据),评测指标为 Dice 等医学指标。**明确:模态与 3DSS(点云)不同。**
- **机制(自动化程度很高)**:用户只需提供数据根目录和 datalist;流水线为:
  1. `data_analyzer` 分析数据集全局信息(强度、尺寸、spacing 等统计);
  2. `bundle_gen` 基于数据统计 + **算法模板**(UNETR、SwinUNETR、SegResNet 等,模板在 Project-MONAI/research-contributions)生成 MONAI bundle 格式的算法目录;
  3. `hpo_gen` 对每个算法做**超参数搜索**;
  4. 并行训练所有算法,保留验证集最优 checkpoint;
  5. `ensemble_builder` 按验证分数排序选算法并做**集成预测**。
  - 对应模块源码(moani 路径 `monai/apps/auto3dseg`):`auto_runner.py`、`data_analyzer.py`、`bundle_gen.py`、`hpo_gen.py`、`ensemble_builder.py`。
  - 来源:https://github.com/Project-MONAI/tutorials/tree/main/auto3dseg (README) ; https://raw.githubusercontent.com/Project-MONAI/MONAI/dev/docs/source/whatsnew_1_0.md ; 模块列表 https://api.github.com/repos/Project-MONAI/MONAI/contents/monai/apps/auto3dseg
- **是否涉及 LLM / agent:未找到公开资料表明 Auto3DSeg 使用 LLM 或 agent。** 其机制是"数据统计 + 算法模板 + HPO + 集成"的**确定性自动化**,不是 LLM 驱动。官方 README 与 MONAI 1.0 release notes 均未提及 LLM/agent。(注:医学影像社区有把 Auto3DSeg 与 LLM 混提的二手资料,但官方源码/文档无此内容,按"未找到"处理。)
- **开源可用性**:完全开源(Apache-2.0),集成于 MONAI(`monai.apps.auto3dseg`),教程与示例在 https://github.com/Project-MONAI/tutorials/tree/main/auto3dseg ,算法模板在 https://github.com/Project-MONAI/research-contributions/tree/main/auto3dseg。
- **效果(医学 3D 分割)**:
  - MICCAI 2022 HECKTOR22(头颈肿瘤 PET/CT 分割)第 1 名(分割任务);
  - MICCAI 2022 INSTANCE22(颅内出血 CT 分割)第 2 名(Dice 第 1);
  - MICCAI 2022 ISLES'22(缺血性卒中病变)第 2 名(Dice 第 1);
  - 多个 challenge 技术报告:KiTS23(arXiv 2310.04110)、SEG.A 2023(arXiv 2310.04114)、ISLES22(arXiv 2209.09546)、INSTANCE22(arXiv 2209.10648)。
  - 来源:https://github.com/Project-MONAI/tutorials/tree/main/auto3dseg ; http://export.arxiv.org/pdf/2310.04110
- **能否作为点云 3DSS 自动化的参考架构:机制上可以,工程上不能直接复用。**
  - 可参考:**"数据统计→模板化算法生成→HPO→并行训练→按验证指标选优/集成"的闭环管线设计**,这是 agent 环境下 3DSS 训练自动化的理想模板;其对"最少用户输入"的追求与 agent 使用场景一致。
  - 不可直接复用:数据格式(医学体素 vs 点云)、预处理、MONAI bundle 生态、Dice 指标、CT/MRI 领域模板。点云需要自己的数据加载器、评估协议(mIoU,见 D)与算法模板(如 PTv3、MinkUNet)。

---

## C. 3DSS 生态工具链成熟度(作为 agent 环境的评估)

### Pointcept(https://github.com/Pointcept/Pointcept)
- **数据集**:开箱支持并附预处理脚本:`ScanNet / ScanNet200 / ScanNet++ / S3DIS / SemanticKITTI / nuScenes / Waymo / HM3D / Structured3D`;还提供 HuggingFace 预处理好数据(https://huggingface.co/Pointcept)。
- **训练/评估**:config 驱动(`configs/*.py` + `tools/train.py` 等),模型 zoo 含 PTv3、OA-CNNs、SPUNet 等,统一 `DataModule/ModelModule` 接口,多 GPU/DDP 支持。
- **脚本化程度**:纯 Python + yaml/py 配置,CLI 可复现,日志/checkpoint 结构规整,**非常适合 agent 调用**(可编程生成配置、启动训练、读日志评估)。
- 来源:https://github.com/Pointcept/Pointcept (README 实测抓取)

### Open3D-ML(https://github.com/isl-org/Open3D-ML)
- **数据集**:`ml3d.datasets` 内置 `SemanticKITTI / S3DIS / ScanNet / Semantic3D / Toronto3D / ParisLille3D / nuScenes / Waymo / KITTI` 等加载器(实测目录:semantickitti.py、s3dis.py、scannet.py 等)。
- **训练/评估**:统一 `Pipeline` API(`SemanticSegmentation(model, dataset, ...)`),yaml 配置(`ml3d/configs/randlanet_semantickitti.yml` 等),含预训练模型 zoo(如 RandLA-Net on SemanticKITTI,可直接下载权重推理);PyTorch / TensorFlow 双后端。
- **脚本化程度**:Python API 一致、配置驱动,`pipeline.run_test()/run_train()` 结构化,**适合 agent 调用**;注意:维护活跃度一般,Linux 上 TF 后端需源码构建(PyPI 轮子不再原生支持 TF)。
- 来源:https://github.com/isl-org/Open3D-ML (README + 目录实测)

### MinkowskiEngine(https://github.com/NVIDIA/MinkowskiEngine)
- 定位:**稀疏张量算子库/自动微分库**(稀疏卷积、池化等),不是完整训练框架。
- 示例训练脚本:`examples/indoor.py`(室内语义分割,S3DIS/ScanNet 预处理)、`minkunet.py`、`classification_modelnet40.py` 等;SemanticKITTI 等更多依赖第三方(如 MMDetection3D)或自写。
- 脚本化程度:作为库嵌入训练代码易,但**没有开箱即用的 3DSS 训练器/评估器**,agent 需自行组装 pipeline。
- 来源:https://github.com/NVIDIA/MinkowskiEngine (README + examples 目录实测)

### TorchSparse(https://github.com/mit-han-lab/torchsparse)
- 定位:**高性能稀疏卷积系统**(MICRO 2023 / MLSys 2022),提供 MinkUNet 等骨干与 ops;提供 MMDetection3D / OpenPCDet 插件;`performance.py` 为算子性能评测。
- 脚本化程度:**无内置数据集加载器/训练器/评估器**(examples 仅 example.py/backbones.py/插件 demo),属于底层库,agent 直接使用成本高。
- 来源:https://github.com/mit-han-lab/torchsparse (README + examples 目录实测)

### 评估服务器 / leaderboard API
- **SemanticKITTI**:官方 benchmark 采用**服务端评测**(CodaBench 托管测试集提交与评分,测试标签不公开,限制提交次数)。本地离线评估可用官方 API **PRBonn/semantic-kitti-api**(含 `evaluate_semantic_segmentation` 等脚本)。
  - 来源:http://semantic-kitti.org/tasks.html ; https://github.com/PRBonn/semantic-kitti-api ; CodaBench 示例 https://www.codabench.org/competitions/13666/
- **ScanNet**:在线 benchmark(https://kaldir.vc.in.tum.de/scannet_benchmark/ ,3D 语义标签榜单,mIoU/20 类);官方评估脚本开源在 ScanNet repo 的 `BenchmarkScripts`(基于 CityScapes 评估移植,本地可跑)。
  - 来源:https://raw.githubusercontent.com/ScanNet/ScanNet/master/BenchmarkScripts/README.md ; https://kaldir.vc.in.tum.de/scannet_benchmark/
- **S3DIS**:**无官方在线评测服务器**;社区协议为 6-fold 交叉验证与 Area-5 留出测试;PapersWithCode 有 S3DIS 3D 语义分割榜单(社区聚合,非服务端 API)。
  - 来源:https://paperswithcode.co/benchmark/s3dis?task=3d-semantic-segmentation ; 协议对比表见 https://ojs.aaai.org/index.php/AAAI/article/view/28625
- **PapersWithCode 榜单(信息聚合,非 API)**:SemanticKITTI / ScanNet / S3DIS 均有 SOTA 页面,提供方法级结果聚合(如 https://paperswithcode.com/sota/semantic-segmentation-on-semantickitti )。
- **小结**:**没有统一的 3DSS 评估服务器 API**;SemanticKITTI 有官方在线服务(限制多),ScanNet 在线服务 + 开源本地评估脚本,3DSS 的"评估服务器"缺口由各开源工具库的本地评估脚本补齐。

---

## D. 3DSS 基准协议要点

- **SemanticKITTI(户外 LiDAR)**:
  - 指标:每类 IoU 与 **mIoU**(语义分割,单帧设置 19 类;多帧设置区分运动/非运动)。
  - 提交:测试序列 11-21 由官方服务器(CodaBench)评测,测试标签不公开,限制提交次数(如部分任务验证集 100 次 / 测试集 10 次)。
  - **本地离线评估:支持**。用 PRBonn/semantic-kitti-api 可在验证集/自建集上直接算 mIoU(对 agent 闭环足够)。
  - 来源:http://semantic-kitti.org/tasks.html
- **S3DIS(室内点云)**:
  - 指标:主流报告 mIoU、OA(overall accuracy)、mAcc;两种协议:**6-fold 交叉验证**(训练 5 个 area、测 1 个)与 **Area-5 留出测试**。
  - 提交:**无官方服务器**;所有评估本地离线完成(各代码库内置)。
  - 来源:协议与数字对比见 https://ojs.aaai.org/index.php/AAAI/article/view/28625 ; 数据集 https://buildingparser.stanford.edu/
- **ScanNet(室内重建点云)**:
  - 指标:mIoU,20 个语义类;在线 benchmark(kaldir)有 3D 语义标签榜单。
  - 提交:曾支持在线提交;官方评估脚本开源(`BenchmarkScripts`,2D/3D 语义与实例),**本地可完全离线评估**。
  - 来源:https://kaldir.vc.in.tum.de/scannet_benchmark/ ; https://raw.githubusercontent.com/ScanNet/ScanNet/master/BenchmarkScripts/README.md
- **对 agent 闭环的意义**:三大基准均能**完全本地离线评估**(ScanNet/S3DIS 用开源脚本,SemanticKITTI 用官方 API 在 val 上算 mIoU),不依赖在线提交即可构成"训练→评估→改进"闭环;官方在线榜单只在最终发布结果时使用。

---

## 结论:3DSS 作为 agent 环境的成熟度(5 条)

1. **训练自动化侧的"agent 缺口"是真实的**:未发现任何公开工作用 LLM agent 驱动点云/ LiDAR 分割模型的训练、调参或架构搜索;点云侧的 LLM agent(LiDARAgent、REALM 等)全部是"推理/分析/交互"型,通用 ML agent(AutoML-Agent、MLAgentBench、MARS)没有 3DSS 任务。**这正是一个可论证的新空白点。**
2. **"自增强数据闭环"已有先例但不在分割上**:PiSA 证明了"3D MLLM 自动标注 + 跨模态校验 + 迭代重训"闭环有效(面向 3D MLLM 理解);One Thing One Click 证明了 3DSS 上伪标签自训练可行;UDA 工作(LiDAR-UDA、ConUDA 等)证明了 LiDAR 分割的伪标签自训练闭环成熟。**把这三者组合成"3DSS 持续改进 agent"在技术上没有阻碍。**
3. **工具链具备"agent 可执行环境"的条件**:Pointcept 与 Open3D-ML 开箱支持 SemanticKITTI / S3DIS / ScanNet(加载器、训练脚本、评估、预训练模型齐全,config/API 驱动,易脚本化);MinkowskiEngine / TorchSparse 是底层算子库,不适合直接做 agent 环境。**推荐以 Pointcept(活跃、覆盖最全)为主执行环境。**
4. **评估可闭环,但无统一"评估服务器 API"**:SemanticKITTI 官方 CodaBench 服务端评测限制提交次数;ScanNet 在线 benchmark 加开源脚本;S3DIS 无官方服务器。**好在三个基准都能本地离线评估,agent 闭环不需要在线服务**,官方榜单仅作最终汇报。
5. **Auto3DSeg 是机制级参考、非代码级复用**:其"数据统计→模板生成→HPO→并行训练→按验证分数选优/集成"的确定性自动化(不含 LLM)为 3DSS 自动化提供了现成的管线范式,但医学体素栈(格式/预处理/MONAI bundle/Dice)不能直接搬到点云,需自建点云侧的模板与评估协议。**"Auto3DSeg 式确定性自动化 + LLM agent 编排 + 自训练闭环"是 3DSS agent 最现实的参考架构。**
