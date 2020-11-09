#다양한 반환값
def hap(list1):
    s=0
    for i in list1:
        s+=i
    return s

def avg(list1):
    s = hap(list1)
    return s/len(list1)

def max_val(list1):
    m = list1[0]
    for i in list1:
        if m < i:
            m = i
    return m

def min_val(list1):
    m = list1[0]
    for i in list1:
        if m > i:
            m = i
    return m

def max_min1(list1):
    res = [list1[0], list1[0]]
    for i in list1:
        if res[0] < i:
            res[0] = i

        if res[1] > i:
            res[1] = i
    return res  #리스트 반환

def max_min2(list1):
    a=b=list1[0]    #a:최대값, b:최소값
    for i in list1:
        if a < i:
            a = i

        if b > i:
            b = i
    return a, b #값을 2개 반환

nums=[3,8,6,1,4,9,2]
print('sum:', hap(nums))
print('avg:', avg(nums))
r = max_min1(nums)
print('max:', r[0])
print('min:', r[1])

#반환된 값 저장할 변수도 2개
x, y = max_min2(nums)
print('max:', x)
print('min:', y)

m, n = 3, 4
print('m:', m)
print('n:', n)
'''
<과제>
1. 숫자를 요소로 갖는 빈 리스트를 하나 만듬.
메뉴:추가(중복안됨), 검색, 수정, 삭제, 전체목록, 전체삭제, 종료

2. 주소록. 빈 리스트에서 시작.
[[이름, 전화, 주소],[],[]](이름을 기준으로 검색, 중복체크, 수정, 삭제)
메뉴:추가(중복안됨), 검색, 수정, 삭제, 전체목록, 전체삭제, 종료
'''
