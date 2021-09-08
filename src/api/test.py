from aiohttp import web
import asyncio

async def test(request):
    return web.Response(text="test")

async def hello(request):
    return web.Response(text="Hello, world")


async def main():
    # add stuff to the loop, e.g. using asyncio.create_task()

    app = web.Application()
    app.router.add_get('/', hello)
    app.router.add_get('/test', test)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner)    
    await site.start()

    # add more stuff to the loop, if needed

    # wait forever
    await asyncio.Event().wait()

asyncio.run(main())
