import openpyxl as excel

book = excel.load_workbook("data_excel/monthly_sales.xlsx", data_only=True).active     #기존 파일 열기

for x in book.iter_rows(min_row=3):
    cell_list = []
    for cell in x:
        if cell.value is None:
            break
        else:
            cell_list.append(cell.value)
            
    print(cell_list)
