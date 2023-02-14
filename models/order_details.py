from pydantic import BaseModel

<<<<<<< HEAD
from pydantic import BaseModel

class Order_details_model(BaseModel):
    orderNumber: int 
    productCode: str
    quantityOrdered: int
    priceEach: float
    orderLineNumber: int
=======

      
class Order_details_model(BaseModel):
          orderNumber: int 
          productCode: str
          quantityOrdered: int
          priceEach: float
          orderLineNumber: int

class Order_details_model(BaseModel):
    orderdetails: list[Order_details_model]
>>>>>>> 0637f5ee41af4809176a890894f21e896fff6ee7
