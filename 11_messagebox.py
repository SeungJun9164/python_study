import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("SeungJun GUI")
root.geometry("640x480")  # 가로 x 세로 (곱하기는 x로 사용한다)

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.") # showinfo : 정보를 알려주는 메시지(하늘색 아이콘 표시)

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.") # showwaring : 경고를 알려주는 메시지(노란색 삼각형 아이콘 표시)

def error():
    msgbox.showerror("에러", "결제 에러가 발생하였습니다.") # showerror : 에러를 알려주는 메시지(빨간색 x 아이콘 표시

def okcancel():
    msgbox.askretrycancel("확인 / 취소", "해당 좌석은 유아동반석입니다.") # 사용자에게 ok/cancel 둘 중 어느것을 고를지 선택

def retrycancel():
    msgbox.askokcancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?") # 사용자에게 ok/cancel 둘 중 어느것을 고를지 선택

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소
    # print(response) # True, False, None -> 예 1, 아니오 0, 그 외
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()
