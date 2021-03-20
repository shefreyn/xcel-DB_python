#importing python package to read excel file (.xlsx and .xlsm ) & write onto (.xlsx)
import pylightxl as xl      
#importing mysql Package
import mysql.connector



#TITLE
print("Hello, welcome to XL Read") 
                       
#Reading file & storing data to a var
xcelFile = xl.readxl(fn='C:/Users/Shefreyn/Desktop/py_excel/excel/test.xlsx')

#

#Database connector
dataBase = mysql.connector.connect(
    host="localhost",
    database="excelread_py",
    user="pma",
    password="123456"
)
print(dataBase)

#interation
for row in xcelFile.ws(ws='Sheet1').rows:
    if(row != ['Name', 'ID', 'Dpt']):
        name,id,dept = row
        #using db cursor and storing it to a variable 'mycursor'
        mycursor = dataBase.cursor()
        mycursor.execute(f"INSERT INTO data_id (NAME, ID) VALUES ('{name}',{id});")
        #executing db commands via the velow funcion
        dataBase.commit() 

#storing Name_values extracted from excel to a py variable
name1 = xcelFile.ws(ws='Sheet1').address(address='A2')
name2 = xcelFile.ws(ws='Sheet1').address(address='A3')
name3 = xcelFile.ws(ws='Sheet1').address(address='A4')

#storing ID_values extracted from excel to a py variable
id1 = xcelFile.ws(ws='Sheet1').address(address='B2')
id2 = xcelFile.ws(ws='Sheet1').address(address='B3')
id3 = xcelFile.ws(ws='Sheet1').address(address='B4')

#testing
for i in range(1,3):
    nameFor1 = xcelFile.ws(ws='Sheet1').address(address='A2')





