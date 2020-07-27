items = 'zero one two three'.split()
print(items)

example = 'python,jquery,javascript'
example.split(",")

a, b, c = example.split(",")
example = 'cs50.gachon.edu'
subdomain, domain, tld = example.split('.')

colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)

result = ' '.join(colors) # 빈칸 1칸으로 연결
print(result)

result = ', '.join(colors) # 연결시 ", "으로 연결
print(result)