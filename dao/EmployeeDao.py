from dao.utility.db import MySql
from models.employee import EmployeeModel

class EmployeeDao:
   
    
    @classmethod
    def get_employee(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM employees")
        data = MySql.getResults()
        results = list()
        for element in data:
            results.append(EmployeeModel(employeeNumber = element[0], lastName = element[1], 
                                    firstName = element[2],extension = element[3], 
                                    email = element[4], officeCode = element[5], reportsTo = element[6],
                                    jobTitle = element[7]))
        MySql.closeConnection()
        return results



    def getEmployeeByEmployeeNumber(self, employeeNumber):
        try:
            MySql.openConnection()
            MySql.query(f'''select *
                                    from employees
                                        where employeeNumber={employeeNumber}''')

            risultato=MySql.getResults()
            employee = list()
            for el in risultato:
                employee = EmployeeModel(employeeNumber = el[0], lastName = el[1], 
                                        firstName = el[2],extension = el[3], 
                                        email = el[4], officeCode = el[5], reportsTo = el[6],
                                        jobTitle = el[7])
                
            MySql.closeConnection()
            
        except Exception as error:
            print(error)
        return employee