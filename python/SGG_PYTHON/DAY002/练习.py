import types
# def revers(number):
#     if number>0:
#         current_str=str(number)
#         # 切片反转
#         current_str=current_str[::-1]
#         print(current_str)
#     else:
#         current_str=str(-number)
#         # 切片反转
#         current_str=current_str[::-1]
#         print(-int(current_str))
# revers(-4567)

# students={
#     "Alice":{
#         "math":90,
#         "English":80,
#         "Science":70
#     },

#     "Ben":{
#       "math":90,
#         "English":80,
#         "Science":70
#     },

#     "peter":{
#         "math":90,
#         "English":80,
#         "Science":70
#     }

# }

# def cal_avg_score():
#     new_dict={}
#     for name,item in students.items():
#         count=sum(item.values())
#         avger_score=count/len(item)
#         new_dict[name]=avger_score
#     print(new_dict)

# cal_avg_score()



class Person:
    def __init__(self,age):
        self.age=age

def get_name(self):
    print(self.age)

Alice=Person(100)
Alice.name='Alice'
print(f"{Alice.name}+{Alice.age}")

Alice.get_name=types.MethodType(get_name,Alice)
Alice.get_name()