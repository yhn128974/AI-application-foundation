# def func1():
#     print("hello world!")
#
#
# func1()
#
#
# def func2(r, pi):
#     area = pi * r ** r;
#     return area
#
#
# print(2 * func2(2, 3.14))
#
#
# # 多参数返回的是元组类型
# def fun3(w, l):
#     """
#     compute ares
#     :param w: with
#     :param l: length
#     :return: with times length
#     """
#     area = w * l
#     return area, w, l
#
#
# print(type(fun3(2, 3.14)), fun3(2, 3.14))
#
# # 对元组进行解包
# e, w, l = fun3(2, 3.14)
# print(e, w, l)
from numpy.ma.extras import average
from tornado.options import options

#
#
# # 计算一个字符串中元音字母的个数
# def count_number(string):
#     """
#     Return the count of a 'start' value (default: 0) plus an iterable of numbers
#     :param string:
#     :return: number of 'start' value (default: 0)
#     """
#     number = 0
#     for char in string:
#         if char in 'aeiouAEIOU':
#             number += 1
#     return number
#
#
# print(count_number('hello world!'))
#
#
# #
# def clac_score(score_list):
#     """
#     get max_score and min_score and average_score from the score_list
#     :param score_list:
#     :return: max_score, min_score, average_scor e
#     """
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg = round(sum(score_list) / len(score_list), 1)
#     return max_s, min_s, avg
# max_s, min_s, avg = clac_score([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(max_s, min_s, avg)

# 指定默认参数
# def fun1(new_msg,message='232',message2='232'):
#     print(f'MESSAGE:{new_msg}and{message}and{message2}')
#
# fun1('hello')


# # 不定长参数的函数,传入的参数以元组的形式保存
# # *args 基于位置传递的参数，**kwargs基于关键字传递的参数
# def fun2(*args, **kwargs):
#     print(type(args))
#     print(args)
#     print(type(kwargs))
#     print(kwargs)
#     if kwargs['flage'] == False:
#         print("结果为Flase")
#     else:
#         print("结果为true")
#
#
# fun2(1, 2, 3, 4, key1="3", key2=100, flage=False)


# # 回调函数:将函数作为参数
# def fun1(message1, message2):
#     print(message1 + message2)
#
#
# def fun2(message1, message2, options):
#     options(message1, message2)
#
#
# fun2('hello', 'world', fun1)


# # 匿名函数(计算属性)
# out_line = lambda: print('_____________________')
# print(out_line())
# 匿名写法
# sumxy = lambda x, y: x + y
# print(sumxy(1, 2))


# # list.sort()排序方法
# data_list = ['c++', 'python', 'java', 'php', 'javascript', 'c', 'Go']
# print(sorted(data_list))
# #
# print(data_list)
# # data_list.sort(key=lambda item: len(item), reverse=True)  # 匿名函数的典型应用场景
# data_list.sort(key=len, reverse=True)  # 匿名函数的典型应用场景,作为高阶函数的参数
# print(data_list)


# # 计算N的阶乘
# def func(number):
#     if number > 1:
#         return number * func(number - 1)
#     else:
#         return 1
#
#
# print(func(5))
"""
案例2:定义一个用于积分抵扣函数
"""

__all__ = ['calc_order_cost']


def calc_order_cost(*args: tuple[str, float, float], coupon: float = 0, score: float = 0, express: float = 0) -> float:
    total_price = [goods[1] * goods[2] for goods in args]
    total_price = sum(total_price)
    #
    if total_price > 5000 and coupon <= total_price:
        total_price -= coupon
    #
    if total_price >= 5000 and score // 100 <= total_price:
        total_price -= score // 100
    #
    total_price += express

    return total_price


#

# total = calc_order_cost(('鼠标', 188, 2), ("键盘", 388, 1), ("手机", 4555, 1), coupon=10, score=4000, express=9.9)
# print(total)

# 直接运行时__name__==__main__,被引用时__name__ ==当前模块名
if __name__ == 'function':
    total = calc_order_cost(('鼠标', 188, 2), ("键盘", 388, 1), ("手机", 4555, 1), coupon=10, score=4000, express=9.9)
    print(total)
