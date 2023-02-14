
<<<<<<< HEAD
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
=======
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
>>>>>>> 0637f5ee41af4809176a890894f21e896fff6ee7
