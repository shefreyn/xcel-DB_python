#importing python package to read excel file (.xlsx and .xlsm ) & write onto (.xlsx)
import pylightxl as xl      
#importing mysql Package
import mysql.connector



#TITLE
print("Hello, welcome to XL Read") 
                       
#Reading file & storing data to a var
xcelFile = xl.readxl(fn='C:/Users/Shefreyn/Desktop/py_excel/excel/test.xlsx')

#printing vals
print(xcelFile.ws(ws='Sheet1').address(address='A2'),"with ID",xcelFile.ws(ws='Sheet1').address(address='B2')) 
print(xcelFile.ws(ws='Sheet1').address(address='A3'),"with ID",xcelFile.ws(ws='Sheet1').address(address='B3'))
print(xcelFile.ws(ws='Sheet1').address(address='A4'),"with ID",xcelFile.ws(ws='Sheet1').address(address='B4'))

#Database connector
dataBase = mysql.connector.connect(
    host="localhost",
    user="pma",
    password="123456"
)
print(dataBase)
