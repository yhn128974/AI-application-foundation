class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def getInfo():
        return f'{self.name} is my name ,and age is{self.age},and live in {self.address}'

# 获取模块的所有成员
print(dir(Person('alice',200,'cq')))