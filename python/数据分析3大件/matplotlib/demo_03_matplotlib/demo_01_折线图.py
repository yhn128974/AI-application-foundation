import numpy as np
import matplotlib.pyplot as plt
# 注意:新版本需要指定 matplotlib 使用 TkAgg 作为图形后端来渲染和显示图表
import matplotlib
matplotlib.use('TkAgg')
# 注意:中文显示需要额外设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建数据
np.random.seed(42)  # 设置随机种子，保证结果可重复
x = np.random.randn(50)
y = x * 2 + np.random.randn(50) * 0.8  # 添加噪声
# 绘制散点图
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red')

# 添加标题和标签
plt.title("散点图示例")
plt.xlabel("X值")
plt.ylabel("Y值")

# 显示网格
plt.grid()

# 显示图表
plt.show()

