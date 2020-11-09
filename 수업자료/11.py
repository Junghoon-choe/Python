def f1():
    print('f1() 호출')


def f2():
    print('f2() 호출')


def f3():
    print('f3() 호출')

def f4(x):#파라메터로 튜플 받음. 튜플:immutable요소로 개수, 값 변경 불가
    print('f4() 호출')
    for i in x:
        print(i, end=', ')
    print()
#params=None => 디폴트 인자. 호출시 생략가능 .
def select(f, params=None):#f: 함수의 참조값을 받아오는 파라메터. 핸들러 등록 함수. params:f의 파라메터
    # 핸들러:이벤트가 발생하면 자동으로 호출되서 그 처리를 하는 함수
    if params == None:
        f() #파라메터 값이 f1이라면 f1() / 파라메터 값이 f2이라면 f2() / 파라메터 값이 f3이라면 f3()
    else:
        f(params)


def main():  # 시작함수
    print('main 호출')
    select(f1) #함수의 참조값.
    select(f2)
    select(f3)
    select(f4,(1,2,3))
    #f1()#함수를 호출하면 그 함수가 사용할 스택 메모리를 할당

main()  #메인을 통해서 f1, f2, f3()호출

