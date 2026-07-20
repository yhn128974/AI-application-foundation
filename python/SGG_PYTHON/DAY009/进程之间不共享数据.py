import os
from multiprocessing import Process


def func(current_list):
    for i in range(10):
        current_list.append(i)
        print(f"当前进程为{os.getpid},{current_list}")

if __name__=="__main__":
    list1=[]
    p1=Process(target=func,args=(list1,))
    p2=Process(target=func,args=(list1,))

    p1.start()
    p2.start()
# 阻塞主进程，等待工作进程结束
    p1.join()
    p2.join()
    # 
    print(list1)