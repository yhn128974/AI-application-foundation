class Gird:
    def __init__(self,name,color,skill_description):
        self.name=name
        self.color=color
        self.skill_description=skill_description
    def fly(self):
        print(f"{self.name} can fly in the sky.")
    def call(self):
        print(f"{self.name} can call in the sky.")
    def use_skill(self):
        print(f"{self.name} can use skill: {self.skill_description}.")  
    
class RedBirds(Gird):
    def __init__(self,name,color,skill_description):
        super().__init__(name,color,skill_description)

    def fly(self):
        print(f" RedBirds {self.name} can fly in the sky.")

    def call(self):
        print(f"RedBirds {self.name} can call in the sky.")

    def use_skill(self):
        print(f" RedBirds {self.name} can use skill: {self.skill_description}.")

class BlueBirds(Gird):

    def __init__(self,name,color,skill_description):
        super().__init__(name,color,skill_description)

    def fly(self):
        print(f" BlueBirds {self.name} can fly in the sky.")

    def call(self):
        print(f"BlueBirds {self.name} can call in the sky.")

    def use_skill(self):
        print(f" BlueBirds {self.name} can use skill: {self.skill_description}.")

class YellowBirds(Gird):

    def __init__(self,name,color,skill_description):
        super().__init__(name,color,skill_description)

    def fly(self):
        print(f" YellowBirds {self.name} can fly in the sky.")

    def call(self):
        print(f"YellowBirds {self.name} can call in the sky.")

    def use_skill(self):
        print(f" YellowBirds {self.name} can use skill: {self.skill_description}.")

class Obstacle:
    def __init__(self,name,strength):
         self.name=name
         self.strength=strength


    def attacked(self,bird:Gird):
        if bird.name=='YellowBirds':
            bird.use_skill()
            print('得到3分')
        elif bird.name=='BlueBirds':
            bird.use_skill()
            print('得到2分')
        elif bird.name=='RedBirds':
            bird.use_skill()
            print('得到一分')
        else:
            print('未得分')


obs=Obstacle('飞行','100')
newYellowGird=YellowBirds('YellowBirds','yellow','分裂')

# print(newYellowGird.name)
# newYellowGird.use_skill()
obs.attacked(newYellowGird)



            