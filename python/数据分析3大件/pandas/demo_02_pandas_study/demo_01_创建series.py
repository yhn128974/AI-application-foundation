"""
需求：
创建series，使用不同方式创建，查看索引和值

步骤：
1.导包
2.创建对象 从列表，从字典
3.指定索引
4.series操作 查看值或索引

"""
#1.导包

import pandas as pd
import numpy as np

# 2.创建对象 从列表
s1=pd.Series([1,2,3,4,5,np.nan,6,7,8,9])
print("从列表创建的Series：\n",s1)


# 从字典
s2 = pd.Series({"a":1,"b":2,"c":3,"d":4,"e":5})
print("从字典创建的Series：\n",s2)

# 3.指定索引
s3 = pd.Series([10,20,30],index=['x','y','z'])
print("指定索引的Series：\n",s3)

#Series操作
print("索引：",s1.index)
print("值：",s1.values)




