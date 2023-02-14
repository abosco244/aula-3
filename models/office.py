from pydantic import BaseModel

class OfficeModel(BaseModel):
    office_code: int | None = None
    city: str
    phone: str
    address_line_1: str
    address_line_2: str | None = None
    state: str | None = None
    country: str
    postal_code: str
    territory: str