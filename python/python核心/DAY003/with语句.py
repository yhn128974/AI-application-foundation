""""
with
    语法
        with expression as variable:
            # 代码块
    说明
        with 是关键字
        as  是关键字
        expression:是一个对象或者是函数调用，要求返回的内容类型必须是上下文管理器对象类型
               上下文管理器类中有两个方法必须提供：__enter__和__exit__方法。

        variable：是可选的，用于存储expression的__enter__方法的返回值

    执行原理
        当执行with语句时，会调用expression对象的__enter__方法。
        __enter__ 方法的返回值可以被存储在 variable 中（如果有），以供 with 代码块中使用。
        __enter__方法的返回值一般是self(当前上下文管理器对象)
        执行with代码块中的内容
        当代码块执行完毕之后，不管是否发生异常，都会执行上下文管理器对象的__exit__方法，在__exit__方法中，将资源释放掉

"""

# 常规方法
# try:
#     try:
#         file=open("test.txt",'w')
#         file.write('a')
#     except:
#         print("errors")
#     finally:
#         file.close()
    
# finally:
#     print(file.closed)

# with 方法
try:
    with open("test.txt",'w') as file:#with的底层会自动关闭文件对象
        file.write(abc)
finally:
    print(file.closed)