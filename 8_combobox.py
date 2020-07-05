import tkinter.ttk as ttk # combobox를 사용하기 위해서
from tkinter import *

root = Tk()
root.title("SeungJun GUI")
root.geometry("640x480")  # 가로 x 세로 (곱하기는 x로 사용한다)

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values) # height=5로 설정하면 목록5개만 보여진다.
combobox.set("카드 결제일") # 최초 목록 제목 설정, 버튼 클릭을 통한 값 설정도 가능
combobox.pack()

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # state : 읽기 전용으로 설정핧 때
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
