from tkinter import *

file_path = ""
def do_it():
    name = ent.get()
    lab_2.config(text=name)

win = Tk()
win.geometry("500x200")
win.title("파이썬GUI창")
win.option_add("*Font", "돋움 16")

lab_1 = Label(win, text="파이썬 프로그램")
lab_1.pack()

btn = Button(win, text="실행")
btn.config(command=do_it)
btn.pack()

ent = Entry(win)
ent.pack()

lab_2 = Label(win, text="이름이 표기 됩니다.")
lab_2.pack()

win.resizable(True, True)
win.mainloop()