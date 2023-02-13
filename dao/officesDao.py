from dao.utility.db import MySql

class officesDao():
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