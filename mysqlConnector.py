import mysql.connector

class SQLConnector:
    def connector():
        #Database connector
        dataBase = mysql.connector.connect(
        host="localhost",
        database="excelread_py",
        user="pma",
        password="123456"
        )
        return dataBase
    