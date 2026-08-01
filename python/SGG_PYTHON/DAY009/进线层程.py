import multiprocessing
import time


# 写文件
def write_file():
    print(f"write_file: {__name__}")
    with open("test.txt", "w", encoding="utf-8") as f:
        while True:
            f.write("hello world!\n")
            # 系统为了避免内存与磁盘过于频繁交互设置了一个缓冲区，
            # 如果要在写的时候实时的将内存的数据写入磁盘需要使用flush方法
            f.flush()
            time.sleep(0.5)


# 读文件
def read_file():
    print(f"read_file: {__name__}")
    with open("test.txt", "r", encoding="utf-8") as f:
        while True:
            time.sleep(0.5)
            line = f.readline().strip()
            if line:
                print(f"读取到: {line}")


# 实现边写边读
if __name__ == '__main__':
    print(f"主进程: {__name__}")

    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_file)

    # 设置守护进程，当主进程结束时子进程会自动退出
    p1.daemon = True
    p2.daemon = True

    # 启动进程
    p1.start()
    p2.start()

    try:
        # 保持主进程运行 5 秒，演示边写边读
        time.sleep(5)
    except KeyboardInterrupt:
        pass

    print("主进程执行完毕")



