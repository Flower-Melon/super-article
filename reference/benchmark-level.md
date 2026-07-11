## 4. Progressive Stress-testing Regimes

### 核心聚焦问题

benchmark 如何通过难度组织实现系统性的压力测试。

### 写作要点

1. 将难度设计写成 **progressive stress-testing regimes**，而不是普通 difficulty levels。

2. 强调四个 regime 构成从静态理解到动态多 UAV 协同重规划的压力阶梯。

3. **Simple regime**  
   面向静态、低复杂度火险场景，主要测试基础火险识别和优先级判断。

4. **Normal regime**  
   引入多火点和多风险区域，主要测试空间火险理解和风险区域抽象。

5. **Hard regime**  
   引入资源限制和单类或少量扰动，主要测试 UAV 约束下的任务调整与重规划。

6. **Expert regime**  
   引入多扰动并发、火势扩散和资源冲突，主要测试多 UAV 动态协同、冲突处理和危机决策。

7. 将 regime 的递进关系落实到可控工程变量上：

   - Fire-risk density
   - Number of risk regions
   - Number of UAVs
   - Resource scarcity
   - Communication degradation
   - Perturbation types
   - Perturbation concurrency
   - Fire spread intensity

8. 这一部分的目标是说明 benchmark 的难度不是主观划分，而是由工程变量控制的系统化压力测试机制。