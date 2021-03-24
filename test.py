import openpyxl
from mysqlConnector import SQLConnector

wb = openpyxl.Workbook()
sheet = wb.active
newConnector = SQLConnector
dataBase = newConnector.connector()

cursorObject = dataBase.cursor()
# selecting query
query = "SELECT * FROM data_id"
cursorObject.execute(query)
start_row = 1
myresult = cursorObject.fetchall()
for x in myresult:
    start_column = 1
    for searchresult in x:
        print(start_row,start_column)
        sheet.cell(row=start_row, column=start_column).value = searchresult
        start_column += 1     
    start_row += 1
    
wb.save("C:\\Users\\Shefreyn\\Desktop\\excel_py\\test.xlsx")


#wb.save("C:\\Users\\Shefreyn\\Desktop\\excel_py\\test.xlsx")

# disconnecting from server
dataBase.close()