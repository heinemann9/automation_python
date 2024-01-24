import openpyxl as excel

book = excel.Workbook()     #새 워크북 생성
sheet = book.active         #위 워크북에서 활성화된 시트를 가져오기

for i in range(1,101):
    for j in range(1,101):
        cell = sheet.cell(row=i, column=j)
        cell.value = cell.coordinate
        
book.save("python_code/autoExcel/hello.xlsx") #저장