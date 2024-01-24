import os 

#폴더 정의
folder_path = "C:/Shared/study/file_rename" #\ -> / 변경이 필요

#변경할 문자열과 새로운 문자열 정의
old_string = "파이썬"
new_string = "파이선"

#폴더내의 파일이름을 모두 가져와서 순차적으로 이름 변경 (for문)
for filename in os.listdir(folder_path): #정의한 폴더내의 파일 목록을 가져옴
    #print(filename)
    #파일의 전체 경로 생성
    file_path = os.path.join(folder_path,filename)

    #변경할 파일명 정의 old -> new
    new_filename = filename.replace(old_string, new_string)

    #파일명 변경
    os.rename(file_path, os.path.join(folder_path,new_filename))