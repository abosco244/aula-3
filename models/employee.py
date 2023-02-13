from pydantic import BaseModel

class EmployeeModel (BaseModel):
  employeeNumber : str
  lastName : str
  firstName : str
  extension : str
  email : str
  officeCode : str
  reportsTo : str | None = None
  jobTitle : str
