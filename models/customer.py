from pydantic import BaseModel

class CustomerModel (BaseModel):
  customerName : str
  customerNumber : str
  contactLastName : str
  contactFirstName : str
  phone : str
  addressLine1 : str
  addressLine2 : str | None = None
  city : str
  state : str | None = None
  postalCode : str | None = None
  country : str
  salesRepEmployeeNumber : str | None = None
  creditLimit : str

