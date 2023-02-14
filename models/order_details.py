from pydantic import BaseModel


      
class Order_details_model(BaseModel):
          orderNumber: int 
          productCode: str
          quantityOrdered: int
          priceEach: float
          orderLineNumber: int

class Order_details_model(BaseModel):
    orderdetails: list[Order_details_model]