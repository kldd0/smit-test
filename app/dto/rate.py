import pydantic as pd


class Rate(pd.BaseModel):
    cargo_type: str
    rate: float