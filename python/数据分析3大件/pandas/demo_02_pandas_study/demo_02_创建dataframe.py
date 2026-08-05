"""
需求：
通过字典或者列表创建dataframe

步骤：
1.导包
2.创建对象
3.查看对象

"""
# # 1.导包

# import pandas as pd
# import numpy as np

# # 从字典创建对象
# data = {
#     '姓名': ['张三', '李四', '王五', '赵六'],
#     '年龄': [25, 30, 35, 28],
#     '城市': ['北京', '上海', '广州', '深圳'],
#     '工资': [5000, 7000, 6000, 8000]
# }

# df = pd.DataFrame(data)
# print("Dataframe为：\n",df)

# # 从列表创建dataframe
# data_list = [
#     ['张三', 25, '北京', 5000],['李四', 30, '上海', 7000],
#     ['王五', 35, '广州', 6000],['赵六', 28, '深圳', 8000]
# ]

# df = pd.DataFrame(data_list)
# print("Dataframe为：\n",df)

# df = pd.DataFrame(data_list,columns=["姓名","年龄","城市","工资"],index=["a","b","c","d"])
# print("Dataframe为：\n",df)

# # 查看dataframe基本信息
# print("形状：\n",df.shape)
# print("列名：\n",df.columns)
# print("索引名：\n",df.index)
# print("数据类型：\n",df.dtypes)




# 
import pandas as pd
import numpy as np
# 从字典创建对象
data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '年龄': [25, 30, 35, 28],
    '城市': ['北京', '上海', '广州', '深圳'],
    '工资': [5000, 7000, 6000, 8000]
}
# 
df=pd.DataFrame(data)
print(df)

print("\n")

# 从列表创建dataframe
data_list = [
    ['张三', 25, '北京', 5000],['李四', 30, '上海', 7000],
    ['王五', 35, '广州', 6000],['赵六', 28, '深圳', 8000]
]
df=pd.DataFrame(data_list,columns=["姓名","年龄","城市","工资"],index=["a","b","c","d"])
print(df)
print(df.shape)
print(df.columns)
print(df.index)
# 按列查看数据类型
print(df.dtypes)









