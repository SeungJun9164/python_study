# Lambda : 함수 이름 없이, 함수처럼 쓸수 있는 익명함수
f = lambda x, y: x + y
print(f(1, 4))

# Map & Reduce
ex = [1, 2, 3, 4, 5]
f = lambda x: x ** 2
print(list(map(f, ex)))

# Reduce
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))