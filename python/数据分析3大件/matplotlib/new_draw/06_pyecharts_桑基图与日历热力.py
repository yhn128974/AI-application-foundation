"""
桑基图 + 日历热力图：适合讲「用户转化路径」「活跃度/贡献度」。
安装：pip install pyecharts
"""
import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar, Page, Sankey
from pyecharts.globals import ThemeType

# ========== 1. 桑基图（电商转化漏斗流量）==========
# 节点名全局唯一；value 表示流量大小，线条越粗越多
nodes = [{"name": n} for n in [
    "广告曝光", "落地页", "商品列表", "商品详情", "加入购物车", "提交订单", "支付成功", "流失"
]]
links = [
    {"source": "广告曝光", "target": "落地页", "value": 10000},
    {"source": "落地页", "target": "商品列表", "value": 6200},
    {"source": "落地页", "target": "流失", "value": 3800},
    {"source": "商品列表", "target": "商品详情", "value": 4100},
    {"source": "商品列表", "target": "流失", "value": 2100},
    {"source": "商品详情", "target": "加入购物车", "value": 1800},
    {"source": "商品详情", "target": "流失", "value": 2300},
    {"source": "加入购物车", "target": "提交订单", "value": 900},
    {"source": "加入购物车", "target": "流失", "value": 900},
    {"source": "提交订单", "target": "支付成功", "value": 650},
    {"source": "提交订单", "target": "流失", "value": 250},
]

sankey = (
    Sankey(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="1000px", height="520px"))
    .add(
        "转化",
        nodes,
        links,
        linestyle_opt=opts.LineStyleOpts(opacity=0.35, curve=0.5, color="source"),
        label_opts=opts.LabelOpts(font_size=12),
        node_gap=12,
        node_width=22,
        levels=[
            opts.SankeyLevelsOpts(depth=0, itemstyle_opts=opts.ItemStyleOpts(color="#4992ff")),
            opts.SankeyLevelsOpts(depth=1, itemstyle_opts=opts.ItemStyleOpts(color="#7cffb2")),
            opts.SankeyLevelsOpts(depth=2, itemstyle_opts=opts.ItemStyleOpts(color="#fddd60")),
            opts.SankeyLevelsOpts(depth=3, itemstyle_opts=opts.ItemStyleOpts(color="#ff6e76")),
        ],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="用户转化桑基图（流量粗细 = 人数）",
            subtitle="可拖动节点；悬停高亮上下游",
        ),
    )
)

# ========== 2. 日历热力图（类似 GitHub 贡献图）==========
random.seed(2026)
begin = datetime.date(2025, 1, 1)
end = datetime.date(2025, 12, 31)
days = (end - begin).days + 1
cal_data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(0, 120)]
    for i in range(days)
]

calendar = (
    Calendar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="1000px", height="260px"))
    .add(
        "每日刷题数",
        cal_data,
        calendar_opts=opts.CalendarOpts(
            range_="2025",
            daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),
            monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),
        ),
        visualmap_opts=opts.VisualMapOpts(
            max_=120,
            orient="horizontal",
            pos_left="center",
            pos_bottom="0%",
            range_color=["#1a1a2e", "#16213e", "#0f3460", "#e94560"],
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2025 学习打卡日历热力图", pos_left="center"),
    )
)

page = Page(layout=Page.SimplePageLayout, page_title="桑基图与日历热力")
page.add(sankey, calendar)
out = "pyecharts_sankey_calendar.html"
page.render(out)
print(f"已生成: {out}，请用浏览器打开查看。")
