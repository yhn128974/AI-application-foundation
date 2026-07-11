import module1 #全局导入
# 具体导入
from module1 import * #导入全部不以单下划线_xxx开头的成员
# from module1 import add_num,num1
# 通过__all__导入

# 导入环境外部模块
import sys
print(sys.path)
sys.path.append("d://aa")
print(sys.path) 

sum= module1.add_num(1,3)
print(sum)

print(add_num(1,2))
print(num1)
# print(_num2)
# __aLL__无法限制类名.属性的方式导入
print(module1._num2)

# dir函数,输出类的成员
import math
print(dir(math))




