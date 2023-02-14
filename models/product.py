from pydantic import BaseModel

class ProductModel (BaseModel):
    productCode: str
    productLine: str
    productScale: str 
    productName: str 
    productVendor: str 
    productDescription: str 
    quantityInStock: int 
    buyPrice: str 
    MSRP: str
    firstInit: bool=True                   