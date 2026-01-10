import asyncio


async def func():
    print("执行到这")
    response = await asyncio.sleep(2)
    print("结束", response)


asyncio.run(func())
