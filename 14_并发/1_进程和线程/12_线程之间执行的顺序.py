import threading
import time


def task():
    time.sleep(1)
    thread = threading.current_thread()
    print(thread)


if __name__ == '__main__':
    for i in range(5):
        sub_trhead = threading.Thread(target=task)
        sub_trhead.start()