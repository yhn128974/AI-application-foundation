# import os

# for element in [1, 2, 3]:
#     print(element)

# for element in (1, 2, 3):
#     print(element)

# for key in {"one": 1, "two": 2}:
#     print(key)

# for char in "123":
#     print(char)

# with open("myfile.txt", "w") as f:
#     f.write("H\ne\nl\nl\no\n \nW\no\nr\nl\nd\n")
# for line in open("myfile.txt"):
#     print(line, end="")
# os.remove("myfile.txt")

"""
以直接作用于 for 循环的数据类型有以下几种：
	容器，如 list 、 tuple 、 dict 、 set 、 str 等。
	generator ，包括生成器和带 yield 的generator function。
这些可以直接作用于 for 循环的对象统称为可迭代对象：Iterable。

"""


from collections.abc import Iterable
# 判断对象是否可以迭代
# isinstance 实例判断函数
# print(isinstance([], Iterable))  # True
# print(isinstance((), Iterable))  # True
# print(isinstance(set(), Iterable))  # True
# print(isinstance({}, Iterable))  # True
# print(isinstance("100", Iterable))  # True
# print(isinstance(100, Iterable))  # False


# # 判读对象是否为迭代器
from collections.abc import Iterator
# print(isinstance([],Iterator))
# print(isinstance((),Iterator))
# print(isinstance({},Iterator))
# print(isinstance(set(),Iterator))
# print(isinstance(" ",Iterator))
# # (x for x in range(10)) 为迭代器表示形式
# print(isinstance((x for x in range(10)),Iterator))

"""
迭代器有两个基本的方法：iter() 和 next()。
在容器对象上使用 for 语句时，在幕后，for 语句会在容器对象上调用 iter()。该函数返回一个定义了 __next__() 方法的迭代器对象，此方法将逐一访问容器中的元素。当元素用尽时，__next__() 将引发 StopIteration 异常来通知终止 for 循环。 你可以使用 next() 内置函数来调用 __next__() 方法。
"""

# class MyT:
#     def __iter__(self):
#         print("hello wrold!")
#         return self

# mine=MyT()

# print(isinstance(mine,Iterable))

# # iter 获取可迭代对象的迭代器
# list1=[1,2,3]
# # 
# aa=iter(list1)
# print(isinstance(list1,Iterable))
# print(isinstance(list1,Iterator))
# # 
# print(isinstance(aa,Iterator))
# # 获取迭代器对象的下一个值
# print(next(aa))


class my_list_iterator:

    def __init__(self,data):
        self.data=data
        self.index=0

    def __next__(self):
        if self.index==len(self.data):
            raise StopIteration

        res=self.data[self.index]
        self.index+=1
        return res

# 
class my_list:
    def __init__(self,data):
        self.data=data
# __iter__要返回一个实例化对象
    def __iter__(self):
         return my_list_iterator(self.data)

ml=my_list([1,2,3,4])

print(isinstance(ml,Iterable))
# 得到可迭代对象的迭代器
ml_Iterator=iter(ml)


for item in ml:
    print(item)
# print(isinstance(ml_Iterator,Iterator))
    