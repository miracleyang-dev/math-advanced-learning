# 随机过程 (Stochastic Processes)

**主教材**：Durrett R. *Probability: Theory and Examples*, 5e（测度论概率主干）  
**SDE 主线**：Le Gall J.-F. *Brownian Motion, Martingales, and Stochastic Calculus*（Springer GTM 274）  
**ML 桥接**：Särkkä S., Solin A. *Applied Stochastic Differential Equations*（Cambridge）  
**参考主讲**：MIT 6.436 Fundamentals of Probability（测度论概率），Berkeley Stat 205 讲义（Aldous）

## 章节地图（20 讲）

### Part I — 测度论概率与鞅（L1–L5）
| # | 主题 | Durrett 5e |
|---|------|-----------|
| L1 | 概率空间、σ-代数、随机变量、分布与期望的测度论重述 | §1.1–1.3, §1.6 |
| L2 | 独立性、Kolmogorov 0–1 律、条件期望作为 $L^2$ 投影 | §2.1–2.2, §4.1 |
| L3 | 滤过、离散时间鞅、Doob 分解 | §4.2–4.3 |
| L4 | 可选停止定理、鞅不等式 | §4.4–4.5 |
| L5 | 鞅收敛定理、一致可积、$L^p$ 收敛 | §4.6–4.7 |

### Part II — 马氏过程（L6–L8）
| # | 主题 |
|---|------|
| L6 | 马氏链：转移核、不变测度、可逆性 |
| L7 | 遍历性、大数律、混合时间入门 |
| L8 | 连续时间马氏过程、生成元、Kolmogorov 前后向方程 |

### Part III — Brownian 与 Itô（L9–L14）
| # | 主题 | Le Gall |
|---|------|--------|
| L9 | Brownian 运动：构造（Lévy）、样本轨道性质 | Ch.1 |
| L10 | Brownian 的鞅性质、Lévy 刻画 | Ch.2 |
| L11 | 二次变差、Itô 积分构造（简单过程 → $L^2$ 拓展） | Ch.4 |
| L12 | Itô 公式、多维形式 | Ch.5 |
| L13 | SDE：存在唯一性（Lipschitz 系数） | Ch.7 |
| L14 | Girsanov 定理、测度变换 | Ch.5 §5.2 |

### Part IV — 分布方程与遍历（L15–L16）
| # | 主题 |
|---|------|
| L15 | Fokker–Planck / Kolmogorov 前向方程；平稳分布 |
| L16 | Langevin 动力学的遍历性；Metropolis-adjusted Langevin |

### Part V — 与生成模型合流（L17–L20）
| # | 主题 | 目标论文 |
|---|------|--------|
| L17 | Score Matching 数学基础：Fisher divergence 与 denoising SM | Hyvärinen 2005；Vincent 2011 |
| L18 | Diffusion 模型的 SDE 统一视角：VE / VP / sub-VP | Song et al. ICLR 2021 |
| L19 | 反向 SDE 与 probability-flow ODE | Anderson 1982；Song 2021 |
| L20 | 论文精读专章：DDPM / flow matching / stochastic interpolants | Ho 2020；Lipman 2023 |

## 符号约定

- 概率空间 $(\Omega, \mathcal F, \mathbb P)$，滤过 $\{\mathcal F_t\}_{t\ge 0}$
- 期望 $\mathbb E$，条件期望 $\mathbb E[\cdot\mid\mathcal G]$
- Brownian 运动统一记为 $B_t$（对齐 Le Gall；Durrett 用 $B_t$，Särkkä 用 $\beta_t$，本仓库不采）
- 一般半鞅记 $X_t, M_t$；SDE 记 $\mathrm dX_t = b(t,X_t)\,\mathrm dt + \sigma(t,X_t)\,\mathrm dB_t$
- 二次变差 $[X]_t$，二次协变差 $[X,Y]_t$
- 转移核 $P(x, A)$；生成元 $\mathcal L$

## 与研究方向的桥接

- L11–L14 Itô / SDE / Girsanov → 扩散模型训练目标推导的核心工具
- L15 Fokker–Planck → 反向过程的 marginal 演化
- L16 Langevin → MCMC 采样、score-based 生成
- L17–L19 → 与 information-theory 课的 VAE ELBO / MI 估计合流
- 附加：Neural SDE、Continuous Normalizing Flow、Rectified Flow
