# =============================================================================
# 第三课【重点】：从文件读入 DataFrame + 快速探查 + 布尔筛选
#
# 【运行注意】
#   路径 'students.txt' 是相对路径 → 相对「当前工作目录」而不是 .py 文件位置。
#   请在 03_pandas 文件夹下运行，或在 IDE 把工作目录设到该文件夹。
#
# 【students.txt 格式】
#   逗号分隔，无表头行：姓名,年龄,性别,分数
# =============================================================================

import pandas as pd
from pathlib import Path


def show(title, result, principle="", keywords=""):
    print("\n" + "=" * 60)
    print(f"【{title}】")
    if principle:
        print("  ■ 原理/原因:", principle)
    if keywords:
        print("  ■ 关键字:", keywords)
    print("  ■ 结果:")
    print(result)

base_dir = Path(__file__).resolve().parent
students_path = base_dir / 'students.txt'
# =============================================================================
# pd.read_csv：把磁盘上的分隔文本读成 DataFrame（最常用的读表方式）
# =============================================================================

# 第一个参数：文件路径字符串
# sep=','：separator 分隔符，字段之间用逗号切开（CSV = Comma Separated Values）
# names=[...]：该文件没有表头行时，手动指定 4 个列名；有表头时一般用 header=0 读第一行

# 
df = pd.read_csv(
    students_path,
    sep=',',
    names=['name', 'age', 'sex', 'score']
)

# df.to_csv('students.csv', index=False)

show(
    "read_csv('students.txt', sep=',', names=[...])",
    df,
    principle="读入后每列自动推断类型；空字段会变成 NaN（见最后一行）",
    keywords="sep→分隔符；names→无表头时列名"
)
print("  ■ type(df):", type(df))

# -------------------------------------------------------------------------
# 探查「这张表有多大、什么类型」—— 分析前必做
# -------------------------------------------------------------------------
print("\n" + "=" * 60)
print("【结构属性一览】")
print("  ndim :", df.ndim, "  ← 表是二维")
print("  shape:", df.shape, "  ← (行数, 列数)")
print("  size :", df.size, "  ← 总单元格数")
print("  columns:", df.columns, "  ← Index 类型，所有列名")
print("  index :", df.index, "  ← 默认 RangeIndex 0,1,2... 未手动指定行名")
print("  dtypes:\n", df.dtypes,
      "\n  ■ score 列读入后常为 float64（因有缺失时无法保持纯 int）")

show("df.values 底层二维数组", df.values,
     principle="带标签的表 ↔ 纯数字矩阵 的桥梁",
     keywords=".values")

# head(n)：看前 n 行，默认 n=5；快速确认读对没有、分隔符对不对
show("df.head(2)", df.head(2),
     principle="只预览头部，不打印整张表，大文件也安全",
     keywords="head(行数)")

# tail(n)：看后 n 行；常用来发现文件末尾的脏数据、空行
show("df.tail(2)", df.tail(2),
     principle="最后一行若有空姓名，说明要清洗",
     keywords="tail(行数)")

# describe()：只对「数值列」做 count/mean/std/min/max 等
show("df.describe()", df.describe(),
     principle="快速看分数分布、是否有异常极值；字符列不会出现",
     keywords="describe()→描述性统计")

# info()：打印每列非空个数、dtype、内存；无 return，直接输出到控制台
print("\n" + "=" * 60)
print("【df.info()】← 看每列有多少非空、有无 object/float 混用")
df.info()

# =============================================================================
# 按列取值：方括号 [] 是 Pandas 最常用的访问语法
# =============================================================================

# df['name']：单层字符串 → 取一列 → 得到 Series（带 index 的一列）
show("df['name'] 单列", df['name'],
     principle="一列 = 一个 Series，行标签与 df 相同",
     keywords="df['列名'] → Series")
print("  ■ type:", type(df['name']))

# df[['name','score']]：双层括号，内层是 list → 取多列 → 仍是 DataFrame
# 原理：传列表表示「要选多列」，返回子表
show("df[['name','score']] 多列", df[['name', 'score']],
     principle="双层 [] 易错：单层选列，双层选多列",
     keywords="df[[列名列表]] → DataFrame")

# =============================================================================
# 布尔索引：用 True/False 「筛行」（Pandas 最核心的筛选方式之一）
# =============================================================================

# df['score']：先取出分数这一列（Series）
# == 98：逐元素比较，等于 98 的位置 True，否则 False
# 原理：对齐 index 后生成等长的布尔 Series
b = df['score'] == 98

show("布尔序列 b = (df['score']==98)", b,
     principle="True 的行会被保留；False 的行隐藏（不是删除原表）",
     keywords="== → 逐元素比较；得到 bool Series")

# df[b]：只把 b 里为 True 的 index 对应的行取出来
show("df[b] 筛选 score==98 的学生", df[b],
     principle="外层 df[内层布尔] 是固定搭配；内层长度必须等于行数",
     keywords="df[布尔Series] → 子 DataFrame")


# =============================================================================
# 保存处理后的数据到CSV文件
# =============================================================================

# 示例1：保存原始读取的DataFrame到CSV文件
# to_csv()：将DataFrame写入CSV文件
# 'students_original.csv'：要保存的文件路径（相对路径）
# index=False：不写入行索引（避免多出一列无意义的索引号）
df.to_csv('students_original.csv', index=False)
print("\n" + "=" * 60)
print("【文件保存】")
print("  ✓ 已保存原始数据到: students_original.csv")
print("  ■ 参数说明: index=False → 不保存行索引")

# 示例2：保存筛选后的数据（分数为98的学生）
df_filtered = df[df['score'] == 98]  # 先筛选出需要的数据
df_filtered.to_csv('students_score_98.csv', index=False, encoding='utf-8-sig')
# 
print("  ✓ 已保存分数为98的学生到: students_score_98.csv")
print("  ■ 参数说明: encoding='utf-8-sig' → 解决Excel打开中文乱码问题")

# 示例3：保存时自定义列顺序和选择特定列
# columns=['name', 'score', 'age', 'sex']：指定列的输出顺序
df.to_csv('students_selected_columns.csv',
          index=False,
          columns=['name', 'score', 'age', 'sex'],
          encoding='utf-8-sig')
print("  ✓ 已保存自定义列顺序的数据到: students_selected_columns.csv")

show("保存示例 - 使用技巧总结",
     "to_csv()常用参数:\n"
     "  • index=False      → 不保存行索引\n"
     "  • encoding='编码'   → 常用'utf-8-sig'解决Excel中文乱码\n"
     "  • columns=[列名列表] → 只保存指定的列并按此顺序\n"
     "  • sep='分隔符'      → 默认逗号，可改为'\\t'制表符等",
     principle="保存前建议先筛选/清洗/聚合，再存储为新的CSV",
     keywords="df.to_csv()")
