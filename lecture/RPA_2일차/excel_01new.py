import openpyxl as excel

book = excel.Workbook()     #새 워크북 생성
sheet = book.active         #위 워크북에서 활성화된 시트를 가져오기
sheet["A1"] = "안녕하세요"  #위치가 A1인 곳에 입력

book.save("data_excel/hello.xlsx") #저장