from fastapi import FastAPI
from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from users.router import router as users_router
from messages.router import router as messages_router
from messages.ws_router import router as ws_messages_router
from templates.router import router as templates_router

import global_config

app = FastAPI()

app.mount(global_config.STATIC_PATH, StaticFiles(directory=global_config.STATIC_DIR), name="static")
app.mount(global_config.MEDIA_PATH, StaticFiles(directory=global_config.MEDIA_DIR), name="media")

app = FastAPI(version='1.0',
              title='WorldConnect')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://127.0.0.1:637")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


app.include_router(ws_messages_router, prefix='/ws', tags=['ws'])
app.include_router(users_router, prefix='/api/v1/users', tags=['rest'])
app.include_router(messages_router, prefix='/api/v1/messages', tags=['rest'])
app.include_router(templates_router, tags=['templates'])
