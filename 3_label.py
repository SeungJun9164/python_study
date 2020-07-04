from tkinter import *

root = Tk()
root.title("SeungJun GUI")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요") # config : 이미 지정되어있는 레이블의 text를 변경하기 명령어

    global photo2 # global : 전역변수로 선언, photo2를 전역변수로 선언을 해야 garbage collection을 방지
    photo2 = PhotoImage(file="img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()


root.mainloop()
