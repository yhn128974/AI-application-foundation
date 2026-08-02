"""
    该案例演示了处理不同类型的异常
"""
# print(int("abc"))                           ValueError:
# print(3/0)                                  ZeroDivisionError: division by zero
# list1 = [1, 2, 3]       print(list1[3])     IndexError: list index out of range
# print(a)                                      NameError: name 'a' is not defined

try:
    print(int("abc"))

except ValueError as e:
    print("valueError:", e)

except IndexError as e:
    print("IndexError:", e)

except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
except:
    print("发生异常了")


