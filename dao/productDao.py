from dao.utility.db import MySql
from models.product import ProductModel
from dao.RispostaModel import *

class ProductsDao():

    @classmethod
    def getProductsByName(cls, productName):
        try:
            MySql.openConnection()
            query = f"""    select * 
                            from products
                            where productName = '{productName}'"""
                        
            MySql.query(query)
            data =  MySql.getResults()
            products_list = list()
            for item in data:
                product = ProductModel(productCode= item[0], productName = item[1], productLine = item[2], productScale = item[3],
                                                productVendor = item[4], productDescription = item[5], quantityInStock = item[6],
                                                buyPrice = item[7], MSRP = item[8])
                products_list.append(product)
            return Risposta(
                risultato = products_list,
                esito = 'OK'
            )
        except Exception as error:
            return Risposta(
                risultato = error,
                esito = 'KO'
            )
        finally:
            MySql.closeConnection()