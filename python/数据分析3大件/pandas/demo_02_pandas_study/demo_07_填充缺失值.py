# =============================================================================
# 第七课：缺失值 NaN 的统计、删除、填充
#
# 【什么是缺失？】
#   空单元格、读不进的字符、刻意留空 → Pandas 统一记为 NaN（Not a Number）
#   NaN ≠ 0，也不等于空字符串；任何与 NaN 的比较结果都是 False
#
# 【清洗数据.csv 特点】
#   有空白、有仅部分列有值 → 用于练习 isnull、dropna、fillna
#
# 【原则】先统计占比 → 再决定删还是填，不要盲目 dropna
# =============================================================================


from pathlib import Path

import pandas as pd
import numpy as np  # NaN 在底层来自 numpy.nan

# 获取当前文件发的父目录
base_dir = Path(__file__).resolve().parent
emp_path = base_dir / '清洗数据.csv'

def show(title, result, principle="", keywords=""):
    print("\n" + "=" * 60)
    print(f"【{title}】")
    if principle:
        print("  ■ 原理/原因:", principle)
    if keywords:
        print("  ■ 关键字:", keywords)
    print("  ■ 结果:")
    print(result)


df = pd.read_csv(emp_path, sep=',')
show("原始表（含缺失）", df,
     principle="逗号分隔；空位读成 NaN",
     keywords="read_csv；sep=','")

# info()：打印每列 Non-Null Count（非空数）、dtype
print("\n" + "=" * 60)
print("【df.info()】")
print("  ■ 看每列 非空个数 / 总行数，判断缺失严重程度")
df.info()

# isnull()：逐格判断是否为 NaN，返回同形状的 True/False 表
# .sum()：对 True 计数（True 当 1），默认按列求和 → 每列缺失个数
show("df.isnull().sum()", df.isnull().sum(),
     principle="True 表示该格缺失；sum 后得到每列缺几个",
     keywords="isnull()→缺失为True；sum()→按列统计")

# len(df)：行数；缺失占比 = 缺失数/行数，用于决定能否删列
show("缺失占比", df.isnull().sum() / len(df),
     principle="占比>50% 的列常考虑整列删除；少量缺失可 fillna",
     keywords="len(df)→行数")

# =============================================================================
# 删除策略
# =============================================================================

# drop：删行或删列；'B' 要删的列名；axis=1 表示沿列方向删（删列）
# axis=0 删行（默认）；原理：返回新表，原 df 不变除非 inplace=True
show("drop('B', axis=1)", df.drop('B', axis=1),
     principle="B 列缺失太多时可直接不要这一列特征",
     keywords="drop(名, axis=1删列)")
print("\n" + "=" * 60)
print(df)

# dropna：删掉含缺失的行（或列）
# how='any'：这一行**只要有一个** NaN 就删
show("dropna(how='any')", df.dropna(how='any'),
     principle="要求「完整案例」时用；会丢很多行要谨慎",
     keywords="dropna；how='any'")

# how='all'：仅当这一行**全部都是** NaN 才删
show("dropna(how='all')", df.dropna(how='all'),
     principle="去掉全空行，保留仍有部分数据的行",
     keywords="how='all'")

# subset=['A']：只根据 A 列是否缺失决定是否删行，其他列 NaN 可保留
show("dropna(subset=['A'])", df.dropna(subset=['A']),
     principle="主键列/核心列不能为空时用 subset",
     keywords="subset=[列名列表]")

# =============================================================================
# 填充策略
# =============================================================================

# fillna：用指定值替换 NaN
# value=df.mean()：用每列均值填（只对数值列有意义，字符列 mean 为 NaN）
show("fillna(value=df.mean())", df.fillna(value=df.mean()),
     principle="数值型常用均值/中位数填；保持样本量不减少",
     keywords="fillna(value=填充值)")

# ffill：forward fill，用**上一个**非空值向下填（时间序列常用）
show("df.ffill()", df.ffill(),
     principle="假设「缺失=沿用最近一次观测」",
     keywords="ffill()=向前填充")

# bfill：backward fill，用**下一个**非空值向上填
show("df.bfill()", df.bfill(),
     principle="末尾缺失只能用后面的值倒填",
     keywords="bfill()=向后填充")

print("\n" + "=" * 60)
print("【小结】isnull查 → dropna删 / fillna填；改的是副本，原表 df 仍在内存里未变")

