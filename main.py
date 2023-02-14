from fastapi import FastAPI
from models.office import OfficeModel
from dao.ordersDao import OrdersDao
from dao.productDao import ProductsDao
from dao.customersDao import CustomersDao
from dao.EmployeeDao import EmployeeDao
from dao.officesDao import OfficesDao
from dao.orderDetailDao import OrderDetailsDao

app = FastAPI()

@app.post('/offices/add')
async def add_office(oggetto: OfficeModel):
    return OfficesDao.addOffice(oggetto)

@app.get('/orders/{customer_number}')
async def get_orders(customer_number: int):
    return OrdersDao.getAllOrdersByCustomerNumber(customer_number)

@app.get('/orderdetails/')
async def get_all_orderdetails():
    return OrderDetailsDao.get_all_orderdetails()

@app.get('/employees/{office_city}')
async def get_employees(office_city: str):
    return EmployeeDao.getEmployeesByCity(office_city)

@app.get("/get-customer/{customer_number}")
async def get_customer(customer_number: int):
    return CustomersDao().getCustomerByCustomerNumber(customer_number)

@app.get("/get-employee/{employee_number}")
async def get_employee(employee_number: int):
    return EmployeeDao().getEmployeeByEmployeeNumber(employee_number)

@app.get("/get-office/{office_code}")
async def get_office(office_code: str):
    return OfficesDao().getOfficeByOfficeCode(office_code)

@app.get("/get-orderdetails-by-status/{order_status}")
async def get_orderdetails_by_status(order_status: str):
    return OrderDetailsDao().getAllOrdersDetailsByStatus(order_status)
    
@app.get("/get-products-by-name/{productName}")
async def getProductsByName(productName: str):
    return ProductsDao().getProductsByName(productName)
