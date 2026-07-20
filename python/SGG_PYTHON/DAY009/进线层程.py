import multiprocessing
import time
# 写文件
def write_file():
    print(f"write_file{__name__}")
    with open("test.txt",'w') as f:
        while True:
            f.write("hello world!")
            # 系统为了避免内存与磁盘过于频繁交互设置了一个缓冲区，
            # 如果要在写的时候实时的将内存的数据写入磁盘需要使用flush方法
            f.flush()
            time.sleep(0.5)

#读文件
def read_file():
    print(f"read_file{__name__}")
    with open("test.txt",'r') as f:
        while True:
             time.sleep(0.5)
             print(f.readline())

           

# 实现边写边读
if __name__ == '__main__':
    print(f"主{__name__}")
    # multiprocessing.Process（）
    p1=multiprocessing.Process(target=write_file )
    p2=multiprocessing.Process(target=read_file )
# 启动进程
    p1.start()
    p2.start()

print("主进行执行完毕")


