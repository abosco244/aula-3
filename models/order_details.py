from pydantic import BaseModel

class Order_detail_model(BaseModel):
    order_number: int | None = None
    product_code: str
    quantity_ordered: int
    price_each: float
    order_line_number: int

class Order_details_model(BaseModel):
    orderdetails: list[Order_detail_model]