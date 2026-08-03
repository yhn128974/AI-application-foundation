"""
需求：使用不同的命令查看不同状态不同类型的dataframe
选择数据，查看选择数据的内容和类型

步骤：
1.导包
2. 创建dataframe
3.查看
4.选择
"""

# 1.导包
import pandas as pd  # 导入pandas库，并简称为pd，pandas是Python数据分析核心库

# 2. 创建dataframe

data = {
    '姓名': ['张三', '李四', '王五', '赵六'],  # 列名：姓名，对应的数据列表
    '年龄': [25, 30, 35, 28],               # 列名：年龄
    '城市': ['北京', '上海', '广州', '深圳'], # 列名：城市
    '工资': [5000, 7000, 6000, 8000]        # 列名：工资
}

# pd.DataFrame()：将字典转换为表格形式的数据结构
# index=["s1","s2","s3","s4"]：为每一行指定自定义索引标签（行名）
df = pd.DataFrame(data, index=["s1","s2","s3","s4"])

print(df)  # 打印整个DataFrame

# 3.查看

# df.head(3)：查看前3行数据（默认是5行），用于快速预览数据头部
print(df.head(3))
# df.tail(2)：查看最后2行数据（默认是5行），用于预览数据尾部
print(df.tail(2))
# df.describe()：仅对数值型列统计计数、均值、标准差、四分位数等
print(df.describe())
# df.info()：查看DataFrame的摘要信息，包括索引类型、列名、非空值数量、内存占用
print(df.info())

print(df.dtypes)

# 4.选择

# 选择单列：df['列名'] 返回一个Series（一维带标签数组）
print(df['姓名'])
print("姓名列的类型为：", type(df['姓名']))  # <class 'pandas.core.series.Series'>

# 选择多列：df[['列名1','列名2']] 返回DataFrame，注意双层方括号
print(df[['姓名','年龄']])
print("姓名加年龄列的类型为：", type(df[['姓名','年龄']]))  # <class 'pandas.core.frame.DataFrame'>

# ---------- 从行来选择 ----------

# 使用 .loc[] —— 基于索引标签（行名/列名）进行选择，包含结束位置（左闭右闭）

# 选择特定行和列：df.loc[行标签列表, 列标签列表]
print(df.loc[['s2'], ["年龄"]])  # 选择行's2'、列'年龄'，结果仍是DataFrame

# 选择多行所有列：df.loc[行标签列表]（省略列名则返回所有列）
print(df.loc[['s1','s3']])      # 选择行's1'和's3'，所有列

# 切片：'s1':'s3' 包含's1','s2','s3'（左闭右闭）
print(df.loc['s1':'s3'])

# 使用 .iloc[] —— 基于整数位置索引（从0开始）进行选择，不包含结束位置（左闭右开）

# 选择单行：df.iloc[行位置] 返回Series
print(df.iloc[0])  # 选择第0行（即's1'对应的行）

# 选择多行：df.iloc[[行位置1, 行位置2]]
print(df.iloc[[0,2]])  # 选择第0行和第2行

# 切片：0:3 表示选择行0、1、2（不包含索引3）
print(df.iloc[0:3])