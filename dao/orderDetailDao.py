from dao.utility.db import MySql
from models.order_details import Order_details_model
from dao.RispostaModel import *

class OrderDetailsDao():
    def getAllOrdersDetailsByStatus(self, status: str):
        query = f"""    select OD.orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber
                        from orderdetails OD, orders O
                        where OD.orderNumber = O.orderNumber
                        and status = '{status}'"""
        orderdetails_list = list()
        try:
            MySql.openConnection()
            MySql.query(query)
            data =  MySql.getResults()
            orderdetails_list = list()        
            for item in data:
                orderdetail = Order_details_model(orderNumber= item[0], productCode = item[1], quantityOrdered = item[2], 
                                               priceEach = item[3], orderLineNumber = item[4])
                orderdetails_list.append(orderdetail)
            return Risposta(
                risultato = {"orderdetails": orderdetails_list},
                esito = 'OK'
            )
        except Exception as error:
            return Risposta(
                risultato = error,
                esito = 'KO'
            )
        finally:
            MySql.closeConnection()

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