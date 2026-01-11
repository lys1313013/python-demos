import multiprocessing
import time
import os


def sing(num, name):
    print(f"唱歌进程的pid：{os.getpid()}")
    print(f"唱歌进程的父进程 pid：{os.getppid()}")
    for i in range(num):
        print(f"{name}唱歌。。。")
        time.sleep(0.5)


def dance(num, name):
    print(f"跳舞进程的pid：{os.getpid()}")
    print(f"跳舞进程的父进程 id：{os.getppid()}")
    for i in range(num):
        print(f"{name}跳舞。。。")
        time.sleep(0.5)


if __name__ == "__main__":
    print(f"主进程{os.getpid()}")
    singer = multiprocessing.Process(target=sing, args=(3, "张三",))
    dancer = multiprocessing.Process(target=dance, kwargs={"num": 2, "name": "李四"})
    singer.start()
    dancer.start()
    singer.join()
    dancer.join()
