"""
    该案例演示了异常的传递
"""
"""
try:
    try:
        try:
            print(3/0)
        except NameError:
            print("第1层")
    except ValueError:
        print("第2层")
except ZeroDivisionError:
    print("第3层")
"""


def m3():
    print(1/0)


def m2():
    m3()


def m1():
    m2()


m1()