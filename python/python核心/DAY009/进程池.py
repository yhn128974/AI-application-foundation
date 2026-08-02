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
    for p in range(process_num):
        # 阻塞式
        # pool.apply(func)
        # 非阻塞式
        pool.apply_async(func)

    # 	close()：阻止后续任务提交到进程池，
    # 当所有任务执行完成后，工作进程会退出。
    pool.close()
    #join()：阻塞主进程，等待工作进程结束。
    # 调用 join() 前必须先调用 close() 或者 terminate()。
    pool.join()
    print("end")
