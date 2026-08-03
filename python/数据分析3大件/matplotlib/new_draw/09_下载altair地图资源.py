"""
下载 Altair 世界地图所需的 topojson 到 assets/，无外网时地图才能显示。
只需运行一次：python 09_下载altair地图资源.py
然后重新运行 04_altair_交互分面散点.py
"""
from __future__ import annotations

import urllib.request
from pathlib import Path

URL = "https://cdn.jsdelivr.net/npm/vega-datasets@1/data/world-110m.json"
OUT = Path(__file__).resolve().parent / "assets" / "world-110m.json"


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    print(f"下载 {URL} ...")
    OUT.write_bytes(urllib.request.urlopen(URL, timeout=30).read())
    print(f"  -> {OUT} ({OUT.stat().st_size} bytes)")
    print("完成。请重新运行 04_altair_交互分面散点.py")


if __name__ == "__main__":
    main()
