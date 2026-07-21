import threading
import time



# def func():
#     flag=0
#     while True:
#         print(f"当前线程{threading.current_thread().name}",f"{flag}"*5)
#         flag=flag^1
#         time.sleep(1)

# if __name__=='__main__':
#     t1=threading.Thread(target=func)
#     t2=threading.Thread(target=func)

#     t1.start()
#     t2.start()


# # 通过继承线程类定义线程对象
# class Worker(threading.Thread):
#     # 重写run方法
#     def run(self):
#         flag=0
#         while True:
#             print(f"当前线程{threading.current_thread().name}",f"{flag}"*5)
#             flag=flag^1
#             time.sleep(1)

# if __name__=='__main__':
#     t1=Worker(name='t1')
#     t2=Worker(name='t2')
#     t1.start()
#     t2.start()

#     print('~~~end~~')


# 通过线程池创建线程
import concurrent.futures

def func(tname):
    global word
    for i, char in enumerate(word):
        word[i] = chr(ord(char) ^ 1)
        print(f"{tname}: {word}\n", end="")
    return word

if __name__ == "__main__":
    word = list("idmmn!vnsme")
    # 使用 with 语句来确保线程被迅速清理
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future1 = executor.submit(func, "线程1")
        future2 = executor.submit(func, "线程2")
        future3 = executor.submit(func, "线程3")
        # word = future1.result()
        # word = future2.result()
        # word = future3.result()

        
print("".join(word))  # hello world







