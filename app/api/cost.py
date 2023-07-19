from fastapi import APIRouter
from typing import List
from datetime import date

from app.dto.cost_req import CostRequest

router = APIRouter(prefix="/cost", tags=["Cargo rate"])


@router.get("")
async def get_cost(request: CostRequest):
    try:
        print(request)
        curr_cargo_rate = 1.5 # getting from db
        return {"cost": curr_cargo_rate * request.insurance_cost}
    except Exception as e:
        print(e)
        return "Failed getting cost"