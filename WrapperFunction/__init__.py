import logging

import fastapi
import asyncio

from fastapi import BackgroundTasks

app = fastapi.FastAPI()


async def background_task():
    logging.info("Background task started")
    await asyncio.sleep(5)
    logging.info("Background task finished")


@app.get("/do_background_task")
async def do_background_task(background_tasks: BackgroundTasks):
    background_tasks.add_task(background_task)
    return {"message": "Background task started, this response should return immediately."}


@app.get("/sample")
async def index():
    return {
        "info": "Try /hello/Shivani for parameterized route.",
    }


@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }
