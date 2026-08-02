# 
# def add(num1,num2):
#     if isinstance(num1,int) and isinstance(num2,int):
#         return num1+num2
#     else:
#         # 主动抛出异常== raise xxxError
#         raise TypeError("TypeError")

# try:
#     res=add(1,2.0)
# except TypeError as e :
#     print(e)
# else:
#     print(res)

# 异常断言
def add(num1,num2):
    # assert == if not ，在底层封装了异常处理
        assert isinstance(num1,int) and isinstance(num2,int),"参数类型错误"
        return num1+num2

print(add(1,20.2))
