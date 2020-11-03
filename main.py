# 피드백 : 코드를 봤을때 직관적으로 볼 수 있게 만들기. 예를 들면, dan과 같이 알아볼 수 있도록 하기.
# git :
'''
 git add -A
 git commit -m "수정 한 내용"
 git push -f origin master
'''
# 2020년 11월 4일
# [과제]
# 1. 주소록 만들기
# 내용 : 이름 전화번호 주소
# 1. 추가
# 2. 검색(이름)
# 3. 수정
# 4. 삭제 (이름)
# 5. 전체 출력
# 6. 종료

# 2. 피보나치 수열 100개 출력 (피보나치 수열 이란? : 앞수와 더해서 결과값이 나오게 할 것. Ex)1, 1, 2, 3, 5, 8, 13... )


# 주소록 구현
# [내가한 것]
'''
list = []
prompt = """
1. 추가
2. 검색(이름)
3. 수정
4. 삭제
5. 전체 출력
6. 종료
Enter number :
"""
# 2중 배열 사용
userList = []
number = 0
while number != 6:
    print(prompt)
    number = int(input())

    # 예시 : list = [[이름,번호,주소],[이름,번호,주소]]
    if number == 1:
        print("[추가]")
        name = input("이름 :")
        phoneNum = int(input("전화번호 :"))
        address = input("주소 :")

        userInfo = [name, phoneNum, address]
        print(userInfo)

        userList.append(userInfo)
    elif number == 2:
        print("검색 입력")
        choice = int(input("검색할 사람의 성함을 입력해주세요 :"))
        # TODO : 리스트에서 찾으면 검색한 사람의 인포메이션이 나올 수 있도록 없으면, 해당 사람이 없습니다 메세지 띄울것
    elif number == 3:
        print("수정 입력")
        choice = int(input("수정할 목록을 선택해주세요 :"))
        # TODO : enumerate 사용해서 목록 보여줄 수 있도록 하기.
    elif number == 4:
        print("삭제 입력")
        choice = int(input("삭제할 목록을 선택해주세요 :"))
        # TODO : enumerate 사용해서 목록 보여줄 수 있도록 하기.
    elif number == 5:
        print("전체출력 입력")
        print(userList)
'''
# [강사님께서 구현한 것]
'''
num = []  # 빈 리스트 생성
flag = True
while flag:
    menu = input("1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.종료")
    if menu == "1":
        print("추가선택")
        x = int(input("숫자입력:"))
        num.append(x)  # 끝에 추가하는 메서드이다.
    elif menu == "2":
        print("검색선택")
    elif menu == "3":
        print("수정선택")
    elif menu == "4":
        print("삭제선택")
    elif menu == "5":
        print("전체출력선택")
        print(num)
    elif menu == "6":
        print("종료선택")
        flag = False
    else:
        print("잘못된 메뉴")
'''
# [수업]

# break 예문
# 점수를 입력 받는데 0~100 이 범위를 벗어나면 다시 입력받음.
'''
score = -1
while 100 < score or score < 0:
    score = int(input('score : '))
print(score)
'''
'''
while True:  # 무한루프 레이블 만드는법 알아보기. 시간되면
    score = int(input('score : '))
    if 0 <= score <= 100:
        break
print(score)
'''

# continue : 루프진행
'''
for i in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
    if i % 2 == 1:  # 2로 나눈 나머지가 1 즉 홀수 이면,
        continue  # continue 를 실행. continue 를 만나면 처음 loop 로 진행한다. 즉 무시한다.
    print(i, end=", ")
    # 즉, 짝수 출력하는 코드가 됨.
'''
# 주소록 만들기
# [강사님께서 구현한 것]
'''
num = []  # 빈 리스트 생성
flag = True
while flag:
    menu = input("1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.종료")
    if menu == "1":
        print("추가선택")
        x = int(input("숫자입력:"))
        num.append(x)  # 끝에 추가하는 메서드이다.
    elif menu == "2":
        print("검색선택")
    elif menu == "3":
        print("수정선택")
    elif menu == "4":
        print("삭제선택")
    elif menu == "5":
        print("전체출력선택")
        print(num)
    elif menu == "6":
        print("종료선택")
        flag = False
    else:
        print("잘못된 메뉴")
'''

# 강사님 말씀
# 반복문의 활용도와 차이점
# for : 리스트, 문자열, 나열된 값들을 처리할 때 활용
# while : 조건에 의해서 반복하고자 할떄

'''
# 마지막 쉼표 없애기
data = [12, 45, 56, 67]
for i in data:
    print(i, end=", ")
print()

for index, i in enumerate(data):  # 변수를 2개(앞이 인덱스, 뒤에는 값) 넣어서 인덱스와 요소를 함께 추출한다.
    print("data[", i, "]", "index:", index)
print()

# [강사님께서 구현한 코드]
ch = ", "
for index, i in enumerate(data):
    if index == len(data) - 1:  # 인덱스가 마지막 이면, -1 해준 이유는 리스트는 0부터 출력되기떄문,
        ch = "\n"  # 줄을 그냥 바뀌줌
    print(i, end=ch)
print()
'''
# 정 삼각형 역 방향 그리기
'''
size = int(input("크기 :"))
for i in range(size):
'''

# 정 삼각형 그리기
'''
size = int(input("숫자를 입력하세요 : "))
for i in range(size):
    print((' ' * (size - i)) + ('*' * (i * 2 + 1)))
'''

# 직 삼각형 그리기
# [내가 한 것]
'''
number = int(input("크기 입력 :"))

for j in range(0, number):
    for i in range(0, number):
        if j >= i:
            print("*", end=" ")
    print(" ")
'''
# [강사님께서 한 것]
'''
size = int(input("size :"))
for i in range(1, size + 1):  # 줄수
    for j in range(0, i):  # i번 줄에 출력될 *갯수
        print("*", end="")
    print()
'''
# 직 삼각형 그리기 역 방향
# [내가 한 것]
'''
numberR = int(input("크기 입력 :"))

for jR in range(0, numberR):
    for iR in range(0, jR):
        sum = iR + jR
        if sum >= iR:
            print("*", end=" ")
        else:
            print(" ", end="")
    print(" ")
'''
# 위 아래 비교해서 뭐가 아닌지 구분하기.
'''
number = int(input("숫자를 입력하세요 : "))
for i in range(number):
    for j in range(number):
        sum = i + j
        if sum < number - 1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print(" ")
'''
# [강사님께서 한 것]
# TODO : 이해해서 사용해보기
'''
size = int(input("size:"))
for i in range(1, size + 1):  # 줄수
    ch = " "
    for j in range(size, 0, -1):  # i번 줄에 출력된 캐릭터 개수
        if j == i:  # 출력할 캐릭터가 *로 바뀌는 시점
            ch = "*"
        print(ch, end="")
    print()
'''
# 2단부터 9단 까지 출력
'''
dan = 2
i = 1
for i in range(1, 10):
    for dan in range(1, 10):
        print(dan, "*", i, "=", dan * i, end="\t")
    print()
'''
'''
number = int(input("크기 입력:"))

for j in range(0, number):
    for i in range(0, number):
        if i > j:
            print("*", end="")
    print()
'''

# 약수 출력
'''
num = int(input("num:"))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()
'''

# 3단 출력 for, range() 사용
# [내가 한 것]
'''
dan = int(input("단 :"))

for i in range(1, 10):
    print(dan, "*", i, "=", dan * i)
'''
# [강사님께서 한 것]
'''
dan = 3
for o in range(1, 10):
    print(dan, "*", o, "=", dan * o)    
'''
# 변수 선언 안해줘도 됨
'''
for i in range(1, 5):
    print(i, end="")
print()

# range(시작값, 끝값, 증가값) << range 함수 정의
for i in range(1, 10, 2): # 2씩 더해서 출력 증가할 값을 설정해줌. 기본값은 1이다.
    print(i, end="")
print()

for i in range(1, 10, 4): # 4씩 더해서 출력
    print(i, end="")
print()
'''

# 리스트 숫자의 합을 구함
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
sum = 0

for i in nums: 
    sum += i
print(sum)
'''
# 숫자 나열하기.
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
# while 문 예제
while i < len(nums):  # len 함수는 리스트의 길이를 계산해 준다. 문자열을 넣으면 문자수를 계산해준다.
    print(nums[i])
    i += 1
print("리스트 길이 :" + str(len(nums)))  # String에 같이 넣을 경우 형 변환 해줘야 한다.
# for 문 예제
for i in nums:
    print(i)
print(nums)
# for 문 문자열 예제
s = "adfasdfadfd"
for x in s:
    print(x, end=", ")

print()

# for 문 문자열 제한 에제
for i in range(1, 5): # 숫자 제한 하기.
    print(i, end=", ")
'''

# 문자열 나열하기.
'''
s = "adfasdfadfd"
i = 0
while i < len(s):
    print(s[i], end=", ")
    i += 1
'''
'''
str = "fmaldksmflks"
i = 0 # << 0으로 초기화 하기.
while i < len(str):
    print(str[i], end=" ") #[i] << 주의하기.
    i += 1
'''
# 리스트에 있는 값을 반복문으로 불러오는 간단한 예제
'''
arr = [1, 2, 3, 4, 5]
i = 0
while i < 5:
    print(arr[i])
    i += 1

i = 0
while i < 5:
    arr[i] = (i + 1) * 10
    i += 1
'''

# [자습]
# 이중 배열로 아이템 구매 할 수 있게 만들기.
'''
money = 10000
list = ["1. 카타나", "2. 도끼", "3. 권총"]
while True:
    print(list)
    ItemNumber = int(input("어떤 아이템을 구매하시겠습니까? : "))

    if ItemNumber == 1 and money >= 10:
        print(list.pop(0) + "을(를) 구매하셨습니다.")
        money = money - 10
        list.insert(0, "판매완료")

    elif ItemNumber == 2 and money >= 10:
        print(list.pop(0) + "을(를) 구매하셨습니다.")
        money = money - 10
        list.insert(1, "판매완료")

    elif ItemNumber == 3 and money >= 10:
        print(list.pop(0) + "을(를) 구매하셨습니다.")
        money = money - 10
        list.insert(2, "판매완료")

    elif money == 0:
        print("돈이 부족합니다.")
        break
    else:
        print("이미 구매가 된 제품입니다.")
        '''
'''
money = 10000
list = ["1. 카타나", "2. 권총", "3. 도끼"]
while money == 0:
    while True:
        list = ["1. 카타나", "2. 권총", "3. 도끼"]
        print(list)
        print("남은 돈 : " + str(money))
        number = int(input("어떤 아이템을 구매하시겠습니까?"))

    if number == 1:
        print(list.pop(0) + "을(를) 구매했습니다.")
        list.insert(0, "판매 완료")
        print(list)
        money -= 1
        print("남은 돈 : " + str(money))
    elif number == 2:
        print(list.pop(1) + "을(를) 구매했습니다.")
        list.remove(1)
        money -= 1
        print("남은 돈 : " + str(money))
    elif number == 3:
        print(list.pop(2) + "을(를) 구매했습니다.")
        list.remove(2)
        money -= 1
        print("남은 돈 : " + str(money))
    else:
        print("잘못 입력됬습니다.")
'''
# 배열에 대한 간단한 이해
'''
list = [1, "이", "3"]
print(list.pop(1))  # pop은 해당 인덱스 값을 복사해온다.
'''
# 아래로 갈 수록 별 적어 지도록 구현(크기의 오른쪽 부분부터 찍힘)
'''
number = int(input("숫자를 입력하세요 : "))

for i in range(number):
    for j in range(number):
        sum = i + j
        if sum < number-1:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print(" ")
'''
# 아래로 갈 수록 별 많아 지도록 구현
'''
number = int(input("숫자를 입력하세요."))
for i in range(number):
    for j in range(number):
        if i >= j:
            print("*", end=" ")
    print(" ")
'''
# for 문에 대한 간단한 이해
'''
for i in range(10):  # 인트형의 변수 i를 1부터 10까지의 길이로 선언,
    print(str(i + 1) + "번")  # 인트형의 변수 i를 string 형태로 바꾸어서 출력한다. 주의해야할 사항은 길이는 항상 0부터 카운터가 된다는 점이다.
'''

# 2020년 11월 3일

# [과제]

# 1. 구구단 한단 출력 (단수 입력 받음.)
# 예시 3*1=3
# 예시 3*2=6 이런식으로
# [내 코드]
'''i = 1

number = int(input("숫자 입력 : "))
while i <= 9:
    sum = number * i
    print(number, '*', i, '=', sum)
    i += 1'''
# [강사님 코드]
'''
dan = int(input("단수 : "))
i = 1
while i < 10:
    print(dan, "*", i, "=", dan * i)
    i += 1

'''
# 2. 구구단 2-9단 모두 출력 (위와 같은 예시로 출력 할 것.)
# [내 코드]
'''
j = 1
while j <= 9:
    i = 2
    while i <= 9:
        sum = i * j
        print(i, '*', j, '=', sum, end='\t')
        i += 1
    j += 1
    print('')
'''
# [강사님 코드]
'''
dan = 2
while dan < 10:
    i = 1
    print(dan, "단")
    while i < 10:
        print(dan, "*", i, "=", dan * i)
        i += 1
    dan += 1
    print()
'''
# 3. 1~100사이의 소수(솟수 : 약수가 1과 자기자신만 있는 수) 출력
# [내 코드]
# TODO : 다시 구현하기.
'''
j=0
check = True
number = int(input("단 :"))

while j <= number:
    i = 2  # 나눌 수
    if i >= j:
        while i <= 100:
            count = 0  # 약수 확인 변수
        number = 1  # 숫자 증가 변수
        while number <= i:
             if i % number == 0:  # 만약 나누어 진다면, 약수로 판별
                 count += 1
                 number += 1  # 숫자 증가
    if count == 2:  # 약수의 갯수 2개 즉 솟수면 출력
        print(i, end=" ")
    i += 1
'''
# [강사님 코드]
'''
num = int(input("num:"))
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print()
'''

# 4. 삼각형1 (크기입력받음)
'''
*
**
***
****
*****
'''
# [내 코드]
'''
number = int(input('숫자를 입력해주세요.'))
# 3을 입력,

i = 1
while i <= number:
    j = 1
    while j <= i:
        print('*', end=" ")  # 오른쪽으로 별을 찍음,
        j += 1
    print()  # 한칸 아래로 내려감
    i += 1
'''
# [강사님 코드]
# 5. 삼각형2 (크기입력받음)
'''
    *
   **
  ***
 ****
*****
'''
# [내 코드]
'''
number = int(input('숫자를 입력해주세요.'))
i = 1
while i <= number:
    j = 1
    while j <= number:
        sum = i + j
        if sum > number:
            print("*", end=" ")  # 오른쪽으로 별을 찍음,
        else:
            print(" ", end=" ")

        j += 1
    print()  # 한칸 아래로 내려감
    i += 1
'''
# [강사님 코드]
# 6. 삼각형3 (크기입력받음)
'''
  *  
 ***
*****
'''
# [내 코드]
'''
number = int(input("숫자를 입력하세요 : "))
i = 0
while i < number:
    print((' ' * (number - i)) + ('*' * (i * 2 - 1)))
    i += 1
'''
# [강사님 코드]

# [수업내용]
# 2중 루프
'''i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print('#', end="")
        j += 1
    print()
    i += 1'''

# 값을 입력해서 약수 출력하기.
# 강사님꼐서 한 것
'''num = int(input('숫자를 입력해주세요 : ')) # 약수를 구할 숫자
i = 1 #나누는 숫자
while i <= num:
    if num % i == 0:
        print(i, end=', ')

    i += 1'''

# 내가 한 것
'''while True:
    number = int(input('숫자를 입력해주세요 : '))
    break

count = 0
print(number, "의 약수 : ", end='')
for a in range(1, number + 1):
    if number == a:
        print(a)
        count += 1
    elif number % a == 0:
        print(a, end=', ')
        count += 1

print(number, "의 약수의 총 개수 :", count)
'''
'''i = 1
while i <= 3:
    print('#', end=',')
    i += 1'''

# 1부터 100까지 더하기
'''
sum = 0
number = 1
while number <= 100:
    sum += number
    number += 1
    print('총 합 :', sum)
    '''

# 1~100사이의 짝수만 추출하기.
'''
i = 2
while i <= 100:
    print(i)
    i += 2

for i in range(1, 101):
    if i % 2 == 1:
        print(i, end=",")
        print()
        '''

# 입력된 정수에 따라서 학점이 다르게 나올 수 있도록 한다.
# 강사님께서 한 것
'''
import sys


score = int(input("score(0-100):"))
while score > 100 or score < 0: #반복해라 뒤에나오는 조건이 True가 될 동안.
    print('잘못된 점수')
    score = int(input("score(0-100):"))

    #sys.exit()  # 프로그램 종료

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
'''

'''
score = int(input("score:"))
if 90 <= score <= 100:
    print("A학점")
elif 80 <= score < 90:
    print("B학점")
elif 70 <= score < 90:
    print("C학점")
elif 60 <= score < 90:
    print("D학점")
else:
    print("F학점")
    '''

# 내가한 것
'''
score = int(input("점수를 입력하세요"))
if score >= 90:
    print("A학점")
elif score < 90 and score >= 80:
    print("B학점")
elif score < 80 and score >= 70:
    print("C학점")
elif score < 70 and score >= 60:
    print("D학점")
elif score < 60:
    print("F학점")
    '''

# 성별과 나이를 입력받아서 성별:여, 나이:20세 이상만 입장가능
# 조건 모두 만족시 입장가능출력. 하나ㅏㄹ도 불만족시 입장불가능출력

# 강사님께서 한것
'''
gender = input('gender(f/m):') #파라미터안에 f또는 m를 입력받는다는 선언이다.
age = int(input('age:'))

if gender == 'f' and age >= 20:
    print("입장가능")
else:
    print('입장불가능')
'''

# 내가 한것
'''
gender = str(input("성별을 입력하세요."))
age = int(input("나이를 입력하세요."))

if gender=="여":
    if age >= 20:
        print("입장 할 수 있습니다.")
    else:
        print("나이가 부족합니다.")
else:
    print("입장 할 수 없습니다.")
    '''

# 홀수 짝수 구분하기.
'''
number = int(input("숫자를 입력하세요"))
if number%2==0:
    print("짝수")
else:
    print("홀수")
    '''

# 입출력 예시
'''
name = input("이름을 입력해주세요.")
print("안녕하세요 "+name+"님")
'''

# 반복문 예시1
'''

prompt = """
1.add
2.Del
3.List
4.Quit
Enter number : 
"""
number = 0
while number != 4:
    print(prompt)
    number = int(input())
    '''

# 반복문 예시2

'''
coffee = 10
while True:
    money = int(input("돈을 넣어주세요 : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1

    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
'''
# 위와 같이 선언하면 4가 나오지 않는 이상 무한 루프돈다.
