import trio


async def child_task(i):
    print(f"任务{i}开始执行")
    await trio.sleep(1)
    print(f"任务{i}执行结束")


async def main():
    async with trio.open_nursery() as nursery:
        for i in range(10):
            nursery.start_soon(child_task, i)
        print("所有任务执行完成")


trio.run(main)
