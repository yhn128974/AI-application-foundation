"""
需求：
创建numpy数组，使用不同的方法创建，查看结果，观察特性

步骤：
1.导包
2.创建数组，一维数组，二维数组
3.创建特殊数组
4.创建序列数组
5.创建随机数组
"""

# 1.导包
import numpy as np

# 2.创建数组，一维数组，二维数组
arr1 = np.array([1,2,3,4,5])
print(type(arr1))
print("一维数组：",arr1)
arr2 = np.array([[1,2,3],[4,5,6]])
print("二维数组：",arr2)
arr3 = np.array([[[1,2],[2,3],[3,4]],[[4,5],[5,6],[6,7]]])
print("三维数组：",arr3)

# 3.创建特殊数组
# 全0数组
zero_arr = np.zeros((3,4))
print("全0数组：\n",zero_arr)

#全1数组
ones_arr = np.ones((2,3,1,2))
print("全1数组：\n",ones_arr)

# 4.创建序列数组
range_arr = np.arange(0,10,2)  # 2是步长
print("范围数组：",range_arr)

range_arr_sim = np.arange(0,10)
print("范围数组简单：",range_arr_sim)

# 除以num -1 有num -1个段落
linspace_arr = np.linspace(0,1,6)
print("等分数组：",linspace_arr)

#5.创建随机数组
# 0-1分布
random_arr = np.random.rand(3,3)
print("随机数组：\n",random_arr)

# 正态分布
normal_arr = np.random.randn(3,3)
print("正态分布：\n",normal_arr)