from dao.utility.db import MySql
from models.order_details import*
from utility.db import MySql



class Order_details_modelDao:

    @classmethod
    def get_all_orderdetails(cls):
        
        MySql.openConnection()
        MySql.query("SELECT * FROM orderdetails")
        laList = MySql.getResults()
        MySql.closeConnection()
        results = []
        try:
            for i in laList:
                results.append(Order_details_model(orderNumber= i[0], productCode = i[1], quantityOrdered = i[2],
                priceEach = i[3],orderLineNumber= i[4]))
                return results  
                          
        except Exception :
            return {"L'OPERAZIONE NON è ANDATA A BUON FINE"}




