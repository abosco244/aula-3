from dao.utility.db import MySql
from models.employee import EmployeeModel

class EmployeeDao:
    
    @classmethod
    def getEmployeesByCity(cls, office_city):
        MySql.openConnection()
        try: 
            MySql.query(
                f'''SELECT *
                FROM employees e
                JOIN offices o ON o.officeCode = e.officeCode
                WHERE o.city = {office_city}'''
            )
            data = MySql.getResults()
            results = list()
            for element in data:
                results.append(EmployeeModel(employeeNumber = element[0], lastName = element[1], firstName = element[2], extension = element[3], email = element[4], officeCode = element[5], reportsTo = element[6], jobTitle = element[7]))  
                
            return {
                "esito": "OK",
                "risultato": results
            }
                
        except Exception as ex:
            return {
                "esito": "KO",
                "risultato": ex
            }
            
        finally:
            
            MySql.closeConnection()    