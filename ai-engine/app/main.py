from fastapi import FastAPI
from app.api.v1 import router

app = FastAPI(title="DeepShieldX AI Engine")

app.include_router(router, prefix="/v1")
