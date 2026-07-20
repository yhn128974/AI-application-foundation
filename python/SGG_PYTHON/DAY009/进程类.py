
import os
from multiprocessing import Process

class Worker(Process):
    def run(self):
        print(f"当前进程id{os.getpid()},父进程为{os.getppid()}")

if __name__=="__main__":
        p1=Worker()
        p2=Worker()
        # 启动进程
        p1.start()
        p2.start()
        print(f"当前进程id{os.getpid()},父进程为{os.getppid()}")
