# =============================================================================
# 第五课：选列、条件筛选、排序
#
# 【业务场景】
#   从员工表里：只看姓名和工资 → 找出高薪技术部 → 按工资排序发工资条
#
# 【emp.txt】短横线 - 分隔，第一行是表头 name-age-dept-sal
# =============================================================================

import os

import pandas as pd


def show(title, result, principle="", keywords=""):
    print("\n" + "=" * 60)
    print(f"【{title}】")
    if principle:
        print("  ■ 原理/原因:", principle)
    if keywords:
        print("  ■ 关键字:", keywords)
    print("  ■ 结果:")
    print(result)

# sep='-'：字段用短横线分隔（不是逗号 CSV）
# 第一行 name-age-dept-sal 会被当作列名（默认 header=0）
base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, 'emp.txt')
# 
     
df = pd.read_csv(path, sep='-')
show("读入 emp 表", df,
     principle="分隔符必须与文件一致，否则整行会挤在一列",
     keywords="read_csv；sep='-'")

# =============================================================================
# 1. 基础列查询
# =============================================================================

# [['name','sal']]：外层 [] 是 Pandas 取子集；内层 [] 是 Python 列表
# 原理：告诉 Pandas「我要这两列」，返回仍是 DataFrame（二维）
show("df[['name','sal']]", df[['name', 'sal','dept']],
     principle="先选列再分析，减少无关字段干扰",
     keywords="双括号 + 列名列表")

# =============================================================================
# 2. 条件查询（布尔索引）
# =============================================================================

# df['sal'] > 5000：生成与行数相同的 True/False
# df[ ... ]：只保留 True 的行
show("df[df['sal'] > 5000]", df[df['sal']>5000],
     principle="内层条件、外层筛行；等价 SQL: WHERE sal > 5000",
     keywords="df[df['列'] 比较符 值]")

# == 字符串全等；区分大小写
show("df[df['dept']=='技术部']", df[df['dept'] == '技术部'],
     principle="字符列用 == 不要用 is（is 比较对象身份）",
     keywords="== 字符串比较")

# 多条件：& 且，| 或，~ 非；每个条件必须加括号
# 原因：& 是位运算/逐元素与，优先级高于比较符，不加括号会报错或结果错
# 不能用 and：and 只接受单个 True/False，不能接受整列 Series
show("高薪 且 技术部", df[(df['sal'] > 5000) & (df['dept'] == '技术部')],
     principle="多条件布尔 Series 用 & | ~，并加括号",
     keywords="& 且；| 或；每个条件 ( )")

# query：把条件写成字符串，列名当变量，更接近 SQL 可读性
# 字符串里 dept 比较要用双引号包部门名，外层用单引号包字符串
show("df.query(...)", df.query('sal>5000 and dept=="技术部"'),
     principle="复杂条件可读性好；内部仍转成布尔筛选",
     keywords="query('条件字符串')；and；列名直接写")

# =============================================================================
# 3. sort_values 排序
# =============================================================================

# by='sal'：按哪一列排；ascending=False：降序（大到小）
# 原理：返回新表排序结果，默认不修改原 df（除非 inplace=True）
show("sort_values 降序", df.sort_values('sal', ascending=False),
     principle="工资条、排行榜常用降序",
     keywords="sort_values(by列, ascending=False降序)")

show("sort_values 升序", df.sort_values('age', ascending=True),
     principle="ascending=True 从小到大",
     keywords="ascending=True升序")

# 
show("sort_values 多列排序", df.sort_values(['age', 'sal'], ascending=[True, False]),
     principle="先按年龄升序，再按工资降序",   keywords="by=[列名列表], ascending=[True/False列表]")

     
