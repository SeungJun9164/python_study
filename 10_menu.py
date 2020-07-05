from tkinter import *

root = Tk()
root.title("SeungJun GUI")
root.geometry("640x480")  # 가로 x 세로 (곱하기는 x로 사용한다)

menu = Menu(root)

def create_new_file():
    print("새 파일을 만듭니다.")

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator() # 메뉴에서 구분을 하기 위한
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # state="disable" : 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) # root.quit : 선택되면 종료
menu.add_cascade(label="File", menu=menu_file) # add_cascade : menu에다가 menu_file만든 것을 넣어주기 위함

# Language 메뉴 추가 (radio 버튼을 클릭해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 추가 (checkbox 버튼을 클릭해서 택1)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)
root.mainloop()
