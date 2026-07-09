# 泛函分析 (Functional Analysis)

**主讲**：MIT 18.102 Introduction to Functional Analysis, Spring 2021, Dr. Casey Rodriguez  
**主教材**：Rudin W. *Functional Analysis*, 2e（严谨基线）  
**辅助**：Brezis H. *Functional Analysis, Sobolev Spaces and PDEs*（PDE 视角），Reed & Simon Vol.1（谱理论）

## 章节地图（22 讲）

### Part I — 赋范空间与线性算子（L1–L6）
| # | 主题 | Rudin 参考 |
|---|------|-----------|
| L1 | 向量空间、范数、Banach 空间；有限维 vs 无穷维的本质区别 | §1.1–1.4 |
| L2 | 有界线性算子、算子范数、$\mathcal B(X,Y)$ 的完备性 | §4.1–4.3 |
| L3 | 商空间与 Baire 纲定理 | §2.2 |
| L4 | 开映射定理、闭图像定理、一致有界原理 | §2.6, §2.11 |
| L5 | Zorn 引理与 Hahn–Banach 定理（解析 + 几何形式） | §3.1–3.4 |
| L6 | 对偶空间、双对偶、自反性 | §4.5 |

### Part II — 测度与积分（L7–L12）
| # | 主题 |
|---|------|
| L7 | σ-代数、外测度、Carathéodory 扩张 |
| L8 | Lebesgue 可测集与 Lebesgue 测度 |
| L9 | 可测函数、Egorov 与 Lusin |
| L10 | 简单函数、Lebesgue 积分 |
| L11 | 收敛定理：MCT、Fatou、DCT |
| L12 | Fubini 与 Tonelli；乘积测度 |

### Part III — L^p 空间（L13–L16）
| # | 主题 |
|---|------|
| L13 | Hölder、Minkowski、$L^p$ 完备性 |
| L14 | 稠密子集、可分性、对偶 $(L^p)^* = L^q$ |
| L15 | 弱收敛、Banach–Alaoglu |
| L16 | 卷积、光滑逼近、Sobolev 初步 |

### Part IV — Hilbert 空间与谱理论（L17–L22）
| # | 主题 |
|---|------|
| L17 | Hilbert 空间、正交投影、Riesz 表示 |
| L18 | 标准正交基、Fourier 级数 |
| L19 | 紧算子的谱定理 |
| L20 | 自伴算子与谱分解 |
| L21 | 无界自伴算子与 Cayley 变换 |
| L22 | 论文精读：泛函分析在深度学习中的应用（如 RKHS、算子学习 Neural Operator） |

## 符号约定

- 域 $\mathbb K \in \{\mathbb R, \mathbb C\}$
- Banach 空间通常用 $X,Y,Z$；Hilbert 空间用 $H$
- 有界线性算子空间 $\mathcal B(X,Y)$，其算子范数 $\|T\|_{\mathrm{op}}$
- 对偶空间 $X^*$；对偶配对 $\langle x^*, x\rangle$
- $L^p(\mu)$ 表示测度空间 $(X,\mathcal A,\mu)$ 上的 $L^p$
- 内积 $\langle\cdot,\cdot\rangle$ 关于第一变量线性（数学惯例，非物理惯例）

## 与研究方向的桥接

- 无穷维优化（Fréchet 导数、变分法）→ Neural ODE / Neural Operator
- RKHS → kernel methods, NTK
- 谱理论 → Graph Laplacian, diffusion maps
- Sobolev 空间 → PINN, PDE-based generative models
