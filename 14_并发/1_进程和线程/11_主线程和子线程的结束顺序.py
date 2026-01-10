import threading
import time


def work():
    for i in range(10):
        print("工作...")
        time.sleep(0.2)


if __name__ == '__main__':
    sun_thread = threading.Thread(target=work)
    # 设置为守护线程
    # sun_thread = threading.Thread(target=work, daemon=True)
    sun_thread.start()

    time.sleep(1)
    print("主线程结束了...")

# 结论：主线程会等待所有的子线程执行结束后再结束
