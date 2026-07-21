
"""
2）互斥锁的概念
某个线程要更改共享数据时，先将其锁定，此时其他线程不能更改。直到该线程释放资源，将资源的状态变成“非锁定”，其他的线程才能再次锁定该资源。互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性。
3）互斥锁的使用
可以通过 threading.Lock() 创建互斥锁。
使用 lock.acquire([blocking=True][, timeout=-1]) 来获取锁（blocking 如果为 True，线程会阻塞直到获取到锁。如果为 False，线程立即返回。获取锁成功返回 True，否则返回 False。timeout 为等待的超时时间，单位为秒。如果超时仍未获取到锁，则返回 False。）。
使用 lock.release() 释放锁。

"""
import time
import threading

def func():
    global g_num
    for _ in range(10):
        # 再循环体内部上锁确保循环内部线程隔离
        lock.acquire()  # 获取锁
        tmp = g_num + 1
        # 不上锁执行时休眠会导致安全问题
        # time.sleep(0.01)
        g_num = tmp
        lock.release()  # 释放锁
        print(f"{threading.current_thread().name}: {g_num}\n", end="")
       
def func2():
    global g_num2
    # 3个线程干活无法明确每个线程会干几次

    while True:
        lock.acquire()
        if g_num2<=0:
            lock.release()
            break
        else:
            g_num2-=1
            time.sleep(0.1)
            print(f"{threading.current_thread().name}卖出了1张票，还剩余{g_num2}张票")
            lock.release()


if __name__ == "__main__":
    lock=threading.Lock()
    g_num = 0
    g_num2=100
    # threading.Thread()方法创建线程
    threads = [threading.Thread(target=func2,name=f"线程{i}")for i in range(3)]
    [t.start() for t in threads ]
    [t.join() for t in threads]
    print(g_num)  # 30
