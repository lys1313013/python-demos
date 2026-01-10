import asyncio


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"


async def main():
    task_list = [
       asyncio.create_task(func(), name="n1"),
       asyncio.create_task(func(), name="n2")
    ]
    print("main 结束")
    done, pedding = await asyncio.wait(task_list, timeout=None)
    print(done)

asyncio.run(main())