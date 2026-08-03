import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1)
# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr2 )
# arr3= np.array([[[1, 2], [3, 4]],   [[5, 6], [7, 8]]])
# print(arr3)

# create an array of zeros
zeros_array = np.zeros((3, 4))
print(zeros_array)
# create an array of ones
ones_array = np.ones((3,3,3,3))
print(ones_array)

#创建一个从0到10的数组，步长为2
range_array = np.arange(0, 10, 2)
print(range_array)

# 创建一个从0到10的数组，步长为1
range_array = np.arange(0, 10)
print(range_array)

# 创建一个从0到1的等间隔数组，包含5个元素
linspace_array = np.linspace(0, 1, 5)
print(linspace_array)

# 创建一个随机数组（0-1分布）
random_array = np.random.rand(3,4)
print(random_array)

# 创建一个随机数组（正太分布）
random_normal_array = np.random.randn(3,4)
print(random_normal_array)



