import multiprocessing
import time

def cpu_bound_task():
    total = 0
    for i in range(10_000_000):
        total += i
    print("计算完成")


if __name__ == "__main__":
    start = time.time()

    p1 = multiprocessing.Process(target=cpu_bound_task)
    p2 = multiprocessing.Process(target=cpu_bound_task())

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"耗时：{time.time() - start:.2f}")