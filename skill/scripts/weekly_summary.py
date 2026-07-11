"""
AI每日复盘教练 - 周度汇总程序
用法：python weekly_summary.py
"""

import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from review_core import (
    load_config,
    create_client,
    generate_weekly_summary,
    load_week_reviews,
    save_review,
)


def main():
    print("=" * 50)
    print("  📊 AI 复盘周度汇总")
    print("=" * 50)
    print()

    # 1. 加载配置
    try:
        config = load_config()
        client = create_client(config)
        model = config["api"]["model"]
    except Exception as e:
        print(f"❌ 配置加载失败：{e}")
        return

    # 2. 确定本周日期范围
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    week_str = f"{monday.strftime('%Y-%m-%d')} ~ {sunday.strftime('%Y-%m-%d')}"

    print(f"📅 汇总周期：{week_str}")
    print()

    # 3. 加载本周复盘
    reviews_text = load_week_reviews()
    if not reviews_text.strip():
        print("⚠️  本周还没有复盘记录。")
        print("   请先运行 daily_review.py 创建每日复盘。")
        return

    # 4. 生成周度汇总
    print("🧠 AI 正在分析本周复盘...")
    print()

    try:
        summary = generate_weekly_summary(client, model, reviews_text)
    except Exception as e:
        print(f"❌ AI调用失败：{e}")
        return

    print("─" * 50)
    print(summary)
    print("─" * 50)
    print()

    # 5. 保存周度汇总
    week_filename = f"{monday.strftime('%Y%m%d')}_周度汇总"
    week_content = f"本周复盘记录\n\n{reviews_text}"
    try:
        filepath = save_review(
            week_filename, week_str, "", "", summary, output_dir="reviews"
        )
        print(f"✅ 周度汇总已保存到：{filepath}")
    except Exception as e:
        print(f"⚠️  保存失败：{e}")

    print()


if __name__ == "__main__":
    main()
