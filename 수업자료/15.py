def f1():
    print('f1()')

def f2():
    print('f2()')

def f3():
    print('f3()')

def f4():
    print('f4()')

f=[f1, f2, f3, f4]
ec = int(input('error code(0-3):'))
if 0<=ec<=3:
    f[ec]()