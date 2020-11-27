from typing import List

from fastapi import APIRouter, Depends

from supervisor.datas import Worker
from supervisor.db import RedisClient
from supervisor.utils import catch_exceptions, get_db

worker_router = APIRouter()


@worker_router.post('/worker/get/all/')
@catch_exceptions
async def get_all_workers(db: RedisClient = Depends(get_db)) -> List[Worker]:
    workers = await db.get_workers()
    return workers
