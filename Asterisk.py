# asterisk : *을 의미
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)

def asterisk_test(a, **kargs): # ** : 키워드 인자를 넘겨줄 때 사용
    print(a, kargs)
    print(type(kargs))

asterisk_test(1, b=2, c=3, d=4, e=5, f=6)

# asterisk -unpacking
def asterisk_test(a, *args):
    print(a, args[0])
    print(type(args))

asterisk_test(1, (2, 3, 4, 5, 6))

def asterisk_test(a, args):
    print(a, *args)
    print(type(args))

asterisk_test(1, (2, 3, 4, 5, 6))
