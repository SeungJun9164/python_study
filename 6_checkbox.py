from tkinter import *

root = Tk()
root.title("SeungJun GUI")
root.geometry("640x480")  # 가로 x 세로 (곱하기는 x로 사용한다)

chkvar = IntVar() # chkvar에 int형으로 값을 저장

chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar) # variable : 체크박스를 선택,해제 했을 때의 값
# chkbox.select() # 체크박스 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
