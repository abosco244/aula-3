from dao.utility.db import MySql
from fastapi import FastAPI
from customersDao import customersDao
from EmployeeDao import EmployeeDao
from officesDao import OfficesDao
from orderDetailDao import OrderDetailsDao
from RispostaModel import Risposta

'''
MySql.openConnection()
MySql.query("select * from orders")
MySql.closeConnection()
'''
app = FastAPI()

# SERVIZI GET

@app.get("/get-customer/{customer_number}")
async def get_customer(customer_number: str):
    if customersDao().getCustomerByCustomerNumber(customer_number):
        return Risposta(risultato=customersDao().getCustomerByCustomerNumber(customer_number), esito="OK")
    else:
        return Risposta(risultato=None, esito="KO")

@app.get("/get-employee/{employee_number}")
async def get_employee(employee_number: str):
    if EmployeeDao().getEmployeeByEmployeeNumber(employee_number):
        return Risposta(risultato=EmployeeDao().getEmployeeByEmployeeNumber(employee_number), esito="OK")
    else:
        return Risposta(risultato=None, esito="KO")

@app.get("/get-office/{office_code}")
async def get_office(office_code: int):
    if OfficesDao().getOfficeByOfficeCode(office_code):
        return Risposta(risultato=OfficesDao().getOfficeByOfficeCode(office_code), esito="OK")
    else:
        return Risposta(risultato=None, esito="KO")

@app.get("/get-orderdetails-by-status/{order_status}")
async def get_orderdetails_by_status(order_status: str):
    if OrderDetailsDao().getAllOrdersDetailsByStatus(order_status):
        return Risposta(risultato=OrderDetailsDao().getAllOrdersDetailsByStatus(order_status), esito="OK")
    else:
        return Risposta(risultato=None, esito="KO")