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
        result = []
        
        for row in rows:
            result.append(
                OrderModel(
                    # orderNumber = 
                    # orderDate: date
                    # requiredDate: date
                    # shippedDate: date | None = None
                    # status: str
                    # comments: str | None = None
                    # customerNumber: int
                )
            )
