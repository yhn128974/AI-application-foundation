"""
需求：查看numpy不同维度的属性
步骤：
1.导包
2.创建数组
3.打印他不同的属性

"""
# 1.导包
import numpy as np

arr = np.array([[1,2,3],[4,5,6]],dtype=np.float64)

#arr = np.array([1,2,3],dtype=np.float64)

print("数组：",arr)

print("数组维度：",arr.ndim)

print("数组形状：",arr.shape)

print("数组大小：",arr.size)

print("数据类型：",arr.dtype)