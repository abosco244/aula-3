from pydantic import BaseModel

class OfficeModel (BaseModel):
  officeCode : str 
  city : str
  phone : str
  addressLine1 : str
  addressLine2 : str | None = None
  state : str | None = None
  country : str
  postalCode : str
  territory : str

