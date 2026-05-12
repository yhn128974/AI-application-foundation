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
from unittest import case

from prompt_toolkit.contrib.telnet import TelnetServer
from scipy.cluster.hierarchy import average

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

# 随机数
random_number = random.randint(1, 100)

# while True:
#     currentNumber=int(input("Enter your number: "))
#     if currentNumber > random_number:
#         print("猜大了")
#         continue
#     if currentNumber < random_number:
#         print("猜测小了")
#         continue
#     else:
#         print("才对了就是这个")
#         break

# 数据容器
# list
# list=[1,2,3,4,5,6,7,8,9]
# #list[0:5:1]步长截取（下标含头不含尾）
# # print(list[0:5:2])
# # print(list[:5:2])
# # print(list[5::2])
# # print(list[0:-5:2])
# list.append(10)  #append==push
# print(list)
# list.insert(1,random_number)
# print(list)
#
# list.remove(1)
# print(list)
#
# list.pop()
# print(list)
#
# list.sort()
# print(list)

#
# list=[]
# for i in range(10):
#     number=int(input(f'请输入第一个{i+1}个数字: '))
#     list.append(number)
#
# list.sort()
# print(list)
# print(sum(list)/len(list))

# 去重合并列表
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [4, 5, 6, 7, 8, 9]
# newList = []
# for i in list1:
#     newList.append(i)
#
# for j in list2:
#         if j not in list1:
#             newList.append(j)
#
# newList.sort()
# print(newList)
#
# # list3=[*list1,*list2]\
# # 解包
# list3=sorted(set([*list1,*list2]) )#
# list4=sorted(set(list1+list2) )#
# print(list3)
# print(list4)

# #生成20个随机数的数列
# num_list=[]
# for i in range(1,20):
#     num_list.append(random.randint(1,100))
# print(num_list)
#
# # 列表推导式
# num_list2=[i**2 for i in range(1,20)]
# print(num_list2)

## 从一个数字列表中提取所有的偶数，并计算组成一个新的列表
# number_list = [i for i in range(1, 20)]
# sum = 0
# for number in number_list:
#     if number % 2 == 0:
#         sum = sum + number
# print(sum)
#
# #demo 高级列表推导式
# new_number_list =[i for i in number_list if i%2==0]
# print(new_number_list)

# 合并字符列表
# list1=['a','b','c','d','e','f']
# list2=['g','h','i','j','k','l','m']
# list3=['c','d','e','f']
# new_list=sorted(set(list1+list2+list3))
# print(new_list)

# 获取能够被3或者5整除的元素，然后去平方
# number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# new_list=[i**2 for i in number_list if i%3==0 & i%5==0]
# print(new_list)

# 提取列表中的正整数
# number_list=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3]
# new_list=[i for i in number_list if i>=0]
# print(new_list)

# 字符串的切片操作
# str='hello_python'
# newStr1=str[0:5:1]
# print(newStr1)
# newStr2=str[-1:-7:-1]
# print(newStr2)

# currentStr = 'hello_world_from_python'
# index = currentStr.find('h')
# print(index)
# countNumber = currentStr.count('o')
# print(countNumber)
# UperStr = currentStr.upper()
# print(UperStr)
# lowerStr = currentStr.lower()
# print(lowerStr)
# # split对字符串进行切割
# slist = currentStr.split('_')
# print(slist)
# newStr = currentStr.replace('_', ' ')
# print(newStr)
# # 是否以指定的字符串开始或者结束
# print(currentStr.startswith('hello'))
# print(currentStr.endswith('from'))
# print('_________________-')
# # 字符串的数据是不可修改的
# print(currentStr)

# demo 对邮箱格式进行验证
# inputStr = input('请输入邮箱地址: ')
# if inputStr.count('@') == 1 and inputStr.count('.') == 1 and '.' in inputStr:
#     print('邮件格式正确')
# else:
#     print("邮箱格式错误")


# 判断回文字符串
# currentStr = '上海自来水来自海上'
# if currentStr[:int(len(currentStr) / 2):1] == currentStr[-1:-int(len(currentStr) / 2+1):-1]:
#     print('是回文数')
# else:
#     print("不是回文数")
#
# print(currentStr[:int(len(currentStr) / 2):1])
# print(currentStr[-1:-int(len(currentStr) / 2):-1])


# 输入十个字符串，反转后全部转化为大写，然后记录在例表中输出
# StrList = []
# for i in range(10):
#     StrList.append(input('请输入文本: ').upper())
# print(StrList)


##元组，不可修改的数组
# tupleList=(10,20,30)
# print(tupleList)
# print(type(tupleList))
# print(tupleList[1::1])


# t1=(1,2,3,4,5)
# t2=(4,5,6,7,8)
# # 组包
# t3=t1+t2
# # 解包
# a,b,c,d,e=t1
# x,*y=t2
# print(a)
# print(y)
# print(t3)
# #轮换
# a=10
# b=20
# a,b=b,a
# print(a)
# print(b)

# #生成一个学生成绩列表元组
# students = (
#     ("S001", "张三", 85, 92, 78),
#     ("S002", "李四", 92, 88, 95),
#     ("s003", "王五", 78, 85, 82),
#     ("S004", "<UNK>", 82, 90, 91),
#     ("S005", "<UNK>", 91, 90, 92),
#     ("S006", "<UNK>", 92, 90, 93),
# )
# countMath = 0
# countEnglish = 0
# countChine = 0
#
# for student in students:
#     countMath += student[2]
#     countEnglish += student[3]
#     countChine += student[4]
#     total = student[2] + student[3] + student[4]
#     print(f"{student[0]}的总分是{total}")
#     if total / 3 >= 90:
#         print(f"{student[0]}是优秀学生")
#
# print(f"班级没科平均分是 {countMath / 3:.2f}/{countEnglish / 3:.2f}/{countChine / 3:.2f}")
# # 提取二位数组中每一列的数据
# # mathScore = [s[2] for s in students]
# # englishScore = [s[3] for s in students]
# # chineScore = [s[4] for s in students]
# # print(mathScore, englishScore, chineScore)
#
#
# # 二位元组解包
# for id, name, mathScore, englishScore, chineScore in students:
#     total = mathScore + englishScore + chineScore
#     if total / 3 >= 90:
#         print("优秀学生")
#     print(f"{id}<UNK>{total}")

### set集合 set是不重复的
# #  定义集合
# s1=set() #定义集合用set(),b不能直接写一个{ }
# s2={1,2,3,4,4,5,5,6,7,7}
# print( type(s2),s2)
# print(s1)
# # 添加元素
# s2.add(8)
# print(s2)
# # 删除元素
# s2.remove(7)
# print(s2)
# #随机删除一个元素
# s2.pop()
# print(s2)
# # 清空集合
# s2.clear()
# print(s2)
# 逻辑方法
# s2 = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}
# s3 = {"e", "f", "g", "h", "i", "j", "k", "l"}
# print(s2.intersection(s3))
# print(s2.union(s3))
# print(s2.difference(s3))
# print(s3.difference(s2))


# # 选修足球学生名单
# football_set = {"王林", "曾牛", "徐立国", "通天", "天运子", "韩立", "厉飞雨", "马五", "紫灵"}
#
# # 选修篮球学生名单
# basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王重", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
#
# # 选修法学学生名单
# french_set = {"许木", "王重", "十三", "虎虎", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
#
# # 选修艺术学生名单
# art_set = {"通天", "天运子", "韩立", "虎虎", "姜老道", "紫灵"}
#
# # 同选修法语与艺术的学生
# print(french_set.intersection(art_set))
# print(french_set & art_set)
#
# # 找出同时选修了全部课程的学生
# print(football_set.intersection(basketball_set.intersection(french_set.intersection(art_set))))
# print(football_set & art_set & french_set & art_set)
#
# # 找出选修了足球但是没有选修篮球的学生
# print(football_set.difference(basketball_set))
# print(football_set - basketball_set)
# newSet = {s for s in football_set if s not in basketball_set}
# print(newSet)
#
# # 获取学生名单
# newList = football_set | basketball_set | french_set | art_set
# print(newList)
#
# # 统计每一个学生选修课程的数量
# all_list = [*newSet, *french_set, *basketball_set, *art_set]
# for s in all_list:

# print(f"{s}选修了{all_list.count(s)}")


# 字典
# core = {
#     "韩立": 100,
#     "王琳": 500,
#     "李纨": 200,
#     "紫灵": 534,
#     (1, 2): 700,
# }
# print(core.get((1, 2)))
#
# core["王琳"] = 600
# print(core.get("王琳"))
#
# #
# core["longyou"] = 999
# print(core.get("longyou"))
#
# # 删除字典中的元素,并获取删除的值
# score = core.pop("longyou")
# print(score)
# # 命令删除
# # del core["longyou"]
#
# #便利输出字典
# for k, v in core.items():
#     print(k, v)
#
shopping_car = {
"矿泉水":{
    "price":100,
    "number":10
}
}

menu="""
###########################
#       1.添加商品          #
#       2.修改商品          #
#       3.查看商品详情       #
#       4.删除商品          #
#       5.退出购物车         #
############################
"""

# print("欢迎使用购物车管理系统")
# print(menu)
#
# choice = input("请选择要执行的操作（1-5）")
# match choice:
#     case "1":
#         name = input("请输入商品名称: ")
#         if name in shopping_car:
#             print("改商品已经存在")
#         else:
#             current_price = input("请输入商品价格")
#             current_number = input("请输入商品数量")
#             shopping_car[name] = {
#                 "price": current_price,
#                 "number": current_number,
#             }
#             print("商品已添加")
#     case "2":
#         name = input("请输入要修改的商品名称")
#         if name in shopping_car:
#             current_price = input("请输入商品价格")
#             current_number = input("请输入商品数量")
#             shopping_car[name] = {
#                 "price": current_price,
#                 "number": current_number,
#             }
#         else:
#             print("抱歉该商品不在购物车中")
#     case "3":
#         name = input("请输入要修改的商品名称")
#         if name in shopping_car:
#           print(shopping_car[name]["number"])
#           print(shopping_car[name]["price"])
#         else:
#             print("抱歉该商品不在购物车中")
#     case "4":
#         name = input("请输入要删除的商品名称")
#         if name in shopping_car:
#             del shopping_car[name]
#             print("已删除该商品")
#     case _:
#         print("退出完毕！")


