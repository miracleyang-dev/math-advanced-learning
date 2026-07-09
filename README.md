# Math Advanced Learning

进阶数学课程学习笔记，中文撰写，保留数学术语原文。

面向 **深度生成 / 推理模型** 研究的数学底子。以"学到东西、可以直接对接论文"为标准挑选教材与主讲，不锁定单一课程来源。

> 本仓库采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可证，详见 [来源声明](#来源声明)。

---

## 学习路径

三门主课并行推进，两条线在"生成模型 / 变分推断"处合流。

| 顺序 | 课程 | 主教材 / 主讲 | 状态 | 进度 |
|------|------|---------------|------|------|
| 1 | [泛函分析](./functional-analysis/) | MIT 18.102 (Rodriguez) + Rudin *Functional Analysis* | 重启 | 0 / 22 |
| 2 | [随机过程](./stochastic-processes/) | Durrett *Probability: Theory and Examples* 5e + Le Gall + Särkkä | 进行中 | 0 / 20 |
| 3 | [信息论](./information-theory/) | Cover & Thomas 2e + Polyanskiy & Wu *From Coding to Learning* + MIT 6.441 | 进行中 | 0 / 18 |

每门课的详细章节地图见各自目录下的 `README.md`。

## 讲义制作方式

每讲一个自包含 HTML 文件（`<course>/src/lecture-XX.html`），MathJax 3 渲染公式，样式统一（`.def-box` / `.thm-box` / `.proof-box` / `.remark`）。用 `scripts/generate_pdf.py` 渲染为 PDF 提交到课程根目录。

讲义由 AI 辅助生成，遵循 [`PROMPT.md`](./PROMPT.md) 中的规范；模板见 [`templates/lecture-template.html`](./templates/lecture-template.html)。

## 目录结构

```
math-advanced-learning/
├── functional-analysis/
│   ├── README.md               # 泛函分析章节地图 + 符号约定
│   └── src/                    # lecture-XX.html
├── stochastic-processes/
│   ├── README.md
│   └── src/
├── information-theory/
│   ├── README.md
│   └── src/
├── templates/
│   └── lecture-template.html   # HTML 骨架
├── scripts/
│   └── generate_pdf.py         # HTML → PDF
├── PROMPT.md                   # AI 生成讲义的 prompt 规范（三种输入源）
└── README.md
```

## 生成 PDF

```bash
pip install playwright
python -m playwright install chromium
python scripts/generate_pdf.py stochastic-processes/src/lecture-01.html ^
  -o stochastic-processes/随机过程_L1.pdf
```

PDF 通过 Git LFS 存储（见 `.gitattributes`）。

## 来源声明

本仓库为个人学习整理，包含基于以下公开材料的衍生笔记：

- **MIT 18.102 Introduction to Functional Analysis**（Dr. Casey Rodriguez）— [MIT OpenCourseWare](https://ocw.mit.edu/), CC BY-NC-SA 4.0
- **MIT 6.441 Information Theory**（Prof. Yury Polyanskiy）— 课程主页公开讲义
- Durrett R. *Probability: Theory and Examples*, 5e — 教学引用
- Cover T., Thomas J. *Elements of Information Theory*, 2e — 教学引用
- Le Gall J.-F. *Brownian Motion, Martingales, and Stochastic Calculus* — 教学引用
- Särkkä S., Solin A. *Applied Stochastic Differential Equations* — 教学引用
- Polyanskiy Y., Wu Y. *Information Theory: From Coding to Learning* — 作者公开草稿

本仓库非任何机构官方出版物，作者与相应版权持有者不为本仓库背书。

## 许可证

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

本作品采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可协议。
