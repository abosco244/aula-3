from pydantic import BaseModel

class EmployeeModel(BaseModel):
    employee_number: int | None = None
    last_name: str
    first_name: str
    extension: str
    email: str
    office_code: int
    reports_to: int | None = None
    job_title: str
