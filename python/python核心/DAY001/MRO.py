class Person1:
    def __init__(self, name,**arguments):
        self.name = name
        super().__init__(**arguments)  # 调用父类的构造方法

    def greet(self):
        return f"Hello, my name is {self.name}."


class Person2:
    def __init__(self, age,**arguments):
        self.age = age
        super().__init__(**arguments)  # 调用父类的构造方法

    def greet(self):
        return f"I am {self.age} years old."


class Person3(Person2, Person1):
    def __init__(self, name, age): 


        super().__init__(name=name,age=age)  # 调用父类Person1的构造方法

        # Person1.__init__(self, name)  # 调用父类Person1的构造方法
        # Person2.__init__(self, age)   # 调用父类Person2的构造方法

    def greet(self):
        return f"{Person1.greet(self)} {Person2.greet(self)}"  # 调用父类的方法

Alice=Person3("Alice", 30)
print(Person3.__mro__)
print(Alice.greet())  # 调用子类的方法，复用父类的方法


