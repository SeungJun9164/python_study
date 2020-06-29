z = """
안녕하세요
이승준입니다.
"""
print(z)


# 여러줄의 문자열을 입력하려면 """ """

def chat(name1, name2):
    print("{}: _hello".format(name1))
    print("{}: _world".format(name2))


chat("알렉스", "윤하")


def dsum(a, b):
    c = a + b
    return c


d = dsum(1, 2)
print(d)

# 반복문
for i in range(10):
    print("hello world")

i = 0
while i < 3:
    print("w_hello world")
    i = i + 1

x = [1, 2, 3, 4]
y = ["hello", 1, 2, 3]

length = len(x)  # 길이
sort = sorted(x)  # 정렬
ssum = sum(x)
print(x.index(3))  # 3이라는 인덱스 위치 찾기
print(3 in x)  # in : x안에 3이라는 숫자가 있는지 확인 true / false

# tuple : 리스트와 비슷하지만 한번 생성되면 값을 변경x
# list의 기능을 거의 사용가능
x = tuple()
y = ('a', 'b', 'c')

# dictionary : key와 value로 구성된 배열
# key값은 불변 값만
x = {
    "name": "이승준",
    "age": 20,
    0: "나는",
}
print(x["name"])
print(x[0])

print(x.keys()) # 모든 key값을 보여라
print(x.values()) # 모든 value값을 보여라

x[0] = "입니다."
print(x[0])


fruit = ["사과","사과","바나나","바나나","딸기","키위","복숭아","복숭아","복숭아"]

d={}
for i in fruit:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)
