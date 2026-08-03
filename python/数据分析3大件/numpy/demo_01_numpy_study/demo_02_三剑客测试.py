"""
需求：体验numpy，pandas，matplotlib分别如何简单使用

步骤：
1.导包
2.使用numpy创建数组
3.使用pandas创建dataframe
4.使用matplotlib画图
"""

# =============================================================================
# 文件说明：NumPy 生成数据 → Pandas 分析 → Matplotlib 可视化（典型数据分析流水线）
# 别名 as：缩短书写，np/pd/plt 是社区约定俗成的缩写
# =============================================================================

# import ... as ...：导入模块并起别名
import numpy as np          # np：数组运算、随机数
import pandas as pd         # pd：表格读写与统计
import matplotlib.pyplot as plt  # plt：pyplot 子模块，类似 MATLAB 的绘图 API
import matplotlib

# matplotlib.use('TkAgg')：
#   use：切换 Matplotlib 的「后端」（backend），决定图形画在哪个窗口/引擎上
#   'TkAgg'：用 Tk 窗口显示，适合本地桌面运行；避免部分环境默认 Agg 只保存不弹窗
matplotlib.use('TkAgg')

# ---------------------------------------------------------------------------
# TODO 1：NumPy 生成复杂结构数据
# ---------------------------------------------------------------------------
# 需求：3 行 10 列的二维数组（可理解为 3 条样本、每条 10 个特征）
# np.random.randn(3, 10)：
#   random.randn：标准正态分布 N(0,1) 的随机数
#   3, 10：shape 元组，表示 (行数, 列数)
my_array = np.random.randn(3, 10)
print(my_array)

# ---------------------------------------------------------------------------
# TODO 2：Pandas 做描述性统计
# ---------------------------------------------------------------------------
# pd.DataFrame(数据, columns=列名列表)：
#   DataFrame：带行列标签的二维表；底层 values 仍是 ndarray
#   columns：列名，便于按语义访问列
df = pd.DataFrame(my_array, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
# describe()：对数值列输出 count/mean/std/min/max 等，快速了解数据分布
print(df.describe())

# ---------------------------------------------------------------------------
# TODO 3：Matplotlib 可视化
# ---------------------------------------------------------------------------
# df.plot(kind='line')：Pandas 封装，对每列画折线；kind 指定图类型
df.plot(kind='line')
# plt.show()：阻塞并弹出图形窗口，直到关闭窗口
plt.show()
