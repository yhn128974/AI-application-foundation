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


# 计算一个字符串中元音字母的个数
def count_number(string):
    """
    Return the count of a 'start' value (default: 0) plus an iterable of numbers
    :param string:
    :return: number of 'start' value (default: 0)
    """
    number = 0
    for char in string:
        if char in 'aeiouAEIOU':
            number += 1
    return number


print(count_number('hello world!'))

#
def clac_score(score_list):
    """
    get max_score and min_score and average_score from the score_list
    :param score_list:
    :return: max_score, min_score, average_score
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg = round(sum(score_list) / len(score_list), 1)
    return max_s, min_s, avg

max_s,min_s,avg= clac_score([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(max_s,min_s,avg)


