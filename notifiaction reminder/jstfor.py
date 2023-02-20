import openpyxl as ox
from pathlib import Path
import datetime as dt
# print(Path.cwd()) gives us the current working directory

#to open the excel sheet the below process
xls=Path(Path.cwd(),"Book1.xlsx")  #here the path is given in the formate of name not slashes

w=ox.load_workbook(xls)   #to open the excel sheet using openpyxl
# print(w)

sheet=w.active


hou=str(dt.datetime.now().hour)
mint=str(dt.datetime.now().minute)
tin=hou+":"+mint+":"+"00"
# print(hou+":"+mint)
size=sheet.max_row

for i in range(2,size+1):
    val="A"+str(i)
    if tin>str(sheet[val].value):
        val1="A"+str(i-1)
        dif=int(sheet[val].value)-int(sheet[val1].value)
        print(dif)

    else:
        print("bjjoiu")   
       

  




    