import asyncio


async def func():
    print("执行到这了")


result = func()
#loop = asyncio.get_event_loop()
#loop.run_until_complete(result)
asyncio.run(result)