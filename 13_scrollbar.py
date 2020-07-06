from tkinter import *

root = Tk()
root.title("SeungJun GUI")
root.geometry("640x480")  # 가로 x 세로 (곱하기는 x로 사용한다)

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set) # set이 없으면 스크롤을 내려도 다시 올라옴
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) # scrollbar와 listbox를 매핑 
root.mainloop()
