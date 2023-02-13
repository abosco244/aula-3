from dao.utility.db import MySql
from models.office import OfficeModel

class officesDao:

    @classmethod
    def getOfficeByOfficeCode(cls,officeCode):
        try:
            MySql.openConnection()
            MySql.query(f"SELECT * FROM offices where officeCode={officeCode}")
            dati=MySql.getResults()
            office=list()
            for el in dati:
                office = (OfficeModel(officeCode = el[0],
                                city = el[1], 
                                phone = el[2], 
                                addressLine1= el[3], 
                                addressLine2= el[4], 
                                state= el[5], 
                                country= el[6], 
                                postalCode= el[7], 
                                territory= el[8]))
            MySql.closeConnection()
            return office
        except Exception as er:
            print(er)



