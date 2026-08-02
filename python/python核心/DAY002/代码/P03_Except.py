"""
    该案例演示了语法错误和异常
"""

"""
# 语法错误  程序在对语法进行解析阶段就发现问题  程序不会执行
def m1():
    print("hello world")
    while True print(1)

m1()
"""
"""
# 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常
def m1():
    print("hello world")
    print(a)
m1()
"""
"""
# 异常处理
try:
    res = 3/0
    print(res)
except:
    print("发生异常了")

print("end")
"""