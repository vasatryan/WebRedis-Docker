from fastapi import FastAPI
import redis
import os

app = FastAPI()

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT',6379))


r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.post("/incremtn")
async def inc_cont():
    count = r.incr('count')
    return {'count': count}