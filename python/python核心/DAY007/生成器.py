"""
创建生成器
"""
from unittest import case

from tornado.process import task_id

# 方式一：推导式
gen =(i for i in range(10))
print(type(gen))
#
# for i in gen:
#     print(i)

print(next(gen))


"""
13.3.1 什么是生成器
生成器（generator）是一个用于创建迭代器的简单而强大的工具。它的写法类似于标准的函数，但当它要返回数据时会使用 yield 语句。
当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后的表达式作为当前迭代的值返回。
每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行（它会记住上次执行语句时的所有数据值），
直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。
"""

# # 通过函数创建生成器
# def fei_bo():
#     a,b=0,1
#     while True:
#         a,b=b,a+b
#         print(b)
#
# fei_bo()

# 通过迭代器创建
# class MyIterator(object):
#     def __init__(self):
#         self.a=0
#         self.b=1
#
#     # 添加迭代器
#     def __next__(self):
#         self.a ,self.b=self.b, self.a+self.b
#         return self.b
#
# it=MyIterator()
#
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())

# 函数方式 2  :只要函数中有yield，这个函数就是生成器函数，返回值是一个生成器类型对象
# def fei_bo(num):
#     a,b=0,1
#     index=0
#     while index<num:
#         a,b,index=b,a+b,index+1
#         yield b
#     return  "函数执行完毕！"
#
#
# fei=fei_bo(5)
# # print(type(fei))
# try:
#     while True:
#         print(next(fei))
# except StopIteration as e:
#         print(e.value)


# 恢复执行并向生成器函数“发送”一个值。 这个值作为当前 yield 表达式的结果。
# send() 方法会返回生成器所产生的下一个值，或者如果生成器没有产生下一个值就退出则会引发 StopIteration。
def gen():
    task_id=0
    int_value=0
    char_value='a'

    while True:
        match task_id:
            case 0:
               int_value+=1
               task_id= yield int_value
            case 1:
                char_value=chr(ord(char_value)+1)
                task_id= yield char_value
            case _:
                task_id=yield


gentor=gen()
# print(next(gentor))
# gentor.send(1)指定当前这次的判定条件，（发生任务id）
# 启动send表达：next(gentor)==gentor.send(None)
print(gentor.send(None))
#
print(gentor.send(1))
print(gentor.send(0))
print(gentor.send(1))
print(gentor.send(0))
print(gentor.send(1))




