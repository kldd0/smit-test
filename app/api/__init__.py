from fastapi import APIRouter

from . import check, rate

router = APIRouter(prefix="/api")
router.include_router(check.router)
router.include_router(rate.router)