# -*- coding: utf-8 -*-
"""
□ 참고 : https://hleecaster.com/tkinter-introduction/
□ 기능: tkinter의 기본 개념
□ 목적: tkinter를 통한 exe 디자인

"""
#%%
import tkinter as tk
#%%
root = tk.Tk()

# Label
widget1 = tk.Label(root, text="이것은 Label입니다.")
widget1.pack()

# Button
widget2 = tk.Button(root, text="이것은 Button입니다.")
widget2.pack()

# Text
widget3 = tk.Text(root)
widget3.pack()

# Listbox
widget4 = tk.Listbox(root)
widget4.pack()

root.mainloop()
#%%
# 1. Label
from PIL import ImageTk # 이미지를 사용할 경우

root = tk.Tk()

# 텍스트 레이블
widget1 = tk.Label(
    root,
    text="이것은 Label입니다.",
    fg="white",
    bg="#34A2FE",
    width=40,
    height=5
)
widget1.pack()

# 이미지 레이블
img = ImageTk.PhotoImage(file="base.jpg")
widget2 = tk.Label(root, image=img)
widget2.pack()

root.mainloop()
#%%
# 2. Button
from tkinter.filedialog import askopenfilename

root = tk.Tk()

# 함수 생성
def open_file():
    filename = askopenfilename(filetypes=(("Excel files", ".xlsx .xls"), ('All files', '*.*')))
    if filename:
        print(filename)
        btn_text.set("선택 완료")

btn_text = tk.StringVar()
btn_text.set("파일 선택")

# 버튼에 함수 연결
widget = tk.Button(
    root,
    textvariable=btn_text,
    command=open_file,
    width=20,
    height=2,
    bg="blue",
    fg="yellow",
)
widget.pack()

root.mainloop()
#%%
# 3. Text
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()

# Text
widget1 = tk.Text(root, width=50, height=10)
widget1.pack()
# ScrolledText
widget2 = ScrolledText(root, width=50, height=10)
widget2.pack()

root.mainloop()
#-------------------------------
root = tk.Tk()

# 1.0 : 맨 앞
widget1 = tk.Text(root, width=50, height=10)
widget1.insert(1.0, "첫 번째 문장입니다.\n")
widget1.insert(1.0, "두 번째 문장입니다.\n")
widget1.pack()

# "end" : 맨 뒤
widget2 = tk.Text(root, width=50, height=10)
widget2.insert("end", "첫 번째 문장입니다.\n")
widget2.insert("end", "두 번째 문장입니다.\n")
widget2.pack()

# x.y : x번째 줄 y번째 글자
widget3 = tk.Text(root, width=50, height=10)
widget3.insert("end", "----------\n")
widget3.insert("end", "----------\n")
widget3.insert(2.7, "O")
widget3.pack()

root.mainloop()
#-------------------------------
root = tk.Tk()

# 텍스트
widget1 = tk.Text(root, width=50, height=10)
widget1.pack()

# 버튼 (command에 lambda 함수 작성)
widget2 = tk.Button(root, text="삭제하기", command=lambda : widget1.delete(1.0, "end"))
widget2.pack()

root.mainloop()
#-------------------------------
root = tk.Tk()

widget = tk.Text(root, width=50, height=10)

widget.config(state='normal')
widget.insert(1.0, "삭제할 수 없는 텍스트입니다.\n")
widget.config(state='disabled')

widget.pack()

root.mainloop()
#%%
# 4. Listbox

root = tk.Tk()

widget = tk.Listbox(root, width=50, height=10)
for i in range(1, 6):
    widget.insert(0, f'{i}번')

widget.pack()

root.mainloop()
#-------------------------------
root = tk.Tk()

# 위젯 생성
widget = tk.Listbox(root, width=50)
for i in range(100):
    widget.insert("end", i)
scrollbar = tk.Scrollbar(root)

# 기능 상호 연결
widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=widget.yview)

# 배치
widget.pack(side="left", fill="y")
scrollbar.pack(side="right", fill="y")

root.mainloop()
#%%
# 5. messagebox
from tkinter import messagebox

root = tk.Tk()

widget = tk.Button(root, text="테스트", command=lambda : messagebox.showinfo())
widget.pack()

root.mainloop()
#-------------------------------
root = tk.Tk() # 다양한 종류의 팝업

messagebox.askokcancel(message="askokcancel()")
messagebox.askquestion(message="askquestion()")
messagebox.askretrycancel(message="askretrycancel()")
messagebox.askyesno(message="askyesno()")
messagebox.askyesnocancel(message="askyesnocancel()")
messagebox.showerror(message="showerror()")
messagebox.showinfo(message="showinfo()")
messagebox.showwarning(message="showwarning()")

root.mainloop()
#%%
