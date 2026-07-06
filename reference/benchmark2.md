## 2. UAV-AirSim Co-design Environment

### 核心聚焦问题

这个 benchmark 的工程真实性从哪里来。

### 写作要点

1. 将真实 UAV 和 AirSim 写成协同设计关系，而不是分别介绍两个平台。

2. 真实 UAV 平台负责提供工程约束，定义救援任务的实际边界。

3. 真实 UAV 约束包括：

   - Flight altitude
   - Camera field of view
   - Battery endurance
   - Payload capacity
   - Communication range
   - Failure modes
   - Mission execution workflow

4. AirSim 负责提供可控、可复现、可扩展的场景生成后端，用于构建现实中难以安全采集的大规模森林火灾救援场景。

5. AirSim 支撑的场景生成能力包括：

   - Simulated camera settings
   - UAV viewpoints
   - Mission context
   - Fire-risk placement
   - Perturbation events
   - Repeatable simulation parameters

6. 补充 real-to-sim 映射关系，使 **sim-to-real informed benchmark** 成为具体工程机制：

   - Real UAV altitude range → AirSim observation height
   - Real camera FOV → Simulated camera configuration
   - Battery capacity → Endurance constraint
   - Payload capacity → Resource allocation constraint
   - Communication range → Coordination availability constraint
   - Failure modes → Event-driven perturbation types

7. 强调 benchmark scenario 是在真实 UAV 参数约束下由 AirSim 生成的，从而避免纯仿真场景脱离实际 UAV 任务边界。

8. 这一部分的目标是把 **sim-to-real informed benchmark** 写实，而不是写成概念口号。

---