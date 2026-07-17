"""
浅拷贝
"""
import copy

# list1 = [1, 2, 3, [100, 200, 300]]
# print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)

# list2 = copy.copy(list1)
# print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)

# list1[0] = 100  # 修改list1[0]整型元素，在赋值的时候list1[0]重新分配了内存

# print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
# print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)

# print('________________________________________________________________________')
# list1[3].append(400) #添加函数内存地址不变
# print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
# print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)

# print("________________________________________________________________________")
# # 
# list3=copy.deepcopy(list1)
# list1[0]=200
# print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
# print(id(list3), id(list3[0]), id(list3[1]), id(list3[2]), id(list3[3]), list3)

# 1.非容器类型（数字，字符串和其他"原子"类型的对象）无法拷贝（内存地址一致）
# var1=99
# print(id(var1),var1)

# var2=copy.deepcopy(var1)
# print(id(var2),var2)


# 2.元组如果只包含原子类型对象，则也不能对其进行拷贝,存储内存一致。
# 一旦包含可变类型则可进行深拷贝,内存改变
tuple1=(1,2,3,4,[100,200])
print(id(tuple1),tuple1)

tuple2=copy.deepcopy(tuple1)
print(id(tuple2),tuple2)    