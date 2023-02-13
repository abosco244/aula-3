from dao.utility.db import MySql

MySql.openConnection()
MySql.query("select * from orders")
MySql.closeConnection()
