---
name: ai-daily-review-coach
version: "1.0.0"
description: >-
  AI每日复盘教练 —— AI是镜子，通过提问帮你想清楚今天干了什么、哪里卡壳、明天重点是什么。
  不支持简单打卡，逼你深度思考。
author: AI实践项目
tags:
  - 复盘
  - 自我管理
  - 成长
  - 学生
dependencies:
  - python>=3.8
  - openai>=1.0.0
  - pyyaml>=6.0
---

# AI每日复盘教练

## 一、技能简介

**AI每日复盘教练** 是一个基于大语言模型的每日反思工具。

它不是打卡软件，而是一面"镜子"——通过3个深度追问，帮你：
- 提炼今日关键事件
- 识别重复出现的卡点
- 给出明天1个可执行的改进建议

复盘结果自动保存为 Markdown 文件，支持周度汇总和月度成长报告。

## 二、核心价值

没有 AI 这个功能根本做不到：
- **智能追问**：根据你的回答动态生成追问，而非固定模板
- **模式识别**：积累一周/一月数据后，AI 自动发现你重复踩的坑
- **情感理解**：不只是分析事实，还会识别你的情绪状态并给予回应

## 三、使用方法

### 环境准备

```bash
pip install openai pyyaml
```

### 配置 API Key

复制 `references/config_example.yaml` 为 `config.yaml`，填入你的 API Key：

```bash
cp skill/references/config_example.yaml config.yaml
# 编辑 config.yaml，填写 api_key
```

### 运行每日复盘

```bash
python skill/scripts/daily_review.py
```

按提示输入今日的复盘内容即可。

### 运行周度汇总

```bash
python skill/scripts/weekly_summary.py
```

## 四、文件结构

```
skill/
├── SKILL.md                     # 本文件
├── scripts/
│   ├── daily_review.py          # 每日复盘主程序
│   ├── weekly_summary.py        # 周度汇总程序
│   └── review_core.py           # 核心AI调用逻辑
└── references/
    ├── config_example.yaml      # API配置示例
    └── usage_guide.md           # 详细使用指南
```

## 五、MVP功能清单

- [x] 输入今日描述 → AI生成3个深度问题
- [x] 回答后AI提炼关键事件 + 识别卡点 + 建议
- [x] 保存为Markdown复盘文件
- [x] 周日AI汇总一周复盘，识别重复问题
- [x] 追踪目标完成度，对比月初目标与进度
