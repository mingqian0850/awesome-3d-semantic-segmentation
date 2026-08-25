# LLM Agent 自动化机器学习工程/实验系统调研笔记

> 用途:为"LLM agent 驱动 3D 点云 / LiDAR 语义分割 (3DSS) 实验自动化"的可行性对比报告收集素材。
> 调研方式:多轮 web_search + 直接抓取 arXiv 摘要/HTML 全文、GitHub README/API、OpenAI 官方页面;每条关键信息均附来源 URL;查不到的数字一律标注"未找到公开数字"。
> 调研时间:2026-08(以抓取到的仓库/页面状态为准)。

## 0. 勘误说明(任务书中的 arXiv 编号有误)

- **MLGym** 的正确 arXiv 编号是 **2502.14499**;2411.17730 实为《Almost sure well-posedness and orbital stability for Schrödinger equation》(与 MLGym 无关)。
- **DS-Agent** 的正确 arXiv 编号是 **2402.17453**;2402.02156 实为《τ-tilting theory: a self-contained introduction》(与 DS-Agent 无关)。
- InnoGym **2512.01822** 核对无误。

---

## 1. MLAgentBench(Stanford)

### 1.1 来源
- 机构/年份:Stanford SNAP(Qian Huang、Percy Liang、Jure Leskovec),arXiv 2310.03302(2023-10 提交,2024-04 v2),ICML 2024 论文。
- URL:[arXiv:2310.03302](https://arxiv.org/abs/2310.03302) · [GitHub: snap-stanford/MLAgentBench](https://github.com/snap-stanford/MLAgentBench)

### 1.2 核心机制
- 13 个端到端 ML 实验任务(从 CIFAR-10 提升精度到 BabyLM 等近期研究问题,含 Kaggle 类任务)。
- Agent 基于 **ReAct 框架**:动作空间 = 读/写文件、执行代码、检查输出;在"接近人类研究者所见"的交互式环境里工作;可运行多个实验并分析结果。论文称其为 ResearchAgent(后续文献 MLAB 即指它)。
- 评估方式:对 agent 工作目录最终快照运行 evaluator 得到单一性能指标;**success 定义为相比 starter code baseline 提升 >10%**;聚合指标为 success rate 与平均提升幅度;效率按 wall-clock 时间与 token 数衡量。
- 日志/记忆:agent_log/main_log、agent_*.json(agent 状态)、env_log/traces(工作区快照)、trace.json(交互轨迹)。
- 支持模型:Claude v1.0 / v2.1 / v3 Opus、GPT-4 / GPT-4-turbo、Gemini-Pro、Mixtral;支持 langchain 与 autogpt agent 变体。

### 1.3 代表性效果数字
- 最佳为 **Claude v3 Opus,平均 success rate 37.5%**(arXiv 摘要原文:"a Claude v3 Opus agent ... with 37.5% average success rate")。
- 各任务 success rate 差异极大:老数据集(如 house-price)100%,训练数据截止之后出现的新 Kaggle 挑战低至 0%(arXiv 摘要)。
- GPT-4 平均 success rate 26%(论文成本分析段提及)。
- 实验设置:8 runs/agent;多数 run 限制 **50 个动作、最长 5 小时**(GPT-4 因 API 成本只允许 30 个动作)(论文 HTML)。
- 来源:[arXiv 摘要](https://arxiv.org/abs/2310.03302)、[论文 HTML](https://arxiv.org/html/2310.03302v2)。

### 1.4 资源成本
- 论文原文:"each run on each task only costs a few dollars. In total, running the entire benchmark with GPT-4-turbo once took 6 million tokens, which is around 60 dollars. However, with the low average success rate of 26%, the expected cost to accomplish a task becomes $231"。
- 即:单任务单 run 数美元;整 benchmark(13 任务)用 GPT-4-turbo 跑一遍约 600 万 token ≈ 60 美元;按成功率折算"达成一个任务"的期望成本 ≈ 231 美元。
- 来源:[论文 HTML 成本段](https://arxiv.org/html/2310.03302v2)。

### 1.5 代码可用性
- 开源,MIT 许可(GitHub API license: MIT,349 stars);提供 Docker 镜像(qhwang123/researchassistant);支持 OpenAI / Claude / CRFM / Gemini / HuggingFace API key。
- 来源:[GitHub 仓库](https://github.com/snap-stanford/MLAgentBench)、[GitHub API](https://api.github.com/repos/snap-stanford/MLAgentBench)。

### 1.6 3DSS 适配性判断
- 任务规模为 CIFAR-10 级别(单次训练分钟级),**未考虑"单次训练数小时~数天"的重训练场景**;50 动作/5 小时的预算在 3DSS 下可能连一次完整训练都跑不完。
- 论文明确指出 LM agent 的挑战:长期规划(long-term planning)与幻觉(arXiv 摘要)——这两点正是 3DSS 长训练轨迹下的痛点。
- 可复用组件:任务环境抽象、evaluator 设计、">10% 提升才算 success"的阈值化成功判定(对评估噪声大的场景有意义)。

---

## 2. AIDE(Weco AI)

### 2.1 来源
- 机构/年份:Weco AI(Zhengyao Jiang 等),arXiv 2502.13138(2025-02);被 OpenAI MLE-bench、METR RE-Bench 引用的 ML 工程 agent。
- URL:[arXiv:2502.13138](https://arxiv.org/abs/2502.13138) · [GitHub: WecoAI/aideml](https://github.com/WecoAI/aideml) · [PyPI: aideml](https://pypi.org/project/aideml/)

### 2.2 核心机制
- 把 ML 工程定义为"代码空间上的优化问题",把 trial-and-error 形式化为**解空间上的树搜索**。
- 三个算子:搜索策略 π(search policy,决定下一步探索哪个方向)、编码算子 f(coding,LLM 生成/修改代码)、摘要算子 Σ(T)(summarization,把已探索的方案树总结压缩进上下文,避免 prompt 过长)。
- 循环结构:生成多个候选草稿(draft)→ 每个草稿作为独立脚本执行评估(得到验证指标)→ 按指标对树剪枝、精化最有希望的方案 → 更新摘要 → 下一轮。
- 默认参数(README):code model 默认 gpt-4-turbo、`agent.steps=20`、`agent.search.num_drafts=5`。
- 记忆/日志:保留 `best_solution.py`、`tree_plot.html`(解树可视化);"node-level code 简洁、每次 LLM 调用聚焦局部问题(如只调试最有希望的脚本)"(论文 4.2)。
- 来源:[GitHub README](https://github.com/WecoAI/aideml)、[论文 HTML](https://arxiv.org/html/2502.13138v1)。

### 2.3 代表性效果数字
- 自家 Weco-Kaggle(63 个 Kaggle 竞赛):AIDE+GPT-4 Turbo **超过 51.38% 的人类参赛者、50.00% 达中位数**;基线对比 H2O AutoML(35.34% / 18.75%)、AutoGPT+LangChain(32.34% / …)(论文 4.1 表)。
- MLE-bench(OpenAI 官方评测):**AIDE+o1-preview 在 16.9% 的竞赛中(单次 pass@1)获得奖牌,约为次优线性 agent(OpenHands)的 4 倍**;两者都用 GPT-4o 时 AIDE 奖牌数约为 OpenHands 的 2 倍(论文 4.2;README 亦写 "wins 4× more medals than the best linear agent (OpenHands)")。
- MLE-bench Lite:o1-preview 单独 valid submission rate 63.6%±4.5% → 加 AIDE 后 **92.4%±2.6%**(论文 4.2)。
- METR RE-Bench(7 个 AI R&D 环境):AIDE+o1-preview **在 6 小时内超过人类科学家的平均分**;在 "Optimize a Kernel" 任务上超过 9 位人类专家 64 小时内的最佳(Triton 优化);但在需要大代码库/多步交互的任务(Rust CodeContests)上落后(论文 4.3)。
- 来源:[论文 HTML](https://arxiv.org/html/2502.13138v1)、[GitHub README](https://github.com/WecoAI/aideml)。

### 2.4 资源成本
- LLM 推理成本(Weco-Kaggle,GPT-4 Turbo,2024 年初价格):**每任务多数 <$1.50,最高约 $2.50**(论文 B.2 Cost Analysis)。
- 注意:这是 LLM API 成本,**不含**训练/评估的计算成本;AIDE 本身是计算换性能("trades computational resources for enhanced performance",arXiv 摘要)。
- 单次实验的 GPU/美元总额:未找到公开汇总数字。

### 2.5 代码可用性
- 开源 MIT(1.5k stars,GitHub API);`pip install aideml`;CLI + Python API + Streamlit Web UI + HTML 树可视化;模型中立(OpenAI / Anthropic / Gemini / 兼容 OpenAI API 的本地模型)。
- 来源:[GitHub 仓库](https://github.com/WecoAI/aideml)、[GitHub API](https://api.github.com/repos/WecoAI/aideml)。

### 2.6 3DSS 适配性判断
- AIDE 面向表格/轻量深度学习 Kaggle 任务,评估假设是"单次执行便宜且快";3DSS 单次训练数小时~数天、GPU 昂贵 → 直接套默认参数(20 steps × 5 drafts)每次全量训练会爆炸(**按公开默认参数推算:20×5=100 次训练调用,若每次 2 小时 A10,约 200 GPU 小时/任务,此为推算而非公开数字**)。
- 但其"解节点独立可评估 + 按指标剪枝 + 摘要算子压缩上下文"的抽象很适合重训练场景的变体:把评估换成小规模 warm-up/代理指标即可。
- README/论文均未提及 3D/点云/LiDAR 场景。

---

## 3. InnoGym(浙江大学)

### 3.1 来源
- 机构/年份:浙江大学(ZJU,Ningyu Zhang 团队;Jintian Zhang 等 13 位作者),arXiv 2512.01822(2025-12 v1,2026-02 v2),**ICLR 2026**。
- URL:[arXiv:2512.01822](https://arxiv.org/abs/2512.01822)

### 3.2 核心机制
- 定位:衡量 agent **创新能力(innovation potential)** 的基准+框架,而非单纯的正确率。
- 两个互补指标:
  - **Performance Gain**:新解相对"已知最优解集合 S_known"的性能提升;
  - **Novelty**:新解与已有方法的方法级差异(代码级 + 高层方法设计级距离)。
- iBench:18 个真实工程/科学任务(NIPS 竞赛、GMCM 数学建模、经典问题如 BEETL、Belka、CirclePacking、CDML、NPR 等),构建时按"资源可访问性、计算成本(CPU/GPU 内存、磁盘、运行时间)可行"过滤;其中 **10 个为主评估子集**;每个任务收集已知解集合以计算 Novelty。
- iGym:统一执行环境,提供长时任务鲁棒恢复、**原生并发(并行工具调用+依赖感知调度)**、统一工具管理,使不同 scaffold 在相同基础设施下可比。
- 对比的三种 ML 工程 agent scaffold(论文 4.1,称沿用 MLE-bench 的选择):
  - **MLAB**(MLAgentBench 的 ResearchAgent):ReAct 风格,自然语言规划,高层动作(读写文件、跑训练脚本、查日志),在 Kaggle 式工作区迭代;
  - **CodeAct**(OpenHands):把所有动作统一为可执行 Python 代码;
  - **AIDE**:树搜索式。
- 主干模型 **DeepSeek-v3.1**,另测 GPT-5、Gemini-2.5-Pro;每任务-每 agent-每模型配置**最多 12 小时 wall-clock**(或提交后提前终止)。
- 来源:[arXiv HTML](https://arxiv.org/html/2512.01822v2)。

### 3.3 代表性效果数字
- 论文结论性发现(未逐任务列全):
  - "当前 agent 在复杂任务上仍**显著低于人类 SOTA**";
  - "**MLab 在 Performance Gain 与 Novelty 两项上都领先**,CodeAct 和 AIDE 均落后(可能因对复杂文件结构与工具使用处理较弱)";
  - "CodeAct 在 CirclePacking 上接近 SOTA,说明其在明确定义的数学优化上强,但不能泛化到更广任务";
  - 核心结论:"**鲁棒性优先于新颖性**——一些 agent 能产出新颖方法,但鲁棒性不足,导致新颖性无法转化为性能增益"(论文 4 章与摘要)。
- 逐任务数字见论文 Table 2(如 BEETL(MI) 上 MLAB:gain ratio -35.66 / novelty 66.67,多数任务 gain 为负)。
- 来源:[arXiv HTML](https://arxiv.org/html/2512.01822v2)、[arXiv 摘要](https://arxiv.org/abs/2512.01822)。

### 3.4 资源成本
- 任务筛选阶段即要求"计算成本可行";主评估每配置上限 12 小时;单次运行美元成本:**未找到公开数字**。

### 3.5 代码可用性
- 论文提及 iGym 代码在 `github.com/zjunlp/igym`(arXiv HTML),但**截至调研(2026-08)该仓库返回 404,不可公开访问**;论文全文/HTML 公开。
- 来源:[arXiv HTML](https://arxiv.org/html/2512.01822v2)。

### 3.6 3DSS 适配性判断
- 任务为数学优化/竞赛级,无 3D 点云/LiDAR;但其核心发现直接适用于 3DSS:**评估噪声大(鲁棒性差)时,agent 产出的"新颖"方案不会转化为 mIoU 增益**——3DSS 评测 agent 时应同时看"是否显著超越基线"与"是否稳定复现"。
- iGym 的"长时任务恢复 + 原生并发"是重训练(单次数小时)场景下 agent 基础设施的明确需求点。

---

## 4. MLGym(Meta FAIR)

### 4.1 来源
- 机构/年份:Meta GenAI/FAIR + UCSB/UCL 等(Deepak Nathani 等 17 位作者),arXiv **2502.14499**(2025-02)。
- URL:[arXiv:2502.14499](https://arxiv.org/abs/2502.14499) · [GitHub: facebookresearch/MLGym](https://github.com/facebookresearch/MLGym)

### 4.2 核心机制
- **第一个面向 ML 任务的 Gym 环境**,目标之一是支持用 RL 算法训练 agent 的研究。
- Agent 通过 **shell 命令**与 docker/podman 沙箱环境交互(任意 bash 命令),可执行任何代码。
- 四个核心组件:Agents(LLM 包装器 + history processors + cost management)、Environment、Datasets、Tasks。
- 工具:文件编辑/查看/搜索、**validate**(运行 eval 脚本返回测试集分数,可反复使用)、**submit**(终局动作,终止轨迹并记录)、文献搜索(Semantic Scholar)、PDF 解析、**memory 模块**(memory_write/memory_read,跨长轨迹保存最佳配置/关键洞察;论文称无 memory 时轨迹超长导致模型遗忘早期最优配置)。
- 预算控制:**单次 agent run 限制 50 步**(与环境交互次数),超限后自动提交最后代码状态;**每个任务另有训练命令超时**(如 CIFAR-10 训练超时 30 分钟),防止 agent 无限加大模型。
- 13 个任务:CIFAR-10、Fashion MNIST、MS-COCO、MNLI、Language Modeling、Breakout、3-SAT、博弈论(Blotto 等)等;任务用配置文件定义(数据集、只读 eval 脚本、conda 环境、starter code、训练超时、GPU 配额)。
- 评估指标:**AUP@4**(performance profile 曲线下面积,源自 AutoML Decathlon 竞赛)。
- 来源:[arXiv HTML](https://arxiv.org/html/2502.14499v1)、[GitHub README](https://github.com/facebookresearch/MLGym)。

### 4.3 代表性效果数字
- 5 个模型 × 4 seeds,AUP@4(表 4):**OpenAI O1-preview 最佳**(Best Attempt 1.150 / Best Submission 1.176);Claude-3.5-Sonnet 1.142/1.135;Gemini-1.5-Pro 1.140/1.125;GPT-4o 1.000/1.029;Llama-3.1-405b 1.015/1.039。
- 论文结论:"**前沿模型能改进给定 baseline,但主要通过找到更好的超参;不能产生新的假设、算法、架构或实质性改进**"(摘要)。
- 每 run 平均 token 用量(表 8):Claude-3.5-Sonnet 约 70.8 万输入、GPT-4o 约 26.7 万、o1-preview 约 36.9 万输入 + 6.1 万输出。
- 来源:[arXiv HTML](https://arxiv.org/html/2502.14499v1)。

### 4.4 资源成本
- 论文有 "Computational Cost" 章节:API cost(USD)对 AUP@4 的帕累托曲线(图 3);任务表给出**平均 agent runtime**(如 CIFAR-10 约 4 小时/1 GPU、Fashion MNIST 约 2 小时/1 GPU、Language Modeling 约 4 小时/2 GPU)与训练超时;
- 单次运行总美元成本:**未找到单一公开数字**。
- 许可为 **CC BY-NC 4.0(非商用)**(README badge),商业使用受限。

### 4.5 代码可用性
- 开源(619 stars,GitHub API),但 CC BY-NC 4.0;需 Docker 或 Podman + nvidia-container-toolkit(GPU 容器);提供 `aigym/mlgym-agent` 容器镜像与轨迹可视化器。
- 来源:[GitHub 仓库](https://github.com/facebookresearch/MLGym)、[GitHub API](https://api.github.com/repos/facebookresearch/MLGym)。

### 4.6 3DSS 适配性判断
- 任务含 CV(MS-COCO 等)但无点云/LiDAR;**其"50 步预算 + 每任务训练超时 + 自动提交"机制正是重训练场景必需的护栏**(3DSS 下应把训练超时设为小时级并限制评估次数)。
- memory 模块解决"长轨迹中遗忘最优配置"的问题,3DSS 一次 agent run 可能跨越多个多小时训练,同样需要持久化记忆。
- 未涉及 3DSS 特有的评估噪声(如 mIoU 方差)与小时级单次训练。

---

## 5. DS-Agent(清华 + 吉林大学)

### 5.1 来源
- 机构/年份:清华大学(Siyuan Guo、Cheng Deng、Ying Wen、Jun Wang)+ 吉林大学(Hechang Chen、Yi Chang),arXiv **2402.17453**(2024-02),ICML 2024。
- URL:[arXiv:2402.17453](https://arxiv.org/abs/2402.17453) · [GitHub: guosyjlu/DS-Agent](https://github.com/guosyjlu/DS-Agent)(官方实现,242 stars;另有镜像 [Sahanduiuc/Data-Science-Agent](https://github.com/Sahanduiuc/Data-Science-Agent))

### 5.2 核心机制
- LLM agent + **案例推理(CBR,case-based reasoning)**,两个阶段:
  - **开发阶段**:按 CBR 框架(检索→复用→评估→修正→保留)构建自动迭代管线,从 Kaggle 检索/复用人类专家经验(案例)生成实验计划,并根据执行反馈迭代修正计划;
  - **低资源部署阶段**:简化 CBR,直接把开发阶段沉淀的成功方案适配生成代码,**显著降低对 LLM 基础能力的要求**。
- 多角色 prompt 设计:RankReviser、Planner、Programmer、Debugger、Logger、Adapter(附录 D)。
- 评估:开发阶段 success rate(固定步数内无 bug 建好模型)、部署阶段 one-pass rate(仅一次尝试即成功)、模型性能用 mean rank / best rank;30 个数据科学任务(12 开发 + 18 部署,六类:表格分类/回归、文本回归、时间序列等)。
- 与传统 AutoML 的关系:论文对比 AutoGluon,指出其"不天然支持多任务分类等设置,用户需重构为多个单任务"。
- 来源:[论文 HTML](https://arxiv.org/html/2402.17453)。

### 5.3 代表性效果数字
- 开发阶段:GPT-4 在 12 个任务上 **100% success rate**;部署阶段 GPT-3.5 / GPT-4 one-pass rate **85% / 99%**,最佳 baseline 仅 56% / 60%;开源 LLM Mixtral-8x7b 的 one-pass rate 从 **6% 提升到 31%**。
- 来源:[论文 HTML](https://arxiv.org/html/2402.17453)(4 章)。

### 5.4 资源成本
- 单 run 美元成本(论文表 4,GPT API 费用,不含计算):开发阶段 GPT-3.5 **$0.06**、GPT-4 **$1.60**;低资源部署阶段 **$0.0045 / $0.135**(成本降低 92.5% / 91.5%)。
- 来源:[论文 HTML](https://arxiv.org/html/2402.17453)。

### 5.5 代码可用性
- 论文声明 data 与 code 开源([arXiv 摘要](https://arxiv.org/abs/2402.17453));官方实现仓库 [guosyjlu/DS-Agent](https://github.com/guosyjlu/DS-Agent)(无 LICENSE 文件,GitHub API);基于 ChatGPT API,含完整 prompt 设计。

### 5.6 3DSS 适配性判断
- 面向表格/文本/时序的 CPU 级训练,非深度学习重训练场景;
- 其"**开发阶段(贵、多轮)沉淀案例 → 部署阶段(便宜、单轮)直接生成代码**"的两段式思路,契合 3DSS"希望少迭代、直接拿到可用配置"的诉求;
- 成本数字($0.13~$1.60/run)说明 LLM API 成本远低于 GPU 训练成本——3DSS 场景中 agent 的 token 开销几乎可忽略,瓶颈是训练计算。
- 未涉及 3D/点云。

---

## 6. OpenAI MLE-bench(基准本身及系统表现)

### 6.1 来源
- 机构/年份:OpenAI(Chan Jun Shern 等),arXiv 2410.07095(2024-10),ICLR 2025;官方博客 2024-10。
- URL:[arXiv:2410.07095](https://arxiv.org/abs/2410.07095) · [GitHub: openai/mle-bench](https://github.com/openai/mle-bench)(官方 leaderboard 在 README) · [OpenAI 博客](https://openai.com/index/mle-bench/)

### 6.2 核心机制(基准本身,不是 agent)
- **75 个 Kaggle 竞赛**,重新划分 train/test + 本地 grading 代码;人类基线直接用 Kaggle 公开排行榜;奖牌(青铜/银/金)按 private leaderboard 分位逻辑施加到全部竞赛;**headline metric = Any Medal %**。
- 官方推荐评测设置(README "Benchmarking"):每竞赛 **24 小时**运行时间;计算资源 **36 vCPUs + 440GB RAM + 单张 24GB A10 GPU**;**至少 3 seeds**,文档原文强调 "agents/LLMs can be quite high-variance!"。
- 初始评测的三个开源 scaffold:**AIDE**、**MLAB**(MLAgentBench ResearchAgent)、**OpenHands**(CodeActAgent)。
- 来源:[GitHub README](https://github.com/openai/mle-bench)、[论文 HTML](https://arxiv.org/html/2410.07095)。

### 6.3 代表性效果数字(官方 leaderboard + 论文)
- 论文主结果:**o1-preview + AIDE(pass@1)在 16.9% 竞赛中获得至少铜牌**;pass@8 提升到 **34.1%**;GPT-4o 24 小时 → 8.7%,放宽到 100 小时 → 11.8%。
- 初始三 scaffold 对比(GPT-4o):AIDE 8.7% > OpenHands 4.4% > MLAB 0.8%(论文 3.1;leaderboard 上对应 8.63 / 4.89 / 1.60)。
- 官方 leaderboard(2026-08 抓取,All = 全部 75 竞赛 Any Medal %):
  - AIDE + o1-preview:**17.12±0.61**;AIDE + gpt-4o:8.63±0.54;AIDE + claude-3-5-sonnet:7.56;AIDE + llama-3.1-405b:3.33;OpenHands + gpt-4o:4.89;MLAB + gpt-4o:1.60。
  - 2025–2026 年新系统(同一评测协议):Famou-Agent 2.0 (Gemini-3-Pro) 64.44、AIBuildAI 63.11、CAIR MARS+ 62.67、MLEvolve 61.33、PiEvolve 61.33、ML-Master 2.0 56.44、AIRA-dojo (o3) 31.60、ML-Master (deepseek-r1) 29.33、R&D-Agent (o1-preview) 22.40 等;leaderboard 自 **2026-04-24** 起暂停接收新提交。
- 硬件扩展实验(GPT-4o+AIDE):CPU-only 9.1%、标准 1×A10 8.7%、2×A10 10.2% —— "性能相似,且人工检查日志未发现 agent 尝试使用第二张 GPU";时间扩展:24h→100h,8.7%→11.8%。
- 论文定性结论:"agent 在能用已知方法解决的竞赛上表现好,但在**调试与从失误中恢复**上挣扎"。
- 来源:[GitHub README(leaderboard)](https://github.com/openai/mle-bench)、[论文 HTML](https://arxiv.org/html/2410.07095)。

### 6.4 资源成本
- 官方环境:24 小时 × 36 vCPU × 440GB RAM × 1×A10 GPU(每竞赛每 seed);论文在 Limitations 中直言:"**由于计算与 token 成本,用户可能难以完全复现我们的实验**"。
- 单竞赛美元成本:**未找到公开汇总数字**(涉及 GPU 集群与 LLM API 双重开销)。

### 6.5 代码可用性
- 开源:repo 含数据集构建、评估逻辑、评测过的 agents;论文 license CC BY 4.0(GitHub API 显示 NOASSERTION);1.7k stars。
- 来源:[GitHub 仓库](https://github.com/openai/mle-bench)、[GitHub API](https://api.github.com/repos/openai/mle-bench)。

### 6.6 3DSS 适配性判断
- 竞赛含 CV/信号处理,但无点云/LiDAR 分割;**"单任务 24 小时 + 单张 A10"的预算量级与 3DSS 一次全量训练相当**——即一个 MLE-bench run 大致等于 3DSS 的一次训练,agent 循环几乎无法在预算内做多轮迭代。
- "pass@k 显著提升(16.9%→34.1%)"与"多 seed 方差大"直接对应 3DSS 的评估噪声问题:评测 agent 必须多 seed + 阈值化判定,不能拿单次 mIoU 当信号。
- 硬件实验结论(agent 不会自动用第二张 GPU)提示:3DSS 多卡并行需要做成显式工具给 agent,而不是指望它自己分配资源。

---

## 7. 传统 AutoML 对照:AutoGluon / Optuna / NNI

> 简述与 LLM agent 的差异(三者为"结构化搜索空间 + 数值优化器",无 LLM、无自由代码动作空间、无自然语言理解)。

### 7.1 AutoGluon(Amazon)
- 来源:Amazon,2019 起,[GitHub: autogluon/autogluon](https://github.com/autogluon/autogluon)(Apache-2.0,约 10.6k stars);官方描述 "Fast and Accurate ML in 3 Lines of Code"。
- 机制:表格/图像/文本/多模态 AutoML;自动数据清洗、特征工程、多模型 **stacking/bagging 集成**;用户只需给数据+任务,无需写训练代码;不生成/修改训练代码,而是搜索模型与集成策略。
- 与 LLM agent 的差异:无代码动作空间、不可跨库组合工具、不可读日志做长时推理;但确定性、低成本、可复现。DS-Agent 论文指出其不天然支持多任务分类等设置(需用户重构)。
- 3DSS 相关性:对小规模超参/集成可行,但无法自主完成"改网络结构→改预处理→跑训练→读日志→再改"的闭环;3DSS 通常需自定义网络与数据管线,超出其能力。
- 来源:[GitHub 仓库](https://github.com/autogluon/autogluon)、[GitHub API](https://api.github.com/repos/autogluon/autogluon)。

### 7.2 Optuna(Preferred Networks)
- 来源:Preferred Networks,2019 起,[GitHub: optuna/optuna](https://github.com/optuna/optuna)(MIT);官方定位 "A hyperparameter optimization framework"。
- 机制:**define-by-run** API 动态构建搜索空间;TPE 等高效采样器 + 剪枝(pruning);可并行扩展到数十~数百 worker(README 关键特性)。
- 与 LLM agent 的差异:只优化给定搜索空间内的超参,不写代码、不选架构、不理解数据;无 LLM 成本。
- 3DSS 相关性:3DSS 中常用于学习率/epoch 等超参搜索,但对架构选择、数据增强策略无能为力;可作为 LLM agent 的"内部调参工具"与之组合。
- 来源:[GitHub 仓库](https://github.com/optuna/optuna)。

### 7.3 NNI(Microsoft)
- 来源:Microsoft,2018 起,[GitHub: microsoft/nni](https://github.com/microsoft/nni)(MIT,约 14.4k stars);官方定位:自动化特征工程、**神经架构搜索(NAS)**、超参调优、模型压缩。
- 机制:多 trial 分布式搜索,支持多种 tuner(含 NAS);注意:**官方仓库已 archived(最后 push 2024-07),开发停滞**(GitHub API)。
- 与 LLM agent 的差异:搜索空间需显式定义(架构/超参),无代码生成与自由推理;对 NAS 有历史贡献但维护已停止。
- 3DSS 相关性:其 NAS 思路(如 3D 点云骨干搜索)与 LLM agent 的代码级搜索不同——LLM agent 在"语义空间"改代码,NNI 在"定义好的结构空间"搜;NNI 停止维护,不建议新项目依赖。
- 来源:[GitHub 仓库](https://github.com/microsoft/nni)、[GitHub API](https://api.github.com/repos/microsoft/nni)。

---

## 8. 对比总表

| 系统 | 机构/年份 | 核心机制 | 动作空间 | 单次成本(公开数字) | 代码可用性 | 3DSS 适配度 |
|---|---|---|---|---|---|---|
| MLAgentBench | Stanford SNAP, 2023 | ReAct 式研究 agent,13 个 ML 实验任务 | 读写文件/执行代码/查输出 | 单任务单 run 数美元;整 benchmark(GPT-4-turbo)≈600 万 token ≈ $60;期望完成成本 $231 | 开源 MIT + Docker 镜像 | 低:任务分钟级训练;但"成功率+阈值判定"设计可借鉴 |
| AIDE | Weco AI, 2025 | 代码空间树搜索(搜索策略+编码+摘要算子) | 生成/修改 Python 脚本并执行评估 | LLM 成本每任务 <$1.50(最高 ~$2.50,不含计算) | 开源 MIT + PyPI + WebUI | 中:树搜索抽象可借鉴,但默认参数在 3DSS 下预算爆炸(推算 ~100 次训练调用) |
| InnoGym | 浙大, 2025 (ICLR'26) | 创新力基准:Performance Gain + Novelty;iGym 统一环境对比 MLAB/CodeAct/AIDE | 取决于 scaffold(文件/代码/树搜索) | 未找到公开美元数字;每配置 ≤12h | 论文开源;iGym 仓库 404 未公开 | 中:结论"鲁棒性优先于新颖性"直接适用;并发/长任务恢复是需求点 |
| MLGym | Meta FAIR, 2025 | 首个 ML 任务 Gym 环境(为 RL 训练 agent 设计) | shell 命令 + 工具(编辑/validate/submit/记忆) | 未找到单一美元数字;任务表给出平均 runtime(如 CIFAR-10 4h/1GPU) | 开源但 **CC BY-NC 4.0 非商用** | 中高:50 步预算+训练超时+memory 模块是重训练场景的护栏范本 |
| DS-Agent | 清华+吉大, 2024 (ICML'24) | LLM+CBR 两段式(开发迭代/部署低资源直出代码) | 生成实验计划与代码(多角色 prompt) | 开发 $0.06~$1.60/run,部署 $0.0045~$0.135/run(GPT API,不含计算) | 开源(无 LICENSE 文件) | 中:两段式"沉淀案例→低成本复用"契合"少迭代出配置"诉求 |
| MLE-bench | OpenAI, 2024 (ICLR'25) | 基准:75 个 Kaggle 竞赛,Any Medal %;官方 24h/1×A10/≥3 seeds | 取决于 scaffold(AIDE/MLAB/OpenHands) | 未找到单竞赛美元汇总;官方承认难复现(计算+token 成本) | 开源(论文 CC BY 4.0) | 中:预算量级≈3DSS 单次训练;多 seed/方差发现直接相关 |
| AutoGluon | Amazon, 2019 | 传统 AutoML:数据清洗+特征工程+stacking 集成 | 无代码动作空间(配置驱动) | 无 LLM 成本;计算视数据规模 | 开源 Apache-2.0 | 低:仅小规模/表格类任务;不可闭环改代码 |
| Optuna | Preferred Networks, 2019 | 超参优化:define-by-run + 剪枝 + 并行 | 超参搜索空间 | 无 LLM 成本;计算视 trial 数 | 开源 MIT | 低-中:可作 3DSS 超参调优工具,可嵌入 agent 作内部工具 |
| NNI | Microsoft, 2018 | AutoML 工具包:HPO/NAS/特征工程/压缩 | 定义好的结构搜索空间 | 无 LLM 成本 | 开源 MIT,但 **已 archived 停更** | 低:NAS 思路可参考,维护已停止 |

## 9. 对 3DSS 可借鉴点

1. **训练预算护栏是刚需**:MLGym 的"50 步限制 + 每任务训练超时 + 自动提交"与 MLE-bench 的"24h/单卡"证明,重训练场景必须显式约束"单次训练时长 × 迭代次数";3DSS(单次数小时~数天)建议先在降采样/少 epoch 的 warm-up 子集上让 agent 迭代,全量训练仅作最终验证(依据:MLGym 论文训练超时设计、MLE-bench 官方设置)。
2. **评估噪声必须显式处理**:MLE-bench 官方要求 ≥3 seeds 且明言 "agents/LLMs can be quite high-variance!";MLAgentBench 用">10% 提升才算 success"的阈值;InnoGym 结论"新颖性不转化为增益,鲁棒性优先"——3DSS 的 mIoU 方差大,agent 反馈信号应先做多 seed 聚合或显著阈值判定,避免把噪声当提升(依据:MLE-bench README、MLAgentBench 论文、InnoGym 论文)。
3. **先沉淀案例库,再做少迭代部署**:DS-Agent 两段式(开发阶段 $1.60/run 迭代沉淀 → 部署阶段 $0.135/run 直接出码)说明:3DSS 应先用人工积累 2–3 个高质量基线(如 PointNet++/MinkUNet 配置)作案例,让 agent 基于案例微调而非从零探索(依据:DS-Agent 论文成本与机制)。
4. **并行要显式做成工具,不能指望 agent 自己用多卡**:MLE-bench 硬件实验显示 agent 不会自动利用第二张 GPU;3DSS 若要多卡/多候选并行,应把 fan-out 做成显式 API/工具(参考 iGym 的原生并发与依赖感知调度、MLGym 的并发工具)(依据:MLE-bench 论文 3.3、InnoGym 论文 iGym 部分)。
5. **成本核算以 GPU 小时为主、LLM token 为辅**:AIDE 每任务 LLM 成本 <$1.5、DS-Agent 每 run ≤$1.60、MLAgentBench 单 run 数美元,均远低于一次 3DSS 训练的 GPU 成本;因此 agent 设计应最小化训练调用次数(减少评估频率、用代理指标/早停),LLM 推理开销可忽略(依据:AIDE 论文 B.2、DS-Agent 论文表 4、MLAgentBench 论文成本段)。
