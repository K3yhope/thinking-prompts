# thinking-prompts

> 一个把「 问题想透、人生理顺 」的 Skill。如果脑子乱、人生迷？让它接住你。

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  ![Language](https://img.shields.io/badge/language-%E4%B8%AD%E6%96%87-blue)  ![Codex Skill](https://img.shields.io/badge/Codex-Skill-black)  ![Prompt Modes](https://img.shields.io/badge/prompt_modes-12-orange)

## 目录

- [为什么需要它](#为什么需要它)
- [核心亮点](#核心亮点)
- [12 个 Prompt 模式速查](#12-个-prompt-模式速查)
- [安装](#安装)
- [快速开始](#快速开始)
- [使用示例](#使用示例)
- [输出强度](#输出强度)
- [意图不清时怎么办](#意图不清时怎么办)
- [不适合的场景](#不适合的场景)
- [项目结构](#项目结构)
- [贡献](#贡献)
- [许可证与鸣谢](#许可证与鸣谢)

## 为什么需要它

AI 时代，很多人都有一种说不清的「底层能力焦虑」：

- 问不清自己真正想要什么
- 学东西浮在表面，学不深
- 问题解不开，在取舍之间反复横跳
- 往深里看，看不清自己的天赋和人生方向

这些感受叠在一起，就是**迷茫**，再加一个词——**无力**。

说到底，你真正想解决的困扰只有一句： ` **脑子乱、人生迷。** `

我们缺的从来不是某个具体技能，而是一套把问题想透、把人生理顺的方法。`thinking-prompts` 就是来接住这些困扰的。

## 核心亮点

- **一个入口**：基础用户只需要记住 `$thinking-prompts`。
- **自动路由**：根据用户意图，自动分发到 12 个 Prompt 模式。
- **隐式调用**：用自然语言随口一说也能触发，不必每次都背 Skill 名称。
- **中文优先**：默认用中文理解、追问和输出。
- **三档输出**：轻量 / 标准 / 深度，按你的表达自动选择。
- **状态可见**：默认可显示当前模式与输出强度；严格输出格式下自动省略。
- **按需加载**：主入口只负责路由，具体模板放在 `references/`。
- **可复用模板**：支持把任意场景改写成可复制的 Prompt。

## 12 个 Prompt 模式速查

| 场景       | 模式           | 内部模块                       | 适合的问题                         |
| ---------- | -------------- | ------------------------------ | ---------------------------------- |
| 问清问题   | 苏格拉底式提问 | `socratic-clarifier`           | 我现在很乱，不知道真正要问什么     |
| 学习概念   | 双层解释法     | `dual-layer-explainer`         | 这个概念听不懂，想先听懂再深入     |
| 拆解案例   | 反向拆解       | `reverse-breakdown`            | 这个产品 / 页面 / 方案为什么做得好 |
| 深度研究   | 横纵分析法     | `horizontal-vertical-research` | 系统研究一个公司、行业、技术或事件 |
| 核查真假   | 事实核查       | `fact-checking`                | 这个观点、数据、结论到底靠谱吗     |
| 多视角会诊 | 专家会诊       | `expert-panel`                 | 需要多个视角互相挑战后给方案       |
| 回到本质   | 第一性原理     | `first-principles`             | 当前方案像在打补丁，想重新推导     |
| 借鉴外部   | 跨领域借解     | `cross-domain-borrowing`       | 想从其他行业找类似问题的解法       |
| 困难决策   | 双向钢人论证   | `steelman-decision`            | A 和 B 都有道理，不知道怎么选      |
| 现实验证   | 最小实验       | `minimum-experiment`           | 不想继续空想，想低成本试一次       |
| 认识自己   | 挖掘隐藏天赋   | `talent-miner`                 | 想知道自己的底层天赋和优势         |
| 设计未来   | 人生设计术     | `life-designer`                | 想生成多个未来版本和原型行动       |

> 隐式调用人工评测语料存放在 `references/implicit-invocation-audit.md`，用于记录和复查「自然语言 → 模式」的匹配结果。

## 安装

在 Claude Code、Codex 等支持 Agent Skills 的工具里，直接说：

```bash
帮我安装这个 skill：https://github.com/K3yhope/thinking-prompts
```

### 其他兼容 Agent Skills 的工具

只要你的 Agent 支持 Agent Skills / `SKILL.md` 结构，通常只需把整个 `thinking-prompts/` 文件夹复制到该工具约定的 skills 目录即可。

**最低要求：**

- 保留 `thinking-prompts/SKILL.md`。
- 保留整个 `thinking-prompts/references/`，其中包含 12 个模式、按需加载的可复制模板和隐式调用评测语料。
- 若工具支持自动触发，确保它会读取 `SKILL.md` frontmatter 中的 `description`。
- 若工具支持显式调用，调用名称通常来自目录名或 `name: thinking-prompts`。

## 快速开始

**显式调用：**

```text
$thinking-prompts 帮我解释一下什么是第一性原理
```

**隐式调用（不需要记名称）：**

```text
我现在有点乱，先别给建议，帮我把真正的问题想清楚
```

未指定严格输出格式时，输出可能以类似下面的格式开始，让你知道当前处在哪个模式：

```text
当前启用：苏格拉底式提问｜输出强度：标准
```

**前置条件**：你的工具需要支持 Agent Skills / `SKILL.md` 结构（如 Claude Code、Codex、WorkBuddy 等）。

## 使用示例

**学习一个概念：**

```text
简单讲一下 RAG 是什么，再给我一个专业版解释
```

**拆解一个案例：**

```text
拆解一下 Linear 官网为什么看起来高级，提炼成可复用规律
```

**核查一个说法：**

```text
这句话靠谱吗：AI 会在三年内替代 90% 的程序员
```

**做一个困难决策：**

```text
我该继续上班还是做自己的产品？先把两边最强理由都讲出来
```

**设计最小实验：**

```text
我想验证这个副业方向值不值得做，帮我设计一个 7 天最小实验
```

**生成可复制 Prompt：**

```text
$thinking-prompts 把“分析一个创业想法是否值得做”改写成可复制 Prompt
```

## 输出强度

| 强度 | 触发说法                         | 适合场景               |
| ---- | -------------------------------- | ---------------------- |
| 轻量 | 简单讲、快速说下、一句话说       | 先拿到核心判断         |
| 标准 | 解释一下、帮我分析一下、拆解一下 | 默认强度，完整但不啰嗦 |
| 深度 | 深入研究、详细展开、系统分析     | 需要完整框架和更多细节 |

## 意图不清时怎么办

如果用户请求同时可能匹配多个模式，Skill 会**先问一个澄清问题**，而不是硬选。

例如：

```text
帮我看看这个技术
```

可能会先澄清：

```text
你更想快速理解、系统研究，还是核查某个说法真假？
```

## 不适合的场景

以下请求通常**不应**触发本 Skill：

- 直接编码、调试 bug、写测试、运行命令。
- 修改文件、处理 PDF / PPT / 表格、发送邮件。
- 普通翻译、普通总结、普通事实问答。
- 医疗、法律、财务等高风险专业建议。
- 紧急危机或安全风险场景。

## 项目结构

```text
thinking-prompts/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── socratic-clarifier.md          # 苏格拉底式提问
    ├── dual-layer-explainer.md        # 双层解释法
    ├── reverse-breakdown.md           # 反向拆解
    ├── horizontal-vertical-research.md # 横纵分析法
    ├── fact-checking.md               # 事实核查
    ├── expert-panel.md                # 专家会诊
    ├── first-principles.md            # 第一性原理
    ├── cross-domain-borrowing.md      # 跨领域借解
    ├── steelman-decision.md           # 双向钢人论证
    ├── minimum-experiment.md          # 最小实验
    ├── talent-miner.md                # 挖掘隐藏天赋
    ├── life-designer.md               # 人生设计术
    ├── implicit-invocation-audit.md   # 隐式调用人工评测语料
    └── prompt-templates/              # 仅生成可复制 Prompt 时加载
        ├── life-designer.md
        └── talent-miner.md
```

## 贡献

欢迎一起让这套思考工具更好用：

- **新增模式**：在 `references/` 下补充新的 Prompt 模块，并在 `SKILL.md` 的路由表中登记。
- **改进模板**：优化已有模式的话术与结构，让输出更稳定。
- **校准隐式调用**：在 `implicit-invocation-audit.md` 中补充「自然语言 → 模式」的匹配样例。
- 提交前请确保 `SKILL.md` 与 `references/` 结构保持一致，并遵循 MIT 许可证。

如有疑问，欢迎开 Issue 讨论。

## 许可证与鸣谢

本项目基于 [MIT 许可证](LICENSE) 开源。

鸣谢 [@KKKKhazix](https://github.com/KKKKhazix)：提供了优秀的 Prompts。
