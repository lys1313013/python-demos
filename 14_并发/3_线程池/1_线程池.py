import threading
from concurrent.futures import ThreadPoolExecutor
import time


def task(n):
    print(f" {threading.current_thread()} 执行了任务{n}")
    time.sleep(0.5)


with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(100):
        executor.submit(task, i)
