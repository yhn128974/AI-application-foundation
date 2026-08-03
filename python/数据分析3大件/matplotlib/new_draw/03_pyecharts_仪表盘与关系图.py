"""
pyecharts = Apache ECharts 的 Python 封装（你说的很可能是 ECharts，不是 Eclipse IDE）。
擅长：仪表盘、水球图、桑基图、地图、日历热力等「炫酷」业务大屏风格。
安装：pip install pyecharts
运行会生成 HTML 文件并用默认浏览器打开。
"""
from pyecharts import options as opts
from pyecharts.charts import Gauge, Graph, Page
from pyecharts.globals import ThemeType

# --- 1. 霓虹风仪表盘 ---
gauge = (
    Gauge(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="900px", height="500px"))
    .add(
        "完成率",
        [("项目进度", 78.5)],
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")],
                width=25,
            )
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="ECharts 仪表盘（暗色主题）"),
        legend_opts=opts.LegendOpts(is_show=False),
    )
)

# --- 2. 力导向关系图（节点会「飘」）---
nodes = [
    {"name": "Python", "symbolSize": 55},
    {"name": "Plotly", "symbolSize": 40},
    {"name": "ECharts", "symbolSize": 45},
    {"name": "Altair", "symbolSize": 35},
    {"name": "Matplotlib", "symbolSize": 50},
]
links = [
    {"source": "Python", "target": "Plotly"},
    {"source": "Python", "target": "ECharts"},
    {"source": "Python", "target": "Altair"},
    {"source": "Python", "target": "Matplotlib"},
    {"source": "ECharts", "target": "Plotly"},
]
graph = (
    Graph(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width="900px", height="500px"))
    .add(
        "",
        nodes,
        links,
        repulsion=4200,
        linestyle_opts=opts.LineStyleOpts(curve=0.3, color="source"),
        label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="可视化库关系图（力导向）"))
)

page = Page(layout=Page.SimplePageLayout)
page.add(gauge, graph)
out = "pyecharts_demo.html"
page.render(out)
print(f"已生成: {out}，请用浏览器打开查看。")
