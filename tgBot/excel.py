import openpyxl
from ..database.storage import DatabaseRobota

def createExcel() -> str:
    
    workbook = openpyxl.Workbook()
    sheet = workbook.active 
    sheet.append(["datetime", "vacancy_count", "change"])
    
    d = DatabaseRobota()
    
    records = d.retrieve_all()
    
    if not records:
        return "data.xlsx"
    
    for row in records:
        formatted_datetime = row[-1].strftime("%d.%m.%Y %H:%M:%S")
        sheet.append([formatted_datetime, row[1], row[2]])
    workbook.save("data.xlsx")
    return "data.xlsx"