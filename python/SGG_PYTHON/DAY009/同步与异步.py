import os
import time
import multiprocessing

# 打印10个数字,每次间隔0.5秒
def func():
    for i in range(10):
        print(os.getpid(), i)
        time.sleep(0.5)

if __name__ == "__main__":
    # 指定进程池大小
    process_num = 5
    pool = multiprocessing.Pool(process_num)
    # 调用进程内容 5个进程 每个次打印-0-9
    for p in range(3):
        # 阻塞式 同步等待一个个执行
        # pool.apply(func)
        # 非阻塞式，async异步执行同时开始不等待上一个的执行
        pool.apply_async(func)

    # 等待所有其他进程完毕之后再结束主进程，如果不加会导致主进程结束之后其他进程也被结束
    pool.close()
    pool.join()
    print("end")



