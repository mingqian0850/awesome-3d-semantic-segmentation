# LLM 驱动的自进化 / 进化式搜索闭环 —— 调研笔记

> 目标场景:3D 点云 / LiDAR 语义分割(3D semantic segmentation,3DSS)的自主研究闭环
> 调研日期:2026-08(基于 arXiv 收录时间与检索结果)
> 调研方法:多轮 web_search + arXiv API / Semantic Scholar API / Crossref API / 官方博客原文核对;**所有数字均来自原文或官方来源,未查到的一律标注"未公开/未找到公开资料"**。

---

## 0. 重要勘误(编号核实结果)

调研开始时对用户提供的两个 arXiv 编号做了逐条核实,发现编号与论文不符,已找到真实论文:

| 任务描述 | 用户提供编号 | 核实结果 | 真实论文 |
|---|---|---|---|
| "Self-Referential Self-Improving Systems (Yu et al.)" | arXiv 2502.00757 | ❌ 2502.00757 实为 **AgentBreeder**(Rosser & Foerster 等,牛津大学) | 精确标题 "Self-Referential Self-Improving Systems" 在 arXiv 上**未找到**;最接近的论文是 **Promptbreeder**(arXiv 2309.16797,"Self-Referential Self-Improvement Via Prompt Evolution")。本节同时覆盖 AgentBreeder 与 Promptbreeder 以防意图偏差 |
| "From AI Assistant to AI Scientist" | arXiv 2502.08651 | ❌ 2502.08651 实为 "Democratizing AI Governance: Balancing Expertise and Public Participation" | 真实论文为 **arXiv 2603.23951**(2026-03) |
| "Hierarchical Self-Improvement" | arXiv 2608.08466 | ✅ 编号正确 | 标题一致 |

> 核实方式:curl arXiv 抽象页 `<title>` + arXiv export API + Semantic Scholar Graph API,三次交叉验证。

---

## 1. The AI Scientist (Sakana AI) v1 / v2 / Nature 版

### 1.1 来源
- v1:Sakana AI + UBC + Oxford,"The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery",arXiv:2408.06292(2024-08);代码 https://github.com/SakanaAI/AI-Scientist ;官方博客 https://sakana.ai/ai-scientist/
- v2:"The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search",arXiv:2504.08066(2025-04);代码 https://github.com/SakanaAI/AI-Scientist-v2
- Nature 正式版:2026-03-26 发表于 Nature,DOI 10.1038/s41586-026-10265-5,博客 https://sakana.ai/ai-scientist-nature/

### 1.2 核心机制:自动科研 pipeline(进化循环的"科研版")
v1 的四阶段闭环(每篇论文一轮,可开放重复):
1. **想法生成(Idea Generation)**:基于给定代码模板(如 nanoGPT),LLM 生成候选研究想法,并用"新颖性检查器"(查重/查相关文献)过滤。
2. **实验(Experiment)**:自动写代码、跑训练、记录指标。
3. **论文写作(Paper Writing)**:自动写 LaTeX 论文(标题/摘要/正文/图表/参考文献)。
4. **自动评审(Automated Review)**:LLM 审稿人打分,模拟 ICLR 评审格式;得分反馈用于迭代。

v2 的关键升级(arXiv:2504.08066 摘要):
- 去掉 v1 依赖的人类代码模板,可跨 ML 领域泛化;
- **渐进式 agentic tree-search(progressive agentic tree search)**:由专门的"实验管理 agent"组织,并行探索多个实验分支;
- 审稿人升级为 **VLM(视觉语言模型)反馈回路**,对图表的内容与美观做迭代优化;
- 成果:把 3 篇全自动论文投给 ICLR workshop 盲审,**1 篇得分超过人类平均接受线**——据称是"首个完全 AI 生成并通过同行评审的论文"(该声明后续有争议,见 1.5)。

Nature 版(2026-03-26):把上述工作整理发表,并新增"审稿人评分随基础模型能力提高而提高"的 scaling law 观察(https://sakana.ai/ai-scientist-nature/)。

### 1.3 代表成果与量化结果
- v1:三个子领域(diffusion、transformer、learning dynamics)各产出一批论文,自动审稿人判定部分论文"超过顶会接受阈值";自动审稿人评分与人类审稿人相关性接近人类间一致性(https://arxiv.org/abs/2408.06292)。
- v2:ICLR workshop 盲审,1/3 论文超过人类平均接受线(arXiv:2504.08066 摘要;TechCrunch 报道 https://techcrunch.com/2025/03/12/sakana-claims-its-ai-paper-passed-peer-review-but-its-a-bit-more-nuanced-than-that/)。
- Nature 版:审稿人分数与基础模型能力呈清晰 scaling law(https://sakana.ai/ai-scientist-nature/)。

### 1.4 资源成本
- v1 论文明确:**每篇论文 <$15(GPT-4o 时代)**,"compute efficient"(arXiv:2408.06292 摘要;"~$15 per paper" 亦见 https://sakana.ai/ai-scientist/ 与 https://the-decoder.com/automated-research-the-ai-scientist-generates-papers-for-15-dollars-each/)。
- v2 / Nature 版:具体美元数**未公开**。

### 1.5 已知局限 / 失败模式
- 论文质量有"偶发缺陷"(Sakana 自己在博客承认:"there are still occasional flaws in the papers produced by this first version",https://sakana.ai/ai-scientist/)。
- v2"通过同行评审"的声明被媒体质疑:Nature 曾报道 AI 生成论文在**计划撤回前**通过了评审流程(https://the-decoder.com/ai-generated-paper-passes-peer-review-before-planned-withdrawal/),暗示评审流程对 AI 论文的审查有效性存疑;TechCrunch 也指出"more nuanced than that"(https://techcrunch.com/2025/03/12/...)。
- 只限于**计算类实验**(Nature 博客原文:"The AI Scientist is limited to computational experiments",https://sakana.ai/ai-scientist-nature/)。
- 伦理/治理风险:淹没同行评审系统、伪造科研履历(博客自述,https://sakana.ai/ai-scientist-nature/)。

### 1.6 对 3DSS 的可借鉴点
- **闭环模板直接可用**:idea 生成 → 实验执行 → 报告写作 → 自动评审,这套骨架与 3DSS 的"改方法 → 训练 → 报 mIoU"天然同构;差别只在实验成本(3DSS 单次训练远贵于 $15/paper 的 nanoGPT 级实验)。
- **审稿人即评估器**:LLM 审稿人可以充当"研究方向的自动把关人",用于筛选候选改进(损失函数、模块设计),避免人工阅读所有实验日志。
- **VLM 图表反馈**(v2)对 3DSS 可视化(点云语义图、混淆矩阵)的报告质量提升有直接借鉴价值。
- 注意:3DSS 无法直接套用"每轮 <$15"假设,成本结构需单独核算(见 §9)。

---

## 2. FunSearch (DeepMind, Nature 2023)

### 2.1 来源
- DeepMind,"Mathematical discoveries from program search with large language models",Nature 625:468–475(2024-01-18 刊出;2023-12 上线);DOI 10.1038/s41586-023-06924-6;https://www.nature.com/articles/s41586-023-06924-6 ;代码 https://github.com/google-deepmind/funsearch
- **无 arXiv 预印本**(经 arXiv API 两次检索确认无匹配记录),以 Nature 全文为准。

### 2.2 核心机制:LLM 作为变异算子的进化程序搜索
- 目标:搜一个 **Python 函数(程序)**,而非解本身;输入是问题的 `evaluate` 函数(打分器)+ 一个初始平凡实现 + 可选骨架。
- 循环:从 **programs database(程序库)** 采样若干高分程序拼成 prompt → 喂给预训练 LLM(Codey,基于 PaLM2)→ LLM 生成新程序(即"变异")→ 执行 `evaluate` 打分 → 正确程序存回程序库,循环往复。
- **多样性机制(关键)**:程序库采用 **islands model(岛屿模型/多群体遗传算法)**,多个子种群独立进化;库内按"签名(在若干测试集上的得分向量)"聚簇,采样时偏向高分且更短的程序;定期让信息在岛屿间流动。论文明确说多样性是避免局部最优的核心(https://www.nature.com/articles/s41586-023-06924-6)。
- 评估器 = 用户提供的 `evaluate` 函数(快速执行打分),问题必须"有高效打分函数"。
- 与普通进化算法的区别:LLM 替代了传统遗传编程里需要人工设计的变异/交叉算子(论文 related work 段)。

### 2.3 代表成果与量化结果
- **cap set 问题(极值组合)**:发现超越已知最优的大 cap set 构造,"20 年来对渐进下界最大的改进"(论文摘要,https://www.nature.com/articles/s41586-023-06924-6)。
- **online bin packing**:发现超越 First-fit / Best-fit 的启发式;在 OR 与 Weibull 分布上全面占优,100,000 件物品时仅比最优下界高 0.03%(论文 Table 1 原文数据:Weibull 5k/10k/100k 下 excess bins 为 0.68%/0.32%/0.03%,而 First-fit 为 4.23%/4.20%/4.00%,Best-fit 为 3.98%/3.90%/3.79%)。
- 论文定位:首次证明"用 LLM 对公认开放问题做出可验证的新科学发现"是可能的。

### 2.4 资源成本
- 论文**未公开** GPU/TPU 小时数或美元;只说明用了大规模 LLM 采样(摘要提及其依赖"从 LLM 大量采样"),并特意选用**推理快**的模型(Codey/PaLM2)而非慢而强的模型,作为采样质量-吞吐的权衡(全文 Methods)。具体规模数字未公开。

### 2.5 已知局限 / 失败模式
- 只处理**单函数、Python、单个优化目标**;要求评估 ≤ ~20 分钟/次(AlphaEvolve 论文对 FunSearch 的对比表,https://arxiv.org/abs/2506.13131 Table 1)。
- 需要**高效的 `evaluate` 函数**才能闭环;无快速打分的任务不适用。
- 后续 AlphaEvolve 论文指出 FunSearch 需要数百万级 LLM 采样,样本效率低(同表)。

### 2.6 对 3DSS 的可借鉴点
- **程序搜索损失函数/数据增强函数/后处理函数**:3DSS 中可搜的目标包括——损失函数(如 Lovász 变体、类别加权)、数据增强策略(点云 dropout / 高斯噪声 / mix 函数)、体素化参数、后处理(类别融合/CRF)函数。这些都是"Python 函数 + 可执行打分"的形式,天然适配 FunSearch 范式。
- **岛屿模型防局部最优**:3DSS 方法空间极易收敛到"某个 trick 上",岛屿模型 + 签名聚簇是现成的抗早熟方案。
- **评估器设计是关键瓶颈**:FunSearch 假设评估廉价(分钟级),而 3DSS 单次训练是小时~天级 → 必须设计**代理评估器**(小规模训练/少 epoch/子集),否则样本效率不可行(详见 §9)。

---

## 3. AlphaEvolve (DeepMind, 2025)

### 3.1 来源
- DeepMind,"AlphaEvolve: A coding agent for scientific and algorithmic discovery",arXiv:2506.13131(2025-06);官方博客 https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ (2025-07-20)。

### 3.2 核心机制:进化 coding agent(整文件级变异 + 多评估器)
- 任务规格:用户给出 `evaluate` 函数(可多个打分)+ 初始代码文件。
- **prompt sampling**:从"存档/提示库"采样历史解与反馈,构造富含上下文的 prompt。
- **creative generation**:LLM(主用 Gemini 系列)直接修改**整个代码文件**(可达数百行,任意语言),支持大范围架构级改动;提供少量"思考/计划"反馈。
- **evaluation**:每个新解由自动评估器打分;支持三种增强:
  1. **evaluation cascade(级联测试)**:由易到难的测试集,先筛掉明显劣解;
  2. **LLM-generated feedback**:对难以形式化的性质(如"简洁性")用额外 LLM 调用打分,并入得分字典引导进化;
  3. **parallelized evaluation**:评估可并行化,单个解可花费 ~100 compute-hours 评估(论文原文:"feasible to spend on the order of 100 compute-hours to evaluate any new solution")。
- **evolution**:基于得分选择与传播,支持异步分布式流水线。
- 与 FunSearch 的官方对比(Table 1):单函数→整个文件;10-20 行→数百行;仅 Python→任意语言;快评估(≤20min CPU)→可评估数小时、并行、加速器;FunSearch 需数百万采样→AlphaEvolve 仅需数千;FunSearch 小模型即可→AlphaEvolve 受益于 SOTA 大模型;单指标→多指标。

### 3.3 代表成果与量化结果
- **4×4 复数矩阵乘法用 48 次标量乘法**:56 年来首次改进 Strassen(1969)在该设定下的结果(arXiv:2506.13131 摘要);为 14 个矩阵乘法算法改进 SOTA(论文正文)。
- 数学构造问题:**约 20% 的问题上超越 SOTA**,包括改进 Erdős 的 Minimum Overlap Problem 构造、11 维 Kissing Numbers 构造(论文正文 §3.2)。
- Google 工程落地:改进数据中心调度算法;TPU 硬件电路的功能等价简化(已进入实际 TPU);**加速 AlphaEvolve 自身底层 LLM 的训练**;优化 FlashAttention 相关 kernel 运行时(博客 + 论文摘要)。

### 3.4 资源成本
- **未公开**总 GPU/TPU 小时或美元;仅透露单解评估可到 ~100 compute-hours(论文 §2.4),LLM 采样数千次(Table 1 对比 FunSearch 的"millions")。按其工程规模(数据中心调度、TPU 电路)推断成本很高,但无公开数字。

### 3.5 已知局限 / 失败模式
- 依赖**强基础模型**(论文明确"benefits from SOTA LLMs",小模型无益)。
- 依赖可并行的、可自动打分的评估器;评估吞吐决定世代更替速度(论文 §2.4 提到评估墙钟时间会限制连续变异的频率)。
- 是 white paper,未见独立第三方复现评估;工程规模大,普通实验室复现门槛高。

### 3.6 对 3DSS 的可借鉴点
- **评估级联(evaluation cascade)最适合 3DSS**:先用小数据集/少 epoch 的代理评估筛掉劣解,再对幸存者做全量验证——这是把"小时级训练"塞进进化循环的可行工程手法。
- **LLM 反馈混合打分**:3DSS 中"loss 曲线是否健康""代码是否干净可读"难以数值化,可像 AlphaEvolve 一样用 LLM 打分并入进化信号。
- **整文件变异**:允许 LLM 同时改模型结构+损失+调度器,比 FunSearch 的单函数变异更贴近 3DSS 真实改进方式(3DSS 的改进往往跨模块)。
- 启示:3DSS 闭环应定位为"数千次采样的样本高效搜索"(AlphaEvolve 风格),而非"百万次采样的暴力搜索"(FunSearch 风格)。

---

## 4. AgentBreeder / Promptbreeder("自指自改进"主题)

> 说明:用户指定 arXiv 2502.00757(Yu et al.),核实后该编号为 AgentBreeder;精确标题 "Self-Referential Self-Improving Systems" 未检索到。为完整覆盖意图,本节写 AgentBreeder(编号对应)+ Promptbreeder(标题最接近"自指自改进")。

### 4.1 AgentBreeder —— arXiv 2502.00757(实际编号对应论文)
- 来源:Rosser, Foerster 等(牛津大学),"AgentBreeder: Mitigating the AI Safety Risks of Multi-Agent Scaffolds via Self-Improvement",arXiv:2502.00757(2025-02);代码 https://github.com/jrosseruk/AgentBreeder 。
- **核心机制**:对**多 agent scaffold(脚手架,即定义多个 LLM 如何协作的代码/提示结构)** 做**多目标进化搜索**。一个 LLM "Meta Agent" 对精英种群施加 **crossover + mutation**,生成新 scaffold 后代;采用受 MAP-Elites 启发的 **quality-diversity 搜索**:按架构特征聚簇,每个 niche 保留精英。双模式:Blue(提升安全+保持能力)、Red(主动寻找可 jailbreak 的弱 scaffold)。
- **评估器**:在验证集上执行 scaffold,以正确率中位数 + 95% Bootstrap CI 为 fitness;多目标权衡能力 vs 安全。
- **成本**:论文**未公开** GPU/LLM 调用次数。
- **量化结果**:Blue 模式在安全基准上平均 **+79.4%** 提升且保持/提升能力分数;Red 模式在与能力优化并发时发现对抗性弱 scaffold(摘要)。
- **对 3DSS 借鉴点**:①scaffold 级进化(而非代码级)思想可迁移为"进化 3DSS 实验配置/训练脚本结构";②quality-diversity + 存档(archive)对保持 3DSS 方法多样性、防早熟有用;③提醒:进化式搜索也可能"进化出"针对特定评估集过拟合的作弊结构——与 3DSS 评估集脆弱性直接相关。

### 4.2 Promptbreeder —— arXiv 2309.16797(标题最接近"Self-Referential")
- 来源:DeepMind,"Promptbreeder: Self-Referential Self-Improvement Via Prompt Evolution",arXiv:2309.16797(2023-09)。
- **核心机制(自指的关键)**:不只进化 **task-prompts**,还进化**用于改进 task-prompts 的 mutation-prompts**——"它不是只在改进任务提示,也在改进改进任务提示的提示"(摘要原文),即改进器本身也在进化,构成自指环。
- **评估器**:在训练集上评估 task-prompt 的任务性能作为 fitness。
- **成本**:**未公开**。
- **量化结果**:在算术与常识推理基准上超越 CoT、Plan-and-Solve 等人工提示策略;还能进化出针对仇恨言论分类的复杂 task-prompt(摘要)。
- **对 3DSS 借鉴点**:自指层(进化"如何改进的提示/策略")可用于 3DSS 的"meta 搜索"——比如进化出更擅长提出 3DSS 改进方案的提示模板;但这层自指在 3DSS 的性价比需谨慎评估(成本叠加,见 §9)。

---

## 5. From AI Assistant to AI Scientist(自动发现 LLM-RL 算法;POISE)

### 5.1 来源与勘误
- **真实论文**:"From AI Assistant to AI Scientist: Autonomous Discovery of LLM-RL Algorithms with LLM Agents",**arXiv:2603.23951**(2026-03)(用户提供的 2502.08651 是另一篇 AI Governance 论文,已核实)。
- 框架名 **POISE**(closed-loop framework for automated discovery of policy optimization algorithms for LLMs)。

### 5.2 核心机制:证据驱动的闭环算法发现
- 维护一个**结构化、系谱化(genealogically linked)的存档**:提案(proposal)、可执行实现(executable implementations)、标准化评估(standardized evaluations)、自然语言反思(natural-language reflections)互相链接,支撑"基于证据的迭代"——即每一轮改进都引用历史实验结果,而非盲目重试。
- 评估器:标准化的 RL 训练评估(数学推理任务上的加权 Overall、AIME25 pass@k)。
- 变异对象:policy optimization 算法机制(如 GRPO 的变体:方差缩放、有效性掩码等)。

### 5.3 代表成果与量化结果
- 从 GRPO 出发,评估 **64 个候选算法**;
- 发现有效机制:**analytic-variance scaling(解析方差缩放)**、**validity masking(有效性掩码)**;
- 最佳变体:加权 Overall **47.8 → 52.5(+4.6)**;AIME25 pass@32 **26.7% → 43.3%**(摘要原文)。

### 5.4 资源成本
- 论文**未公开** GPU 小时/美元;仅可知评估了 64 个候选(每个候选需一次或多次标准 RL 训练,推断成本可观)。

### 5.5 已知局限
- 搜索空间限于"机制级修改 + 训练动态耦合"的问题;需要标准化评估管道;论文未讨论跨任务泛化是否成立。

### 5.6 对 3DSS 的可借鉴点
- **系谱化存档 + 反思链**是 3DSS 闭环最有价值的架构细节:每个候选 3DSS 改进都挂上"父代、实现、评估结果、LLM 反思",后续迭代才能站在证据上而非重复踩坑。
- "从 GRPO 出发发现新机制"的模式 ≈ "从 MinkowskiNet/PointNet++ 基线出发,进化出新的损失/模块"——起点明确、单点替换、标准化评估,与 3DSS 现状高度契合。
- 64 个候选的规模对 3DSS 是现实的预算参考(若单候选评估可压缩,见 §9)。

---

## 6. EvoPrompt / EvoAgent 等 LLM 进化优化方法(简述)

### 6.1 EvoPrompt(arXiv:2309.08532)
- 来源:Guo, Wang, Ge 等(清华 / 微软),"Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers",arXiv:2309.08532(2023-09);代码 https://github.com/microsoft/EvoPrompt 。
- 机制:用 LLM 充当**变异与交叉算子**,在离散 prompt 空间上做进化;以开发集(development set)性能为 fitness,无梯度、无参数;迭代生成新 prompt 并更新种群。
- 成果:31 个数据集(语言理解、生成、BIG-Bench Hard),针对 GPT-3.5 与 Alpaca,**显著超越人工 prompt 与现有自动 prompt 优化方法**(摘要)。
- 成本:未公开。
- 3DSS 借鉴:提示级进化对 3DSS 的"实验提示/分析提示"优化有用,但价值低于代码级搜索;属于轻量组件。

### 6.2 EvoAgent(arXiv:2406.14228)
- 来源:"EvoAgent: Towards Automatic Multi-Agent Generation via Evolutionary Algorithms"(2024-06)。
- 机制:把现有 agent 框架作为初始个体,用**变异、交叉、选择**等进化算子自动把单 agent 扩展为多 agent 系统,提升复杂任务求解能力。
- 成本:未公开。
- 3DSS 借鉴:多 agent 化 3DSS 研究管线(如:提出者 agent + 实验者 agent + 分析者 agent)的自动组装,但 3DSS 的主瓶颈是实验成本而非 agent 数量,优先级低。

### 6.3 其他同族(一句话)
- EvoPrompting(arXiv:2302.14838):LLM 作为变异/交叉算子做**代码级神经架构搜索**,结合 soft prompt 微调;早期证明"纯提示 NAS 不够,需结合可训练组件"。
- Self-Taught Optimizer / STOP(arXiv:2310.02304):seed improver 程序递归改进自身所在 scaffold,是"程序自改进"的最小原型。
- 失败模式共性(见 §8):进化优化普遍面临**过拟合评估集、多样性崩塌、评估成本爆炸**,EvoPrompt 系论文多以开发集选优,换测试集后提升幅度常缩小。

---

## 7. Harness Engineering / Agent Self-Evolution 综述与框架

### 7.1 Hierarchical Self-Improvement(HSI)—— arXiv:2608.08466
- 来源:Tailin Zhou 等,"Hierarchical Self-Improvement: A Framework for Task-Specific Evolvable Agent Harnesses",arXiv:2608.08466(2026-08);代码 https://github.com/TailinZhou/hsi 。
- **核心机制**:单个**冻结 LLM** 在三个层级作用:
  1. task harness $H$(执行任务的脚手架);
  2. evolver(重写 $H$);
  3. meta-evolver(在冻结外层锚下重写 evolver 的策略代码)。
  每个任务族维护自己的 harness,通过固定"任务注入缝(task-injection seam)"热切换,用环境反馈重写。
  **thinking on/off 设计**:任务执行时禁用推理、自我修改时启用推理,以隔离"harness 进化"本身的贡献。
- **两个界(理论贡献)**:
  1. **feedback-fidelity bound**:进化需要信息丰富的奖励信号来指导选择;
  2. **backbone capability bound**:harness 重写无法突破冻结模型本身的能力上限。
- 论文自称包含 **31 个 harness engineering 与 agent self-evolution(2025–2026)代表工作的扩展综述**(摘要)。
- **量化结果**(BALROG,冻结骨干 DeepSeek-V4-Flash-Preview,中等难度任务,raw % Progress):BabyAI **+39.3**、Crafter **+33.0**、TextWorld **+25.0**、MiniHack **+15.0**;在 BabaIsAI 未见过的 20% 划分上有强留出泛化(BreakStop 0.98 / GoTo 1.00 best-test);**超出骨干能力的任务(NLE)上 harness 进化无收益**——实证了 backbone capability bound。
- 成本:未公开。
- **3DSS 借鉴点**:①"冻结骨干 + 进化 harness"与 3DSS 场景(冻结点云编码器、进化训练/后处理管线)结构同构,成本远低于全量重训;②**两个 bound 直接告诫**:3DSS 闭环的收益上限由"评估信号质量"与"骨干模型能力"决定——如果 mIoU 代理评估噪声大或骨干太弱,闭环会空转;③thinking on/off 的消融设计是评估"进化贡献"的好方法论。

### 7.2 Recursive Self-Improvement in AI 综述 —— arXiv:2607.07663
- 来源:"Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops",arXiv:2607.07663(2026-07);(ar5iv:https://ar5iv.labs.arxiv.org/html/2607.07663)。
- **规模与结构**:综述 **1,250 篇 arXiv 论文(2024–2026)**;两条轴:①改进什么(部署行为 / 训练策略 / 评估器 / 研究过程本身);②闭环程度(人机协同 → 全闭环)。
- **核心分类**:区分**有界自改进(bounded self-refinement)**——收敛、可评估、已是工业实践;与**开放式递归自改进(open-ended RSI)**——在接地(grounding)、崩塌动力学、计算约束上处处受限。
- **评估器设计空间(本综述最独特的贡献)**:把自改进信号排序成**验证层级(verification hierarchy)**:形式验证器(最强)→ 过程奖励模型 / 验证器 / 规则 → 内在自我评估(最弱);观察到**已演示的自改进强度与该层级严格对应**。
- **失败模式(明确总结)**:self-confirming loops(自我确认回路)、model collapse(模型崩塌)、diversity collapse(多样性崩塌)——均由违反验证层级导致;另指出"研究方向设定(research direction-setting)"瓶颈让人类保持在环,位于层级顶端;**治理级自改进度量是该领域最空白的 niche**。
- **3DSS 借鉴点**:这是对 3DSS 闭环最重要的"失败模式清单"来源(详见 §8);建议直接按验证层级设计 3DSS 评估器(形式可验证的指标 → 交叉验证的 mIoU → LLM 主观评分,逐级降级使用)。

### 7.3 其他相关综述/理论(一句话)
- **Self-Reference in LLMs: The Introspection Threshold for Recursive Self-Improvement**(arXiv:2607.04277):用 Kleene 第二递归定理论证"内省"是可持续自改进的门槛,当前 LLM 只有"准内省",受限于 Transformer 前馈结构与计算类约束——对"LLM 能否真正自我改进 3DSS 方法"给出理论冷水。
- **Noise-to-Meaning RSI**(arXiv:2505.02888):最小形式模型,自反馈越过信息整合阈值后复杂度无界增长;含安全警告——对"自进化可能发散/失控"的建模。

---

## 8. 已知失败模式与缓解策略小结(跨系统归纳)

综合 §1–§7(尤其 2607.07663 综述与 HSI 论文),自进化/进化式搜索闭环的通用失败模式与缓解策略:

| # | 失败模式 | 表现 | 缓解策略 | 出处 |
|---|---|---|---|---|
| 1 | **过拟合评估器 / 评估集过拟合(hacking the evaluator)** | 进化出的方案在开发集暴涨、在留出集/新数据崩塌;AgentBreeder Red 模式即是"故意进化出评估器漏洞" | 固定留出集分层验证;多数据集交叉验证;评估器多样化(形式指标+重训多次取分布);禁止在测试集上做任何选择 | AgentBreeder(arXiv:2502.00757);2607.07663;EvoPrompt 系 |
| 2 | **自我确认回路(self-confirming loops)** | LLM 审稿人/评分器被进化过程"驯化",给自我生成的方案虚高分数 | 验证层级(形式验证器 > 过程验证器 > 主观 LLM 评分);评审器与被评对象隔离;定期用人类/外部基准校准 | 2607.07663;AI Scientist 自动审稿人争议 |
| 3 | **模型崩塌 / 多样性崩塌(model & diversity collapse)** | 种群收敛到同质方案,后续变异无新信息;或自训练数据污染导致能力退化 | 岛屿模型/quality-diversity/签名聚簇存档(FunSearch、AgentBreeder);定期注入外部多样性(新论文、新数据);限制自生成数据占比 | FunSearch(Nature 2023);2607.07663 |
| 4 | **成本爆炸(cost explosion)** | 每代全量训练/评估,预算线性~超线性增长;AI Scientist 单篇 $15 尚可,但 3DSS 单次训练贵 2–4 个数量级 | 代理评估(小规模/少 epoch/子集)做漏斗;评估级联由易到难(AlphaEvolve);系谱化存档避免重复实验(POISE);冻结骨干只进化 harness(HSI) | AlphaEvolve;POISE(arXiv:2603.23951);HSI(arXiv:2608.08466) |
| 5 | **反馈保真度不足(feedback-fidelity bound)** | 评估信号太噪/太稀,进化变成随机游走 | 提高评估信噪比(重复种子取分布、增大验证集);把不可数值化的性质交给 LLM 辅助打分(AlphaEvolve) | HSI(arXiv:2608.08466) |
| 6 | **骨干能力上限(backbone capability bound)** | 冻结模型/harness 之上无论如何进化都无法突破基线能力 | 明确闭环边界:只在骨干能力范围内承诺收益;需要突破时切换到全量训练(成本换能力) | HSI(BALROG 上 NLE 无收益的实证) |
| 7 | **方向设定瓶颈(direction-setting bottleneck)** | 自动系统能优化给定目标,但"该研究什么"仍需人类/高层 LLM | 保留人类在环设定顶层方向;或引入 meta-evolver 层(HSI);但注意该层成本与失控风险 | 2607.07663;HSI |
| 8 | **理论天花板(自指不足)** | LLM 缺乏真正内省,递归自改进未必可持续 | 对"LLM 完全自主改进 3DSS"保持审慎预期;把自进化定位为"人机协同的加速器"而非"取代研究者" | 2607.04277;2505.02888 |

---

## 9. 对比总表

| 对象 | 机构 / 年份 | 进化循环机制 | 变异算子 | 评估器 | 记忆/存档 | 成本(公开) | 代表成果 | 3DSS 可借鉴点 |
|---|---|---|---|---|---|---|---|---|
| **The AI Scientist v1/v2** | Sakana AI / UBC / Oxford;2024 / 2025 / Nature 2026 | 想法→实验→写作→自动评审的科研闭环,可开放重复 | LLM 生成想法与代码(整文件) | LLM 自动审稿人(v2 为 VLM+审稿人) | 论文库、审稿分数反馈 | v1 **<$15/篇**;v2/Nature 未公开 | 3 领域自动论文;v2 论文过 ICLR workshop 盲审;Nature 封面 | 闭环骨架、自动审稿人当方向把关、VLM 图表反馈;成本模型不可照搬 |
| **FunSearch** | DeepMind;Nature 2023(2024-01 刊出) | LLM 采样=变异,程序库+岛屿模型;循环:evaluate→存库→采样→生成 | LLM 生成新 Python 函数 | 用户提供的 `evaluate` 执行打分(需 ≤~20min 快评估) | programs database(岛屿模型+签名聚簇) | **未公开**(大量 LLM 采样;用快推理模型) | cap set 20 年最大渐进下界改进;bin packing 全面超越 First/Best-fit(100k 件 0.03% off) | **搜损失/增强/后处理函数**;岛屿模型防早熟;需代理评估器解决"训练太贵" |
| **AlphaEvolve** | DeepMind;2025 | 整文件级进化 coding agent;级联测试+LLM 反馈+并行评估;异步流水线 | LLM 直接改整个代码文件(数百行、任意语言) | 自动 evaluate(可多指标)+ LLM 辅助打分;级联由易到难 | 提示/存档库;每代选择与传播 | **未公开**;单解评估 ~100 compute-hours;数千采样 | 4×4 复数矩阵乘 48 次乘法(56 年首破 Strassen);~20% 数学问题超 SOTA;数据中心调度/TPU 电路/加速自身训练 | **评估级联**适配"训练贵"场景;整文件变异贴近真实改进;样本高效(数千次)定位 |
| **AgentBreeder** | 牛津;2025 | 多目标进化搜 multi-agent scaffold;Meta Agent 做 crossover/mutation;MAP-Elites 式 quality-diversity | LLM 生成新 scaffold 代码 | 验证集正确率中位数+95% CI;能力 vs 安全双目标 | 精英集/niche 存档(ARCHIVE 注入 prompt) | **未公开** | Blue 模式安全基准平均 +79.4% 且保能力;Red 模式发现 jailbreak 弱 scaffold | 存档+多样性搜索防 3DSS 早熟;警示:进化可"进化出"评估集作弊 |
| **Promptbreeder** | DeepMind;2023 | 自指:同时进化 task-prompts 与改进它们的 mutation-prompts | LLM 变异 prompt(含变异算子自身的进化) | 任务性能(训练集 fitness) | 双种群(任务 prompt + 变异 prompt) | **未公开** | 算术/常识推理超 CoT、Plan-and-Solve;进化仇恨言论分类 prompt | meta 层(进化"如何提出改进")可移植到 3DSS 提示策略;成本叠加需谨慎 |
| **POISE(AI Assistant→AI Scientist)** | 2026 | 闭环算法发现:提案→实现→标准评估→反思,系谱化存档驱动迭代 | LLM 生成机制级修改(RL 算法变体) | 标准化 RL 评估(Overall、AIME25 pass@k) | 系谱化存档(提案/实现/评估/反思互链) | **未公开**(评估 64 个候选) | 从 GRPO 出发:Overall 47.8→52.5;AIME25 pass@32 26.7%→43.3% | **系谱化存档+反思链**(3DSS 闭环最有价值的架构细节);64 候选规模是现实预算 |
| **EvoPrompt** | 清华/微软;2023 | LLM 作变异/交叉算子优化离散 prompt;开发集 fitness | LLM 生成 prompt 变体 | 开发集任务性能 | 种群迭代 | 未公开 | 31 数据集超越人工 prompt 与现有方法 | 提示级优化组件,轻量;价值低于代码级搜索 |
| **EvoAgent** | 2024 | 进化算子把单 agent 自动扩成多 agent | 变异/交叉/选择 agent 配置 | 任务性能 | 种群 | 未公开 | 多 agent 自动生成提升复杂任务 | 3DSS 研究管线多 agent 化;优先级低(瓶颈在实验成本) |
| **HSI(Hierarchical Self-Improvement)** | 2026 | 冻结 LLM 三层:harness / evolver / meta-evolver;任务注入缝热切换 | LLM 重写 harness 与 evolver 策略代码 | 环境反馈(任务奖励);thinking on/off 消融 | 每任务族独立 harness;策略代码可重写 | 未公开 | BALROG: BabyAI +39.3、Crafter +33.0、TextWorld +25.0、MiniHack +15.0;超骨干任务无收益 | **冻结骨干+进化 harness** 与 3DSS 同构;两 bound(反馈保真/骨干能力)界定闭环上限;含 31 篇 harness/self-evolution 综述 |
| **RSI 综述** | 2026 | 1,250 篇论文两轴分类;验证层级 | —(综述) | 验证层级:形式验证器>过程验证器>自我评估 | — | — | 自改进强度与验证层级严格对应;失败模式=违反层级 | **失败模式清单**(过拟合评估、自我确认、崩塌、成本);评估器按验证层级设计 |
| **自指理论(内省阈值)** | 2026 | 理论:内省是可持续自改进门槛 | — | — | — | — | Kleene 定理论证内省程序存在;LLM 只有准内省 | 对"LLM 完全自主改进 3DSS"设合理预期 |

---

## 10. 对 3DSS 自主研究闭环的整体结论与建议

1. **范式选择**:3DSS 单次训练成本(小时~天级 GPU)决定了**不能照搬 FunSearch 的百万采样暴力搜索**,应走 **AlphaEvolve / POISE 风格**:数千次采样的样本高效搜索 + **评估级联**(小规模代理评估筛劣解 → 全量验证幸存者)。
2. **评估器设计(决定成败)**:按验证层级(2607.07663)设计——第一层:形式可验证指标(如参数量、FLOPs、确定性正确性);第二层:跨数据集交叉验证的 mIoU(多 seed 取分布,避免单 seed 噪声);第三层才用 LLM 主观评分。**任何选择都不允许触碰留出测试集**。
3. **架构建议(综合 POISE + HSI)**:系谱化存档(提案/代码/评估/反思互链)+ 冻结骨干进化 harness/损失/增强/后处理 + meta-evolver 层可选;明确两个 bound:评估信号信噪比与骨干能力决定收益上限。
4. **防崩塌**:岛屿模型/quality-diversity 存档(FunSearch/AgentBreeder)防早熟;定期注入外部多样性(新论文、新数据集、新 SOTA 骨干)。
5. **成本护栏**:代理评估漏斗、缓存复用已跑实验(POISE 系谱化)、预算按"候选数 × 单候选成本"显式建模(AI Scientist $15/篇与 POISE 64 候选是两个可参考量级;3DSS 需自建)。
6. **期望管理**:自指理论(2607.04277)提示 LLM 目前只有"准内省",3DSS 闭环定位为**人机协同加速器**(人类定方向,系统跑搜索与实验)比"全自主科学家"更现实;同时注意 AI Scientist"过同行评审"声明引发的争议,避免把自动审稿分数当作科学真理。

---

## 附:核心来源链接

- AI Scientist v1:https://arxiv.org/abs/2408.06292 ;博客 https://sakana.ai/ai-scientist/ ;代码 https://github.com/SakanaAI/AI-Scientist
- AI Scientist v2:https://arxiv.org/abs/2504.08066 ;代码 https://github.com/SakanaAI/AI-Scientist-v2 ;Nature 博客 https://sakana.ai/ai-scientist-nature/ ;Nature 论文 DOI 10.1038/s41586-026-10265-5
- FunSearch:https://www.nature.com/articles/s41586-023-06924-6 ;代码 https://github.com/google-deepmind/funsearch
- AlphaEvolve:https://arxiv.org/abs/2506.13131 ;博客 https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/
- AgentBreeder:https://arxiv.org/abs/2502.00757 ;代码 https://github.com/jrosseruk/AgentBreeder
- Promptbreeder:https://arxiv.org/abs/2309.16797
- POISE(AI Assistant→AI Scientist):https://arxiv.org/abs/2603.23951
- EvoPrompt:https://arxiv.org/abs/2309.08532 ;代码 https://github.com/microsoft/EvoPrompt ;EvoAgent:https://arxiv.org/abs/2406.14228 ;STOP:https://arxiv.org/abs/2310.02304
- HSI:https://arxiv.org/abs/2608.08466 ;代码 https://github.com/TailinZhou/hsi
- RSI 综述:https://arxiv.org/abs/2607.07663 ;自指内省阈值:https://arxiv.org/abs/2607.04277 ;Noise-to-Meaning RSI:https://arxiv.org/abs/2505.02888
- AI Scientist 评审争议:https://techcrunch.com/2025/03/12/sakana-claims-its-ai-paper-passed-peer-review-but-its-a-bit-more-nuanced-than-that/ ;https://the-decoder.com/ai-generated-paper-passes-peer-review-before-planned-withdrawal/
