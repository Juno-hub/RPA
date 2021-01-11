from openpyxl import Workbook
wb = Workbook() # Creating new workbook
ws = wb.active # Bring actived sheet
ws.title = "JunoSheet"
wb.save("sample.xlsx")
wb.close()