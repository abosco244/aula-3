from dao.utility.db import MySql
from models.office import *
from dao.RispostaModel import *

class OfficesDao:

    @classmethod
    def getOfficeByOfficeCode(cls, officeCode):
        try:
            MySql.openConnection()
            MySql.query(f"SELECT * FROM offices WHERE officeCode = {officeCode}")
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

    @classmethod
    def addOffice(cls, office):
        try:
            MySql.openConnection()
            MySql.query(f"insert into offices\
                          values ('{office.officeCode}',\
                                  '{office.city}',\
                                  '{office.phone}',\
                                  '{office.addressLine1}',\
                                  '{office.addressLine2}',\
                                  '{office.state}',\
                                  '{office.country}',\
                                  '{office.postalCode}',\
                                  '{office.territory}')")
            MySql.commit()

            return {"esito": "OK",
                    "risultato": office}

        except Exception as errore:
            return {"esito": "KO",
                    "risultato": str(errore)}
        finally:
            MySql.closeConnection()