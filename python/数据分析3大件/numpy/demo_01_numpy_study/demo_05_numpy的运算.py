"""
需求：查看数组不同元素符号的结果

步骤：
1.导包
2.创建原始数组
3.进行不同类型的运算
4.查看如何计算计算结果
"""

# 1.导包
import numpy as np

# 2.创建原始数组

a = np.array([1, 2, 3, 4])
b = np.array([1, 6, 7, 8])

# 3.进行不同类型的运算
print("加法：",a + b)
print("减法：",a - b)
print("乘法：",a * b)
print("除法：",a / b)
print("幂运算：",a ** 3)

# 4.数组之间的比较运算

print("大于比较",a > 2)
#c = np.array([2, 2, 2, 2])

print("等于比较",a == b)

# 补充
# // 整除；% 取余；** 幂
print(b // a)
print(b % a)
print(a ** b)

