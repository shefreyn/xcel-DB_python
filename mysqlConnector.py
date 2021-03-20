import mysql.connector

#Database connector
dataBase = mysql.connector.connect(
    host="localhost",
    database="excelread_py",
    user="pma",
    password="123456"
)