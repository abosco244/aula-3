from dao.utility.db import MySql
from models.office import *
from dao.RispostaModel import *

class OfficesDao:

    @classmethod
    def getOfficeByOfficeCode(cls, officeCode):
        try:
            MySql.openConnection()
            MySql.query(f"SELECT * FROM ooffices WHERE officeCode = {officeCode}")
            data = MySql.getResults()
            office = list()
            for el in data:
                office = (OfficeModel(officeCode = el[0],
                                city = el[1], 
                                phone = el[2], 
                                addressLine1= el[3], 
                                addressLine2= el[4], 
                                state= el[5], 
                                country= el[6], 
                                postalCode= el[7], 
                                territory= el[8]
                ))
            return Risposta(
                risultato = office,
                esito = 'OK'
            )
        except Exception as error:
            return Risposta(
                risultato = error,
                esito = 'KO'
            )
        finally:
            MySql.closeConnection()