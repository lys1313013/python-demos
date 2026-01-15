import asyncio
import time
from datetime import datetime


# 简单的并发限制器实现
class SimpleLimiter:
    def __init__(self, max_concurrent):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.active_tasks = 0
        self.completed_tasks = 0

    async def __aenter__(self):
        await self.semaphore.acquire()
        self.active_tasks += 1
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.semaphore.release()
        self.active_tasks -= 1
        self.completed_tasks += 1

    def get_stats(self):
        return {
            "active": self.active_tasks,
            "completed": self.completed_tasks,
            "max_concurrent": self.max_concurrent
        }


# 模拟一个耗时的任务
async def simulate_task(task_id, duration=2):
    start_time = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 任务 {task_id} 开始执行")

    # 模拟任务执行
    await asyncio.sleep(duration)

    end_time = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 任务 {task_id} 完成，耗时: {end_time - start_time:.2f}秒")
    return f"任务 {task_id} 结果"


# 使用限制器的任务执行函数
async def execute_with_limiter(limiter, task_id, duration=2):
    async with limiter:
        return await simulate_task(task_id, duration)


# 演示无限制并发 vs 有限制并发
async def demo_unlimited_vs_limited():
    print("=== 无限制并发演示 ===")

    # 创建10个任务，无限制并发
    tasks = [simulate_task(i, 2) for i in range(10)]
    start_time = time.time()

    # 同时启动所有任务
    results = await asyncio.gather(*tasks)

    total_time = time.time() - start_time
    print(f"无限制并发总耗时: {total_time:.2f}秒")
    print(f"完成的任务数量: {len(results)}")
    print()

    print("=== 有限制并发演示 (最大并发数: 3) ===")

    # 创建限制器，最大并发数为3
    limiter = SimpleLimiter(3)

    # 创建10个任务，使用限制器
    limited_tasks = [execute_with_limiter(limiter, i, 2) for i in range(10, 20)]
    start_time = time.time()

    # 同时启动所有任务（但会被限制器控制）
    results = await asyncio.gather(*limited_tasks)

    total_time = time.time() - start_time
    stats = limiter.get_stats()

    print(f"有限制并发总耗时: {total_time:.2f}秒")
    print(f"限制器统计: {stats}")
    print(f"完成的任务数量: {len(results)}")


# 更复杂的演示：不同类型的任务使用不同的限制器
async def demo_multiple_limiters():
    print("\n=== 多限制器演示 ===")

    # 创建不同类型的限制器
    cpu_limiter = SimpleLimiter(2)  # CPU密集型任务限制为2个
    io_limiter = SimpleLimiter(4)  # IO密集型任务限制为4个
    network_limiter = SimpleLimiter(1)  # 网络请求限制为1个

    # 模拟不同类型的任务
    async def cpu_intensive_task(task_id):
        async with cpu_limiter:
            print(f"[CPU] 任务 {task_id} 开始执行")
            await asyncio.sleep(3)  # 模拟CPU计算
            print(f"[CPU] 任务 {task_id} 完成")

    async def io_intensive_task(task_id):
        async with io_limiter:
            print(f"[IO] 任务 {task_id} 开始执行")
            await asyncio.sleep(1)  # 模拟IO操作
            print(f"[IO] 任务 {task_id} 完成")

    async def network_intensive_task(task_id):
        async with network_limiter:
            print(f"[网络] 任务 {task_id} 开始执行")
            await asyncio.sleep(2)  # 模拟网络请求
            print(f"[网络] 任务 {task_id} 完成")

    # 创建混合任务
    tasks = []
    for i in range(3):
        tasks.append(cpu_intensive_task(i))
    for i in range(6):
        tasks.append(io_intensive_task(i))
    for i in range(2):
        tasks.append(network_intensive_task(i))

    # 随机打乱任务顺序
    import random
    random.shuffle(tasks)

    await asyncio.gather(*tasks)

    print(f"CPU限制器统计: {cpu_limiter.get_stats()}")
    print(f"IO限制器统计: {io_limiter.get_stats()}")
    print(f"网络限制器统计: {network_limiter.get_stats()}")


# 使用trio库的CapacityLimiter（与原始代码相同）
async def demo_trio_style():
    print("\n=== Trio风格限制器演示 ===")

    # 模拟trio.CapacityLimiter
    class CapacityLimiter:
        def __init__(self, capacity):
            self.capacity = capacity
            self._semaphore = asyncio.Semaphore(capacity)

        async def __aenter__(self):
            await self._semaphore.acquire()
            return self

        async def __aexit__(self, *args):
            self._semaphore.release()

    limiter = CapacityLimiter(2)

    async def limited_task(task_id):
        async with limiter:
            print(f"任务 {task_id} 在限制器控制下执行")
            await asyncio.sleep(1)
            print(f"任务 {task_id} 完成")

    tasks = [limited_task(i) for i in range(5)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    print("并发限制器演示程序")
    print("=" * 50)

    # 运行演示
    asyncio.run(demo_unlimited_vs_limited())
    asyncio.run(demo_multiple_limiters())
    asyncio.run(demo_trio_style())
