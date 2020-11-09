#다양한 형태의 함수들
#함수안에 코드를 다 실행하면 함수는 종료.
#return 함수종료
def f1():
    print('파라메터 없고 리턴값도 없다')

def f0(num):
    if num%2==0:
        return #함수 종료
    else:
        print(num)

def f2(num):#파라메터의 타입이 고정되지 않기 때문에 어떤 값을 전달해도 받을 수 있음.
    # 하지만 함수안에서 실행시 에러 발생할 수 있음
    if isinstance (num, int):# num의 타입이 int냐?
        print('num/3:', num/3)
    else:#num이 문자열이면. '1234' 'asdf'
        if num.isdigit():#'1234'가 맞으면 계산
            print('num/3:', int(num) / 3)
        else:#'asdf'
            print('알파벳은 계산 불가')


def f3(name):#변수인데 함수가 호출될 때 함수에서 필요한 값을 받아오는 변수
    print('name:', name)

def f4(x):#파라메터로 리스트를 받아서 출력
    for i in x:
        print(i, end=', ')

f2('123')
f2(123)
f2('qwer')

s = [1,2,3,4,5]
f4(s)


