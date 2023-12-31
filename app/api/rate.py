from fastapi import APIRouter
from typing import List
from datetime import date

from app.dto.rate import Rate

router = APIRouter(prefix="/rate", tags=["Cargo rate"])


@router.post("/load")
async def load_rate(input_payload: dict[date, List[Rate]]) -> str:
    try:
        print(input_payload)
        return "ok"
    except Exception as e:
        print(e)
        return "Failed loading JSON"