from dao.utility.db import MySql
from models.order import OrderModel

class OrdersDao:
    
    @classmethod
    def getAllOrdersByCustomerNumber(cls, customer_number):
        MySql.openConnection()
        MySql.query(
            f'''SELECT *
                FROM orders o
                o.customerNumber = {customer_number}'''
        )
        rows = MySql.getResults()
        MySql.closeConnection()

        for row in rows:
            test = True
            pass
