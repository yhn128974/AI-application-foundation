"""
Altair：声明式语法（类似 ggplot），基于 Vega-Lite，Jupyter 里交互顺滑。
安装：pip install altair pandas vega_datasets
"""
import json
from pathlib import Path

import altair as alt
import pandas as pd
from vega_datasets import data

# 启用最大行数（默认 5000 行限制，大数据集需调大）
alt.data_transformers.disable_max_rows()

ASSETS = Path(__file__).resolve().parent / "assets"
WORLD_TOPO = ASSETS / "world-110m.json"

# ISO 3166-1 numeric → 汽车数据集 Origin 字段（Europe 含主要产车国）
ORIGIN_COUNTRY_IDS = pd.DataFrame(
    {
        "id": [840, 392, 276, 250, 380, 826, 752, 724, 616, 528],
        "Origin": [
            "USA",
            "Japan",
            "Europe",
            "Europe",
            "Europe",
            "Europe",
            "Europe",
            "Europe",
            "Europe",
            "Europe",
        ],
    }
)

cars = data.cars()
df = pd.DataFrame(cars)[["Horsepower", "Miles_per_Gallon", "Origin", "Year", "Cylinders"]].dropna()
# vega_datasets 新版 cars 里 Year 为 datetime64，需取年份而非 astype(int)
if pd.api.types.is_datetime64_any_dtype(df["Year"]):
    df["Year"] = df["Year"].dt.year
else:
    df["Year"] = df["Year"].astype(int)


def _load_world_topo() -> dict:
    if not WORLD_TOPO.exists():
        raise FileNotFoundError(
            f"缺少 {WORLD_TOPO.name}，请先运行：python 09_下载altair地图资源.py"
        )
    return json.loads(WORLD_TOPO.read_text(encoding="utf-8"))


world_map = (
    alt.Chart({"values": _load_world_topo(), "format": {"type": "topojson", "feature": "countries"}})
    .mark_geoshape(stroke="white")
    .encode(
        color=alt.condition(
            alt.datum.Origin,
            alt.Color("Origin:N", legend=alt.Legend(title="产地")),
            alt.value("#e8e8e8"),
        ),
        tooltip=[alt.Tooltip("id:Q", title="国家代码")],
    )
    .transform_lookup(
        lookup="id",
        from_=alt.LookupData(ORIGIN_COUNTRY_IDS, "id", ["Origin"]),
    )
    .properties(width=700, height=280, title="汽车产地分布（世界地图）")
)

scatter = (
    alt.Chart(df)
    .mark_circle(size=70, opacity=0.75)
    .encode(
        x=alt.X("Horsepower:Q", title="马力"),
        y=alt.Y("Miles_per_Gallon:Q", title="油耗 MPG"),
        color=alt.Color("Origin:N", legend=alt.Legend(title="产地")),
        size=alt.Size("Cylinders:Q", scale=alt.Scale(range=[30, 400]), legend=alt.Legend(title="缸数")),
        tooltip=["Origin", "Year", "Horsepower", "Miles_per_Gallon", "Cylinders"],
    )
    .properties(width=700, height=420, title="Altair 交互散点（框选缩放、悬停提示）")
    .interactive()
    .facet(column=alt.Column("Origin:N", title=None))
    .resolve_scale(color="independent")
)

chart = alt.vconcat(world_map, scatter).resolve_scale(color="shared")

# 保存为可嵌入网页的 HTML（地图 topojson 内嵌，无需外网加载）
out = "altair_cars_faceted.html"
chart.save(out)
print(f"已生成: {out}，请用浏览器打开查看。")
# display() 仅在 Jupyter / 部分 IDE 交互窗口有效；命令行运行用 HTML 即可
try:
    chart.display()
except Exception:
    pass
