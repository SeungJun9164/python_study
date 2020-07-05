# from 모듈 import 변수/함수 : 해당 모듈 내에 있는 특정 메소드나 모듈 내 정의된 변수를 가져온다.
# import 모듈 as 이름 : 모듈을 가져오면서 이름으로 사용

from tkinter import *

root = Tk()
root.title("SeungJun GUI")
root.geometry("640x480") # 가로 x 세로 (곱하기는 x로 사용한다)
#root.geometry("640x480+300+100") # 가로 x 세로 + x좌표 + y좌표

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()
