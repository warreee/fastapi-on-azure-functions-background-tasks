import logging

import fastapi
import asyncio

from fastapi import BackgroundTasks

app = fastapi.FastAPI()


def write_notification():
    print("Writing to file")
    with open("log.txt", mode="w") as email_file:
        # loop over 1 to 10000 and write to file
        content = ""
        for i in range(1, 100000000):
            # write to file
            content += f"notification for {i}: some message here\n"
        email_file.write(content)
    print("Writing to file completed")


@app.get("/send-notification")
def send_notification(background_tasks: BackgroundTasks):
    print('Going to send notifications in the background')
    background_tasks.add_task(write_notification)
    print("Notification sent in the background")
    return {"message": "Notifications sent in the background"}


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
