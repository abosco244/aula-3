from dao.productDao import ProductsDao
from dao.utility.db import MySql
from fastapi import FastAPI
from dao.customersDao import CustomersDao
from dao.EmployeeDao import EmployeeDao
from dao.officesDao import OfficesDao
from dao.orderDetailDao import OrderDetailsDao

'''
MySql.openConnection()
MySql.query("select * from orders")
MySql.closeConnection()
'''
app = FastAPI()

# SERVIZI GET

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