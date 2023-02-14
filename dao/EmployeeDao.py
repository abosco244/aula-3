from dao.utility.db import MySql
from models.employee import *
from dao.RispostaModel import *


class EmployeeDao:
    
    @classmethod
    def getEmployeesByCity(cls, office_city):
        MySql.openConnection()
        try: 
            MySql.query(
                f'''SELECT *
                FROM employees e
                JOIN offices o ON o.officeCode = e.officeCode
                WHERE o.city = \'{office_city}\''''
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
            
    @classmethod           
    def getEmployeeByEmployeeNumber(cls, employeeNumber):
        try:
            MySql.openConnection()
            MySql.query(f"SELECT * FROM employees WHERE employeeNumber={employeeNumber}")
            risultato=MySql.getResults()
            employee = list()
            for el in risultato:
                employee = (EmployeeModel(employee_number = el[0], 
                                        last_name = el[1], 
                                        first_name = el[2],
                                        extension = el[3], 
                                        email = el[4], 
                                        office_code = el[5], 
                                        reports_to = el[6],
                                        job_title = el[7]
                ))
            return Risposta(
                risultato = employee,
                esito = 'OK'
            )    
        except Exception as error:
            return Risposta(
                risultato = error,
                esito = 'KO'
            )
        finally: 
            MySql.closeConnection()    
           