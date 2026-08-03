"""
下载 pyecharts 所需的 ECharts 静态资源到 assets/，无外网时图表才能显示。
只需运行一次：python 08_下载pyecharts离线资源.py
然后重新运行 07_pyecharts_PyCharm快速展示.py
"""
from __future__ import annotations

import urllib.request
from pathlib import Path

BASE = "https://assets.pyecharts.org/assets/v6/"
FILES = [
    "echarts.min.js",
    "echarts-liquidfill.min.js",
    "themes/macarons.js",
    "themes/chalk.js",
    "themes/light.js",
    "themes/dark.js",
]

OUT = Path(__file__).resolve().parent / "assets"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        url = BASE + name
        dest = OUT / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        print(f"下载 {url} ...")
        urllib.request.urlretrieve(url, dest)
        print(f"  -> {dest} ({dest.stat().st_size} bytes)")
    print("完成。请重新运行 07_pyecharts_PyCharm快速展示.py")


if __name__ == "__main__":
    main()
