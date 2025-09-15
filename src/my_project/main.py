from fastapi import FastAPI
from .config import settings

app = FastAPI(title="MyFastAPI 企业级后台管理系统")

@app.get("/")
def read_root():
    return {"msg": "Welcome to MyFastAPI!"}