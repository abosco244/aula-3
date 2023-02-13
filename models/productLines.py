from pydantic import BaseModel

class ProductLinesModel (BaseModel):
    productLine: str
    textDescription: str
    htmlDescription: str | None = None
    image: str | None = None 