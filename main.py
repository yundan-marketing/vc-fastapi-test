from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.get("/hello")
async def hello_endpoint():
    return {"message": "Hello from FastAPI!"}


@app.get("/random")
async def random_number():
    return {"random_number": random.randint(1, 100)}


@app.get("/random-color")
async def random_color():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return {"color": color}

