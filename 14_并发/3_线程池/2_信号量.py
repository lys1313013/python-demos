import time
from concurrent.futures import ThreadPoolExecutor
from threading import Semaphore

# 最多允许 2（运行）+ 3（排队）= 5 个任务存在
sem = Semaphore(2)


def task(i):
    print(f"这是第{i}个任务")
    time.sleep(2)


def safe_submit(executor, fn, *args):
    if sem.acquire(blocking=False):
        future = executor.submit(fn, *args)    # 任务完成后释放许可
        future.add_done_callback(lambda f: sem.release())
    else:
        print("任务已满，暂时停止执行")


with ThreadPoolExecutor(max_workers=2) as exe:
    for i in range(20):
        time.sleep(0.5)
        safe_submit(exe, task,i)  # 超过5个时会阻塞在此
