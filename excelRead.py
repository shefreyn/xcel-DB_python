#importing python package to read excel file (.xlsx and .xlsm ) & write onto (.xlsx)
import pylightxl as xl      
#importing mysql Package
import mysql.connector
from mysqlConnector import SQLConnector


class mainRead:
    def excelreadFun():
        #Conncetion Object
        newConnector = SQLConnector
        dataBase = newConnector.connector()
        #TITLE
        print("Hello, welcome to XL Read")                      
        #Reading file & storing data to a var
        xcelFile = xl.readxl(fn='C:/Users/Shefreyn/Desktop/py_excel/excel/test.xlsx')
        #interation
        for row in xcelFile.ws(ws='Sheet1').rows:
            if(row != ['Name', 'ID', 'Dpt']):
                name,id,dept = row
                #using db cursor and storing it to a variable 'mycursor'
                mycursor = dataBase.cursor()
                mycursor.execute(f"INSERT INTO data_id (NAME, ID) VALUES ('{name}',{id});")
                #executing db commands via the velow funcion
                dataBase.commit() 
