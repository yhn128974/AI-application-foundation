import math
import random

# 全部导入
import function as locat_function
# 指定功能导入
from function import calc_order_cost


# 使用导入的模块
total1 = locat_function.calc_order_cost(('鼠标', 188, 2), ("键盘", 388, 1), ("手机", 4555, 1), coupon=10, score=4000, express=9.9)
print(total1)


total2 = calc_order_cost(('鼠标', 188, 2), ("键盘", 388, 1), ("手机", 4555, 1), coupon=10, score=4000, express=9.9)
print(total2)


# print(random.randint(1,100))


