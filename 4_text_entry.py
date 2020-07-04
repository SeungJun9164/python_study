from tkinter import *

root = Tk()
root.title("SeungJun GUI")
root.geometry("640x480")  # 가로 x 세로 (곱하기는 x로 사용한다)

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")  # insert : text상자의 초기 문구를 지정해주는 명령어

e = Entry(root, width=30)  # Entry : text와 동일하지만 Entry는 한줄만 입력가능하다(enter가 불가능하다)
e.insert(0, "한 줄만 입력하세요")  # END와 0 동일
e.pack()


def btncmd():
    print(txt.get("1.0", END))  # text안에 있는 문구를 가져오기, get("1.0", END) : 처음부터 끝까지 모든 문구를 가져오라, 1.0 : 1 : 첫번째 라인, 0 : 0번째 column위치
    print(e.get()) # Entry의 문구를 가져오기 위해서는 get()만 써주면 된다.

    # 내용 삭제
    txt.delete("1.0", END) # delete : 기존에 적혀져 있던 문구를 삭제한다
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
