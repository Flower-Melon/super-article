# 论文叙事主线修改计划

## 1. 修改目标

本轮修改不再以模块功能为主要组织线索，而是围绕一个统一的中心问题重构全文叙事：

> 在资源受限且任务状态动态变化的多无人机野火救援中，LLM 能否作为高层闭环决策核心；随着运行压力提高，Validation、Memory 和 Runtime Replanning 分别在什么条件下发挥作用？

全文需要依次回答三个问题：

1. 完整系统能否执行从视觉理解到运行时修复的端到端闭环任务？
2. Validation、Memory 和 Runtime Replanning 分别针对什么决策风险，并在什么任务条件下发挥作用？
3. 这种高层规划能力能否转移到更紧凑、低开销的模型？

现有三组实验分别回答上述三个问题，不增加实验，也不改变实验结果。

## 2. 逐章修改计划

| 修改位置 | 修改内容 | 修改目的 |
| --- | --- | --- |
| `main.tex`，Abstract | 减少模块清单式介绍，先提出资源约束和状态动态变化共同造成的闭环决策问题，再说明框架如何形成从理解、规划到执行修复的闭环。按照端到端能力、组件作用和紧凑模型部署三个层次总结现有结果。 | 让摘要首先回答论文研究了什么问题。 |
| `sections/01-introduction.tex`，问题背景 | 强化资源约束与动态变化的耦合：初始计划不仅需要可行，还必须在资源消耗、任务变化和 UAV 故障后保持有效。说明该问题不同于单独的感知、路径规划或静态任务分配。 | 解释为什么需要高层闭环决策。 |
| `sections/01-introduction.tex`，方法引入 | 在介绍系统前明确提出中心研究问题。随后按照失败模式解释系统机制：Validation 控制计划可靠性，Memory 支持复杂条件下的经验复用，Runtime Replanning 处理执行状态变化。 | 将模块从功能列表转变为解决关键失败模式的机制。 |
| `sections/01-introduction.tex`，评测介绍 | 将评测套件描述为对中心问题的压力测试：四个难度等级逐步增加资源、调度和运行时扰动压力，六项指标分别观察任务完成和执行质量。 | 解释评测设计与中心问题之间的关系。 |
| `sections/01-introduction.tex`，贡献列表 | 保留三项贡献，但调整为闭环问题与框架、面向该问题的评测体系，以及对整体能力、组件作用和紧凑部署的实证回答。模块名称可以出现，但不再作为贡献句的主体。 | 使贡献直接对应中心问题。 |
| `sections/02-related-work.tex`，UAV-based Wildfire Response | 保留现有引用和技术分类，重写主题句与总结句。突出感知、导航、覆盖和任务分配分别解决决策链的一部分，但不能共同保证资源约束下的初始计划以及动态条件下的任务连续性。 | 从功能综述转变为对研究缺口的论证。 |
| `sections/02-related-work.tex`，多无人机工作总结 | 强化静态或开环决策与本文动态闭环问题的区别。保留不可直接进行端到端数值比较的说明，但将重点放在任务定义差异，而不是为缺少 baseline 辩护。 | 自然导出本文研究空缺。 |
| `sections/02-related-work.tex`，LLM-Based Robotic Agents | 将现有工作按照高层规划、具身感知和反馈修正组织。每组工作后说明其与多无人机资源约束、任务耦合和运行时扰动之间仍存在的距离。 | 说明 LLM 已具备部分相关能力，但尚未回答本文的中心问题。 |
| `sections/02-related-work.tex`，章节结尾 | 增加综合性总结：LLM 决策需要受到约束、能够复用经验，并能在执行状态变化后修复计划。由此引出后续系统设计，而不是再次平行列举模块。 | 建立 Related Work 到 System Overview 的逻辑衔接。 |
| `sections/03-system-overview.tex`，章节开头 | 在现有定义和公式前补充设计逻辑：系统围绕持续更新的决策循环构建，并面对计划不可行、复杂经验无法复用和运行时计划失效三类风险。 | 先解释为什么这样设计，再进入形式化定义。 |
| `sections/03-system-overview.tex`，架构介绍 | 将架构图说明从模块枚举改为闭环流程说明，强调信息和反馈如何在 Vision Analysis、Mission Planning、Validation、Memory 和 Runtime Replanning 之间流动。 | 使系统首先被理解为闭环，而不是模块集合。 |
| `sections/03-system-overview.tex`，各模块段落 | 保留全部定义、公式和处理流程，仅调整各段开头与结尾：先说明模块对应的决策风险，再说明其在闭环中的输入、输出以及与其他机制的关系。 | 减少逐项说明带来的割裂感。 |
| `sections/04-evaluation-suite-design.tex`，章节开头 | 明确评测体系用于检验 LLM 高层闭环决策在逐步增加的 operational pressure 下是否仍然有效。 | 将评测设计接回中心问题。 |
| `sections/04-evaluation-suite-design.tex`，难度分层 | 不修改难度定义和数据，只补充说明各等级如何逐步引入资源压力、调度耦合和运行时扰动。 | 使难度等级成为分析机制作用条件的依据。 |
| `sections/05-experiments.tex`，Experimental Setup | 将三组实验明确表述为对三个递进问题的回答：整体闭环能力、组件作用和紧凑部署。保持现有实验顺序与配置。 | 避免三组实验彼此割裂。 |
| `sections/05-experiments.tex`，End-to-End Evaluation | 强调该实验回答完整闭环能否运行，以及其表现是否过度依赖单一基座模型；模型排名保持为次要观察。 | 回答整体能力问题。 |
| `sections/05-experiments.tex`，Ablation Studies | 在开头和结尾增加机制导向总结：Validation、Memory 和 Runtime Replanning 分别针对什么风险，以及其作用如何随任务条件变化。所有数值保持不变。 | 用消融结果解释系统设计的必要性。 |
| `sections/05-experiments.tex`，Fine-Tuned Planner Evaluation | 将该实验定位为闭环框架中初始规划模块的部署问题，明确其不重新验证完整闭环，也不覆盖 Hard 和 Expert 条件下的运行时重规划。 | 将紧凑模型实验纳入主线并保持结论边界。 |
| `sections/06-conclusion.tex`，Conclusion | 首先直接回答中心问题，再总结三类证据：完整系统可执行闭环任务、三个机制具有随任务条件变化的作用、紧凑模型可降低初始规划开销。最后保留现有限制。 | 使结论回答研究问题，而不是重复模块和结果清单。 |

## 3. 全文术语规范

| 表达对象 | 统一用语 |
| --- | --- |
| 全文研究对象 | `high-level closed-loop decision making` |
| 系统定位 | `LLM-centered closed-loop decision framework` |
| 资源、调度和扰动形成的综合压力 | `operational pressure` |
| 实验中的四档设置 | `episode difficulty` |
| 是否完成救援目标 | `task completion` |
| 时间、资源、协调和稳定性表现 | `execution quality` |
| 动态条件下维持或恢复任务 | `mission continuity` |
| 正式模块名称 | `Validation`, `Memory`, `Runtime Replanning` |
| 一般处理过程 | `validation`, `memory retrieval`, `runtime replanning` |

`pipeline` 仅用于描述具体数据处理路径。讨论论文整体方法和贡献时，使用 `framework` 或 `closed-loop decision system`。

## 4. 不修改范围

本轮修改严格限定为语言表达和段落衔接，不修改以下内容：

- 任务定义、符号和数学公式；
- 系统模块、数据流和算法步骤；
- 难度等级、评价指标及其计算方式；
- 模型配置、episode 数量和训练设置；
- 表格数值、图像内容和实验结果；
- 现有章节顺序和三组实验顺序；
- 已确定的 baseline 结论边界。

## 5. 实施顺序

1. 先重写 Introduction 和 Related Work，确立问题、研究缺口和设计需求。
2. 再调整 System Overview 的开头、架构说明及模块间衔接，使系统设计回应前文提出的问题。
3. 调整 Evaluation Suite 和 Experiments 的导入与总结段，使评测设计和三组实验逐一回答中心问题。
4. 最后统一 Abstract 和 Conclusion，使全文首尾使用相同的研究问题和结论结构。

## 6. 验收标准

修改完成后应满足以下要求：

1. 读者能够从摘要和引言中明确识别唯一的中心研究问题。
2. 每个系统机制都对应一个具体的闭环决策风险，而不是作为独立功能出现。
3. 三组实验分别对应整体能力、组件作用和部署可行性。
4. 各章开头和结尾能够回到同一条闭环决策主线。
5. Git diff 只包含叙事文字变化，不涉及定义、公式、表格数据、实验配置和图表。
6. 完整编译后不存在未解析引用、LaTeX 警告或新增段落引起的版面溢出。
