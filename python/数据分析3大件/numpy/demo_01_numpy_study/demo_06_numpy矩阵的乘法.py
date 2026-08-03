import numpy as np

# 创建两个二维矩阵（必须是 2D 才谈「矩阵乘」）
# m1: 2 行 3 列 → shape (2, 3)
#  np.array()得到是一个矩阵可以进行矩阵运行
m1 = np.array([[1, 2, 3],
               [4, 5, 6]])

# m2: 3 行 2 列 → shape (3, 2)；m1 的列数 3 == m2 的行数 3，可以相乘
m2 = np.array([[2, 1],
               [1, 3],
               [3, 4]])

# m1 = [1,2,3]
# m2 = [4,5,6]

# ----- 方法1：@ 运算符（Python 3.5+，可读性最好）-----
# @：矩阵乘法运算符，底层调用 matmul 逻辑
# 数组乘法用*，矩阵乘法用@
result1 = m1 @ m2  # 结果 shape (2, 2)
print("\n========== 方法1: 使用 @ 运算符 ==========")
print(result1)
print(f"结果形状: {result1.shape}")  # f-string：格式化字符串；.shape 属性

# ----- 方法2：np.matmul(a, b) -----
# matmul：matrix multiply 的缩写，与 @ 等价
result2 = np.matmul(m1, m2)
print("\n========== 方法2: 使用 np.matmul() ==========")
print(result2)

# ----- 方法3：np.dot(a, b) -----
# 二维数组时 dot 与 matmul 结果相同；一维时 dot 是内积（标量）
result3 = np.dot(m1, m2)
print("\n========== 方法3: 使用 np.dot() ==========")
print(result3)
