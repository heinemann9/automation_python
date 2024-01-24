import openpyxl as excel

book = excel.load_workbook("data_excel/hello.xlsx")     #기존 파일 열기

sheet = book.worksheets[0]      #첫 번째 워크시트 가져오기
cell = sheet["A1"]              #위치가 A1인 곳의 값을 cell에 입력

print(cell.value)               #받아온 값 출력