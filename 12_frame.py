from tkinter import *

root = Tk()
root.title("SeungJun GUI")
root.geometry("640x480")  # 가로 x 세로 (곱하기는 x로 사용한다)

Label(root, text="메뉴를 선택해주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1) # relief : 테두리 모양 / bd : 외곽선 굵기
frame_burger.pack(side="left", fill="both", expand=True) # side : 어느 위치에 넣을 것인지 / expand : 확장시킬 것인지

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_dirnk = LabelFrame(root, text="음료") # LabelFrame : 제목이 있는 프레임
frame_dirnk.pack(side="right", fill="both", expand=True)
Button(frame_dirnk, text="콜라").pack()
Button(frame_dirnk, text="사이다").pack()

root.mainloop()
