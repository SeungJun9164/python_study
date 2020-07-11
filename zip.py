kor = ["사과", "바나나", "오렌지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng)))
# [('사과', 'apple'), ('바나나', 'banana') 이런식으로 묶인다.

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))
# zip(*mixed)를 하면 묶인것을 각각 사과,바나나,오렌지 / apple,banana,orange 로 푼다.

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)
