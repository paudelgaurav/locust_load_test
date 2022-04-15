from imp import reload
import time

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/ping')
def ping():
    return 'pong'


@app.get('/slow-ping')
def slow_ping():
    time.sleep(3)
    return 'Slow Ping'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
