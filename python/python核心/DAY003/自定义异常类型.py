"""
自定义异常类型
"""
class MyException(Exception):
    pass 


# 
def get_age(age):
        if age>=200 or age<=0:
            # 主动抛出一个异常
            raise MyException("年龄不合法")
        else:
            print(age)
# 
try:
    get_age(1000)
except MyException as e:
    print(e)
finally:
    print('程序结束')

