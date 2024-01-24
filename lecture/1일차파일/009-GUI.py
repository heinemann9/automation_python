from tkinter import *

win = Tk()
win.geometry("300x500")
win.title("파이썬GUI창")
win.option_add("font","돋움 16")
win.resizable(False,False)

def do_it(): #함수 버튼실행
    name = ent.get() #ent 입력박스에서 받은(get()) 값을 name 변수에 입력
    lab_2.config(text=name) #lab_2의 text를 지금 받은 name으로 변경



lab_1 = Label(win, text="파이썬 프로그램")
lab_1.pack()

btn = Button(win, text="실행")
btn.config(command=do_it)
btn.pack()

ent = Entry(win)
ent.pack()

lab_2 = Label(win, text="이름이 표기 됩니다.")
lab_2.pack()

win.mainloop()