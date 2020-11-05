def func1():
    print('hello function')

def func2(a, b):
    print(a, '+', b, '=', a + b)

def func3(a, b):
    return a + b

func1()
func2(1, 2)
res = func3(3, 4)
print('result : ', res)


# 계산기
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return None
    return x / y

while True:
    menu = int(input('1.add 2.sub 3.mul 4.div 0.exit : '))

    if menu == 0:
        break
    else:
        num1 = int(input('num1 : '))
        num2 = int(input('num2 : '))

        if menu == 1:
            res = add(num1, num2)
        elif menu == 2:
            res = sub(num1, num2)
        elif menu == 3:
            res = mul(num1, num2)
        elif menu == 4:
            res = div(num1, num2)
        else:
            print('Invalid menu')
            res = None

        if res != None:
            print('result : ', res)

'''
x, y = map(int, input('x, y 입력 : ').split())
print(add(x, y))
print(sub(x, y))
print(mul(x, y))
print(div(x, y))
'''