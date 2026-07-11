# 异常处理
# try:
#     res=3/0
#     print(res)
# # except ==catch
# except:
#     print('error')
# print('end')


# def handle_error():
#     try:
#       res=3/0
#       print(res)
# # except ==catch
#     except:
#         print('error')
#     print('end')

# handle_error()

# 多异常类型处理
# try:
#     print(3/1)
# except ValueError as e:
#     print("valueError",e)
# except IndexError as e:
#     print("index_erroe",e)
# except ZeroDivisionError as e:
#     print("zero_divion_error",e)
# except:
#     # 其他异常
#     print("error");
# else:
#     # 如果try中代码没有异常，将执行else中的代码
#     print('no error')
#     # 无论是否发生异常都要执行的代码，一般将资源释放的代码放到里面
# finally:
#     print("finally")


# # 练习
# try:
#     num1=int("123avc")
# except ValueError as e:
#     try:
#         with open("error.log",'w') as file:
#             file.write(str(e))
#     except e:
#         print(e)
# else:
#     print(num1)
# finally:
#     print("执行完毕")

#  练习2，自定义异常类
# class InvalidAgeError(Exception):
#     pass
# class UnrealisticAgeError(Exception):
#     pass

# def check_age(age):
#     if age<0:
#         raise InvalidAgeError("年龄错误")
#     elif age>=120:
#         raise UnrealisticAgeError("年龄过大")
#     else:
#         print(f"{age}岁了")



# try:
#     check_age(-100)
# except UnrealisticAgeError as e:
#     print(e)
# except InvalidAgeError as e:
#     print(e)
# except e:
#     print(e)
# else:
#     print('无异常')
# finally:
#     print("程序结束")