import threading
import time
# 受限于 GIL, 多线程并不能真正实现并行, 只能并发执行


def cpu_bound_task():
    total = 0
    for i in range(10_000_000):
        total += i
    print("计算完成")


if __name__ == "__main__":
    thread1 = threading.Thread(target=cpu_bound_task)
    thread2 = threading.Thread(target=cpu_bound_task)

    start = time.time()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"耗时：{time.time() - start:.2f}")