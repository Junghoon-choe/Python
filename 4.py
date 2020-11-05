'''
nums = [0]*10
for i in range(0, 10):#0~9: 리스트 인덱스
    nums[i]=int(input('num:'))

for i in nums:
    print(i, end=', ')
print()
'''
# 리스트 요소의 합과 평균, 최대값, 최소값 출력
'''
n=list()# n=[]
for i in range(0, 10):
    n.append(int(input('num:')))

s = 0
for i in n:
    s+=i    #합 계산
    print(i, end=', ')
print()

f = s/len(n)    #평균계산

m1=m2=n[0]  #m1:최대값, m2:최소값
for i in n:
    if m1<i: #최대값 찾기
        m1=i

    if m2>i: #최소값 찾기
        m2=i

print('합:', s, '/ 평균:', f)
print('최대값:', m1, '/ 최소값:', m2)

#bubble sort

for i in range(0, len(n)-1):
    for j in range(0, len(n)-1-i):
        if n[j]>n[j+1]:
            tmp = n[j]
            n[j] = n[j+1]
            n[j+1] =tmp

n = [8, 3, 6, 10, 9, 1, 7, 2, 4, 5]
print(n)
search_num = int(input('search_num:'))

#i가 0-n까지 if n[i]==search_num 을 만족하는 방이 있는가를 비교
flag = True
for i in range(0, len(n)):
    if search_num==n[i]:
        print(i, '번째 방에 있음')
        flag = False    #flag가 True이면 값이 없다. False이면 찾았다
        break

if flag==True:
    print('not found')


#insert sort

for i in range(1, len(n)):#i:자기 자리 찾을 값의 위치
    tmp=n[i]               #i위치의 값이 지워지지 않게 tmp 옮겨놓음
    j=i-1               #j: i의 앞 위치로 i값의 위치를 찾기위해 비교할 대상의 위치
    while j>=0 and n[j]>tmp:
        n[j+1]=n[j] #j위치의 값을 뒤로 한칸 이동
        j-=1        #j를 한칸 앞으로 이동
    j+=1
    n[j]=tmp


n = [8, 3, 6, 10, 9, 1, 7, 2, 4, 5]
print(n)
#select sort
for i in range(0, len(n)-1): #i: 정렬할 위치
    min=i                   #min: 최소값의 위치. 초기값으로 i값 할당
    for j in range(i+1, len(n)):    #j: 최소값을 찾기 위해 한칸씩 위치 이동할 인덱스로 사용
        if n[min] > n[j]:           #min 위치의 값, 즉 최소값보다 더 작은 값을 만나면(j번째 방에서)
            min = j                 #최소값의 위치를 j로 변경. 이 동작을 j가 리스트 끝까지 도달할때까지 반복
    if min != i:                #60번줄에서 min에 i 값을 할당했기 때문에 min이 이동하지 않았다면 i에 최소값이 있는 경우
        tmp = n[min]            #위 경우에는 자리 바꿀 필요없음
        n[min] = n[i]           #그런데 min과 i가 같지 않다면 min이 최소값 있는 위치로 이동한 것이고 그 최소값이 i위치의
        n[i] = tmp              #값으로 들어가야 함. 그러므로 min과 i가 같지 않으면 두 위치의 값을 swap

print(n)
#이진 탐색
search_num = int(input('search_num:'))
f=0  #f: 리스트 검색 시작위치
l=len(n)-1  #l: 리스트 검색 마지막위치
while f<=l:#시작위치와 끝위치가 역전되지 않는한 반복
    m=(f+l)//2  #리스트 중간 위치 찾기
    if n[m]>search_num:     #중간값보다 찾는 값이 작으면 찾는 값이 중간값 앞에 있음
        l=m-1               #l를 중간 앞으로 이동
    elif n[m]<search_num:   #중간값보다 찾는 값이 크면 찾는 값이 중간값 뒤에 있음
        f=m+1               #f를 중간값 뒤로 이동
    else:                   #n[m]==search_num 인 경우로 m번째 방에서 찾음을 의미
        print('found. idx:', m) #break로 루프 빠져나옴
        break

if f>l:     #f>l은 위 루프에서 break로 종료되지 않았음을 의미하고 이는 찾는 값이 없음을 의미
    print('not found')


#리스트는 요소의 타입에 제한이 없다
#정수, 문자열, 리스트, 객체...

a = [[1,2,3], [4,5,6]] #a는 요소 2개.

for k in a:
    print(k)

for i in a:
    for j in i:
        print(j, end=', ')
    print()


a = [[0,0,0], [0,0,0]]
print(a)

for i in range(0, 2):
    for j in range(0, 3):
        a[i][j] = i*3+j+1

print(a)
'''
# ============================
# 3명 학생의 이름, 번호, 국, 영, 수 점수를 입력받아 총점, 평균을 출력하시오
'''
data = [[], [], []]
title = ['name', 'num', 'kor', 'eng', 'math', 'total', 'avg']
for i in range(0, len(data)):  # data 리스트 길이만큼(3) 반복
    for cnt in range(0, 5):  # 입력
        d = input(title[cnt] + ': ')
        if cnt != 0:  # 입력받은 값이 이름이 아니면
            d = int(d)  # 정수로 변환
        data[i].append(d)
    data[i].append(data[i][2] + data[i][3] + data[i][4])
    data[i].append(data[i][5] / 3)

for i in title:
    print(i, end='\t')
print()

for i in data:
    for j in i:
        print(j, end='\t')
    print()
'''