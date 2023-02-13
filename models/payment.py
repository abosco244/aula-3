from pydantic import BaseModel

class Payment_model(BaseModel):
    customer_number: int
    check_number: str
    payment_date: str
    amount: float