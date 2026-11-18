from datetime import datetime, timezone
from pydantic import BaseModel, Field, BeforeValidator
from typing import Dict, Literal, Optional, Annotated
from bson import ObjectId

PyObjectId = Annotated[str, BeforeValidator(str)]

class StockInfo(BaseModel):
    total: int = Field(default=0, ge=0)
    min_alert: int = Field(default=5, ge=0)
    by_warehouse: Dict[str, int] = Field(default_factory=dict)

class ProductSchema(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias='_id')
    sku: str = Field(..., min_length=3, max_length=50)
    name: str = Field(..., min_length=1, max_length=150)
    price: float = Field(..., ge=0)
    stock: StockInfo = Field(default_factory=StockInfo)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    model_config = {"populate_by_name": True}

class StockMovementSchema(BaseModel):
    id: Optional[PyObjectId] = Field(default=None, alias='_id')
    product_id: PyObjectId
    sku: str
    warehouse: str
    type: Literal['IN', 'OUT', 'ADJUSTMENT']
    quantity: int = Field(..., gt=0)
    reason: str
    creatred_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
