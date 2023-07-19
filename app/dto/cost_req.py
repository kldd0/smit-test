import pydantic as pd


class CostRequest(pd.BaseModel):
    cargo_type: str
    insurance_cost: float