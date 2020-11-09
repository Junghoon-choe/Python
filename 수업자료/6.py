#이름,전화,주소
member = []
#추가
'''
for i in range(0, 3):
    n = input('name:')
    t = input('tel:')
    a = input('address:')
    member.append([n, t, a])
'''
#함수: 코드를 모듈화 해서 필요할때마다 호출하여 사용하는 방법
def make_mem(): #함수정의
    global member   #전역변수
    n = input('name:')
    t = input('tel:')
    a = input('address:')
    member.append([n, t, a])

make_mem()  #함수호출
print(member)

make_mem()
print(member)

make_mem()
print(member)

