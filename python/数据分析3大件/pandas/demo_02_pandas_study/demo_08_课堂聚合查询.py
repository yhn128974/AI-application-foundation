import pandas as pd  # 导入Pandas库，用于数据分析和处理

# ==================== 数据读取 ====================
# pd.read_csv()：从CSV文件读取数据并返回DataFrame对象
# "sales_data.csv"：文件路径，假设包含'产品'、'地区'、'销售额'等列
df = pd.read_csv("sales_data.csv")

# print()：在控制台输出内容
# df：DataFrame对象，展示表格数据（行索引、列名、数据值）
print(df)

# ==================== 分组聚合（groupby）====================
print("\n按产品分组计算总销售额:")

# df.groupby('产品')：按'产品'列的值进行分组，相同产品的行归为一组
# ['销售额']：选择要操作的目标列（只对销售额列进行计算）
# .sum()：对每组内的销售额求和，返回Series（索引=产品名，值=总销售额）
print(df.groupby('产品')['销售额'].sum())

print("\n按产品和地区分组计算统计量:")

# df.groupby(['产品', '地区'])：按两个列同时分组，形成多级索引
# ['销售额']：指定要聚合的列
# .agg(['sum', 'mean'])：同时应用多个聚合函数
#   - 'sum'：计算每组销售额总和
#   - 'mean'：计算每组销售额平均值
print(df.groupby(['产品', '地区'])['销售额'].agg(['sum', 'mean']))

# ==================== 数据透视表（pivot_table）====================
# df.pivot_table()：创建数据透视表，类似Excel透视表功能
# index='产品'：将'产品'列设为行索引（每行代表一个产品）
# values='销售额'：指定要聚合的数值列
# aggfunc='sum'：聚合方式为求和（默认是均值）
pivot_df = df.pivot_table(index='产品', values='销售额', aggfunc='sum')
print(pivot_df)  # 输出结果与上面groupby('产品')求和类似但格式不同

# 复杂透视表：多级行索引 + 多聚合函数
# index=['产品', '地区']：行索引包含产品和地区两级（嵌套行标签）
# values='销售额'：依然对销售额进行运算
# aggfunc=['sum', 'mean']：对每组同时计算总和与平均值
pivot_df = df.pivot_table(index=['产品', '地区'], values='销售额', aggfunc=['sum', 'mean'])
print(pivot_df)