## 1. Task Motivation and Benchmark Positioning

### 核心聚焦问题

为什么 UAV 森林火灾救援需要一个新的 benchmark，以及该 benchmark 应该被定位成什么。

### 写作要点

1. 先说明本文 benchmark 面向 UAV-assisted forest fire rescue，核心目标是评估模型在森林火灾救援中的闭环决策能力。

2. 将任务边界定义为一个连续决策链：

   ```text
   Aerial Perception
   → Spatial Fire-risk Interpretation
   → Resource-constrained Mission Planning
   → Event-driven Replanning
   ```

3. 强调该任务不是单纯的火点检测，也不是单纯的路径规划，而是跨越感知、空间风险理解、资源约束和动态重规划的综合救援任务。

4. 说明现有 benchmark 的核心问题是 evaluation boundary mismatch，即它们无法覆盖 UAV 森林火灾救援的完整评估边界。

5. 展开四类已有 benchmark 的不足：

   - Vision benchmark 关注火点、烟雾或目标检测，但缺少下游救援决策链。
   - Multi-agent planning benchmark 关注任务分配或路径规划，但缺少灾害语义和火险动态。
   - LLM / agent benchmark 关注推理、工具使用或通用规划，但缺少 UAV 级工程约束。
   - Disaster-response benchmark 多关注文本决策支持或宏观协调，缺少细粒度 UAV 任务重规划。

6. 最后引出本文 benchmark 的核心定位：它是一个面向 UAV 森林火灾救援闭环决策的 **sim-to-real informed, scenario-engineered stress-testing protocol**。

---