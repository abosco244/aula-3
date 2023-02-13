from dao.utility.db import MySql
from fastapi import FastAPI
from dao.officesDao import officesDao
from models.office import OfficeModel
from dao.ordersDao import OrdersDao
from dao.orderDetailDao import Order_details_modelDao
from dao.EmployeeDao import EmployeeDao

app = FastAPI()

@app.post('/offices/add')
async def add_office(oggetto: OfficeModel):
    return officesDao.addOffice(oggetto)

@app.get('/orders/{customer_number}')
async def get_orders(customer_number: int):
    return OrdersDao.getAllOrdersByCustomerNumber(customer_number)

@app.get('/orderdetails/')
async def get_all_orderdetails():
    return Order_details_modelDao.get_all_orderdetails()

@app.get('/emplyees/{office_city}')
async def get_employees(office_city: str):
    return EmployeeDao.getEmployeesByCity(office_city)