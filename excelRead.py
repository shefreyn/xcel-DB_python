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

#storing Name_values extracted from excel to a py variable
name1 = xcelFile.ws(ws='Sheet1').address(address='A2')
name2 = xcelFile.ws(ws='Sheet1').address(address='A3')
name3 = xcelFile.ws(ws='Sheet1').address(address='A4')

#storing ID_values extracted from excel to a py variable
id1 = xcelFile.ws(ws='Sheet1').address(address='B2')
id2 = xcelFile.ws(ws='Sheet1').address(address='B3')
id3 = xcelFile.ws(ws='Sheet1').address(address='B4')

#using db cursor and storing it to a variable 'mycursor'
mycursor = dataBase.cursor()

#executing db commands via the velow funcion
print(f"INSERT INTO data_id (NAME, ID) VALUES ('{name1}',{id1});")

mycursor.execute(f"INSERT INTO data_id (NAME, ID) VALUES ('{name1}',{id1});")

