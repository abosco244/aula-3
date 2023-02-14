from pydantic import BaseModel

class EmployeeModel(BaseModel):
    employeeNumber: int | None = None
    lastName: str
    firstName: str
    extension: str
    email: str
    officeCode: int
    reportsTo: int | None = None
    jobTitle: str
