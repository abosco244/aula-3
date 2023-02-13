from dao.utility.db import MySql
from models.order_details import *

class Order_details_modelDao:

    @classmethod
    def get_all_orderdetails(cls):
        
        MySql.openConnection()
        try:
            results = []
            MySql.query("SELECT * FROM orderdetails")
            laList = MySql.getResults()
            for i in laList:
                results.append(Order_details_model(orderNumber= i[0], productCode = i[1], quantityOrdered = i[2],
                priceEach = i[3],orderLineNumber= i[4]))
            return {"esito": "OK",
                    "risultato": results}
        except Exception as ex:
            return {"esito": "KO",
                    "risultato": ex}
        finally:
            MySql.closeConnection()