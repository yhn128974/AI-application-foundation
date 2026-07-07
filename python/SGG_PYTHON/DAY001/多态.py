
"""
多态演示
"""
class Animal:
    def move(self):
        print("动物可以移动")
class Dog(Animal):
    def move(self):
        print("狗可以跑和走")
class Snake(Animal):
    def move(self):
        print("蛇可以爬行")
class Fish(Animal):
    def move(self):
        print("鱼可以游泳") 
class Bird(Animal): 
    def move(self):
        print("鸟可以飞翔")

# 在方法的参数中使用多态
def run(animal:Animal):
    animal.move()

# 再返回值中使用多态
def get_animal(name: str) -> Animal:
    if name == "dog":
        return Dog()
    elif name == "snake":
        return Snake()
    elif name == "fish":
        return Fish()
    elif name == "bird":
        return Bird()
    else:
        raise ValueError("Unknown animal")
# 
run(Dog())  # 输出: 狗可以跑和走
run(Snake())  # 输出: 蛇可以爬行
run(Fish())  # 输出: 鱼可以游泳         
# 
get_animal("dog").move()  # 输出: 狗可以跑和走
get_animal("snake").move()  # 输出: 蛇可以爬行
get_animal("fish").move()  # 输出: 鱼可以游泳
get_animal("bird").move()  # 输出: 鸟可以飞翔

# 再声明变量时候使用多态
AnimalList = [Dog(), Snake(), Fish(), Bird()]
for animal in AnimalList:
    animal.move()  # 输出: 狗可以跑和走, 蛇可以爬行, 鱼可以游泳, 鸟可以飞翔
    