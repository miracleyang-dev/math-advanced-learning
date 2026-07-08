# Math Advanced Learning

进阶数学课程学习笔记，中文撰写，保留数学术语原文。

> 本仓库采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可证，详见 [来源声明](#来源声明)。

---

## 学习路径 (MIT 课程体系)

严格遵循 MIT 数学系进阶路径，按下列顺序推进：

| 顺序 | 课程 | 来源 | 状态 | 进度 |
|------|------|------|------|------|
| 1 | [泛函分析](./functional-analysis/) | MIT 18.102 | 进行中 | 10 / 23 |
| 2 | [离散概率与随机过程](./stochastic-processes/) | MIT 18.619J | 进行中 | 3 / 25 |
| 3 | 信息论 | MIT 18.424 | 计划中 | 0 / — |
| 4 | 离散数学 | MIT 18.404 | 计划中 | 0 / — |
| 5 | 组合分析 | MIT 18.211 | 计划中 | 0 / — |

## 泛函分析 — MIT 18.102

授课：Dr. Casey Rodriguez

| # | 主题 | 笔记 |
|---|------|------|
| 1 | Basic Banach Space Theory | [泛函分析_L1](./functional-analysis/泛函分析_L1.pdf) |
| 2 | Bounded Linear Operators | [泛函分析_L2](./functional-analysis/泛函分析_L2.pdf) |
| 3 | Quotient Spaces, Baire Category Theorem | [泛函分析_L3](./functional-analysis/泛函分析_L3.pdf) |
| 4 | Open Mapping Theorem, Closed Graph Theorem | [泛函分析_L4](./functional-analysis/泛函分析_L4.pdf) |
| 5 | Zorn's Lemma, Hahn-Banach Theorem | [泛函分析_L5](./functional-analysis/泛函分析_L5.pdf) |
| 6 | Double Dual, Outer Measure | [泛函分析_L6](./functional-analysis/泛函分析_L6.pdf) |
| 7 | Sigma Algebras | [泛函分析_L7](./functional-analysis/泛函分析_L7.pdf) |
| 8 | Lebesgue Measurable Subsets and Measure | [泛函分析_L8](./functional-analysis/泛函分析_L8.pdf) |
| 9 | Lebesgue Measurable Functions | [泛函分析_L9](./functional-analysis/泛函分析_L9.pdf) |
| 10 | Simple Functions | [泛函分析_L10](./functional-analysis/泛函分析_L10.pdf) |
| ... | ... | ... |

### 涵盖内容

- 赋范空间、完备性、Banach 空间
- 泛函、Hahn-Banach 定理、对偶性
- Lebesgue 测度、可测函数、L^p 空间
- Hilbert 空间、标准正交基、Fourier 级数
- 紧算子、自伴算子、谱定理

## 离散概率与随机过程 — MIT 18.619J

授课：Prof. Elchanan Mossel

| # | 主题 | 笔记 |
|---|------|------|
| 1 | 概率空间回顾与集中不等式 (Markov / Chebyshev / Chernoff / Hoeffding / McDiarmid) | [随机过程_L1](./stochastic-processes/随机过程_L1.pdf) |
| 2 | 条件期望与鞅 (Doob 鞅、可选停止、Azuma-Hoeffding、鞅收敛) | [随机过程_L2](./stochastic-processes/随机过程_L2.pdf) |
| 3 | 马尔可夫链与混合时间 (平稳分布、耦合、谱间隙、Cutoff) | [随机过程_L3](./stochastic-processes/随机过程_L3.pdf) |
| ... | ... | ... |

### 涵盖内容

- 集中不等式：Markov / Chebyshev / Chernoff / Hoeffding / McDiarmid
- 条件期望、滤过、Doob 鞅、可选停止定理
- Azuma-Hoeffding 与鞅集中方法
- 有限状态马尔可夫链、平稳分布、可逆性
- 混合时间、耦合方法、谱间隙、Cutoff 现象
- Glauber 动力学、MCMC 与统计物理应用

## 后续课程 (计划中)

以下课程将在完成前两门后依序推进，笔记与练习将补充到相应目录：

- **MIT 18.424 信息论 (Seminar in Information Theory)** — 熵、互信息、信源信道编码、Shannon 定理
- **MIT 18.404 离散数学 (Theory of Computation)** — 自动机、可计算性、复杂度类
- **MIT 18.211 组合分析 (Combinatorial Analysis)** — 生成函数、Polya 计数、极值组合、随机方法

## 笔记制作方式

每讲笔记基于以下材料整理：

1. MIT OpenCourseWare 发布的**官方讲义**
2. 课程录像的**视频字幕**
3. **个人重组** — 以定义、定理、证明、小结的结构重新编排，中文撰写

数学公式使用 MathJax 排版，渲染为 PDF。

## 来源声明

本仓库包含基于以下材料的衍生作品：

- **MIT 18.102 Introduction to Functional Analysis, Spring 2021**
  授课：Dr. Casey Rodriguez
  来源：[MIT OpenCourseWare](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/)
  许可证：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

- **MIT 18.619J Discrete Probability and Stochastic Processes**
  授课：Prof. Elchanan Mossel
  来源：[MIT OpenCourseWare](https://ocw.mit.edu/)
  许可证：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

本仓库为独立整理的学习笔记，非 MIT 官方出版物，MIT 不为本仓库背书。

## 许可证

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

本作品采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可协议。
