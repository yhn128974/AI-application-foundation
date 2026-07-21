"""
    该案例演示了通过队列实现了进程之间的通信
"""
import multiprocessing
import os
import random
import time


# 向队列中放入数据
def func1(queue):
    while True:
        num = random.randint(1, 50)
        queue.put(num)
        print(f"进程{os.getpid()}向队列中放入了元素{num}")
        time.sleep(0.3)

# 从队列中取数据
def func2(queue):
    while True:
        num = queue.get()
        print(f"进程{os.getpid()}从队列中取出了元素{num}")
        time.sleep(0.3)

if __name__ == '__main__':
    # queue = multiprocessing.Queue() 定义进程间的共享数据
    queue = multiprocessing.Manager().Queue()

    # 定义独立进程方案
    # p1 = multiprocessing.Process(target=func1, args=(queue,))
    # p2 = multiprocessing.Process(target=func2, args=(queue,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()


    # 进程池方案
    pool=multiprocessing.Pool(2)
    pool.apply_async(func1,args=(queue,))
    pool.apply_async(func2,args=(queue,))
    
    pool.close()
    pool.join()



    print("主进程结束！")
