import tkinter.ttk as ttk # progressbar를 사용하기 위해서
from tkinter import *
import time # 시간을 사용하기 위해

root = Tk()
root.title("SeungJun GUI")
root.geometry("640x480")  # 가로 x 세로 (곱하기는 x로 사용한다)

progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # mode = indeterminate : 언제 종료될지 결정되지 않은 상태
                                                                     # mode = determinate
progressbar.start(10) # 10ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop() # progressbar 작동 중지


btn = Button(root, text="중지", command=btncmd)
btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # i값이 증가하는 것을 볼 수 있음
        # 이상태로 실행 하면 100이 되었을 때 한번에 보여지게 된다.
        progressbar2.update() # update를 해줘야 i가 한번 끝날 때마다 결과를 반영
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()
