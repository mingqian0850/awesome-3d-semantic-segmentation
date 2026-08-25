# 智能体自进化做 3D 语义分割:可行性调研与系统对比报告

> 调研日期:2026-08 · 范围:LLM 驱动的自进化/自主 ML 研究系统对 3D 语义分割(点云/LiDAR)的适用性
> 配套落地文档:[`agentic-3dss-implementation.md`](agentic-3dss-implementation.md)(前提条件、标签引擎架构、第一周验证实验、分阶段执行)
> 配套调研笔记(原始证据与逐条来源 URL):
> - `research-notes/ml-agent-systems.md` — 通用 ML 工程 agent 系统(AIDE / MLAgentBench / MLGym / InnoGym / DS-Agent / MLE-bench / AutoML)
> - `research-notes/self-evolution-loops.md` — 自进化 / 进化式搜索闭环(AI Scientist / FunSearch / AlphaEvolve / AgentBreeder / POISE / HSI / RSI 综述)
> - `research-notes/3d-specific-automation.md` — 3D 专项自动化现状与工具链成熟度(PiSA / One Thing One Click / Auto3DSeg / Pointcept / Open3D-ML)

---

## 0. 结论摘要(先看这里)

**可行,而且 3DSS 是这套范式(harness agent 套在领域任务上)的优质落地点之一;但"3DSS 训练自动化 + LLM agent"目前没有任何成熟公开系统——这是一个可论证的新空白点。**

1. **通用侧基础设施已齐**:LLM 代码级 agent([MLAgentBench](https://arxiv.org/abs/2310.03302)、[AIDE](https://arxiv.org/abs/2502.13138)、[MLGym](https://arxiv.org/abs/2502.14499))、进化式程序搜索([FunSearch](https://www.nature.com/articles/s41586-023-06924-6)、[AlphaEvolve](https://arxiv.org/abs/2506.13131)、[POISE](https://arxiv.org/abs/2603.23951))、全自动研究闭环([AI Scientist](https://arxiv.org/abs/2408.06292))、可进化 harness 框架([HSI](https://arxiv.org/abs/2608.08466))。这些系统已在 ML 竞赛、数学发现、算法发现上证明了闭环有效。
2. **3DSS 侧环境成熟度足够**:Pointcept / Open3D-ML 提供标准化数据集加载 + 训练 + 评估;SemanticKITTI / ScanNet / S3DIS **三大基准均可完全本地离线评估**,agent 闭环不依赖在线提交服务器。
3. **主要障碍不是"能不能",而是成本与统计纪律**:单次训练贵(GPU 小时~天)、评估有噪声(seed 方差)、自进化系统天然会过拟合验证集。三条铁律:**代理评估漏斗、多 seed/阈值化判定、holdout 终评**。
4. **推荐架构**(综合调研结论):**AlphaEvolve/POISE 风格**的样本高效搜索(数千次候选,而非 FunSearch 式百万采样)+ **评估级联**(小规模代理评估筛劣解 → 全量复验幸存者)+ **系谱化实验存档**(提案/代码/评估/反思互链)+ **冻结骨干、进化训练配方/harness**(HSI 同构)+ 按**验证层级**设计评估器。
5. **期望管理**:自指理论提示 LLM 目前只有"准内省",把闭环定位为**人机协同加速器**(人类定方向,agent 跑搜索与实验)比"全自主 AI 科学家"更现实;AI Scientist 的自动审稿分数也不应被当作科学真理(其"通过同行评审"声明存在争议)。

---

## 1. 概念框架:四类范式

| 范式 | 代表 | 动作空间 | 谁来"进化" | 成本量级(已验证数字) |
| --- | --- | --- | --- | --- |
| A. 传统 AutoML / HPO | Optuna、AutoGluon、NNI | 预定义配置空间 | 采样器/贝叶斯优化 | 无 LLM 成本;NNI 已停更(archived) |
| B. LLM 代码级 agent | MLAgentBench、AIDE、MLGym、DS-Agent | 任意代码/配置修改 + 跑实验 | LLM 提出 patch,实验反馈闭环 | LLM API 成本每任务 **<$1.5~$2.5**(AIDE);单 run 数美元(MLAgentBench) |
| C. 进化式程序搜索 | FunSearch、AlphaEvolve、POISE | 程序/函数/机制级修改 | LLM 作为变异算子 + 进化选择 | FunSearch 需百万级采样(样本效率低);AlphaEvolve 数千采样、单解评估可 ~100 compute-hours |
| D. 全自动研究闭环 | AI Scientist、HSI、RSI 综述 | 研究全流程(idea→实验→论文)或 harness 重写 | 整个 pipeline 自我引用 / 冻结 LLM 分层进化 | AI Scientist v1 **<$15/篇**(GPT-4o 时代) |

**关键认识**:A 是"搜参数",B 是"搜配方与代码",C 是"搜程序/机制",D 是"搜研究过程本身"。把 harness agent 套在 3DSS 上,对应的正是 **B+C+D 的组合**:agent 改训练配方/代码(B)、可定向搜索损失与增强函数(C)、并把实验结果沉淀成系谱化知识库驱动下一轮假设(D)。

---

## 2. 通用系统对比

### 2.1 ML 工程 agent(A 组)

| 系统 | 机构/年份 | 核心机制 | 动作空间 | 成本(公开数字) | 代码可用性 | 3DSS 适配度 |
|---|---|---|---|---|---|---|
| [MLAgentBench](https://arxiv.org/abs/2310.03302) | Stanford SNAP, ICML'24 | ReAct 式研究 agent,13 个 ML 实验任务;success = 相对 starter baseline 提升 >10% | 读写文件/执行代码/查输出 | 单 run 数美元;整 benchmark ≈600 万 token ≈$60;期望完成成本 **$231**(26% 成功率折算) | 开源 MIT + Docker | 低:任务分钟级训练,50 动作/5h 预算在 3DSS 下跑不完一次训练;但"阈值化成功判定"可借鉴 |
| [AIDE](https://arxiv.org/abs/2502.13138) | Weco AI, 2025 | 代码空间树搜索:搜索策略 π + 编码算子 + 摘要算子;每轮多 draft 并行评估后剪枝 | 生成/修改 Python 脚本并执行评估 | **LLM 成本每任务 <$1.50**(最高 ~$2.50,不含计算) | 开源 MIT + PyPI + WebUI | 中:树搜索抽象可借鉴;默认参数(20 steps × 5 drafts)直接套 3DSS 会预算爆炸,需换成代理评估 |
| [InnoGym](https://arxiv.org/abs/2512.01822) | 浙大, ICLR'26 | 创新力基准:Performance Gain + Novelty;iGym 统一环境对比 MLAB/CodeAct/AIDE | 取决于 scaffold | 未公开;每配置 ≤12h wall-clock | 论文公开;iGym 仓库未公开(404) | 中:核心结论"**鲁棒性优先于新颖性**——新颖方案若不可靠不会转化为增益"直接适用于 mIoU 噪声大的 3DSS |
| [MLGym](https://arxiv.org/abs/2502.14499) | Meta FAIR, 2025 | 首个 ML Gym 环境(为 RL 训练 agent 设计);shell + 沙箱 | shell 命令 + 工具(编辑/validate/submit/**memory**) | 未公开美元;CIFAR-10 平均 ~4h/1GPU | 开源但 **CC BY-NC 4.0 非商用** | 中高:**50 步预算 + 每任务训练超时 + 自动提交 + memory 模块**是重训练场景护栏范本;结论"agent 主要靠调超参,不能产生新假设/架构" |
| [DS-Agent](https://arxiv.org/abs/2402.17453) | 清华+吉大, ICML'24 | LLM + 案例推理(CBR)两段式:开发阶段迭代沉淀案例 → 低资源部署阶段直接出码 | 生成实验计划与代码 | 开发 **$0.06~$1.60/run**,部署 **$0.0045~$0.135/run**(GPT API,不含计算) | 开源(无 LICENSE 文件) | 中:**两段式"先沉淀案例库、再少迭代复用"**契合 3DSS"少迭代直接拿可用配置"的诉求 |
| [MLE-bench](https://arxiv.org/abs/2410.07095) | OpenAI, ICLR'25 | 基准:75 个 Kaggle 竞赛,Any Medal %;**官方设置 24h/竞赛、单张 A10、≥3 seeds** | 取决于 scaffold(AIDE/MLAB/OpenHands) | 未公开单竞赛美元;官方承认难复现 | 开源 | 中:**24h+单卡的量级 ≈ 3DSS 一次全量训练**,即一个 MLE-bench run ≈ 3DSS 一次训练;官方明言 "agents can be quite high-variance!" |

**MLE-bench 关键数字**(官方 leaderboard,2026-08):AIDE+o1-preview **17.1%** 奖牌率(pass@8 34.1%);GPT-4o 8.7%→100h 放宽 11.8%;硬件实验显示 **agent 不会自动利用第二张 GPU**;2025–2026 新系统(如 MLEvolve 61.3%、PiEvolve 61.3%)已把奖牌率推到 56–64%。

### 2.2 自进化 / 进化式搜索闭环(B 组)

| 对象 | 机构/年份 | 进化循环机制 | 评估器 | 记忆/存档 | 成本(公开) | 代表成果 | 3DSS 可借鉴点 |
|---|---|---|---|---|---|---|---|
| [AI Scientist v1/v2](https://arxiv.org/abs/2408.06292) | Sakana AI, 2024/2025/Nature 2026 | idea→实验→论文→自动评审 四阶段科研闭环 | LLM 审稿人(v2 为 VLM+审稿人) | 论文库 + 审稿分数反馈 | v1 **<$15/篇**;v2 未公开 | v2 论文过 ICLR workshop 盲审(有争议) | 闭环骨架可直接套用;审稿人可当"方向把关人";成本模型不可照搬 |
| [FunSearch](https://www.nature.com/articles/s41586-023-06924-6) | DeepMind, Nature 2023 | LLM 采样=变异 + 程序库 + **岛屿模型**防早熟 | 用户提供的 `evaluate` 函数(需分钟级快评估) | programs database(签名聚簇) | 未公开(需百万级采样,样本效率低) | cap set 20 年最大渐进下界改进;bin packing 100k 件仅 0.03% off 最优 | **搜损失/增强/后处理函数**;岛屿模型防局部最优;评估必须代理化 |
| [AlphaEvolve](https://arxiv.org/abs/2506.13131) | DeepMind, 2025 | 整文件级进化 coding agent;级联测试 + LLM 反馈 + 并行评估 | 自动 evaluate(可多指标、可并行) | 提示/存档库;异步流水线 | 未公开;单解评估可 ~100 compute-hours;数千采样 | 4×4 复数矩阵乘法 48 次标量(56 年首破 Strassen);~20% 数学问题超 SOTA | **评估级联**是把小时级训练塞进进化循环的关键手法;**整文件变异**贴近真实改进方式 |
| [AgentBreeder](https://arxiv.org/abs/2502.00757) | 牛津, 2025 | 多目标进化搜 multi-agent scaffold;MAP-Elites 式 quality-diversity | 验证集正确率中位数 + 95% CI | 精英集/niche 存档 | 未公开 | Blue 模式安全基准 +79.4%;Red 模式发现 jailbreak 弱 scaffold | 存档+多样性搜索防早熟;**警示:进化可能"进化出"评估集作弊** |
| [POISE](https://arxiv.org/abs/2603.23951) | 2026 | 闭环算法发现:提案→实现→标准评估→反思,**系谱化存档**驱动 | 标准化 RL 评估(Overall、AIME25 pass@k) | 系谱化存档(提案/实现/评估/反思互链) | 未公开(**64 个候选**) | 从 GRPO 出发:Overall 47.8→52.5;AIME25 pass@32 26.7%→43.3% | **系谱化存档+反思链是 3DSS 闭环最有价值的架构细节**;64 候选是现实预算量级 |
| [HSI](https://arxiv.org/abs/2608.08466) | 2026 | 冻结 LLM 三层:harness / evolver / meta-evolver;任务注入缝热切换 | 环境反馈;thinking on/off 消融 | 每任务族独立 harness | 未公开 | BALROG:BabyAI +39.3、Crafter +33.0 等;超骨干能力任务无收益 | **冻结骨干+进化 harness 与 3DSS 结构同构**;两个 bound(反馈保真度、骨干能力)界定闭环收益上限 |
| [RSI 综述](https://arxiv.org/abs/2607.07663) | 2026 | 1,250 篇论文两轴分类;**验证层级**:形式验证器 > 过程验证器 > 自我评估 | — | — | — | 自改进强度与验证层级严格对应 | **失败模式清单**(过拟合评估、自我确认回路、崩塌、成本爆炸)与评估器设计准则 |

### 2.3 传统 AutoML 对照(一句话)

Optuna(define-by-run + TPE,可作 agent 的内部调参工具)、AutoGluon(stacking/集成,无代码动作空间)、NNI(HPO/NAS,但**已 archived 停更**)——三者都是"搜预定义空间",无法完成"改网络→改预处理→跑训练→读日志→再改"的闭环,但可嵌入 agent 作为子工具。

### 2.4 跨系统共同发现(对 3DSS 设计的 5 条硬约束)

1. **训练预算护栏是刚需**:MLGym 的 50 步 + 训练超时、MLE-bench 的 24h/单卡 → 3DSS 必须显式约束"单次训练时长 × 迭代次数",先在小规模 warm-up 上迭代,全量仅作最终验证。
2. **评估噪声必须显式处理**:MLE-bench 要求 ≥3 seeds;MLAgentBench 用 >10% 阈值;InnoGym 结论"鲁棒性优先于新颖性" → 3DSS 反馈信号需多 seed 聚合或显著阈值判定。
3. **先沉淀案例库,再少迭代部署**(DS-Agent 两段式):先用人工积累 2–3 个高质量基线配置作案例,让 agent 基于案例微调而非从零探索。
4. **并行要显式做成工具**:MLE-bench 实验显示 agent 不会自己用第二张 GPU → 多卡/多候选 fan-out 做成显式 API。
5. **成本以 GPU 小时为主、LLM token 为辅**:AIDE <$1.5/任务、DS-Agent ≤$1.6/run、MLAgentBench 单 run 数美元——LLM 开销相对一次 3DSS 训练可忽略,设计重心是**最小化训练调用次数**。

---

## 3. 3DSS 作为 agent 环境:成熟度评估

### 3.1 工具链(可直接当"环境 API")

| 组件 | 角色 | 成熟度 |
| --- | --- | --- |
| [Pointcept](https://github.com/Pointcept/Pointcept) | 训练框架,集成 PTv1/v2/v3、SphereFormer 等 SOTA,config 驱动,统一 DataModule/ModelModule 接口,附 HF 预处理好数据 | **高,推荐作主执行环境** |
| [Open3D-ML](https://github.com/isl-org/Open3D-ML) | 内置 SemanticKITTI/S3DIS/ScanNet/nuScenes/Waymo 等加载器,统一 Pipeline API + yaml 配置 + 预训练模型 zoo | 高(TF 后端需源码构建,注意维护活跃度一般) |
| [semantic-kitti-api](https://github.com/PRBonn/semantic-kitti-api) | SemanticKITTI 官方评估 API(本地离线算 mIoU) | 高,官方 |
| [MinkowskiEngine](https://github.com/NVIDIA/MinkowskiEngine) / [TorchSparse](https://github.com/mit-han-lab/torchsparse) | 稀疏张量/稀疏卷积底层算子库 | 低(无开箱训练器/评估器,不适合直接做 agent 环境) |

### 3.2 基准协议(评估器设计约束)

| 基准 | 指标 | 评估方式 | agent 闭环可用性 |
| --- | --- | --- | --- |
| SemanticKITTI | mIoU(单帧 19 类) | test 走官方 CodaBench 服务端(限提交次数);val 用官方 API **本地离线** | ✅ 本地闭环 |
| ScanNet | mIoU(20 类) | 在线 benchmark + 官方开源 `BenchmarkScripts` **本地可跑** | ✅ 本地闭环 |
| S3DIS | mIoU / OA / mAcc | **无官方服务器**;社区协议 Area-5 / 6-fold 不一 | ✅ 本地闭环(但 agent 的评估器必须固定协议并入库,否则跨实验不可比) |

→ 三大基准全部支持本地离线评估,**agent 闭环不需要在线服务**;官方榜单仅作最终汇报。S3DIS 协议混乱反而是 agent 的卖点:让 agent 固定并记录评估协议,保证可比性。

### 3.3 成本基线(决定 proxy 协议设计)

3DSS 单次全量训练:数小时(S3DIS 小模型)~数天(SemanticKITTI 大模型),显存需求大。**必须设计 proxy 协议**:小子集 / 少 epoch / 低体素分辨率 / 提前停止,并用少量"复验实验"校准 proxy 与全量之间的相关性。

---

## 4. 3DSS 专项自动化现状

### 4.1 核心发现:训练自动化侧存在真实空白

**未找到任何公开工作用 LLM agent 驱动点云/LiDAR 分割模型的训练、调参或架构搜索。** 点云领域的 LLM agent 全部是"推理/分析/交互"型:

- [LiDARAgent](https://github.com/pkurelab/LiDARAgent)(北大):生态遥感点云分析 agent(任务规划+工具调用),非训练自动化
- REALM(CVPR 2026):3DGS 上的开放世界推理分割/编辑 agent,推理期交互
- LLM-Supervised Point Cloud Processing(ISPRS):LLM 监督场景图生成,非训练

通用 ML agent(AutoML-Agent、ML-Bench、MARS 等)均无 3DSS 任务;点云 NAS 只有 Point-NAS(TIP 2023)、Auto-Points(TMM 2023)两个较早的传统 NAS 工作,后续基本停滞。→ **"3DSS 训练自动化 agent"是一个可论证的新空白点。**

### 4.2 最近邻先例:"自增强数据闭环"在 3D 上已被证明可行

- [PiSA](https://arxiv.org/pdf/2503.10529)(CUHK-SZ,2025):"3D MLLM 自动标注 → 2D MLLM 跨模态校验 → 迭代重训"三阶段 self-augmented 数据引擎,数据质量随训练提升(data-model 共演化)。面向 3D MLLM 理解,但闭环机制可直接借鉴到分割。
- [One Thing One Click](https://arxiv.org/abs/2104.02246)(CVPR 2021):3DSS 上最直接的伪标签自训练工作(每类点一次 + self-training)。
- LiDAR 分割的伪标签自训练闭环成熟:LiDAR-UDA、ConUDA、密度感知自训练等(均面向无监督域自适应)。
- 仓库内相关的还有:[LLM-Guided Taxonomy and Hierarchical Uncertainty for 3D Point Cloud Active Learning](https://arxiv.org/abs/2505.18924)(LLM 已进入 3D 点云主动学习)、[3D-AVS](https://arxiv.org/abs/2406.09126)(auto-vocabulary)、[RePL](https://arxiv.org/abs/2604.06825)/[UniLiPs](https://arxiv.org/abs/2601.05105)(伪标签精修/无监督伪标签)。

→ 把"自动标注/伪标签 + 迭代重训"组合成"3DSS 持续改进 agent"(数据进化层)在技术上没有阻碍。

### 4.3 Auto3DSeg(MONAI):机制级参考、代码级不可复用

- 定位:**医学影像 3D 体素分割**(CT/MRI/PET,非点云),确定性自动化(未发现 LLM/agent 参与)。
- 机制:"数据统计 → 算法模板生成(UNETR/SwinUNETR 等)→ HPO → 并行训练 → 按验证分数选优/集成",最少用户输入。
- 战绩:MICCAI 2022 HECKTOR22 第 1、INSTANCE22/ISLES'22 第 2。
- 结论:其"统计→模板→HPO→并行训练→选优集成"是 agent 环境下 3DSS 训练自动化的**理想管线模板**,但医学体素栈(格式/预处理/MONAI bundle/Dice)不能搬到点云,需自建点云侧模板(PTv3/MinkUNet)与评估协议(mIoU)。

---

## 5. 失败模式与 Gap 分析

### 5.1 自进化闭环的已知失败模式(跨系统归纳,必须预防)

| # | 失败模式 | 表现 | 3DSS 下的缓解策略 |
|---|---|---|---|
| 1 | **过拟合评估器** | 方案在开发集暴涨、留出集崩塌;AgentBreeder Red 模式即"故意进化出评估器漏洞" | 固定留出集分层验证;多 seed 取分布;任何选择不触碰测试集 |
| 2 | **自我确认回路** | LLM 审稿/评分被进化过程"驯化",虚高分数 | 评估器与被评对象隔离;验证层级:形式指标 > 交叉验证 mIoU > LLM 主观评分 |
| 3 | **多样性崩塌** | 种群收敛同质,变异无新信息;或自训练数据污染 | 岛屿模型/quality-diversity 存档(FunSearch/AgentBreeder);定期注入外部多样性(新论文/新数据) |
| 4 | **成本爆炸** | 每代全量训练,预算线性~超线性增长 | 代理评估漏斗 + 评估级联(AlphaEvolve);系谱化存档复用已跑实验(POISE);冻结骨干只进化配方(HSI) |
| 5 | **反馈保真度不足** | 信号太噪/太稀 → 进化变随机游走(HSI feedback-fidelity bound) | 重复种子取分布、增大验证集、提高信噪比 |
| 6 | **骨干能力上限** | 冻结骨干之上无论怎么进化都无法突破(HSI backbone bound,BALROG 实证) | 明确闭环边界;需要突破时切换到全量训练(成本换能力) |
| 7 | **方向设定瓶颈** | 系统能优化给定目标,但"该研究什么"仍需人类/高层 | 人类在环设定顶层方向(最现实的定位) |
| 8 | **理论天花板** | LLM 只有"准内省",递归自改进未必可持续(2607.04277) | 定位为人机协同加速器,而非取代研究者 |

### 5.2 从通用系统到 3DSS 的差距表

| 挑战 | 通用系统现状 | 3DSS 需要的定制 |
| --- | --- | --- |
| 单次实验成本 | MLAgentBench 任务分钟级;MLE-bench 24h/单卡 | proxy 协议 + 分级验证 + 预算封顶(轮数/GPU 小时) |
| 评估噪声(seed 方差) | MLE-bench 要求 ≥3 seeds;MLAgentBench >10% 阈值 | 配对比较(同 seed)、小候选多 seed、完整记录 config |
| 过拟合 val | 已知失败模式(5.1 #1) | holdout 测试集终评;动作空间受限;强制 hypothesis rationale |
| 代码破坏(patch 跑不起来) | 有 smoke test 实践 | lint + dry-run + git 回滚 + checkpoint 隔离 |
| 环境准备(数据下载/注册) | 无(基准自带数据) | 环境准备阶段脚本化(ScanNet 注册、SemanticKITTI 下载) |
| 跨实验可比性 | 部分(S3DIS 无官方协议) | 固定评估协议并入库,协议变更必须显式记录 |
| 领域知识 | 无点云先验 | 案例库注入(DS-Agent 式):2–3 个高质量基线配置起步 |

---

## 6. 推荐架构与路线图

### 6.1 推荐架构(综合 AIDE + POISE + HSI + AlphaEvolve)

```
┌─ 主 agent(提议者,冻结骨干 LLM)──────────────────────────┐
│  读系谱化实验存档 → 形成 hypothesis → 生成 patch/配置 diff  │
└──────────────┬──────────────────────────────────────────┘
               ▼
   评估级联(AlphaEvolve 风格):
   ① proxy 评估(小子集/少 epoch,≤30 min)→ 快速筛掉劣解
   ② 幸存者全量复验(小时级)── 每级评估器按验证层级设计
               ▼
   统一评估器(固定协议,多 seed 聚合 mIoU)+ 写回系谱化存档
   (提案/代码/评估/反思互链,POISE 风格)
               ▼
   选择/变异(岛屿模型防早熟)→ 下一轮(预算封顶:候选数 × 单候选成本)
```

设计原则(全部有调研依据):

1. **验证层级评估器**(RSI 综述):形式可验证指标(参数量/FLOPs)→ 跨数据集交叉验证的 mIoU(多 seed)→ LLM 主观评分(最后才用);任何选择不触碰留出测试集。
2. **冻结骨干、进化配方/harness**(HSI 同构):把耗钱的骨干训练冻结,只进化损失、增强、体素化、后处理与训练调度——成本降低 1–2 个数量级;明确收益上限 = 骨干能力 + 反馈保真度。
3. **系谱化存档**(POISE):每个候选挂"父代、实现、评估结果、LLM 反思",站在证据上迭代,避免重复踩坑。
4. **并行 fan-out 显式化**(MLE-bench 教训):多候选并行训练做成显式工具(后台 job),不指望 agent 自己分卡。
5. **案例库起步**(DS-Agent):先人工固定 2–3 个高质量基线(如 MinkUNet / PTv3 标准配置)作为初始种群与对照。

### 6.2 路线图

- **P0(可行性质证)**:环境 = Pointcept + S3DIS(Area 1–4 训练 / Area 5 验证,固定协议);动作空间 = 训练配方(体素化、学习率、增强、损失权重、类别权重);每轮 3–5 个候选 × 限时 proxy 训练(≤30 min);实验库 JSONL 记录 (config, seed, mIoU, rationale);保留 baseline 对照。**验收标准:agent 在有限预算内找到 ≥2 个显著优于基线的配方,且 holdout 复现成立。**
- **P1(配方/机制进化)**:放开架构模块开关、主干替换;失败驱动定向优化(per-class IoU 最差类别);FunSearch 式搜索损失/增强函数(AlphaEvolve 级联 + 岛屿模型)。
- **P2(数据进化)**:伪标签自训练闭环(agent 生成标签 → 再训练 → 再评估,参考 PiSA/One Thing One Click);接入 SemanticKITTI/ScanNet 验证跨域;最后把结果沉淀回本仓库的 `benchmarks.md` / `papers.md`(知识库回写,让仓库从静态 awesome list 变成 agent 的可进化工作台——现有 paper-watcher 自动化是现成的第一步)。

---

## 7. 参考链接

**ML 工程 agent 与基准**
- MLAgentBench:[arXiv:2310.03302](https://arxiv.org/abs/2310.03302) · [GitHub](https://github.com/snap-stanford/MLAgentBench)
- AIDE:[arXiv:2502.13138](https://arxiv.org/abs/2502.13138) · [GitHub](https://github.com/WecoAI/aideml) · [PyPI](https://pypi.org/project/aideml/)
- InnoGym:[arXiv:2512.01822](https://arxiv.org/abs/2512.01822)
- MLGym:[arXiv:2502.14499](https://arxiv.org/abs/2502.14499) · [GitHub](https://github.com/facebookresearch/MLGym)
- DS-Agent:[arXiv:2402.17453](https://arxiv.org/abs/2402.17453) · [GitHub](https://github.com/guosyjlu/DS-Agent)
- MLE-bench:[arXiv:2410.07095](https://arxiv.org/abs/2410.07095) · [GitHub](https://github.com/openai/mle-bench) · [OpenAI 博客](https://openai.com/index/mle-bench/)
- AutoGluon / Optuna / NNI:[GitHub](https://github.com/autogluon/autogluon) / [GitHub](https://github.com/optuna/optuna) / [GitHub](https://github.com/microsoft/nni)

**自进化 / 进化式搜索闭环**
- AI Scientist v1:[arXiv:2408.06292](https://arxiv.org/abs/2408.06292) · [博客](https://sakana.ai/ai-scientist/) · [代码](https://github.com/SakanaAI/AI-Scientist);v2:[arXiv:2504.08066](https://arxiv.org/abs/2504.08066);Nature 版:[DOI 10.1038/s41586-026-10265-5](https://www.nature.com/articles/s41586-026-10265-5)
- FunSearch:[Nature](https://www.nature.com/articles/s41586-023-06924-6) · [代码](https://github.com/google-deepmind/funsearch)
- AlphaEvolve:[arXiv:2506.13131](https://arxiv.org/abs/2506.13131) · [博客](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- AgentBreeder:[arXiv:2502.00757](https://arxiv.org/abs/2502.00757) · [代码](https://github.com/jrosseruk/AgentBreeder);Promptbreeder:[arXiv:2309.16797](https://arxiv.org/abs/2309.16797)
- POISE:[arXiv:2603.23951](https://arxiv.org/abs/2603.23951)
- EvoPrompt:[arXiv:2309.08532](https://arxiv.org/abs/2309.08532);EvoAgent:[arXiv:2406.14228](https://arxiv.org/abs/2406.14228);STOP:[arXiv:2310.02304](https://arxiv.org/abs/2310.02304)
- HSI:[arXiv:2608.08466](https://arxiv.org/abs/2608.08466) · [代码](https://github.com/TailinZhou/hsi)
- RSI 综述:[arXiv:2607.07663](https://arxiv.org/abs/2607.07663);内省阈值:[arXiv:2607.04277](https://arxiv.org/abs/2607.04277);Noise-to-Meaning:[arXiv:2505.02888](https://arxiv.org/abs/2505.02888)
- AI Scientist 评审争议:[TechCrunch](https://techcrunch.com/2025/03/12/sakana-claims-its-ai-paper-passed-peer-review-but-its-a-bit-more-nuanced-than-that/)

**3D 专项与生态**
- PiSA:[arXiv:2503.10529](https://arxiv.org/pdf/2503.10529) · [代码](https://github.com/CG-ops/PiSA)
- One Thing One Click:[arXiv:2104.02246](https://arxiv.org/abs/2104.02246)
- Auto3DSeg:[教程](https://github.com/Project-MONAI/tutorials/tree/main/auto3dseg) · [模板](https://github.com/Project-MONAI/research-contributions/tree/main/auto3dseg)
- Pointcept:[GitHub](https://github.com/Pointcept/Pointcept) · Open3D-ML:[GitHub](https://github.com/isl-org/Open3D-ML) · semantic-kitti-api:[GitHub](https://github.com/PRBonn/semantic-kitti-api)
- SemanticKITTI:[官方](http://semantic-kitti.org/tasks.html) · ScanNet:[benchmark](https://kaldir.vc.in.tum.de/scannet_benchmark/) · S3DIS:[数据集](https://buildingparser.stanford.edu/)
- 仓库内相关条目:`label-efficient.md`([RePL](https://arxiv.org/abs/2604.06825)、[UniLiPs](https://arxiv.org/abs/2601.05105)、[LLM-Guided 主动学习](https://arxiv.org/abs/2505.18924)、[LaserMix](https://arxiv.org/abs/2207.00026))、`benchmarks.md`(SOTA 表与协议说明)

---

## 附:调研勘误记录(arXiv 编号核实)

调研过程中对 5 个编号做了 arXiv 交叉验证,4 个有误,均已在上文使用正确编号:

| 任务书编号 | 核实结果 | 正确论文 |
|---|---|---|
| MLGym 2411.17730 | ❌ 无关论文(Schrödinger 方程) | [arXiv:2502.14499](https://arxiv.org/abs/2502.14499) |
| DS-Agent 2402.02156 | ❌ 无关论文(τ-tilting theory) | [arXiv:2402.17453](https://arxiv.org/abs/2402.17453) |
| Self-Referential Self-Improving 2502.00757 | ❌ 该编号实为 AgentBreeder;精确标题在 arXiv 不存在 | [AgentBreeder](https://arxiv.org/abs/2502.00757);最接近标题为 [Promptbreeder](https://arxiv.org/abs/2309.16797) |
| "From AI Assistant to AI Scientist" 2502.08651 | ❌ 该编号是 AI Governance 论文 | [POISE, arXiv:2603.23951](https://arxiv.org/abs/2603.23951) |
| HSI 2608.08466 | ✅ 正确 | [arXiv:2608.08466](https://arxiv.org/abs/2608.08466) |
