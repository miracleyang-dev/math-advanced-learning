# 信息论 (Information Theory)

**打底教材**：Cover T., Thomas J. *Elements of Information Theory*, 2e  
**现代研究**：Polyanskiy Y., Wu Y. *Information Theory: From Coding to Learning*（作者公开草稿）  
**推断桥接**：MacKay D. *Information Theory, Inference, and Learning Algorithms*（免费官方 PDF）  
**主讲**：MIT 6.441 Information Theory（Polyanskiy），Stanford EE 376A（Weissman）

## 章节地图（18 讲）

### Part I — Shannon 主干（L1–L7）
| # | 主题 | C&T | P&W |
|---|------|-----|-----|
| L1 | 熵、联合熵、条件熵；链式法则 | Ch.2 | Ch.1 |
| L2 | 互信息、KL 散度、数据处理不等式 | Ch.2 | Ch.2 |
| L3 | AEP、典型集、渐近均分性 | Ch.3 | Ch.10 |
| L4 | 无损信源编码：Kraft、Shannon、Huffman | Ch.5 | Ch.10 |
| L5 | 信道容量：BSC / BEC / Gaussian；Shannon 第二定理 | Ch.7, Ch.9 | Ch.19 |
| L6 | 微分熵、Gaussian 通道容量 | Ch.8, Ch.9 | Ch.3 |
| L7 | 率失真理论 | Ch.10 | Ch.24 |

### Part II — 现代变分工具（L8–L11）
| # | 主题 | 关键结果 |
|---|------|--------|
| L8 | 最大熵原理与指数族 | Boltzmann 分布 |
| L9 | f-divergence 与变分表示 | Donsker–Varadhan；Nguyen-Wainwright-Jordan |
| L10 | Fenchel 对偶、凸共轭、Bregman 散度 | 支撑 L9、L15 |
| L11 | Fano 不等式、下界工具 | 假设检验、极小极大 |

### Part III — 与深度学习合流（L12–L18）
| # | 主题 | 目标论文 |
|---|------|--------|
| L12 | VAE 的 ELBO 推导：KL 分解与重参数化 | Kingma 2014 |
| L13 | Information Bottleneck；Deep VIB | Tishby 1999；Alemi 2017 |
| L14 | 互信息神经估计：MINE、InfoNCE、CPC | Belghazi 2018；Oord 2018 |
| L15 | 对比学习的信息论视角与紧下界 | Poole 2019 |
| L16 | PAC-Bayes 泛化上界 | McAllester 1999；Catoni 2007 |
| L17 | 熵正则化 RL：KL 约束、软 Q-learning、PPO | Haarnoja 2018 |
| L18 | 论文精读：率失真视角的生成模型（Neural Compression / RD-VAE） | Ballé 2018；Yang 2023 |

## 符号约定

- 离散熵 $H(X)$，微分熵 $h(X)$（区别于 Hilbert 空间 $H$，靠上下文）
- 互信息 $I(X;Y)$；条件互信息 $I(X;Y\mid Z)$
- KL 散度 $D_{\mathrm{KL}}(P\|Q)$；一般 $f$-散度 $D_f(P\|Q)$
- 对数默认自然对数 $\ln$（贴 ML 惯例）；只在讨论信道容量时改用 $\log_2$，届时显式声明
- 分布用 $P,Q$；样本用 $x,y$；随机变量用大写 $X,Y$
- 参数化分布 $p_\theta(x)$，编码器 $q_\phi(z\mid x)$，解码器 $p_\theta(x\mid z)$

## 与研究方向的桥接

- L9 变分表示 → L14 MINE / InfoNCE 的理论根源
- L12 ELBO ↔ 随机过程课 L18 Diffusion 的 ELBO（同一变分不等式的不同应用）
- L13 IB → 表征学习的"充分性 vs 最小性"张力
- L16 PAC-Bayes → 泛化理论与贝叶斯深度学习交叉点
- L17 → RLHF、DPO 的理论基座
