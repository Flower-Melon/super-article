# Introduction 与 Related Work 合并修改说明

修改后的正文不再设置独立的 Related Work。现有相关工作会按“研究挑战”嵌入
Introduction，使读者在看到一类现有方法后，立即知道它解决了什么、还缺少什么，
以及该缺口如何引出本文设计。压缩以删除重复论述和合并同类文献为主，不通过改换
既有名词获得表面上的简洁；Introduction 现有贡献列表的内容完整保留。

文件结构直接调整为：

```text
sections/01-introduction.tex
sections/02-system-overview.tex
sections/03-evaluation-suite-design.tex
sections/04-experiments.tex
sections/05-conclusion.tex
```

具体文件操作如下：

| 当前文件 | 修改后 |
|---|---|
| `sections/01-introduction.tex` | 重写为包含相关工作的 Introduction |
| `sections/02-related-work.tex` | 删除 |
| `sections/03-system-overview.tex` | 重命名为 `sections/02-system-overview.tex` |
| `sections/04-evaluation-suite-design.tex` | 重命名为 `sections/03-evaluation-suite-design.tex` |
| `sections/05-experiments.tex` | 重命名为 `sections/04-experiments.tex` |
| `sections/06-conclusion.tex` | 重命名为 `sections/05-conclusion.tex` |

`main.tex` 中当前的章节输入：

```latex
\input{sections/01-introduction}
\input{sections/02-related-work}
\input{sections/03-system-overview}
\input{sections/04-evaluation-suite-design}
\input{sections/05-experiments}
\input{sections/06-conclusion}
```

直接改为：

```latex
\input{sections/01-introduction}
\input{sections/02-system-overview}
\input{sections/03-evaluation-suite-design}
\input{sections/04-experiments}
\input{sections/05-conclusion}
```

Introduction 不增加 `Related Work`、`Background` 等子标题。参照 CoMA-IKG 的
Introduction，用连续段落完成背景、相关研究、问题和贡献之间的推进。重写后的正文
按下面顺序展开。

| 新位置 | 使用现有内容 | 具体改法 | 保留的引用 |
|---|---|---|---|
| 第 1 段：任务背景 | `01` 第 4--22 行 | 将野火威胁、UAV 观测优势、资源限制和状态变化合并为一个开篇段落。删除两次解释“不是独立感知或路径规划任务”的句子，段尾只保留一次结论：多 UAV 野火救援需要闭环决策。 | `bowman2020wildfire`, `allan2022remote`, `floreano2015science`, `erdelj2017help` |
| 第 2 段：火情理解 | `02` 第 19--49 行 | 把火灾检测、语义分割、三维重建、探索和 next-best-view 归为“从航拍图像形成任务状态”的相关工作。每项工作只说明其能力，不再逐篇展开技术细节。段尾指出这些方法提供感知证据，但不负责把火点转换为受资源约束的舰队任务。 | `yuan2021uavfire`, `zhang2022uavtransformer`, `yang2022uav3dreconstruction`, `popovic2021uavdisaster`, `bircher2016nbv` |
| 第 3 段：舰队规划 | `02` 第 35--64 行中与规划有关的内容 | 把自主导航、覆盖规划、多智能体任务分配和搜救协作归为“从任务状态形成 UAV 行动”的相关工作。删除“单项能力与完整任务不同”的多轮解释，只在段尾集中指出：现有方法通常优化导航、覆盖或固定初始状态下的分配，不能保证动态资源约束下的任务连续性。 | `xiao2021uavrl`, `yu2022coverageuav`, `yang2023multiagentuav`, `waharte2021uavsar` |
| 第 4 段：LLM 计划生成与约束 | `01` 第 36--45 行；`02` 第 80--118 行 | 先说明 LLM 可连接高层意图、结构化观测和机器人技能，再用 SayCan、Code as Policies 和 ChatGPT for Robotics 说明任务分解与动作生成，用 RT-1、PaLM-E 和 Socratic Models 说明视觉或具身状态接入。段尾只保留一个限制：生成结果具有语义合理性，不代表同时满足续航、载荷、通信、优先级和安全约束。由此引出 Validation。 | `ahn2022saycan`, `liang2023codeaspolicies`, `vemprala2023chatgptrobotics`, `brohan2023rt1`, `driess2023palme`, `zeng2023socratic` |
| 第 5 段：反馈与经验 | `02` 第 120--131 行 | 用 Inner Monologue、LM-Nav 和 Voyager 概括反馈修订、语义导航和经验积累。删除对各系统机制的详细介绍，重点说明它们主要面向单智能体或开放式探索，没有处理多 UAV 之间的资源耦合，也没有说明运行时事件发生后如何修复舰队计划。由此引出 Memory 和 Runtime Replanning。 | `huang2023innermonologue`, `shah2023lmnav`, `wang2023voyager` |
| 第 6 段：研究缺口 | `01` 第 24--34 行；`02` 第 66--76、133--143 行 | 将目前分散在三处的 research gap 合并成一个段落。最终只陈述一次：现有研究分别推进了感知、规划、协同和反馈式智能体，但尚未把火情理解、资源约束规划、计划验证、经验利用和运行时修复连接为同一个舰队级闭环。随后直接提出本文研究问题。 | 不新增引用；使用前文已经建立的文献依据 |
| 第 7 段：本文方案 | `01` 第 47--61 行 | 当前文字逐个解释 Semantic Validation、Deterministic Rule Validation、Episodic Memory、Lesson Memory 和 Runtime Replanning，和系统章节重复。改为三句话：第一句说明 Vision Analysis 与 Mission Planning 生成初始任务；第二句说明 Validation 和 Memory 分别保证可执行性并提供经验；第三句说明 Runtime Replanning 根据执行状态修复活动计划。 | 无 |
| 第 8 段：评测与主要发现 | `01` 第 63--74 行；摘要中的核心结果 | 将评测套件介绍压缩为一句，将三组实验及最重要结论压缩为两句。不在这里解释六项指标的具体含义，也不重复列出全部实验配置。 | 无 |
| 贡献列表 | `01` 第 76--94 行 | 三项贡献完整保留，不把其中的框架模块、难度条件、实验范围、评测对象、compact planner 或 planning overhead 说明删掉。该部分不承担篇幅压缩，只允许调整 LaTeX 源码换行。 | 无 |

贡献列表具体按当前内容原样保留：

```latex
\begin{enumerate}[leftmargin=1.6em,itemsep=2pt,topsep=3pt]
    \item We formulate resource-constrained multi-UAV wildfire rescue as a
    high-level closed-loop decision problem and develop an LLM-centered
    closed-loop decision framework that connects fire-situation understanding
    and resource-constrained mission planning with Validation, Memory, and
    Runtime Replanning.
    \item We construct a real-UAV-informed AirSim evaluation suite that exposes
    the decision loop to controlled increases in operational pressure through
    resource limitations, scheduling constraints, and runtime perturbations
    across four difficulty levels, and measures both task completion and
    execution quality with six mission-level metrics.
    \item We evaluate end-to-end behavior against an Optimization-Based Planner
    and across multiple foundation-model configurations, characterize through
    controlled ablations how Validation, Memory, and Runtime Replanning
    contribute as operational pressure increases, and assess whether validated
    demonstrations can specialize a compact planner with lower planning
    overhead.
\end{enumerate}
```

这段不改写、不缩写，也不把其中的信息挪到前文后再从贡献列表中删除。

新的 Introduction 将以类似下面的逻辑连接各段，而不是继续使用当前“介绍一次问题、
综述后再介绍一次问题、贡献前第三次介绍问题”的写法：

```text
野火救援需要闭环决策
  -> 现有 UAV 感知可以识别环境，但不能形成舰队任务
  -> 现有规划可以生成路线或分配，但难以维持动态任务连续性
  -> 现有 LLM 智能体可以生成高层动作，但缺少舰队约束保证
  -> 现有反馈式智能体可以修订行为，但没有解决多 UAV 资源耦合
  -> 因而需要 Validation、Memory 和 Runtime Replanning 组成的闭环
  -> 本文给出框架、评测套件和三组实验
```

以下现有内容会直接删除，而不是换一种说法继续保留：

- `02` 第 6--17 行对完整决策链的预告，因为第 1 段已经完成任务定义。
- `02` 第 28--33、43--49、57--64 行中反复出现的“单项能力不能形成完整任务”。
- `02` 第 66--76 行对不可直接数值比较和研究缺口的展开，压缩后只在第 6 段保留
  必要结论。外部基线不可直接比较的限制仍留在 Conclusion，不在 Introduction 重复。
- `02` 第 80--89 行对 LLM 一般作用的铺垫，与 `01` 第 36--45 行合并。
- `02` 第 102--104、112--118、127--131 行三次出现的舰队资源约束限制，合并成
  第 4、5 段各自的段尾句。
- `02` 第 133--143 行对 Validation、Memory 和 Runtime Replanning 的完整预告，
  因为第 6、7 段会更短地完成同一任务。
- `01` 第 47--74 行中与系统设计、评测套件章节重复的模块和指标说明。

参考文献不删减。原两个章节中的 22 个不同引用键全部进入新的 Introduction；其中
`driess2023palme` 在两个原文件中均有出现。`references.bib` 不作任何改动。为了避免
每篇文献各占一句，性质相近的工作改为组合引用，例如：

```latex
Recent UAV studies have advanced fire detection, semantic segmentation, and
geometric scene reconstruction
\cite{yuan2021uavfire,zhang2022uavtransformer,
      yang2022uav3dreconstruction}.
```

以及：

```latex
LLM-based robotic agents have connected language reasoning with executable
skills, programmatic policies, and embodied observations
\cite{ahn2022saycan,liang2023codeaspolicies,
      brohan2023rt1,driess2023palme}.
```

这种修改减少的是逐篇复述，不减少文献覆盖。引用首次出现顺序改变后，IEEE 编号会
自动重排。

上面表格中的“火情理解”“舰队规划”等中文仅用于说明内容位置，不代表要在英文正文
中创造新的名称。实际改写必须沿用原文已经使用的英文术语，并保持其大小写、连字符、
单复数和模块命名一致。以下核心表达固定使用原文形式：

| 内容 | 固定使用的原文表达 |
|---|---|
| 研究任务 | `multi-UAV wildfire rescue`；`resource-constrained multi-UAV wildfire rescue` |
| 问题定义 | `high-level closed-loop decision problem`；`high-level closed-loop decision core` |
| 总体框架 | `LLM-centered closed-loop decision framework` |
| 决策阶段 | `fire-situation understanding`；`resource-constrained mission planning`；`runtime replanning` |
| 系统模块 | `Vision Analysis`；`Mission Planning`；`Validation`；`Memory`；`Runtime Replanning` |
| 验证模块 | `Semantic Validation`；`Deterministic Rule Validation` |
| 记忆模块 | `Episodic Memory`；`Lesson Memory` |
| 评测套件 | `real-UAV-informed AirSim evaluation suite` |
| 条件与事件 | `operational pressure`；`runtime perturbations` |
| 评测结果 | `basic task completion`；`execution quality`；`mission continuity`；`mission-level metrics` |
| 对比对象 | `Optimization-Based Planner`；`foundation-model configurations` |
| 微调实验 | `validated demonstrations`；`compact planner`；`planning overhead` |

修改普通连接句时同样优先删句、并句和删除重复修饰语。不得为了避免重复而将
`resource-constrained mission planning` 改写成 `resource-aware planning`，将
`Runtime Replanning` 改成 `online plan repair`，或给其他既有概念另起名称。模块名称
在作为专有模块引用时继续使用原文的大写形式。

章节文件重排后，正文中的硬编码章节号也要同步处理。具体改动为：

| 位置 | 当前写法 | 修改后指向 |
|---|---|---|
| 新 `03-evaluation-suite-design.tex` 原第 8、16、104 行 | `Section~3` | Task Modeling and System Design，即新的 Section II |
| 新 `03-evaluation-suite-design.tex` 原第 123 行 | `Section~4.1` | Real-to-Sim Calibration，即新的 Section III-A |
| 新 `04-experiments.tex` 原第 7 行 | `Section~4` | Evaluation Suite Design，即新的 Section III |
| 新 `04-experiments.tex` 原第 61 行 | `Section~3` | Task Modeling and System Design，即新的 Section II |

这些位置不继续手写数字，而是在对应 `\section` 或 `\subsection` 后加入 `\label`，
并改用 `Section~\ref{...}`，避免下一次章节调整后再次失效。`README.md` 中的文件树也
同步更新为新的 `01`--`05` 文件名。

合并前两个章节约 1950 词。新的 Introduction 控制在 1100--1250 词，其中相关工作
约占 500--600 词；预计减少 700--850 词。压缩量来自重复背景、逐篇综述和重复的
research gap，不来自贡献列表或术语替换；同时保留所有相关文献、研究缺口和三项
贡献的完整内容。最终正文将从五个章节连续编号：Introduction、Task Modeling and System
Design、Evaluation Suite Design、Experiments、Conclusion。
