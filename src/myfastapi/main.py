from fastapi import FastAPI
from .api import router as api_router

app = FastAPI(title="MyFastAPI 企业级后台管理系统")
app.include_router(api_router)
