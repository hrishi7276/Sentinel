from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SymbolCreate(BaseModel):
    symbol: str
    exchange: str
    is_active: bool = True


class SymbolResponse(BaseModel):
    id: int
    symbol: str
    exchange: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)