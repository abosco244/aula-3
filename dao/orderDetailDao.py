from dao.utility.db import MySql
from models.order_details import Order_details_model

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
            
            MySql.closeConnection()
            
            for item in data:
                orderdetail = Order_details_model(orderNumber= item[0], productCode = item[1], quantityOrdered = item[2], 
                                               priceEach = item[3], orderLineNumber = item[4])
                orderdetails_list.append(orderdetail)
                
        except Exception as e:
            print(e)
            
        return {"orderdetails": orderdetails_list}
'''''' 

