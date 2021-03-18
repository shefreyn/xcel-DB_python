import pylightxl as xl                                     #importing python package to read excel file (.xlsx and .xlsm ) & write (.xlsx)
print("Hello, welcome to XL Read")                         #test
db = xl.readxl(fn='C:\Users\Shefreyn\Desktop\Python Excel\excel\test.xlsx')
print(db)