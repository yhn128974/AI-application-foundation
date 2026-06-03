class ErrorClass:
    def errorPrint(self):
        print(10 / 0)


#
#
# list = []
# newError = ErrorClass()
# # 错误处理
# try:
#     print("=======开始执行代码======")
#     # list.append('123')
#     # newError.errorPrint()
#     print("123"[6])
#     print("=======代码执行结束======")
# except ZeroDivisionError as e:  # 要指定异常类型
#     print("除数不能为0")
#     print(e)
#     print("=======<UNK>======")
# except IndexError as e:
#     print("索引错误")
# except Exception as e:
#     print(e)
# finally:
#     print("释放资源~")


choice = input("Enter your choice: ")

try:
    match choice:
        case "1":
            print('1')
        case "2":
            print('2')
            int(choice)
        case "3":
            print('3')
except ValueError as e:
    print(e)
except Exception as e:
    print(e)