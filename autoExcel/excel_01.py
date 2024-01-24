import openpyxl as excel

book = excel.Workbook()
sheet = book.active
sheet["A1"] = "안녕"

book.save("python_code/autoExcel/hello.xlsx")