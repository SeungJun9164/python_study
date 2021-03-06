vector_a = [1, 2, 10] # List로 표현했을 경우
vector_b = (1, 2, 10) # Tuple로 표현했을 경우
vector_c = {'x':1, 'y':1, 'z':10} # dict 표현했을 경우

u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [sum(t) for t in zip(u, v, z)]
print(result)

u = [1, 2, 3]
v = [4, 5, 6]
alpha = 2
result = [alpha * sum(z)for z in zip(u, v)]

matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [3, 7]]

result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]

print(result)

matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)]

print(result)

matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)