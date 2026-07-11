"""
AI每日复盘教练 - 每日复盘主程序
用法：python daily_review.py
"""

import sys
from datetime import datetime
from pathlib import Path

# 将当前目录加入 path
sys.path.insert(0, str(Path(__file__).parent))

from review_core import (
    load_config,
    create_client,
    generate_questions,
    analyze_review,
    save_review,
)


def main():
    print("=" * 50)
    print("  🪞  AI 每日复盘教练")
    print("=" * 50)
    print()
    print("让我帮你回顾今天，找出卡点，明确明天的方向。")
    print()

    # 1. 加载配置
    try:
        config = load_config()
        client = create_client(config)
        model = config["api"]["model"]
    except Exception as e:
        print(f"❌ 配置加载失败：{e}")
        print()
        print("💡 解决方式：")
        print("   1. 复制 skill/references/config_example.yaml 为 config.yaml")
        print("   2. 编辑 config.yaml，填写你的 API Key")
        return

    # 2. 获取用户今日复盘内容
    print("请输入你今天的情况（可以随便写，越真实越好）：")
    print("（输入完成后按 Enter，然后输入 END 并按 Enter 结束）")
    print()

    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip().upper() == "END":
            break
        lines.append(line)

    user_input = "\n".join(lines).strip()
    if not user_input:
        print("❌ 没有输入内容，退出。")
        return

    print()
    print("🤔 AI 正在思考，生成深度追问...")
    print()

    # 3. AI 生成追问
    try:
        questions = generate_questions(client, model, user_input)
    except Exception as e:
        print(f"❌ AI调用失败（生成追问）：{e}")
        return

    print("─" * 50)
    print(questions)
    print("─" * 50)
    print()

    # 4. 用户回答追问
    print("请逐一回答以上3个问题（每题回答完后按 Enter，输入 END 结束）：")
    print()

    answers_list = []
    for i in range(3):
        print(f"▶ 回答第{i+1}个问题：")
        ans_lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line.strip().upper() == "END":
                break
            ans_lines.append(line)
        ans = "\n".join(ans_lines).strip()
        answers_list.append(ans if ans else "（未回答）")
        print()

    answers = "\n".join(
        f"{i+1}. {a}" for i, a in enumerate(answers_list)
    )

    print("🧠 AI 正在分析你的复盘，请稍候...")
    print()

    # 5. AI 分析复盘
    try:
        analysis = analyze_review(client, model, user_input, questions, answers)
    except Exception as e:
        print(f"❌ AI调用失败（分析复盘）：{e}")
        return

    print("─" * 50)
    print(analysis)
    print("─" * 50)
    print()

    # 6. 保存复盘结果
    today_str = datetime.now().strftime("%Y-%m-%d")
    try:
        filepath = save_review(today_str, user_input, questions, answers, analysis)
        print(f"✅ 复盘已保存到：{filepath}")
    except Exception as e:
        print(f"⚠️  保存失败：{e}")

    print()
    print("🌟 明天继续加油！每天复盘一点点，成长看得见。")


if __name__ == "__main__":
    main()
