# 仿真任务综合评分说明

---

## 1 子指标计算

### 1.1 `completion`（火点完成率）

$$\text{score} = 100 \times \frac{\text{covered}}{\text{total\_fire\_points}}$$

纯粹的火点覆盖比例。

### 1.2 `response`（火点响应时效）

1. 收集所有已覆盖火点的 `effective_s`（`fly_to_point → drop_water_bomb`，扣除中断耗时）
2. 分别计算平均响应时间 `avg_response` 和最差响应时间 `worst_response`
3. 分别线性评分后加权：

$$\text{avg\_score} = \text{linear\_score}(avg\_response,\ 70,\ 180)$$

$$\text{worst\_score} = \text{linear\_score}(worst\_response,\ 100,\ 260)$$

$$\text{response} = 0.65 \times \text{avg\_score} + 0.35 \times \text{worst\_score}$$

| 参数 | best | worst |
|------|------|-------|
| 平均响应 | 70s | 180s |
| 最差响应 | 100s | 260s |

### 1.3 `time`（任务耗时）

$$\text{score} = \text{linear\_score}(mission\_duration\_s,\ 450,\ 1500)$$

| 参数 | best | worst |
|------|------|-------|
| 任务总时长 | 450s | 1500s |

### 1.4 `event_stability`（事件稳定性）

$$\text{score} = \max(0,\ 100 - 35 \times trigger\_count - 15 \times replan\_count - 20 \times resupply\_count)$$

| 事件 | 每次扣分 |
|------|----------|
| `trigger`（突发事件） | -35 |
| `replan`（重规划新增火点） | -15 |
| `resupply`（补给） | -20 |

### 1.5 `resource_pressure`（资源压力）

$$\text{total\_energy\_score} = \text{linear\_score}(total\_consumed\_pct\_sum,\ 120,\ 220)$$

$$\text{max\_uav\_score} = \text{linear\_score}(max\_single\_uav\_consumed\_pct,\ 35,\ 75)$$

$$\text{resource} = 0.65 \times \text{total\_energy\_score} + 0.35 \times \text{max\_uav\_score}$$

| 参数 | best | worst |
|------|------|-------|
| 全队总耗电百分比之和 | 120% | 220% |
| 单机最高耗电百分比 | 35% | 75% |

### 1.6 `coordination`（负载均衡）
`

1. 对三个维度分别计算变异系数 $CV = \sigma / \mu$：

| 维度 | 含义 |
|------|------|
| `actions` | 每架无人机完成的任务动作数 |
| `distance_m` | 每架无人机的飞行距离 |
| `duration_s` | 每架无人机的执行时长 |

2. 取三个 CV 的平均值 `avg_cv`

$$\text{coordination} = 100 \times (1 - \text{clamp}(avg\_cv,\ 0,\ 1))$$

### 1.7 加权原始分数

$$\text{raw\_score} = \sum_{k \in \text{subs}} \text{subs}[k] \times \text{weights}[k]$$

权重：

| 子指标 | 权重 |
|--------|------|
| `completion` | 35% |
| `response` | 20% |
| `time` | 15% |
| `event_stability` | 15% |
| `resource_pressure` | 10% |
| `coordination` | 5% |

---

## 2 难度压力系数修正

$$\text{pressure} = 0.25 \times \text{clamp}\left(\frac{\text{fire\_points} - 2}{5},\ 0,\ 1\right) + 0.30 \times \text{clamp}\left(\frac{\text{trigger\_count}}{2},\ 0,\ 1\right) + 0.20 \times \text{clamp}\left(\frac{\text{resupply\_count}}{2},\ 0,\ 1\right) + 0.25 \times \text{clamp}\left(\frac{\text{mission\_duration\_s} - 600}{900},\ 0,\ 1\right)$$

| 维度 | 权重 | 公式 | 饱和点 |
|------|------|------|--------|
| 火点数 | 25% | `(fire_points - 2) / 5` | ≥ 7 个 |
| 突发事件 | 30% | `trigger_count / 2` | ≥ 2 次 |
| 补给次数 | 20% | `resupply_count / 2` | ≥ 2 次 |
| 任务时长 | 25% | `(duration_s - 600) / 900` | ≥ 1500s |

修正公式：

$$\text{score\_after\_pressure} = \text{raw\_score} \times (1 - 0.25 \times \text{pressure})$$

> **设计意图**：同等规划质量下，困难场景的 raw_score 天然偏低。难度压力系数让困难场景的 raw_score 扣得少一些。

---

### 3 最终分数

$$total\_score = \text{clamp}(score\_after\_caps,\ 0,\ 100)$$

**计算流程总览**

```
              ┌───────────────┼───────────────┐
              │               │               │
         completion       response          time
           (35%)           (20%)            (15%)
              │               │               │
              ├─────── event_stability ───────┤
              │            (15%)              │
              │               │               │
              ├────── resource_pressure ──────┤
              │            (10%)              │
              │               │               │
              └─────── coordination ──────────┘
                           (5%)
                              │
                     raw_score (加权求和)
                              │
                    × (1 - 0.25 × pressure)
                              │
                    硬性惩罚 (上限 / 折扣)
                              │
                     clamp(0, 100)
                              │
                        total_score
```