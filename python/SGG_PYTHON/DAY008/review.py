

# class My_iterator:
#     def __init__(self,data):
#         self.data=data;
#         self.index=0;

# # 使其可迭代
#     def __iter__(self):
#         return self
        
# # 定义迭代器输出内容
#     def __next__(self):
#         if self.index==len(self.data):
#             raise StopIteration()
#         else:
#             self.index+=1;
#         return self.data[self.index-1]

# it=My_iterator([10,20,30,40])

# for item in it:
#     print(f"{item}")


# list=[]

# for i  in range(1,11,):
#     if i%2==0:
#         list.append(i)

# for item in list:
#     print(item)

# 实现一个迭代器
from collections.abc import Iterable
from collections.abc import Iterator

class MyIterator:

    def __init__(self,data):
        self.data=data
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index>=len(self.data)|self.index<0:
            raise StopIteration()
        else:
             self.index+=1
             return self.data[self.index-1]
mine=MyIterator([10,20,30,40])
print(isinstance(mine,Iterable))
print(isinstance(mine,Iterator))
for item in mine:
    print(item)





