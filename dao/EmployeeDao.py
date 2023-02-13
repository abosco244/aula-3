from dao.utility.db import MySql
from models.employee import *
from dao.RispostaModel import *

class EmployeeDao:
    
    @classmethod
    def getEmployeeByEmployeeNumber(cls, employeeNumber):
        try:
            MySql.openConnection()
            MySql.query(f"SELECT * FROM employees WHERE employeeNumber={employeeNumber}")
            risultato=MySql.getResults()
            employee = list()
            for el in risultato:
                employee = (EmployeeModel(employeeNumber = el[0], 
                                        lastName = el[1], 
                                        firstName = el[2],
                                        extension = el[3], 
                                        email = el[4], 
                                        officeCode = el[5], 
                                        reportsTo = el[6],
                                        jobTitle = el[7]
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