class Student:
    def __init__(self, name, age, math_score, english_score, china_score):
        self.name = name
        self.age = age
        self.math_score = math_score
        self.english_score = english_score
        self.china_score = china_score

    def __str__(self):
        return f"name:{self.name},age:{self.age},math:{self.math_score},english:{self.english_score},china:{self.china_score}"

    def update(self, china_score=None, math_score=None, english_score=None):
        self.math_score = math_score
        self.english_score = math_score
        self.china_score = china_score


Alice = Student('Alice', 20, 100, 100, 100)
print(Alice.__str__())

Alice.update(90, 90, 90)
print(Alice.__str__())


class StudentManger:
    system_version = '1.0.0'
    system_name = 'student Manger System'

    def __init__(self):
        self.students = []

    #
    def add(self):
        """
        :return:
        """
        name = input('enter name')
        for student in self.students:
            if student.name == name:
                print("student name already exist")
                return
        age = input('enter age')
        math_score = input('enter math score')
        english_score = input('enter english score')
        china_score = input('enter china score')
        self.students.append(Student(name, age, math_score, english_score, china_score))

    #
    def set(self):
        """
        :return:
        """
        name = input('enter name')
        for student in self.students:
            if student.name == name:
                math_score = input('enter math score')
                english_score = input('enter english score')
                china_score = input('enter china score')
                student.update(china_score, math_score, english_score)
                print(student.__str__())
                return
        print('this name is not exist')

    #
    def remove(self, name):
        """
        :param name:
        :return:
        """
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("student was removed")
                return
        print("student name doesn't exist")

    #
    def showAll(self):
        """
        :return:
        """
        for student in self.students:
            print(student.__str__())

    #
    def show(self):
        """
        :return:
        """
        name = input('enter name: ')
        for student in self.students:
            if student.name == name:
                print(student.__str__())
                return
        print("student name doesn't exist")


currentManger = StudentManger()
currentManger.students = [Student('Alice', 20, 100, 100, 100)]
# currentManger.add()
# currentManger.remove('Alice')
# currentManger.show()
# currentManger.set()
currentManger.showAll()







