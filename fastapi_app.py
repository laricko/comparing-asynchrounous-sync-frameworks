import asyncio

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def some_slow_router():
    await asyncio.sleep(5)
    return 'hello world'
