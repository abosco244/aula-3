from dao.utility.db import MySql
from models.customer import *

class CustomersDao:

    @classmethod
    def getCustomerByCustomerNumber(cls, customer_number):
        try:
            MySql.openConnection()
            MySql.query(f"SELECT * FROM Customers WHERE customerNumber = {customer_number}")
            data = MySql.getResults()  
            output = list()
            for el in data:
                output = (customer(customerNumber = el[0], 
                                        customerName = el[1], 
                                        contactLastName=  el[2], 
                                        contactFirstName = el[3],
                                        phone = el[4], 
                                        addressLine1 = el[5], 
                                        addressLine2=  el[6], 
                                        city = el[7],
                                        state = el[8], 
                                        postalCode = el[9], 
                                        country=  el[10], 
                                        salesRepEmployeeNumber = el[11],
                                        creditLimit = el[12]
                ))
            MySql.closeConnection()
        except Exception as error:
            print(error)
        return output
        