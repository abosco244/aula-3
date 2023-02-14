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