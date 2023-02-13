from pydantic import BaseModel
from datetime import date


class OrderModel(BaseModel):
    orderNumber: int
    orderDate: date
    requiredDate: date
    shippedDate: date | None = None
    status: str
    comments: str | None = None
    customerNumber: int
