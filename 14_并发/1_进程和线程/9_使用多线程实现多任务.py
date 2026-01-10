import threading
import time


def sing():
    for i in range(3):
        print("唱歌。。。")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print("跳舞。。。")
        time.sleep(0.5)

# 创建子线程
sing_thread = threading.Thread(target=sing)
dance_thread = threading.Thread(target=dance)
# 启动线程
sing_thread.start()
dance_thread.start()