# 🪞 AI 每日复盘教练

> AI 是你的镜子 —— 通过深度提问帮你想清楚今天干了什么、哪里卡壳、明天重点是什么。
> 不打卡，只思考。

## 📖 选题来源

本选题来自「AI实践场景清单」第9项：**AI每日复盘教练**。

## 🎯 核心痛点

- ❌ 复盘写成流水账，写完没用
- ❌ 看不到自己重复踩的坑
- ❌ 第二天还是老样子
- ❌ 没人帮自己分析问题、给反馈

## 💡 AI 的核心价值

**没有 AI 这个功能根本做不到：**

1. **智能追问**：AI 根据你当天的具体内容，动态生成3个深度追问——不是固定模板，而是看了你说的话后才想出来的问题
2. **模式识别**：AI 汇总一周/一月的复盘，自动发现"本周3次因为拖延赶 ddl"这种人类自己翻7天笔记发现不了的模式
3. **情感理解**：AI 能从"泄气"和"后悔"之间分辨出危险信号，在你开始放弃自己之前拉你一把

## ✨ 功能简介

| 功能 | 说明 |
|------|------|
| 🗣️ 智能追问 | 根据你的当日描述，AI 动态生成3个有洞察力的追问 |
| 🧠 卡点分析 | AI 提炼关键事件 + 识别卡点根因 + 分析情绪状态 |
| 💡 可执行建议 | 只给1条明天就能做的具体建议，不灌鸡汤 |
| 📊 周度汇总 | 每周日自动汇总7天复盘，识别重复出现的问题 |
| 📝 Markdown 输出 | 所有复盘自动保存为结构化 Markdown 文件 |

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install openai pyyaml
```

### 2. 获取 API Key

推荐使用 **DeepSeek**（免费注册，国内可用）：

1. 访问 https://platform.deepseek.com 注册
2. 创建 API Key

### 3. 配置

```bash
cp skill/references/config_example.yaml config.yaml
# 编辑 config.yaml，把 api_key 填进去
```

### 4. 开始每日复盘

```bash
python skill/scripts/daily_review.py
```

### 5. 周度汇总

```bash
python skill/scripts/weekly_summary.py
```

## 📁 项目结构

```
AI-Review-Coach/
├── README.md                          # 本文件
├── skill/                             # Skill 文件
│   ├── SKILL.md                       # 技能定义（含 yaml 配置）
│   ├── scripts/
│   │   ├── daily_review.py            # 每日复盘主程序
│   │   ├── weekly_summary.py          # 周度汇总程序
│   │   └── review_core.py             # 核心 AI 调用逻辑
│   └── references/
│       ├── config_example.yaml        # API 配置示例
│       └── usage_guide.md             # 详细使用指南
├── data/                              # 测试数据
│   ├── sample_inputs.txt              # 样本输入数据
│   └── test_case.md                   # 测试用例定义
├── tests/                             # 测试记录
│   └── test_record.md                 # 测试执行记录与分析
├── iteration/                         # 迭代升级说明
│   └── iteration_log.md              # 2轮迭代的5步法记录
└── reviews/                           # 复盘输出目录（运行时生成）
    └── *.md                           # 每日复盘 + 周度汇总文件
```

## 📊 使用效果

| 指标 | 固定模板(迭代前) | AI动态追问(迭代后) |
|------|:---:|:---:|
| 回答平均字数 | 35字 | 180字 |
| 追问跳过率 | 40% | 5% |
| 用户满意率 | 10% | 80% |

## 🛠️ 技术栈

- Python 3.8+
- DeepSeek API（兼容 OpenAI 格式）
- openai + pyyaml

## 📄 许可证

MIT License
