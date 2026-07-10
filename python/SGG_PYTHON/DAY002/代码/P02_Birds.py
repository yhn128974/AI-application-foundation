"""
    愤怒的小鸟案例
"""
from abc import abstractmethod, ABC


# 鸟的基类
class Birds(ABC):
    def __init__(self,name,color,skill_desc):
        self.name = name
        self.color = color
        self.skill_desc = skill_desc

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def call(self):
        pass

    def use_skill(self):
        print(f"{self.name}使用了技能:{self.skill_desc}")


class RedBirds(Birds):
    def __init__(self):
        super().__init__("红火","红色","正常飞行攻击")

    def fly(self):
        print("正常飞行")

    def call(self):
        print("吱吱")


class YellowBirds(Birds):
    def __init__(self):
        super().__init__("黄蜂", "黄色色", "加速飞行攻击")

    def fly(self):
        print("加速飞行")

    def call(self):
        print("呀呀")


class BlueBirds(Birds):
    def __init__(self):
        super().__init__("蓝冰", "蓝色", "分裂多只进行攻击")

    def fly(self):
        print("分裂飞行")

    def call(self):
        print("滋滋")


class Obstacle:
    def __init__(self,name,strength):
        self.name = name
        self.strength = strength

    def be_attacked(self,bird):
        print(f"{bird.name}向{self.name}发起了攻击")
        bird.fly()
        bird.call()
        bird.use_skill()

        # 判断当前发起攻击的鸟是哪类
        # isinstance（self,class）判断当前对象是否是对应的类型
        if isinstance(bird, RedBirds):
            damage = 50
        elif isinstance(bird, YellowBirds):
            damage = 80
        else:
            damage = 30 * 3

        self.strength -= damage

        if self.strength <= 0:
            print(f"{self.name}已被摧毁")
        else:
            print(f"{self.name}还剩{self.strength}生命值")

r1 = RedBirds()
o1 = Obstacle("木头房子",100)
o1.be_attacked(r1)
y1 = YellowBirds()
o1.be_attacked(y1)