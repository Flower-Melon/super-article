## 3. Structured Scenario State and Evaluation Protocol

### 核心聚焦问题

每个 benchmark instance 是什么，以及这些场景如何测试模型能力。

### 写作要点

1. 将每个测试样例定义为 **structured rescue scenario state**，而不是普通数据样本。

2. 使用结构化表示：

   ```text
   S = {O, F, R, U, C, E, G}
   ```

3. 说明各元素含义：

   - **O: Aerial observations**  
     UAV 空中图像或多视角观测。

   - **F: Fire-risk elements**  
     火点、烟雾、潜在扩散点等风险元素。

   - **R: Risk-region abstraction**  
     由火险元素聚合得到的任务区域。

   - **U: UAV operational states**  
     UAV 位置、电量、载荷、通信状态和可用性。

   - **C: Mission constraints**  
     续航、载荷、任务优先级、协同关系等约束。

   - **E: Event-driven perturbations**  
     UAV 故障、电量不足、新火点、火势扩散、通信退化等动态事件。

   - **G: Evaluation goals**  
     当前场景希望测试的能力目标。

4. 强调 **G** 的作用：每个场景不仅描述救援态势，也明确规定需要测试的决策能力。

5. 进一步说明场景如何转化为工程化评估协议：模型需要沿着完整救援链条完成感知、理解、规划、重规划和约束检查。

6. 评估链条可以概括为：

   ```text
   O → F → R → P → P'
   ```

   其中：

   - O → F：从空中观测识别火险元素。
   - F → R：将火险元素抽象为风险区域。
   - R, U, C → P：基于风险区域、UAV 状态和任务约束生成初始任务计划。
   - P, E → P'：在扰动事件发生后进行任务重规划。
   - P' checking：检查最终计划是否满足资源、时序、协同和可用性约束。

7. 这一部分的目标是把 benchmark instance 和 evaluation protocol 统一起来，说明场景不是静态输入，而是驱动闭环决策评估的结构化状态。

---