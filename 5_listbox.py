from tkinter import *

root = Tk()
root.title("SeungJun GUI")
root.geometry("640x480")  # 가로 x 세로 (곱하기는 x로 사용한다)

listbox = Listbox(root, selectmode = "extended", height=0) # selectmode : 선택하는 옵션 extended : ctrl를 누르고 선택하면 다중선택 가능 / single : 하나만 선택 가능
# height : 지정된 갯수 만큼의 리스트를 보여주는 역할 0 : 모든 리스트를 보여줌
listbox.insert(0, "사과") # listbox의 0번째에 "사과"라는 값을 삽입
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # END를 인덱스로 넣으면 listbox의 맨 마지막인덱스에 대입
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
   # listbox.delete(END) # 맨 뒤의 항목을 삭제
   # listbox.delete(0) # 맨 앞의 항목을 삭제

    # 갯수 확인
    print("리스트에는", listbox.size(), "개가 있습니다.")

    # 항목 확인
    print(listbox.get(0, 2)) # get : 0번째 부터 2번 인덱스까지의 항목을 얻어온다

    # 선택된 항목 확인(인덱스 번호로 반환)
    print("선택된 항목 : ", listbox.curselection()) # curselection() : 선택된 항목을 얻어온다.
    

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
