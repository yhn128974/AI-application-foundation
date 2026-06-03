class Car:
    # 类属性
    while_number = 4
    car_id = 101

    # 构造函数,实例属性
    def __init__(self, brand, name, price, while_number):
        self.brand = brand
        self.name = name
        self.price = price
        self.while_number = while_number

    # 类函数
    def print_info(self):
        print(self.brand, self.name, self.price)
    #
    def total_price(self, discount=0.3, rate=0.5):
        """
        :param discount:
        :param rate:
        :return: real total price
        """
        return self.price * discount + self.price * (1 - rate)

    # 魔法方法
    def __str__(self):
        """
        :return: string of car info
        :param self:
        :return:
        """
        return f"{self.brand} {self.name} {self.price}"

    def __eq__(self, other):
        return self.brand == other.brand and self.name == other.name and self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price


car = Car('BMW', 'x5', 100, 2)

car2 = Car('BMW', 'x5', 90, 4)
# car.brand = 'BMW'
# car.name = 'X5'
# car.price = 100
print(car.__dict__)  # obj.dict输出对象的所有属性
car.print_info()
#
print(car.total_price(discount=0.2, rate=0.5))
# 使用默认参数
print(car.total_price())
# 定义魔法方法后对象调用免费方法进行对比，这是不在比较地址
print(car == car2)
#
print(car > car2)
#
print(car < car2)
# 满足就近原则
print(f"轮数:{car.while_number}，id:{car.car_id}")
