"""
    测试题
"""
import types
from abc import abstractmethod, ABC

"""
# 编写一个函数，接受一个整数作为参数，返回该整数的反转形式。例如，输入 123，返回 321；输入 -456，返回 -654。
def reverse_num(num):
    if num < 0:
        str_num = str(-num)
        r_num = str_num[::-1]
        return -int(r_num)
    else:
        str_num = str(num)
        r_num = str_num[::-1]
        return int(r_num)

print(reverse_num(-456))
"""
"""
# 有一个嵌套字典，存储了学生的课程成绩信息。 编写一个函数，计算每个学生的平均成绩，并返回一个新的字典，键为学生名字，值为平均成绩
students = {
    "Alice": {
        "Math": 85,
        "English": 90,
        "Science": 78
    },
    "Bob": {
        "Math": 92,
        "English": 88,
        "Science": 95
    },
    "Charlie": {
        "Math": 70,
        "English": 75,
        "Science": 80
    }
}
# 遍历出每一个学生的各科成绩
def cal_avg_score(students):
    new_dict = {}
    for std_name,course_scores  in students.items():
        total = sum(course_scores.values())
        count = len(course_scores)
        avg_score = total / count
        new_dict[std_name] = "{:.2f}".format(avg_score)

    return new_dict

print(cal_avg_score(students))
"""
"""
# 定义一个 Person 类，在类外动态地给 Person 类的一个对象添加一个 hobby 属性，值为 "reading"，并打印该属性。
class Person:
    pass

p = Person()
p.hobby = "reading"
print(p.hobby)
"""
"""
# 定义一个 Circle 类，该类有一个 radius 属性。在类外定义一个函数 calculate_area，功能是计算圆的面积（面积公式：(S = π r^2），
# 然后将这个函数动态地添加为 Circle 类的一个对象的方法，并调用该方法计算半径为 5 的圆的面积。（提示：可使用 types.MethodType）
class Circle:
    def __init__(self, radius):
        self.radius = radius

def calculate_area(self):
    return 3.14 * self.radius * self.radius
    # return (s := 3.14 * self.radius * self.radius)

c = Circle(5)

# 给实例对象动态的绑定外部的实例方法
c.calculate_area = types.MethodType(calculate_area,c)

print(c.calculate_area())
"""
"""
# 定义一个 BankAccount 类，有一个私有属性 __balance（初始余额为 0），
# 提供一个 deposit 方法用于存钱，一个 withdraw 方法用于取钱，取钱时如果余额不足则打印提示信息。
class BankAccount:
    def __init__(self):
        self.__balance = 0

    # 存钱
    def deposit(self, amount):
        if amount <= 0:
            print("存款金额不合理")
        else:
            self.__balance += amount
            print(f"存款成功,余额{self.__balance}")

    # 取钱
    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            print("取款金额不合理")
        else:
            self.__balance -= amount
            print(f"取款成功,余额{self.__balance}")

ba = BankAccount()
ba.deposit(100)
ba.withdraw(80)
"""
# 定义一个 Shape 类，有一个抽象方法 area（方法体为空）。再定义 Rectangle 类和 Circle 类继承自 Shape 类，
# 分别实现 area 方法计算矩形面积（长 × 宽）和圆的面积(pi r^2）。创建 Rectangle 和 Circle 类的对象，
# 将它们放入一个列表中，遍历列表并调用每个对象的 area 方法。

# 抽象方法：  只知道需要声明这个方法，但是方法的具体实现不能完成，可以在方法上加@abstractmethod
# 抽象类:    如果类中存在抽象方法，那么这个类就是抽象类    需要让这个类继承 ABC
# 注意：抽象类是不能被实例化的    如果子类继承了抽象父类，必须对父类中的抽象方法进行实现，如果没有实现，那么子类也属于抽象类不能被实例化
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 对父类中的抽象方法进行重写
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


r = Rectangle(100, 200)
c = Circle(5)

shape_list = [r,c]

for shape in shape_list:
    print(shape.area())
