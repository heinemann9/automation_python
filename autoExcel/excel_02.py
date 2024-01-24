import openpyxl as excel

book = excel.load_workbook("python_code/autoExcel/hello.xlsx")
sheet = book.worksheets[0]
cell = sheet["A1"]
cell_a2 = sheet["A2"]
cell_b1 = sheet["B1"]

print(cell.value)
print(cell_a2.value)
print(cell_b1.value)
# book.save("python_code/autoExcel/hello.xlsx")