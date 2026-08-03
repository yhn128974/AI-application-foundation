"""
Plotly Express：少量代码做动画、渐变面积图。
安装：pip install plotly pandas
"""
import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.templates.default = "seaborn"

# 模拟多城市月度销量
months = pd.date_range("2024-01", periods=12, freq="ME")
cities = ["北京", "上海", "深圳", "杭州"]
rows = []
base = {"北京": 120, "上海": 100, "深圳": 90, "杭州": 70}
for i, m in enumerate(months):
    for c in cities:
        rows.append(
            {
                "month": m,
                "city": c,
                "sales": base[c] + i * 8 + (hash(c) % 17),
                "frame": m.strftime("%Y-%m"),
            }
        )
df = pd.DataFrame(rows)

# 动画柱状图（播放条可拖动月份）
fig_bar = px.bar(
    df,
    x="city",
    y="sales",
    color="city",
    animation_frame="frame",
    range_y=[0, df["sales"].max() * 1.15],
    title="各城市月销量（动画）",
    text_auto=".0f",
)
fig_bar.update_layout(showlegend=False, transition={"duration": 400})
fig_bar.show()

# 渐变面积图（多系列堆叠 + 半透明）
fig_area = px.area(
    df,
    x="month",
    y="sales",
    color="city",
    line_group="city",
    title="累计销量趋势（渐变面积）",
)
fig_area.update_traces(line=dict(width=0.5))
fig_area.show()
