from dao.utility.db import MySql
from fastapi import FastAPI
from dao.officesDao import officesDao
from dao.ordersDao import OrdersDao
from models.office import OfficeModel

app = FastAPI()

@app.post('/offices/add')
async def add_office(oggetto: OfficeModel):
    return officesDao.addOffice(oggetto)

@app.get('/orders/{customer_number}')
async def get_orders(customer_number: int):
    return OrdersDao.getAllOrdersByCustomerNumber(customer_number)
