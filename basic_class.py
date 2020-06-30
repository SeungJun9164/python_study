# 함수 정의
def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()


def profile(name, age, main_lang):
    print("이름 : {}\t 나이 : {}\t주 언어 : {}".format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile(main_lang="c언어", age=22, name="김태호")  # 키워드 이용하면 순서 상관x


def profile2(name, age, main_lang="파이썬"):
    print("이름 : {}\t 나이 : {}\t주 언어 : {}".format(name, age, main_lang))


profile2("김태호", 20)


class Person:
    def __init__(self, name, age):  # self를 첫 인자로 받고 person에서 새로 쓸 변수를 설정
        self.name = name
        self.age = age

    def say_hello(self):
        print("안녕! 나는 " + self.name)

    def introduce(self):
        print("내이름은 " + self.name + " 나이는 " + str(self.age))


seungjun = Person("승준", 25)
michael = Person("마이클", 24)
jenny = Person("제니", 23)

seungjun.say_hello()
michael.say_hello()
jenny.say_hello()

seungjun.introduce()
michael.introduce()
jenny.introduce()


# 상속

class Police(Person):
    def arrest(self, to_arrest):
        print("넌 체포됐다." + to_arrest)


class Programmer(Person):
    def program(self, to_program):
        print("다음엔 뭘 만들지? " + to_program)


seungjun = Person("승준", 25)
jenny = Police("제니", 23)
michael = Programmer("마이클", 22)

jenny.introduce()
jenny.arrest("승준")
michael.program("이메일 클라이언트")
