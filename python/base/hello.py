# s1 = 72
# s2 = 85
# s3=(s2-s1)/s1
# print('小明的成绩提升了%.2f%%.'%(s3*100))
# print('小明的成绩提高了{0:.2f}%'.format(s3*100))
# print('小明的成绩提高了{s3*100.2f}%')

# 字面量的写法
# print(True)
# print(False)
# print("hello python")
# print(None)#空类型

# print(True+1)
# print(False-1)


# #变量
# num=100.1;
# num=2000;
# print(num)
# num='ok'
# print(num)
# base=20.1;
# mon=50;
# print("播放总量为",base+mon*3)

# #数据类型
# print(type('string'))
# print(type(None))
# num=100;
# print(type(num))
# #类型判定 
# print(isinstance('string',str)) 
# print(isinstance('string',int)) 

# #字符串
# s3="""
# hello
# world!
# """
# print(s3)
# s1=' it\'s am apple ' #\ 转译操作
# s2="hello 的意思是'你好' "
# print(s1)
# print(s2)

# s4=' \t欢迎你\n的到来' #\n 换行,\t缩进
# print(s4)

# #字符串拼接
# print(s2+s4)
# name='hello'
# age=20
# address='chongqing'
# print("我是%s,年龄%s,住在%s" %(name,age,address))
# #字符串前面加f 拼接在{}里面
# print(f"你好{name},年龄{age}，地址{address}")


# #转化为字符串
# num4=100
# print("hello"+str(num4) )

# name=input("请输入您的姓名")
# age=input("您的年龄是")
# print(f"欢迎{name}，今年{age}岁了") #前面不要忘记加f


# 类型转换 int()
# num=input("您的银行卡密码为：")
# print(f"正确的密码为：{int(num)-1}")

# 请输入两个数字  计算x+y与x-y
# x=int(input("请输入x:"))
# y=int(input("请输入y:"))
# print("x+y=",x+y)
# print("x-y=",x-y)

# 计算BMI
# weight=float(input("请输人体重："))
# height=float(input("请输人身高："))
# print("BMI为",weight/height**2)


# 逻辑运算符号
# num1=float(input("请输入数字1: "))
# num2=float(input("请输入数字2: "))
# if (num1>50 and num2>50):
#     print('全部大于')
# else:
#     print('不满足条件')

# if( num1!=50 or num2!=50):
#     print('至少有一个不等于50')
# else: 
#      print('都等于50')

# score=70
# if score>=90:
#     print('优秀')

# elif score>=60:
#     print('及格')
# else:
#     print('不及格')

# 登录验证
# username=input("请输入用户名：")
# password=input("请输入密码：")
# if username=='admin' and password=='123456':
#     print('登录成功')   
# else:
#     print('登录失败')


# years=int(input("请输入年份："))
# if (years%4==0 and years%100!=0 )or years%400==0:
#     print(f"{years}是闰年")
# else:    
#     print(f"{years}不是闰年")

# 三角形判断
# a=float(input("请输入三角形的第一条边："))
# b=float(input("请输入三角形的第二条边："))
# c=float(input("请输入三角形的第三条边："))
#
# if a+b>c and a+c>b and b+c>a:
#         if a==c  or a==b or b==c:
#             print("可以构成等腰三角形")
#         elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#              print("可以构成直角三角形")
#         else:
#             print("可以构成普通三角形")
# else:
#     print("不能构成三角形")

"""
hello world!
"""
import random
from operator import truediv

from prompt_toolkit.contrib.telnet import TelnetServer

# match
# day=int(input("请输入数字1-7: "))
# match day:
#     case 0:
#         print("星期一")
#     case 1:
#         print("星期二")
#     case 2:
#         print("星期二")
#     case 3:
#         print("星期二")
#     case 4:
#         print("星期二")
#     case 5:
#         print("星期二")
#     case 6 | 7:
#         print("restDay")
#         # 默认操作
#     case _:
#         print("error")

# while
# i = 0
# sum = 0
# while i < 10:
#     print("hello world!")
#     if (i % 2 == 0):
#         sum = sum + 1
#     i += 1
# else:
#     print("循环结束")
#
# print(sum)


# for 循环
# list = ["hello world!","python"]
# for i in list:
#     print(i)
# else:
#     print("循环结束")


# range
# for i in range(0,10,1):#含头不含尾
#     print(f"<UNK>{i}<UNK>")

# for in for
# height = int (input("Enter the height of your input: "))
# length =int(input("Enter the length of your input: "))
# for i in range(0,height):
#     print('\n')
#     for j in range(0,length):
#         print("*",end=' ')


# for i in range(1, 10):
#     print('\n')
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i * j}', end='\t') #\t  制表符



# while True:
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     if username == " " or password == "":
#         print("Please enter your username and password.")
#         continue
#     elif username=='admin' and password=='123456':
#         break
#     else:
#      print("Username and/or password incorrect.")
#      continue
# print('登录成功！')

#随机数
random_number = random.randint(1, 100)

while True:
    currentNumber=int(input("Enter your number: "))
    if currentNumber > random_number:
        print("猜大了")
        continue
    if currentNumber < random_number:
        print("猜测小了")
        continue
    else:
        print("才对了就是这个")
        break



