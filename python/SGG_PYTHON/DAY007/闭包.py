def outer():
    a,b=10,20
    def inner():
        print(a)
        print(b)
    return inner


ff=outer()
print(ff)
# 得到函数返回元组
print(ff.__closure__)
print(ff.__closure__[0].cell_contents)
print(ff.__closure__[1].cell_contents)
