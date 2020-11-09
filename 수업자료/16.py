li = [1,2,3,4,5]

for i in li:    #i:요소값
   print(i, end=', ')
print()

for i in range(0, len(li)): #i:인덱스
    print('li[',i, ']=', li[i])

for idx, i in enumerate(li):    #idx:인덱스, i:요소값
    print('li[',idx, ']=', i)

id='aaa'
pwd='111'

while True:
    id2 = input('id:')
    pwd2 = input('pwd:')
    if id==id2 and pwd==pwd2:
        print('로그인 성공')
        break
    else:
        print('다시 입력')
        
print('메뉴:1.내정보확인 2.내정보수정 3.로그아웃')

