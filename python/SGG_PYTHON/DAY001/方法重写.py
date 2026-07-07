class Person:
    home='earth'
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

class YellowPerson(Person):
   color='yellow'
 
   def __init__(self, name):
       Person.__init__(self, name)  # 调用父类的构造方法
# 方法重写
   def say_hello(self):
       print(f"Hello, my name is {self.name}. I am a yellow person.")
    # 不支持方法重载，后一个函数导致上一个函数被覆盖，导致上一个函数无法调用
   def say_hello(self,food):
        print(f"I am a yellow person. and I like {food}.")

Alcice=YellowPerson("Alice")
# print(Alcice.color)  # 调用子类的属性
# print(Alcice.name)  # 调用父类的属性
# print(Alcice.home)  # 调用父类的属性
print(Alcice.say_hello("apple"))  # 调用子类的方法，复用父类的方法


