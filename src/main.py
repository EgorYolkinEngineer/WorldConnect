from fastapi import FastAPI
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from users.router import router as users_router
from messages.router import router as messages_router
from messages.websockets import router as ws_messages_router
import messages.models

app = FastAPI(version='1.0',
              title='WorldConnect')


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://127.0.0.1:637")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


app.include_router(ws_messages_router, prefix='/ws', tags=['ws'])
app.include_router(messages_router, prefix='/messages', tags=['rest'])
app.include_router(users_router, prefix='/users', tags=['rest'])
