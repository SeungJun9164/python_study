from tkinter import *

root = Tk()
root.title("SeungJun GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()  # .pack()을 해야 가시적으로 표시

btn2 = Button(root, padx=5, pady=10, text="버튼2")  # padx = padding x, pady = padding y
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼 4")  # 버튼 크기를 설정
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")  # fg = foreground, bg = background
btn5.pack()

photo = PhotoImage(file="img.png") # image파일을 이용하여 이미지 버튼을 생성, 경로는 "gui_basic/img.png"
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd(): # btn7이 눌렸을 때 발생할 함수
    print("버튼이 클릭되었습니다.")

btn7 = Button(root, text="동작하는 버튼", command=btncmd) # command : 버튼이 눌렸을 때 발생하는 동작(함수)
btn7.pack()

root.mainloop()
