
from math import sqrt
# # 
# def fun(x):
#     return sqrt(x)

# # 装饰器,返回内层函数
# def decerator(f):
#     # 返回被装饰函数
#      def inner(x):
#         x=abs(x)
#         return f(x)
#      return inner

# inn=decerator(fun)(-4)
# print(inn)

# # 装饰器语法糖，在被装饰的函数上加@装饰函数，效果等于fun2=decerator2(fun2)
# def decerator2(f):
#     def inner(x):
#         x=abs(x)

#         return f(x)
#     return inner

# def get_int(f):
#     def inner(x):
#         x=int(x)
#         return f(x)
#     return inner

# # 确保decerator先存在。多个装饰器要注意流程避免错误，先装饰的后之前，距离函数越近越先装饰
# @get_int
# @decerator2 
# def fun2(x):
#     return sqrt(x)

# print(fun2('-4'))


# # 类装饰器
# class My_class:
#     def __call__(self):
#         print("hello world!")
#     def m1(self):
#         print("124")

# mine=My_class()
# mine.m1()
# # 魔法方法 __call__ 在直接使用对象（）时候执行   
# mine()

# 演示类装饰器
def funx(x):
    return sqrt(x)

class Myclass:
    def __init__(self,f):
        self.f=f

    def __call__(self,x):
        x=abs(x)
        return self.f(x)

mc=Myclass(funx)
print(mc(-4))
print(Myclass(funx)(-4))