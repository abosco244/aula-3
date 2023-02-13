from dao.utility.db import MySql
from models.customer import CustomerModel

class CustomersDao:
    
    @classmethod
    def getAllCustomers(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Customers")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(CustomerModel(customerNumber = element[0], customerName = element[1], 
                                    contactLastName = element[2],contactFirstName = element[3], 
                                    phone = element[4], addressLine1 = element[5], addressLine2 = element[6],
                                    city = element[7], state = element[8], postalCode = element[9],
                                    country = element[10], salesRepEmployeeNumber = element[11], creditLimit = element[12]))
        MySql.closeConnection()
        return results