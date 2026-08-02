"""
    该案例演示了raise
"""
"""
# 两个整数的加法计算
def add(num1,num2):
    if isinstance(num1 ,int) and isinstance(num2,int):
        return num1 + num2
    else:
        # 抛出异常
        raise TypeError("参数类型错误")


try:
    res = add(1,2.0)
except TypeError as e:
    print(type(e))
    print(e)
else:
    print(res)
"""

def int_add(x, y):
    assert isinstance(x, int) and isinstance(y, int), "参数类型错误"
    return x + y

print(int_add(1, 2.0))
