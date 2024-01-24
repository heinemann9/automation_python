import openpyxl as excel

book = excel.load_workbook("python_code/autoExcel/hello.xlsx")
sheet = book.worksheets[0]

for i in range(2, 5):
    data_list = []
    for j in range(2, 5):
        data_cell = sheet.cell(row=i, column=j).value
        data_list.append(data_cell)
    print(data_list)

print(data_list)