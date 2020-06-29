# 함수 정의
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def profile(name, age, main_lang):
    print("이름 : {}\t 나이 : {}\t주 언어 : {}".format(name,age,main_lang))

profile("유재석",20,"파이썬")
profile(main_lang="c언어",age=22,name="김태호") # 키워드 이용하면 순서 상관x

def profile2(name, age, main_lang="파이썬"):
    print("이름 : {}\t 나이 : {}\t주 언어 : {}".format(name,age,main_lang))

profile2("김태호",20)