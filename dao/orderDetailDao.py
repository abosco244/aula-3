from dao.utility.db import MySql
from models.order_details import *
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
                orderdetail = Order_detail_model(order_number= item[0], product_code = item[1], quantity_ordered = item[2], 
                                               price_each = item[3], order_line_number = item[4])
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