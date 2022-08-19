# import time
from fastapi import FastAPI, requests
from api.utils.dbUtil import database
from api.auth import router as auth_router

# from utils.dbUtil import database
# from auth import router as auth_router

app = FastAPI(
    docs_url = "/docs",
    redoc_url = "/redocs",
    title = "FastAPI (Python)",
    description = "FastAPI Framework, high performance, <br>"
                  "easy to learn, fast to codem ready for production",
    version = "0.0.1",
    openapi_url = "/openapi.json"
)

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

@app.get("/hello")
def hello():
    return "Hello Programmer! Mike, I got you!"

# app.include_router(auth_router.router, tags=["Auth"])
