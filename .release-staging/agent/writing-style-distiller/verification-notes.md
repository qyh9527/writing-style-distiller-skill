# Writing Style Distiller v2 验证记录

## 重构范围

从 v1 的平铺 XML schema + 线性工作流，迁移到 v2 的 XML 壳+纯文本 + 自适应多阶段工作流 + 审查门。

## 迁移清单

- [x] 删除废弃文件：output-schema.md, prompt-optimization.md, citation-and-examples.md, verification-notes.md
- [x] 创建知识库：knowledge/style-families.md, label-risk-table.md, model-adaptation.md
- [x] 创建格式定义：output-format.md（含汪曾祺完整示例）
- [x] 重写质检清单：quality-checklist.md（5 维精简版）
- [x] 创建阶段指令：phases/research.md, diagnosis.md, drafting.md, optimization.md
- [x] 重写主入口：SKILL.md（自适应路由 + 审查门）
- [x] 创建验证记录：verification-notes.md

## 基线对比

### v1 失败模式（RED）

- XML 子标签嵌套过深（4 系统 × 3-6 子字段 ≈ 20+ 字段），Claude 容易忽略子标签
- 固定填充要求导致弱字段被 AI 乱造名词注水
- 所有风格用同一 schema，违反「不同文风风不能共享模板」的社区共识
- 无中间产物，用户只能在最终输出后才能介入
- 目标 1100-1400 tokens 偏重

### v2 预期通过（GREEN）

- 一级 XML 分区 + 纯文本内容，边界清晰且 token 高效
- 按风格家族自适应密度（600-1200 tokens），不需要的区块可压缩/省略
- 三种深度模式自动匹配输入复杂度
- 每阶段文件落盘 + 审查门，用户可在关键节点介入
- 知识库独立管理，便于维护和扩展

## 验证案例

### 案例 1：汪曾祺（深度模式 / 语言特征类）
- 输入类型：作者名 → 深度模式 4 阶段
- 风格家族：语言特征类
- 预期行为：
  - P1 搜索收集《受戒》等原文摘录
  - P2 诊断为语言特征类，aesthetics 语言区高密度
  - P3 生成 XML 壳+纯文本初稿
  - P4 质检通过，终稿 ~1000 tokens

### 案例 2：二次元文风（标准模式 / 情感表达类）
- 输入类型：风格描述（>100字）→ 标准模式 3 阶段
- 风格家族：情感表达类
- 预期行为：
  - P1 分析描述中的情感/段落特征
  - P2 生成初稿，expression 和 aesthetics 高密度
  - P3 质检通过，终稿 ~800 tokens

### 案例 3：已有文风微改（快速模式）
- 输入类型：已有文风 + 修改请求 → 快速模式 2 阶段
- 预期行为：
  - P1 直接修改并生成草稿
  - P2 质检输出
