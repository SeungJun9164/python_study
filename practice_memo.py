import os  # 파일이 존재하는지 여부 확인하기 위한
from tkinter import *

root = Tk()
root.title("제목없음-Windows 메모장")
root.geometry("640x480")

# txt파일 생성 / 저장
filename = "mynote.txt"

def memo_open():
    if os.path.isfile(filename):  # os.path.isfile(파일이름) : (파일이름) 파일이  존재하는지 여부 확인 / 존재하면 true, 없으면 false
        with open(filename, "r", encoding="utf8") as file:  # with open : 파일을 여는 방법
            txt.delete("1.0", END)
            txt.insert(END, file.read())  # file,read : 파일을 읽어오는 것


def memo_save():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


# 메뉴 뷰뷴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command="memo_open")
menu_file.add_command(label="저장", command="memo_save")
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바
scrollbar = Scrollbar(root)  # root를 하나의 프레임으로 생각해서 바로 대입
scrollbar.pack(side="right", fill="y")

# 글쓰기 부분
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()
