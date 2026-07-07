"""
单继承
"""
class Person:
    home='earth'
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

class YellowPerson(Person):
   color='yellow'
   
yp=YellowPerson("张三")#自动调用父类的构造方法

yp.say_hello()  # 继承父类的属性
print(yp.color)  # 调用子类的属性
print(yp.name)  # 继承父类的方法后得到的属性
print(yp.home)  # 调用父类的属性

"""
多继承
"""
class student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)  # 调用父类的构造方法
        self.student_id = student_id

    def study(self):
        print('先打个招呼？')
        super().say_hello()  # 调用父类的方法
        # Person.say_hello(self)  # 调用父类的方法
        print(f"{self.name} is studying.")


class CHineseStudent(student,YellowPerson):
    nationality = 'Chinese'
    

print(issubclass(CHineseStudent, student))  # True
print(issubclass(CHineseStudent, YellowPerson))  # True

cs=CHineseStudent("李四", "2023001")
print(cs.__dict__)  # 调用父类的属性
print(cs.study())  # 调用父类的方法,如果继承的父类都有这个方法则从左到右查到先找到谁的就用谁的方法
print(CHineseStudent.__mro__)  # 查看继承顺序
print(student.__mro__)  # 查看继承顺序

#super()函数的作用是调用父类的方法，super()函数返回的是父类对象的一个临时对象，可以用来调用父类的方法。
# 调用顺序沿着__mro_属性查找，先查找子类，再查找父类，直到找到为止。

"""
复用父类的方法
"""




