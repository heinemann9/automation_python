import openpyxl as excel

book = excel.load_workbook("data_excel/write_cellname.xlsx")     #기존 파일 열기
sheet = book.worksheets[0]      #첫 번째 워크시트 가져오기

#연속 데이터 가져오기
for i in range(1, 20):
    data_list = []
    for j in range(1, 10):
        data_cell = sheet.cell(row=i, column=j).value
        data_list.append(data_cell)
    
    print(data_list)

for x in sheet["B2":"E8"]:
    cell_list = []
    for cell in x:
        cell_list.append(cell.value)
    print(cell_list)
