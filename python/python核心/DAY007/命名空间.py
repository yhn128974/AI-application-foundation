num=10

def m1():
        # 局部作用域要访问全局变量需要加 global关键字
        global  num
        num+=10
        print(num)
m1()

