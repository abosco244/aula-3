from dao.utility.db import MySql
from fastapi import FastAPI

MySql.openConnection()
MySql.query("select * from orders")
MySql.closeConnection()

app = FastAPI()