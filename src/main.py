from fastapi import FastAPI
from users.router import router as users_router
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
import database

app = FastAPI(version='1.0',
              title='WorldConnect')


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://127.0.0.1:637")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


# app.include_router(websockets.router, tags=['ws'])
app.include_router(users_router, prefix='/users', tags=['rest'])
