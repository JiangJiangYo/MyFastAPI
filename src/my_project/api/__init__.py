from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"msg": "Welcome to MyFastAPI 企业级后台"}