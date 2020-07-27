# for + append
result = []

for i in range(10):
    result.append(i)

print(result)

# list comprehension
result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 == 0] # filter : if문 조건만 만족한 것만
print(result)

word_1 = "Hello"
word_2 = "World"
result = [i+j for i in word_1 for j in word_2]
# for i in word_1:
  # for j in word_2: 와 동일하다

print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]

for i in stuff:
    print(i)

