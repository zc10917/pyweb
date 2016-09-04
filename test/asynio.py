import asyncio
import time

@asyncio.coroutine
def hello():
    print("Hello world!"+str(time.time()))
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!"+str(time.time()))

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(asyncio.wait([hello(),hello()]))
loop.close()