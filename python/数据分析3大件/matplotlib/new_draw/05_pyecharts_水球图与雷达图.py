"""
水球图 + 雷达图：大屏里最常见的「炫酷」组合之一。
- 水球图：百分比、完成率、饱和度
- 雷达图：多维度能力/指标对比
安装：pip install pyecharts
"""
from pyecharts import options as opts
from pyecharts.charts import Liquid, Page, Radar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

# ========== 1. 水球图（三种形状，霓虹渐变）==========
liquid_circle = (
    Liquid(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="420px", height="380px"))
    .add(
        "Python 掌握度",
        [0.72],
        is_outline_show=False,
        color=["#2af598", "#009efd"],
        label_opts=opts.LabelOpts(
            font_size=28,
            formatter=JsCode("function(p){return Math.round(p.value*100)+'%';}"),
            color="#fff",
            position="inside",
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="圆形水球", pos_left="center"))
)

liquid_pin = (
    Liquid(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="420px", height="380px"))
    .add(
        "项目交付",
        [0.58],
        shape="pin",
        color=["#f83600", "#f9d423"],
        label_opts=opts.LabelOpts(
            font_size=26,
            formatter=JsCode("function(p){return Math.round(p.value*100)+'%';}"),
            color="#fff",
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="水滴形", pos_left="center"))
)

liquid_rect = (
    Liquid(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="420px", height="380px"))
    .add(
        "作业完成",
        [0.91],
        shape="rect",
        color=["#7117ea", "#ea6060"],
        label_opts=opts.LabelOpts(
            font_size=26,
            formatter=JsCode("function(p){return Math.round(p.value*100)+'%';}"),
            color="#fff",
        ),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="矩形", pos_left="center"))
)

# ========== 2. 雷达图（两名学员 vs 班级均值）==========
schema = [
    opts.RadarIndicatorItem(name="Python 语法", max_=100),
    opts.RadarIndicatorItem(name="正则/文本", max_=100),
    opts.RadarIndicatorItem(name="Pandas", max_=100),
    opts.RadarIndicatorItem(name="可视化", max_=100),
    opts.RadarIndicatorItem(name="工程化", max_=100),
]

radar = (
    Radar(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="900px", height="480px"))
    .add_schema(schema, shape="polygon")
    .add("班级均值", [[72, 65, 70, 58, 62]], color="#5470c6", areastyle_opts=opts.AreaStyleOpts(opacity=0.15))
    .add("学员 A", [[88, 82, 75, 90, 70]], color="#91cc75", areastyle_opts=opts.AreaStyleOpts(opacity=0.25))
    .add("学员 B", [[60, 78, 85, 55, 80]], color="#fac858", areastyle_opts=opts.AreaStyleOpts(opacity=0.25))
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="就业班能力雷达对比"),
        legend_opts=opts.LegendOpts(pos_bottom="2%"),
    )
)

page = Page(layout=Page.SimplePageLayout, page_title="水球图与雷达图")
page.add(liquid_circle, liquid_pin, liquid_rect, radar)
out = "pyecharts_liquid_radar.html"
page.render(out)
print(f"已生成: {out}，请用浏览器打开查看。")
