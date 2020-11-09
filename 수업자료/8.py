#단수를 파라메터로 받아 그 한단만 출력하는 함수 정의 및 호출

def gugudan(dan):
    for i in range(1, 10):
        print(dan, ' * ', i, ' = ', dan*i)

def f1(num):#약수 구하는 함수
    for i in range(1, num+1):
        if num%i==0:
            print(i, end=', ')
    print()

def f2(num):
    res=[]
    for i in range(1, num+1):
        if num%i==0:
            res.append(i)
    return res

for i in range(2, 10):
    gugudan(i)

f1(25)
l = f2(6)
print(l)