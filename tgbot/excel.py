import openpyxl
from database.storage import DatabaseRobota

def createExcel() -> str:
    workbook = openpyxl.Workbook()
    sheet = workbook.active 
    sheet.append(["datetime", "vacancy_count", "change"])
    
    d = DatabaseRobota()
    records = d.retrieve_all()
    
    if not records:
        workbook.save("data.xlsx")  
        return "data.xlsx"
    
    for row in records:
        sheet.append([row[2], row[0], row[1]])
    
    workbook.save("data.xlsx")
    return "data.xlsx"