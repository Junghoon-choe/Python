# << 파이썬에서 주석처리.
# 변수 정의
a = 'Joe'
b = 'Hello'
c = 1580
d = 12.43
e = 30

# 불린선언
falseTest = False
trueTest = True

# 변수 출력
print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)
print('e=', e)
print('c+e=', c + e)

# 파라미터 : 출력 또는 입력할 내용을 적어서 함수화 시키는 장소 ,https://lancoding.tistory.com/ << 참고하기

A = 3
B = 'qwer'
C = "abc"
D = 3.14
E = True

'''
print('A=',A,'type=',type(A))
print('B=',B,'type=',type(B))
print('C=',C,'type=',type(C))
print('D=',D,'type=',type(D))
'''
# 위와같이 ''' 로 묶어주면 전체 주석처리 가능
print('E=', E, 'type=', type(E))

# 파이썬은 모두 객체타입이다 (강사님 말씀)

aa = 10
bb = 20

cc = aa + bb
print(aa, '+', bb, '=', cc)

ww = str(aa) + str(bb)  # 형변환 하는 방법
print(ww)  # 출력결과 1020

name = input('이름을 입력하시오')

if (name == "Joe"):
    print('안녕')

while True:
    str = input('메세지를 입력하세요. 멈추려면 /stop을 입력')
    if str == '/stop':
        break;  # 왜 오류가 나는지 알아보기.
        print('루프종료')
    else:
        print(str)

'''
while True:
number = int (input('어떤 동작을 할 지 선택하세요.'))
print('1. 산책 2. 공부')

if number == 1:
    print('산책을 선택하셨습니다.')
    break


elif number == 2 :
    print('공부를 선택하셨습니다.')
        break

else:
    print('다시 입력해주세요.')
    '''

'''
age = int (input('나이를 입력하시오'))
dept = input('학과를 입력하시오')

c = age+5

print('name:',name)
print('age:',age)
print('age about 5years later:',c)
print('dept:',dept)
'''
