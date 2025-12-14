from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.get("/hello")
async def hello_endpoint():
    return {"message": "Hello from FastAPI!"}

