"""
pyecharts 快速上手精选（https://pyecharts.org/#/zh-cn/quickstart ）

PyCharm 展示（推荐）：
  右键本文件 → Run
  → 生成 pyecharts_pycharm_tab.html 并打开（Tab 切换 4 图）
  → 或在项目树双击 HTML → 编辑器右上角「在浏览器中打开」→ PyCharm 内预览

单张图：
  python 07_pyecharts_PyCharm快速展示.py bar
  python 07_pyecharts_PyCharm快速展示.py liquid

PyCharm Run Cell（# %% 单元格，光标在单元格内 → Run Cell）：
  在 Console 内嵌显示当前图（需本文件已至少 Run 过一次以加载函数）
"""
from __future__ import annotations

import argparse
import webbrowser
from pathlib import Path

from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Liquid, Pie, Tab
from pyecharts.commons.utils import JsCode
from pyecharts.globals import CurrentConfig, ThemeType

OUT_DIR = Path(__file__).resolve().parent
ASSETS_DIR = OUT_DIR / "assets"
TAB_HTML = OUT_DIR / "pyecharts_pycharm_tab.html"


def configure_assets() -> None:
    """
    图表依赖 ECharts JS。勿使用 v5 CDN（官方已 500，页面会一片空白）。
    优先本地 assets/（运行 08_下载pyecharts离线资源.py 生成）；否则用 pyecharts 2.x 默认 v6 在线地址。
    """
    if (ASSETS_DIR / "echarts.min.js").is_file():
        # 相对路径，HTML 与 assets 同目录结构，file:// 打开也有效
        CurrentConfig.ONLINE_HOST = "assets/"
        print(f"使用本地资源: {ASSETS_DIR}")
    else:
        # 默认 https://assets.pyecharts.org/assets/v6/
        print(f"使用在线 CDN: {CurrentConfig.ONLINE_HOST}")
        print("若无外网导致空白，请先运行: 08_下载pyecharts离线资源.py")


configure_assets()


def show_chart(chart, html_name: str) -> None:
    """IPython Console 内嵌；否则写 HTML 并打开浏览器。"""
    try:
        from IPython import get_ipython
        from IPython.display import HTML, display

        if get_ipython() is not None:
            display(HTML(chart.render_embed()))
            return
    except Exception:
        pass

    path = OUT_DIR / html_name
    chart.render(str(path))
    webbrowser.open(path.as_uri())
    print(f"已打开: {path}")


def chart_bar() -> Bar:
    return (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="900px", height="420px"))
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="【实用】柱状图", subtitle="快速入门 · 分类对比"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
        )
    )


def chart_line() -> Line:
    months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
    return (
        Line(init_opts=opts.InitOpts(theme=ThemeType.MACARONS, width="900px", height="420px"))
        .add_xaxis(months)
        .add_yaxis("销售额", [120, 132, 101, 134, 90, 230, 210, 182, 191, 234, 290, 330], is_smooth=True)
        .add_yaxis("利润", [60, 72, 51, 74, 40, 110, 100, 82, 91, 124, 150, 170], is_smooth=True)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="【实用】折线图", subtitle="趋势 · 可缩放"),
            datazoom_opts=[opts.DataZoomOpts(type_="inside"), opts.DataZoomOpts(type_="slider")],
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
        )
    )


def chart_liquid() -> Liquid:
    return (
        Liquid(init_opts=opts.InitOpts(theme=ThemeType.DARK, width="900px", height="420px"))
        .add(
            "本周学习完成度",
            [0.76],
            is_outline_show=False,
            color=["#294D99", "#156ACF", "#1598ED", "#45BDFF"],
            label_opts=opts.LabelOpts(
                font_size=36,
                color="#fff",
                formatter=JsCode("function(p){return Math.round(p.value*100)+'%';}"),
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="【炫酷】水球图"))
    )


def chart_rose_pie() -> Pie:
    data = [("Python", 48), ("Java", 22), ("Go", 12), ("前端", 10), ("其他", 8)]
    return (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width="900px", height="420px"))
        .add("", data, radius=["20%", "70%"], rosetype="area",
             label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="【炫酷】玫瑰饼图"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="15%"),
        )
    )


CHARTS = {
    "bar": (chart_bar, "_tmp_bar.html"),
    "line": (chart_line, "_tmp_line.html"),
    "liquid": (chart_liquid, "_tmp_liquid.html"),
    "rose": (chart_rose_pie, "_tmp_rose.html"),
}


def main_tab() -> None:
    tab = Tab(page_title="pyecharts · PyCharm 展示")
    tab.add(chart_bar(), "实用-柱状图")
    tab.add(chart_line(), "实用-折线图")
    tab.add(chart_liquid(), "炫酷-水球图")
    tab.add(chart_rose_pie(), "炫酷-玫瑰饼图")
    tab.render(str(TAB_HTML))
    webbrowser.open(TAB_HTML.as_uri())
    print("=" * 60)
    print("Tab 页已打开，点击顶部标签切换 4 张图")
    print(f"HTML: {TAB_HTML}")
    print("请用 Chrome/Edge 打开 HTML（需加载 JS）；PyCharm 纯文本预览看不到图")
    print("=" * 60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("chart", nargs="?", choices=CHARTS.keys())
    args = parser.parse_args()
    if args.chart:
        factory, html = CHARTS[args.chart]
        show_chart(factory(), html)
    else:
        main_tab()
    raise SystemExit(0)


# ----- 以下 # %% 仅供 PyCharm「Run Cell」，整文件 Run 不会执行 -----
# %% 【实用】柱状图
show_chart(chart_bar(), "_tmp_bar.html")

# %% 【实用】折线图
show_chart(chart_line(), "_tmp_line.html")

# %% 【炫酷】水球图
show_chart(chart_liquid(), "_tmp_liquid.html")

# %% 【炫酷】玫瑰饼图
show_chart(chart_rose_pie(), "_tmp_rose.html")
