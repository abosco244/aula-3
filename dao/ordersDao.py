from utility.db import MySql
from models.order import OrderModel

class OrdersDao:
    
    @classmethod
    def getAllOrdersByCustomerNumber(cls, customer_number):
        MySql.openConnection()

        try:
            MySql.query(
                f'''SELECT *
                    FROM orders o
                    WHERE o.customerNumber = {customer_number}'''
            )
            rows = MySql.getResults()
            result = []
            
            for row in rows:
                result.append(
                    OrderModel(
                        orderNumber = row[0],
                        orderDate = row[1],
                        requiredDate = row[2],
                        shippedDate = row[3],
                        status = row[4],
                        comments = row[5],
                        customerNumber = row[6]
                    )
                )
            return {
                "esito": "OK",
                "risultato": result
            }
        except Exception as ex:
            return {
                "esito": "KO",
                "risultato": ex
            }
        finally:
            MySql.closeConnection()
