# AI每日复盘教练 - 使用指南

## 一、快速开始

### 1. 环境要求

- Python 3.8+
- 能够访问大模型 API（推荐 DeepSeek，免费注册即可使用）

### 2. 安装依赖

```bash
pip install openai pyyaml
```

### 3. 获取 API Key

推荐使用 **DeepSeek**（国内可用，注册送免费额度）：

1. 访问 https://platform.deepseek.com
2. 注册账号
3. 在「API Keys」页面创建 API Key
4. 复制 API Key

### 4. 配置

```bash
# 复制配置模板
cp skill/references/config_example.yaml config.yaml

# 编辑 config.yaml，将 api_key 替换为你的真实 Key
```

### 5. 运行

```bash
# 每日复盘
python skill/scripts/daily_review.py

# 周度汇总（每周日运行）
python skill/scripts/weekly_summary.py
```

## 二、每日复盘流程

```
你输入今日描述
      ↓
AI 生成 3 个深度追问
      ↓
你逐一回答这 3 个问题
      ↓
AI 分析你的回答，输出：
  - 📌 今日关键事件
  - 🔍 卡点分析
  - 💡 明天一个重点建议
  - 📊 今日状态评分
      ↓
自动保存为 Markdown 文件
```

## 三、使用技巧

### 输入技巧

- **越真实越好**：AI 需要真实的素材才能给出有价值的分析
- **越具体越好**：说"今天高数刷了20道积分题，错了5道"比"今天学习了"好
- **允许自己说"什么都没干"**：这种描述本身就能触发 AI 有价值的追问

### 回答技巧

- 像跟朋友聊天一样，不需要写得正式
- 如果你觉得某个问题问到了点子上，多写一点
- 如果不知道答案，就说"不知道"——AI 会根据你的回答调整方向

## 四、常见问题

### Q: API 调用失败怎么办？
A: 检查以下内容：
1. config.yaml 中的 api_key 是否正确
2. 网络是否能访问 API 地址
3. API 账户是否有余额/额度

### Q: 想用其他大模型怎么办？
A: 修改 config.yaml 中的 base_url、api_key、model，只要兼容 OpenAI API 格式即可。

### Q: 如何查看历史的复盘记录？
A: 所有复盘都保存在 `reviews/` 目录下，以 Markdown 格式存储，可以直接用任何编辑器打开。

### Q: 不想把数据发到云端怎么办？
A: 本项目依赖云端大模型 API。如果你有本地部署的大模型（如 Ollama），可以将 base_url 指向本地地址。

## 五、最佳实践

1. **每天固定时间复盘**：建议晚上睡前10分钟
2. **先写再做**：写下今天的情况，让 AI 追问，再深入思考
3. **每周日做周度汇总**：看看哪些问题在反复出现
4. **不要追求完美**：哪怕只写一句话，也比不写好
5. **诚实面对自己**：AI 不会评判你，但你的诚实会让分析更准
