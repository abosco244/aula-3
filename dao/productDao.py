from dao.utility.db import MySql
from models.product import ProductModel

class ProductsDao():
    def getProductsByName(self, productName : str):
        try:
            MySql.openConnection()
            
            query = f"""    select * 
                            from products
                            where productName = '{productName}'"""
                        
            MySql.query(query)
            data =  MySql.getResults()
            MySql.closeConnection()
            products_list = list()
            for item in data:
                product = ProductModel(productCode= item[0], productName = item[1], productLine = item[2], productScale = item[3],
                                                productVendor = item[4], productDescription = item[5], quantityInStock = item[6],
                                                buyPrice = item[7], MSRP = item[8])
                products_list.append(product)
            return products_list
        except Exception as e:
            print(e)