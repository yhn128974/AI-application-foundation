
"""
    该案例演示了finally


"""

"""
try:
    res = 3/0
except:
    print(int("aa"))
    print("发生了异常")
else:
    print(f"结果是:{res}")
finally:
    print("finally")
print("~~~end~~~")
"""

#
# def m1():
#     try:
#         for i in range(10):
#             if i == 5:
#                 return
#             print(f"i的值{i}")
#     except:
#         print("发生了异常")
#     finally:
#         print("finally")
#
# m1()