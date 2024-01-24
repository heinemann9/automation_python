import os #기본 내장 라이브러리 - 파일,폴더 구조를 가져오기 위한
from tkinter import * #GUI
import tkinter.font as tkFont #폰트 설정
from tkinter import filedialog #디렉토리명을 가져오기 위해서

reWin = Tk() #창 정의
reWin.geometry("330x400+200+100")
reWin.title("파이썬-파일명바꾸기APP") #창 
reWin.resizable(False, False)
reWin.option_add("*Font","돋움 14") 

font_label = tkFont.Font(family="돋움", size=14)
font_result = tkFont.Font(family="돋움", size=14, weight="bold", underline=False, overstrike=False, slant="roman")

oldLab = Label(reWin,
    font=font_label,
    text="찾을단어 :",
    width=12,
    height=2,
    relief="flat",
    borderwidth=1,
    foreground="#888888",
    background="#EEEEEE"
    )
oldLab.grid(row=0,column=0)

oldEnt = Entry(reWin,
    font=font_label,
    width=18,
    text=""
    )
oldEnt.grid(row=0,column=1)

newLab = Label(reWin,
    font=font_label,
    text="바꿀단어 :",
    width=12,
    height=2,
    relief="flat",
    borderwidth=1,
    foreground="#888888",
    background="#EEEEEE"
    )
newLab.grid(row=1,column=0)

newEnt = Entry(reWin,
    font=font_label,    
    width=18,
    text=""
    )
newEnt.grid(row=1,column=1)


pathLab = Label(reWin,
    font=font_label,
    text="",
    width=31,
    height=5,
    wraplength = 280,
    foreground="#888888",
    background="#DDDDDD"
    )
pathLab.grid(row=2,column=0,columnspan=2)


resultLab = Label(reWin,
    font=font_label,
    text="",
    width=31,
    height=5,
    wraplength = 280,
    foreground="#888888",
    background="#DDDDDD"
    )
resultLab.grid(row=5,column=0,columnspan=2)

global dir_fullPath

def find_dir(): #폴더 경로 반환 함수
    global dir_fullPath

    reWin.dirName=filedialog.askdirectory() #폴더경로반환
    dir_fullPath = reWin.dirName #폴더경로를 dir_fullPath 저장
    pathLab.config(text="경로 : "+reWin.dirName) #폴더경로 pathLab에 보여줌

    return(reWin.dirName) #폴더 경로 반환

def change_filename(): #이름 변경 함수
    count = 0               #전체 파일 수
    count_change = 0        #처리한 파일 수
    oldText = oldEnt.get()
    newText = newEnt.get()

    #print(oldText, newText)

    #리스트에 모든 파일 넣어두기
    file_fullPath = []
    for i in os.listdir(dir_fullPath): #해당 폴더에 모든 파일목록
        file_fullPath.append(os.path.join(dir_fullPath, i))

    #print(file_fullPath) 모든 파일 목록
    #file_fullPath 리스트의 파일 목록 모두 변경
    for file in file_fullPath:
        dir_path = os.path.dirname(file) #dir_path에 경로명이 저장
        file_name = os.path.basename(file) #file_name에 파일명만 저장

        if file_name.count(oldText) > 0: #바꿀문자가 있다면
            count += 1
            count_change += 1
            file_newName = file_name.replace(oldText,newText) #변경될 파일명 변수에 넣기
            os.rename(file, os.path.join(dir_path, file_newName))
        else:
            count += 1 #바꿀 문자가 없어도 

        result_msg = f"총 {count}건의 파일에서 {count_change}건의 파일 이름을 수정했습니다."
        resultLab.config(text=result_msg)
            


butFind = Button(reWin, text="경로찾기", width=30, height=2, overrelief="solid", command=find_dir)
butFind.grid(row=3, column=0, columnspan=2)

butChange = Button(reWin, text="이름변경", width=30, height=2, overrelief="solid", command=change_filename)
butChange.grid(row=4, column=0, columnspan=2)



reWin.mainloop() #창 실행