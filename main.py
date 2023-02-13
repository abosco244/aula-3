from dao.utility.db import MySql
from fastapi import FastAPI
from dao.officesDao import officesDao
from models.office import OfficeModel

app = FastAPI()

@app.post('/offices/add')
async def add_office(oggetto: OfficeModel):
    return officesDao.addOffice(oggetto)