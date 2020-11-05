def fun1(): #함수 이름은 변수 이름 규칙과 동일
    '''
    파라메터 없음. 반환값 없음.
    파라메터: 함수가 동작할 때 필요한 값을 받아올 변수로 함수이름 옆의 괄호에 나열한다.
    반환값(리턴값): 함수의 결과물을 호출한 쪽으로 던져줌
    :return:
    '''
    print('hello funtion')

def fun2(a, b):# 2개의 파라메터를 갖음
    print(a,' + ', b, ' = ', a+b)#파라메터로 받은 2개의 값을 더해서 출력
    #리턴값이 없다.

def fun3(a, b):
    return a+b #return:함수종료. return 값:값을 호출한 곳으로 반환

fun1()#파라메터가 없기 때문에 호출할때도 괄호에 아무값도 안넣음
fun2(1,2)
res = fun3(3,4)
print('res:', res)


def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def dev(a, b):
    if b==0:
        print('0으로 나눌 수 없음')
        return None
    return a/b

while True:
    menu = int(input('1.add 2.sub 3.mul 4.dev 5.stop'))
    if 1 <= menu <= 4:
        num1 = int(input('num1:'))
        num2 = int(input('num2:'))
    res = 0
    if menu==1:
        res = add(num1, num2)#함수를 호출하면 그 함수 정의로 점프(분기)
    elif menu==2:
        res = sub(num1, num2)
    elif menu==3:
        res = mul(num1, num2)
    elif menu==4:
        res = dev(num1, num2)
    elif menu==5:
        print('종료')
        break
    else:
        print('잘못된 메뉴')
        res = None #None: 값이 없음을 나타내는 상수

    if res!=None:
        print('res:', res)

