# class Dog:
#     name:''
#     age:0
#     address:''
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
    
#     def bark(self):
#         return "Woof!"  

# #输出对象内容
# dog= Dog("Buddy", 3, "123 Bark Street")

# print(dog.name)
# print(dog.age)
# print(dog.address)  
# print(dog.bark())




# 动态的给实例对象添加方法
# class Person:
#     name:''
#     age:0
#     address:''
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
    
#     def drink(self):
#         return self.name + " is drinking water."


# zs=Person("张三", 20, "北京市")

# def say_hello():
#     print("Hello!")

# zs.say_hello = say_hello  # 动态添加方法
# zs.say_hello()  # 调用动态添加的方法



# import types
# # 动态添加实例方法
# class Person:
#     name:''
#     age:0
#     address:''
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
    
#     def drink(self):
#         return self.name + " is drinking water."

# # 可以被对象动态服用的要加上self参数
# def say_hello(self):
#     print("Hello!")

# #
# zs=Person("张三", 20, "北京市")
#  # 动态添加实例方法
# zs.say_hello=types.MethodType(say_hello, zs) 
# zs.say_hello()  # 调用动态添加的实例方法


"""
在定义时动态的添加一个类方法
"""
# def drink(self):
#      return self.name + " is drinking water."

# class Person:
#     name:''
#     age:0
#     address:''
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
    
#     drink=drink # 动态添加类方法

# zs=Person("张三", 20, "北京市")
# print( zs.drink())  # 调用动态添加的类方法
# # 删除对象方法
# del zs.drink  # 删除对象的drink方法
# print(zs.drink())  # 调用drink方法会报错 

"""
同slot限制类对象的属性和方法
"""
# class Person:
#     __slots__ = ['name', 'age', 'address']  # 限制类对象的属性和方法
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

# zs=Person("张三", 20, "北京市")
# zs.name = "李四"  # 可以修改属性
# zs.age = 25  # 可以修改属性
# zs.address = "上海市"  # 可以修改属性
# print(zs.name+str(zs.age)+zs.address)
# zs.phone = "123456789"  # 会报错，不能添加新的属性

"""
# 私有化属性和方法
"""
# class Girl:
#     def __init__(self, name, age):
#         self._name = name  # 私有化属性,非强制
#         self.__age = age    # 私有化属性，强制,只有类内部可以访问
#     def get_age(self):
#         return self.__age  # 通过类内部方法访问私有化属性

# Ailce=Girl("Ailce", 18)
# print(Ailce._name)  # 可以访问私有化属性
# # print(Ailce.__age)  # 会报错，不能访问私有化
# print(Ailce.get_age())  # 通过类内部方法访问私有化属性
# # 私有化通过改名实现可以通过 _类名__属性名 访问
# print(Ailce._Girl__age)

"""
常用设置私有属性和方法的方式
"""
class Girl:
    def __init__(self, name, age):
        self.name = name  # 私有化属性
        self.__age = age    # 私有化属性

    @property
    def age(self):
        if self.__age>=18:
            return 18
        else:
              return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

Alice=Girl("Alice", 16)
print(Alice.name)  # 可以访问私有化属性
print(Alice.age)  # 通过@property访问私有化属性
Alice.age = 25  # 通过@age.setter设置私有化属性
print(Alice.age)  # 通过@property访问私有化属性



