import time
import asyncio
import aiohttp
import aiofiles
import aiohttp
import aiohttp_requests
async def func1():  # 调用协程函数的那个函数也需要是一个协程函数
    print(1)
    await func2()  # 调用协程函数的时候要在前面加await
    print(2)
async def func2():
    print(3)

c = func1()
loop = asyncio.get_event_loop() # 创建事件循环
task1 = loop.create_task(c) 
print(task1)
loop.run_until_complete(task1)