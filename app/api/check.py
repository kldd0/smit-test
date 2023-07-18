from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["Healthcheck"])

@router.get("")
async def check() -> str:
    return "Pong"