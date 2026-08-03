"""
Plotly：交互式、默认样式现代，适合课堂演示 / Streamlit / Dash。
安装：pip install plotly pandas numpy
运行后会在浏览器打开 HTML（或 Jupyter 内嵌显示）。
"""
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.io as pio

# 暗色模板，比默认 matplotlib 观感新很多
pio.templates.default = "plotly_dark"

rng = np.random.default_rng(42)
n = 800
df = pd.DataFrame(
    {
        "x": rng.normal(0, 1, n),
        "y": rng.normal(0, 1, n),
        "z": rng.normal(0, 1, n),
        "score": rng.uniform(0, 100, n),
        "group": rng.choice(["A", "B", "C"], n),
    }
)

fig = px.scatter_3d(
    df,
    x="x",
    y="y",
    z="z",
    color="score",
    symbol="group",
    size="score",
    size_max=18,
    opacity=0.85,
    color_continuous_scale="Turbo",
    title="Plotly 3D 散点（悬停 / 旋转 / 缩放）",
    labels={"score": "得分"},
)
fig.update_layout(
    paper_bgcolor="#0e1117",
    scene=dict(
        xaxis=dict(backgroundcolor="#0e1117", gridcolor="#333"),
        yaxis=dict(backgroundcolor="#0e1117", gridcolor="#333"),
        zaxis=dict(backgroundcolor="#0e1117", gridcolor="#333"),
    ),
    margin=dict(l=0, r=0, t=50, b=0),
)
fig.show()
# 也可导出独立网页：fig.write_html("plotly_3d.html", include_plotlyjs="cdn")
