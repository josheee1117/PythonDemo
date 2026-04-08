---
id: teaching-standards
type: knowledge
title: 每日训练生成规范
status: active
created: 2026-04-08
updated: 2026-04-08
tags: [teaching, methodology, daily-training, labex, standards]
---

# 每日训练生成规范

本文件定义生成每日学习任务和材料时必须遵守的结构和质量标准。

## 每日训练四环节

每天 120-150 分钟，按以下顺序生成：

### 环节 1：Lab（引导实验）— 40-50 分钟

**对标**：LabEx Learn by Doing 格式

**结构要求**：
- 1-2 个核心概念，不贪多
- 3-6 个短步骤，每步 5-10 分钟
- 每步包含：做什么 → 运行什么 → 看到什么 → 为什么
- starter 文件里 TODO 不超过 5 个
- 步骤间递进：先观察 → 再修改 → 最后从零写
- 必须有 Java 对照说明
- 必须有常见错误部分

**文件命名**：`0X_lab_*.md` + 配套 `0X_*_lab.py`

**反模式**（不要这样做）：
- 一个 Lab 塞入 3+ 个概念
- 大段文字解释后才开始动手
- TODO 超过 5 个变成填空题集
- 缺少预期输出，让用户猜结果

### 环节 2：Challenge（无引导挑战）— 30-40 分钟

**对标**：LabEx Challenge 模式

**结构要求**：
- 只给目标描述和验证条件（测试文件或断言）
- 不给实现步骤和思路提示
- 难度略超当天 Lab 范围，需要查文档或组合概念
- 完成后提供参考实现（放在单独文件或折叠区域）
- 参考实现附 Pythonic 改进点评

**文件命名**：`0X_challenge_*.md` + 配套 `0X_*_challenge.py`（测试/验证文件）

**难度标定**：
- 不能是 Lab 的简单重复
- 需要至少 1 个 Lab 未直接演示但相关的知识点
- 允许多种解法，但参考实现展示最 Pythonic 的方式

### 环节 3：Code Taste（代码品味训练）— 20-30 分钟

**对标**：《Python编程之美》第 4-5 章

**三种训练形式**（每天至少用 1 种）：

1. **对比阅读**：左栏糟糕写法，右栏 Pythonic 写法，逐行解释差异
2. **陷阱识别**：给出含 bug 的代码片段，要求找出问题并修复
3. **重构练习**：给出 Java 风格的 Python 代码（过度抽象、冗长、非 Pythonic），重构为地道写法

**素材来源优先级**：
1. 《Python编程之美》第 4 章中与当天主题匹配的内容
2. 当天 Lab/Challenge 中可以进一步优化的代码
3. 真实项目中的常见反模式

**文件命名**：`0X_taste_*.md`

### 环节 4：日结回顾 — 10 分钟

不生成单独文件，在 daily_tasks 的任务文件末尾以 checklist 形式呈现：
- [ ] 用自己的话总结今天的核心概念（写在日志里）
- [ ] 写出 1 个 Java → Python 的关键差异
- [ ] 标记未理解的问题

## 每日任务文件模板

```markdown
# 第 N 天学习任务

**日期**：YYYY-MM-DD
**学习阶段**：阶段 X - 阶段名
**今日主题**：主题名
**今日品味点**：《Python编程之美》pXX — 具体习语/陷阱名

## 今日目标
- [ ] 目标 1（Lab 相关）
- [ ] 目标 2（Challenge 相关）
- [ ] 目标 3（Code Taste 相关）

## 学习顺序

1. [ ] Lab：标题 — 预计 XX 分钟
2. [ ] Challenge：标题 — 预计 XX 分钟
3. [ ] Code Taste：标题 — 预计 XX 分钟
4. [ ] 日结回顾 — 10 分钟

## 今日完成标准
（具体的可验证条件）

## Java / Python 映射重点
（当天最关键的 1-2 个对比）

## 预计总时长
约 XXX 分钟
```

## 进阶节奏

- **每 3-5 天**：安排 1 个 Mini-Project（综合近几天所学，30-50 行完整小工具）
- **Mini-Project 替换当天的 Challenge 环节**，Lab 和 Code Taste 照常
- **阶段 B 开始后**：Code Taste 环节可引入第 5 章的代码阅读（从 HowDoI 开始递进）

## 文件目录约定

```
python_basics/YYYY-MM-DD/
├── 01_start_here.md          # 入口页
├── 02_lab_*.md                # Lab 说明
├── 03_*_lab.py                # Lab starter 文件
├── 04_challenge_*.md          # Challenge 说明
├── 05_*_challenge.py          # Challenge 测试/验证文件
├── 06_taste_*.md              # Code Taste 训练
└── 07_*_project.py            # Mini-Project（每 3-5 天）
```

## 质量自检

生成材料后，按以下标准自检：
- 每个 Lab 步骤是否都能在 10 分钟内完成？
- Challenge 是否真的没有泄露实现思路？
- Code Taste 的糟糕写法是否真实存在（不是故意编造的稻草人）？
- Java 对照是否点出了真正的思维差异，而非表面语法区别？
- 总时长是否在 120-150 分钟范围内？
