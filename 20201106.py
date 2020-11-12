import sys
import os

# 네모네모로직 알아보기.
# 피드백 : 코드를 봤을때 직관적으로 볼 수 있게 만들기. 예를 들면, dan과 같이 알아볼 수 있도록 하기.
# 피드백 : 다양하게 많이 해봐야 한다. 코딩테스트를 잘 봐야 인정 받음.
# 최종으로 어떤 프로젝트 진행 할 지 고민해보기.
# Vo Dto = valueObject, DataTranceObject
# Service = 기능을 제공해주는 클래스 (추가, 수정, 삭제, 등등......)
# Dao = database access object 데이터접근객체
# functools.wraps, 변수 데코레이터
# MVC 패턴이란 ? = 모델 뷰 컨트롤를 의미한다. 모델 = 데이터 비즈니스로직, 뷰 = UI, 컨트롤 = 제어하는 부분을 말한다.
# MVC 이점 : 조립할 수 있다.
# Plsql 할줄 알아야한다.
# 참고 사이트 : https://lancoding.tistory.com/


# git :
'''
 git add -A
 git commit -m "수정 한 내용"
 git push -f origin master
'''


# TODO : 2020년 00월 00일
# [과제]
# [수업]


# 맨마지막 숫자만 출력해주는 코드
"""
f = open("btest.txt", 'rb')
f_copy = open("btest1.txt", 'w')

f.seek(-1, 2)
ch = str(f.read(1)).split("\'")[1]  # b값 바이너리 값을 없애기 위해서 split 사용
print(ch[0])
f.close()
"""


f = open("btest.txt", 'r')
s = f.readlines()
print(s[-1])
# s[2].truncate(1)








# TODO : 2020년 11월 11일
# [과제]
# [수업]

# 클래스 :
# 캡슐화(VO) - 하나의 객체 표현
# DAO - 디비작업 전담 클래스 : 저장소에 저장, 검색, 수정, 삭제...
# SERVICE - 비즈니스 로직. 사용자에게 제공하는 기능 정의, 메서드는 사용자의 기능을 구행하는데 필요한 값을 입력받고, DAO를 사용해 저장소에 저장, 수정, 삭제를 완료
# 메뉴클래스 (UI) - 메뉴 돌림
# main - 메뉴 실행

# TODO : 잘 이해하기. class 의 로직.
'''
class Test:
    def __init__(self, x, y):
        self.x = x  # public : 클래스 밖에서 잘 보임.
        self.__y = y  # private : 클래스 밖에서 안 보임.
        # 멤버변수는 항상 private으로 해줘야 한다.
        # 기능 호출하는 변수는 외부에서 변경할 수 있도록 public으로 제어한다.

    def printXY(self):
        print("x:", self.x, "y:", self.__y)


    # setter : private 멤버를 외부에서 수정, 값을 넣을(set) 수 있게 하는 메서드
    # setter 만드는법
    def setY(self, y):
        self.__y = y

    # getter : private 멤버를 외부에서 값을 읽을 (get) 수 있게 하는 메서드
    def getY(self):
        return self.__y


def main():
    t1 = Test(10, 20)
    t1.printXY()

    print("t1.x:", t1.x)
    t1.setY(300)
    print("t1.y:",t1.getY())


main()
'''
'''
class Test:
    x = 0  # 클래스 변수 자바의 static 변수와 비슷하다, (객체 소속이 아니라 클래스 소속이다.)

    # 모든 객체가 공유. 클래스이름. 변수명
    def __init__(self):
        self.y = 0  # 맴버 변수. 객체마다 생성되는 변수, 객체이름.변수명
        z = 0  # 지역변수 이 함수가 끝나면 없어진다.

    # 정적변수도 있지면 정적메서드도 있다.
    @staticmethod  # 언더 테이션 (@는 컴파일러에게 알려주는 역할을 한다.)
    def printNum(r):  # 클래스 메서드. 멤버변수 사용없고, 정적메서드는 self가 없다.
        print('정적 메서드')
        PI = 3.14
        w = r * r * PI
        print('원의 넓이 :', w)


def main():
    Test.printNum(5) # << 5를 넣어줌.
    t1 = Test()
    Test.x += 1
    t1.y += 1
    print('x:', Test.x, ', y:', t1.y)

    t2 = Test()
    Test.x += 1
    t2.y += 1
    print('x:', Test.x, ', y:', t2.y)

    t3 = Test()
    Test.x += 1
    t3.y += 1
    print('x:', Test.x, ', y:', t3.y)


main()
'''

'''
f = open("btest.txt", 'rb')
f_copy = open("btest1.txt", 'w')

for i in range(1, len(f.read()) + 1):
    f.seek(-i, 2)
    #f.read(1).decode()
    ch = str(f.read(1)).split("\'")[1]  # b값 바이너리 값을 없애기 위해서 split 사용
    print(ch, end="")
    f_copy.write(ch)

f.close()
# f_copy.close()
'''

# TODO : 2020년 11월 10일
# [과제]
# [수업]

# 문제

# Product :
#   [제품번호, 제품명, 가격, 수량]
# 추가 검색(번호로 검색) 수정(번호로 검색) 삭제(번호로 검색) 전체목록

"""
class Product:
    def __init__(self, number, name, price, amount):
        self.number = number
        self.name = name
        self.price = price
        self.amount = amount


class Dao:
    def __init__(self):
        self.datas = []  # DB 역할을 함.

    def insert(self, s):
        self.datas.append(s)
        print("")

    def search(self, number):
        for i in range(len(self.datas)):
            if self.datas[i] == number:
                return print(i)
            else:
                print("\n정보 없음\n")

    def edit(self, number):
        for i in range(len(self.datas)):
            data = self.datas[i][1]
            if data == number:
                return i
            else:
                print("\n정보 없음\n")

    def remove(self, number):
        for i in range(len(self.datas)):
            data = self.datas[i][1]
            if data == number:
                return i
            else:
                print("\n정보 없음\n")

    def selectAll(self):
        return self.datas


class Service:  # UI
    def __init__(self):
        self.dao = Dao()

    def addProduct(self):  # 학생 정보 하나를 추가.
        number = int(input("제품 번호 :"))
        name = input("제품 명 :")
        amount = int(input("제품 수량 :"))
        price = int(input("제품 가격 :"))

        s = Product(number, name, amount, price)
        self.dao.insert(s)

    def searchProduct(self):  # 번호로 제품 검색
        number = int(input("검색할 제품 번호 :"))
        self.dao.search(number)

    def editProduct(self):
        number = int(input("수정할 제품 번호 :"))
        self.dao.edit(number)

    def removeProduct(self):
        number = int(input("삭제할 제품 번호 :"))
        self.dao.remove(number)

    def printAll(self):
        all = self.dao.selectAll()
        for i in all:
            i.printInfo()

"""
prompt = """1. 추가
2. 검색(번호로 검색)
3. 수정(번호로 검색)
4. 삭제(번호로 검색)
5. 전체목록
6. 종료"""
"""

def main():
    service = Service()
    while True:
        print(prompt)
        number = int(input("숫자 입력 :"))
        if number == 1:
            service.addProduct()
            print()
        elif number == 2:
            service.searchProduct()
            print()
        elif number == 3:
            service.editProduct()
            print()
        elif number == 4:
            service.removeProduct()
            print()
        elif number == 5:
            service.printAll()
            print()
        elif number == 6:
            sys.exit(0)
        else:
            print("다시 입력하세요.")


main()
"""
# 좌표를 담을 클래스
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printPoint(self):
        print('(', self.x, ',', self.y, ')')


def main():
    points = [Point(1, 2), Point(3, 4), Point(5, 6)]  # 저장.
    for i in points:
        i.printPoint()


main()
'''
# 성적처리 프로그램 (클래스 사용)
# [강사님께서 구현하신 코드]
# - MVC 패턴 -
"""
class Student:  # 한 학생의 정보 및 성적처리하는 클래스
    def __init__(self, name, number, kor, eng, math):
        self.name = name
        self.number = number
        self.kor = kor
        self.eng = eng
        self.math = math

    def calculrator(self):
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3

    def printInfo(self):
        print("name :", self.name)
        print("number :", self.number)
        print("kor :", self.kor)
        print("eng :", self.eng)
        print("math :", self.math)
        print("total :", self.total)
        print("avg :", self.avg)
        print("---------------------")


class Dao:  # 데이터를 저장하는 역할. 저장소에 추가, 검색, 수정, 삭제 등의 작업 수행
    def __init__(self):
        self.datas = []  # DB역할을 함.

    def insert(self, sum):
        self.datas.append(sum)

    def selectAll(self):
        return self.datas


class Service:  # 비지니스 로직 사람들에게 기능 제공할 서비스.
    def __init__(self):
        self.dao = Dao()

    def addStudent(self): # 학생 정보 하나를 추가.
        name = input("이름 :")
        number = int(input("번호 :"))
        kor = int(input("국어 :"))
        eng = int(input("영어 :"))
        math = int(input("수학 :"))
        s = Student(name, number, kor, eng, math)
        s.calculrator()
        self.dao.insert(s)

    def printAll(self):
        all = self.dao.selectAll()
        for i in all:
            i.printInfo()


def main():
    service = Service()
    service.addStudent()
    service.addStudent()
    service.addStudent()
    service.printAll()


main()
"""
# 클래스를 사용하는 이유 캡슐화
# 객체 : 프로그램으로 모델링 할때 구성 요소들 (사람,사물,개념)
# 클래스는 사용자가 직접 정의하는 타입
# 변수를 만들려면 먼저 타입 정의
'''
userList = []
class Member:
    def setData(self, name, tel):
        self.name = name
        self.tel = tel

    def print(self):
        print(self.name)
        print(self.tel)

prompt ="""1. 추가
2. 전체보기
3. 종료"""
'''"""
def main():
    m1 = Member()
    while True:
        print(prompt)
        number=int(input("입력할 숫자 :"))
        if number == 1:
            name = input("이름 :")
            tel = input("번호 :")
            memberList = [name, tel]
            userList.append(memberList)
            
        
    
    
    
    

    m1.setData(name, tel)

    print("m1.name :", m1.name)
    print("m1.tel :", m1.tel)
    print(userList)
    print()


    m1.print()"""

'''
def main():
    m1 = Member()
    m1.setData('aaa','111')
    m1.print()
    print()

    m2 = Member()
    m2.setData('bbb', '222')
    m2.print()
    print()

    m3 = m1 # 객체의 얕은 복사 , 참조값 복사
    print("변경전 m3 :",end=" ")
    m3.print()
    m1.name="!!!"
    print("변경후 m3 :", end=" ")
    m3.print()
    print("변경후 m1 :", end=" ")
    m1.print()

main()
'''
'''
class Student:
    number = 1
    StudentList = []
    name = "최정훈"
    kor = 10
    eng = 20
    math = 30
    def write(s,name,kor,eng,math):
        s.name = input("이름 :")
        s.kor = int(input("국어 :"))
        s.eng = int(input("영어 :"))
        s.math = int(input("수학 :"))
    
def main():
    s = Student()
    print(s.number, s.name, s.kor, s.eng, s.math)
main()'''

# 클래스는 맴버 변수와 메서드로 구성된다
# 맴버 변수 : 객체 안의 변수
# 사람의 정보 - 이름 나이 3명
# 맴버 변수 : 객체안의 변수
# 메서드 : 클래스 안에 정의한 함수 첫 파라메터는 항상 self(객체 자신) 호출할 때 이 파라메터는 전달 안함
'''
class Person:  # 클래스 안에 있으면 메서드로 말함.
    def __init__(self, name, age):  # 생성자, 함수, 객체 생성시 호출되는 함수, 객체 초기화
        self.name = name  # self.name >> 맴버 변수 self가 없으면 지역변수이다.
        self.age = age

    def printPerson(self):  # 메서드
        print("이름 :", self.name)
        print("나이 :", self.age)


def func1():
    print("asdfghqwe")


def main():  # 밖에 있으면 함수.
    p1 = Person("최정훈", 20)
    print("name :", p1.name) # 개별적으로 불러옴.
    print("name :", p1.age)
    print()
    print(p1)
    p1.printPerson()
    print()
    p1 = Person("aaa", 111)  # 클래스로 변수 생서 => 객체
    p1.printPerson()
    p2 = Person("bbb", 222)
    p2.printPerson()
    p3 = Person("ccc", 333)
    p3.printPerson()


main()
'''
# 클래스 정의와 객체 생성
'''
#test Class
class Student:

    cnt = 0 # 클래스 변수

    def setVal1(s,val): # 첫 번재 파라메터는 self(현재 객체)
        s.num = val # 객체 멤버변수 정의
    def setVal2(s,val):
        s.name = val
    def printVal(s):
        print(s.num)
        print(s.name)

def main():
    s1 = Student()
    print(s1.cnt)
    s1.setVal1(12)
    s1.setVal2('aaa')
    s1.printVal()
main()
'''
# raise : 예외 객체를 던짐
# 사용자 정의 예외 클래스
'''
class MyError(Exception):  # Exception 은 파이썬에서 모든 예외의 조상 클래스 이다.
    def __init__(self, msg):  # 생성자. 객체 생성시 한번 호출되는 함수로 객체를 초기화한다.
        # self 는 자바에서 this와 같은 역할을 한다.
        self.msg = msg # self.msg는 맴버벼수, 파라메터는 현재 함수가 종료하면 없어지지만 
        # 멤버변수는 객체가 살아있는 한 계속 존재한다 

def printNum():
    num = int(input('num (1~5 사이만 입력 :)'))

    if num < 1 or num > 5:
        raise MyError("잘못된 값")  # 예외 발생 시킨다.

    print("input value :", num)


def main():
    try:
        printNum()
    except MyError as e:
        print("예외발생", e)


while True:
    main()
'''
# 예외처리 예제
'''
a = 5
b = 0
c = [1, 2, 3]
d = {"name": "aaa", "age": 12}
print("0으로 나누기 전")
try:  # 예외가 발생할 만한 코드를 묶는다.
    print("try블록 시작")
    print(a / b)
    print("0으로 나눈 뒤")
    c[5] = 10
    print(d["tel"])
    print("c[5]=10")
    '''
'''
except ZeroDivisionError:  # 예외 처리 블록 발생한 예외 이름이 같아야 받는다
print("예외 발생")

except (ZeroDivisionError, IndexError, KeyError) as e:  # 한꺼번에 처리가능
    print("예외발생 :", e)

print()

try:
    print("c[5]=10")
    c[5] = 10
    print("위에서 중단되면 여기는 출력 안됨")
except Exception as e:  # 예외 처리 블록 발생한 예외 이름이 같아야 받는다 또는 이와같이 처리하면 모든 예외 객체를 받아서 처리할 수 있다.
    print("모든 예외 처리")
    print(type(e))

else:
    print("예외 발생하지 않음")
finally:  # 프로그램이 끝나기 전에 무조건실행되는 블록
    print("예외가 발생했던 안했던 무조건 실행되는 블록")
print("위에서 중단되면 여기는 출력 안됨")
'''
# 예외처리
# try :
# 예외가 발생 할 만한 코드
# except 예외명 :
# try 블록에서 발생한 예외 중 동일한 이름의 예외만 받아서 처리
# else
# try 블록에서 예외가 발생하지 않았을 때 실행될 코드 구현
# finally
# 정상종료, 비정상종료 모두 종료 되기전 실행되는 블록

# 리스트 - 변경가능 요소도 변경가능 가장 많이 사용됨
# 셋 - 변경가능 , 요소변경 안됨
# 튜플 - 변경안됨. 요소변경 가능 리스트를 요소로 지정 우회적으로 요소추가가능
# 딕셔너리 키와값을 맵핑해서 저장 키를 통해서 빠른 검색을 지원 웹과 연결 시 파라메터 전달 활용

# <입출력>
# 표준입력 : sys.stdin (키보드로 읽는 함수 제공)
# 표준출력 : sys.stdout (콘솔에 출력하는 함수 제공)
# 표준에러 : sys.stderr (콘솔에 표준 에러 메시지 출력하는 함수 제공)

# <표준 입출력을 쉽게 할 수 있는 함수>
# input()
# print()
# <파일 입출력>
# open("파일경로","오픈모드") - 파일 오픈으로
# 오픈 모드 - r/w/a rb/wb/ab  r+/w+/a+ 읽고쓰기
# TODO : 모드마다 차이점 정확히 이해하기.

# f= open("파일경로","오픈모드") - 파일 오픈으로
# f.read() - 파일 읽기
# f.write() - 파일 쓰기
# f.close() - 파일 닫기
# f.seek() - 커서 위치를 변경
# f.tell() - 현재 위치 반환


# TODO : 2020년 11월 09일
# [과제]
# 메모장 만들기. 프로그램시작하면 하위에 메모디렉토리를 생성한다.
prompt = """1. 파일 읽기
2. 파일 쓰기
3. 파일 삭제
4. 파일 전체 삭제
5. 종료"""
'''

# 1. 읽기 (읽고 싶은 파일을 선택 할 수 있게 구현하기.)
def readFile():
    print("파일 읽기!")


# 2. 쓰기 (파일명을 입력받는데, 중복이 되면 안됨. 중복이되면 다시 입력 할 수 있게끔,
# 또는 새로쓰게하거나, 이어쓰거나)
# 무한루프로 계속 파일 작성 할 수 있게 구현하기. /exit > 종료 > 저장
def writeFile():
    # os.chdir("../")
    # new_dir = input("생성할 디렉토리 이름을 입력하세요 :")
    # while True:
    #     if os.path.isdir(new_dir) == True:
    #         print("이미 중복되는 디렉토리가 있습니다.")
    #
    #     elif os.path.isdir(new_dir) == False:
    #         os.mkdir(new_dir)  # 디렉토리 생성하는 메서드
    #         break

    print("파일 쓰기!")
    arr = []
    file_name = input("파일 명:")
    while True:
        string = input("(작성 완료 하려면 /exit 입력!) :")
        if string == "/exit":
            break
        arr.append(string + '\n')
    print(arr)
    file = open(file_name, "w")
    file.writelines(arr)
    file.close()


# 3. 삭제 () (파일 목록 > 삭제 > 파일 선택 > 파일 삭제)
def removeFile():
    print("파일 삭제!")


# 4. clear (메모 전체 삭제)
def removeFileAll():
    print("파일 전체 삭제!")


# 5. 종료
def exit():
    print("종료!")
    sys.exit(0)


os.chdir("파일")  # 디렉토리를 바꿔줌
print("현재 :", os.getcwd())
# 리스트에 파일들을 담놓고 컨트롤 할 수 있다.

while True:

    print(prompt)
    number = int(input("숫자 입력 :"))
    if number == 1:
        readFile()
    elif number == 2:
        writeFile()
    elif number == 3:
        removeFile()
    elif number == 4:
        removeFileAll()
    elif number == 5:
        exit()
'''
# [수업]


# 입출력
# 스트림 : 단방향
# 입력 스트림 : 밖에서 프로그램쪽으로 데이터 흐름 구현
# 출력 스트림 : 프로그램에서 박으로의 데이터 흐름 구현

# 1. 표준스트림
# sys : 표준 시스템 객체나 함수가 정의. 표준입력, 표준출력, 표준에러 정의
# 표준입력 : sys.stdin
# 표준출력 : sys.stdout
# 표준에러 : sys.stderr

# 2. 스트림의 읽기/쓰기 함수
# 1) 입력 스트림의 읽기 함수
# read(size) : size 만큼 읽음
# read(): 전체내용 읽음 >> 파라미터에 파일이나 읽고싶은 내용을 넣으면 읽어줌.
# readLine(): 한 줄 읽음

# 2) 출력 스트림의 쓰기 함수
# write(str) : str을 씀
# write() ...

# 추가 참고 : https://lancoding.tistory.com/29?category=743320

# 파일제어함수들
# truncate(size) - size 크기로 파일 절삭
# rename(old,new) - 파일명을 old에서 new로 변경
# remove(파일명) - 파일 삭제.

# r+ : 읽고 쓰기모드 . r특징 가지고있음. 없는 파일 열면 에러
# w+ : 읽고 쓰기모드 . w특징 가지고있음. 없는 파일 열면 새로생성하여 오픈 (기존 내용 지움.)
# a+ : 읽고 쓰기모드 . a특징 가지고있음. 기존 내용 있으면 이어쓰기.


'''
def main():
    print("현재 작업 디렉토리 :", os.getcwd())
    print()

    new_dir = input("생성할 디렉토리 이름을 입력하시오 :")
    print(new_dir, "존재하나요?", os.path.isdir(new_dir))  # 존재 유무확인.
    os.mkdir(new_dir)
    print(new_dir, "디렉토리 생성!")
    print(new_dir, "존재하나요?", os.path.isdir(new_dir))
    print()

    os.chdir(new_dir)
    print(new_dir, "로 디렉토리 이동~!")
    print("현재 작업 디렉토리!:", os.getcwd())

    list1 = ["a.txt", "b.txt", "c.txt"]
    for file_name in list1:
        file = open(file_name, "w")
        print(file_name, "파일 생성~! 내용으로 파일명 작성!")
        file.write(file_name)
        file.close()
    print()

    os.chdir("../")
    print("상위 디렉토리로 이동~!")
    print("현재 작업 디렉토리! :", os.getcwd())

    files = os.listdir(new_dir)
    print(new_dir, "디렉토리의 파일 목록")

    for file_name in files:
        file = open(new_dir + "/" + file_name, "r")
        print(file_name, "(content :", file.read(), ")")
        file.close()
    for file_name in files:
        print(new_dir + "/" + file_name, "파일삭제!")
        os.remove(new_dir + "/" + file_name)

    print(new_dir, "디렉토리의 파일 목록")
    print(os.listdir(new_dir))
    print()

    print(new_dir, "디렉토리 삭제")
    os.rmdir(new_dir)
    print(new_dir, "존재하나요?", os.path.isdir(new_dir))


main()
'''
# 디렉토리 제어 (메모장 만들때 필요함)
# 경로에는 절대 경로와 상대 경로가 있다.
# 절대 경로 = /User/~~
# 상대 경로 = ../상위 폴더를 표시해준다. . 은 현재위치 .. 은 상위 디렉토리
"""
import os
os.getcwd() #현재 작업 디렉토리 명 반환
os.chdir(path) # 작업 디렉토리는 path로 변경
os.mkdir(path) # 폴더 만들때 사용하면됨 디렉토리 생성 없을때 맨처음 한번만 실행. 
os.rmdir(path) # 디렉토리 삭제
os.listdir(path) # 그 디렉토리안에 파일 이름들을 반환해준다. (리스트에 담아서) 디렉토리 파일 목록 리스트로 반환
os.path.isfile(path) # path의 파일이 존재하면 True, 아니면 False >> 중복확인할때 사용한다. 이어쓸건지 or 새로 파일 명 입력 받을지 
os.path.isdir(path) # path의 디렉토리가 존재하면 True, 아니면 False 
"""

'''
import os


def main():
    file = open("rem.txt", "w+")
    file.write("hello mate")
    file.seek(0)
    print(file.read())
    file.close()

    os.remove("rem.txt")

    file = open("rem.txt", "r")  # 파일이 없기 때문에 여기서 에러 발생
    print(file.read())
    file.close()


main()
'''
# 파일명 수정 테스트
'''
import os

def main():
    old_name = input("이름을 수정할 파일명을 입력하세요:")
    new_name = input("새 파일명을 입력하세요:")

    os.rename(old_name, new_name)

    file = open(new_name, "r")
    print(file.read())
    file.close()
main()
'''
# 파일크기 자르기 테스트
'''
def main():
    string = "123456789012345667890"
    file = open("f.txt", "w")
    file.write(string)
    file.truncate(10)  # 파일의 크기를 10으로 절삭해줌.
    file.close()

    file = open("f.txt", "r")
    print(file.read())
    file.close()
main()
'''
# 다른 파일에 복사하기. (숫자 거꾸로 입력 되게)
'''
f = open("btest.txt", 'rb')
f_copy = open("btest1.txt", 'w')

for i in range(1, len(f.read()) + 1):
    f.seek(-i, 2)
    #f.read(1).decode()
    ch = str(f.read(1)).split("\'")[1]  # b값 바이너리 값을 없애기 위해서 split 사용
    print(ch, end="")
    f_copy.write(ch)

f.close()
# f_copy.close()
'''

# asdfasdf
# seek(3,0) == f부터 읽음
# seek(-1,1) == d부터 읽음
# seek(-4,2) == m부터 읽음 2는 - 음수로 정의해야함.
"""
def main2():
    f = open('btest.txt', 'w')
    str1 = '1234567890'
    f.write(str1)
    f.close()

    print(str1)
    f = open('btest.txt', 'rb')  # 위치 제어하려면 바이너리 모드로 오픈해야함
    print(f.read(3))
    print("현재 위치:", f.tell())

    f.seek(5)
    print("현재 위치:", f.tell())
    print("맨 앞에서 5위치의 문자 :", f.read(1))

    f.seek(10, 0)
    print("현재 위치:", f.tell())
    print("맨앞에서 10 위치의 문자", f.read(1))

    f.seek(3, 1)
    print("현재 위치:", f.tell())
    print("현재 위치에서 -3위치의 문자:", f.read(1))

    f.seek(-3, 2)
    print("현재 위치:", f.tell())
    print("맨뒤에서-3위치의 문자:", f.read(1))

    f.close()


main2()
"""
# 바이너리 읽고 쓰기
# 모드 : "rb" - 읽기 / "wb" - 쓰기 / "ab" - 이어쓰기
# 강사님 꼐서 구현한 것
# 파일 복사 하기.
'''
img1 = open('dami.jpeg', 'rb')
img2 = open('dami2.jpeg', 'wb')

data = img1.read()
img2.write(data)

img1.close()
img2.close()
'''
# 내가 한 것
'''
def main():
    f = open("dami.jpeg", "rb")  # 바이너리 읽기 모드로 오픈
    b_data = f.read()
    print("바이너리 데이터")
    print(b_data)
    f.close()

    f = open("dami.jpeg","wb")
    f.write(b_data)
    f.close()
main()
'''

# 리스트 이용해서 한번에 써서 저장하기.
'''
def main3():
    arr = []
    while True:
        str1 = input('str(끝내려면 /exit입력):')
        if str1 == "/exit":
            break
        arr.append(str1 + "\n")
    print(arr)
    f = open('b.txt', 'w') # 리스트나 튜플에 저장된 여러 라인을 한번에 써준다.
    f.close()


main3()
'''
# 스플릿메서드
# 복사파일 만들때 효과적임.
'''
s = "aaa,vvv,bbb,ddd,ccc,eee,fff,rrr,aaa,sss,ddd,fff"
s2 = s.split(",")
print(s2)
for i in s2:
    print(i)
'''

# 문제
# 파일을 쓰기모드로 오픈해서 키보드로 입력받은 애용을 파일에 저장하시오.
# 파일 이름도 입력 받을 것.
# /stop을 입력받을때 까지 반복하고 /stop 입력받으면 저장하고 빠져나옴
# 빠져나오면 파일 내용을 읽어줘서 콘솔에 출력해준다.
# 강사님께서 구현한 코드
'''
file_name = input("file name:")
file = open(file_name, "a", encoding="utf-8") # 파일 쓰기모드 오픈 : ocreate(파일 있으면 그 파일 열고 없으면 새로 생성)
# and otruncate(기존 쓰던 파일을 오픈하면 기존 내용을 모두 지움)
# attend모드는 계속 이어서 쓰게됨. 모드를 "a"로 바꿔주면됨.
while True:
    msg = input("입력 :")
    if msg == "/stop":
        break
    else:
        file.write(msg+"\n")
file.close()

file = open(file_name,"r",encoding="utf-8")
msg = file.read()
print(msg)

file.close()
'''
# 내가 구현한 코드
'''
def write():다
    file = open("testText.txt", "w", encoding="utf-8")

    while True:
        message = input("입력 내용 :")
        if message == "/stop":
            f = open("testText.txt", "r", encoding="utf-8")
            str1 = f.read()
            print(str1)
            f.close()

            break
write()
'''

'''
def main():
    f = open("a", "r", encoding="utf-8")
    str1 = f.read()
    print(str1)
    f.close()


main()


def main2():
    f = open("a", "r")
    while True:
        str1 = f.read(3)  # 3개씩만 읽어줌.
        if str1 == "":
            break
        print(str1)
    f.close()


main2()


def main3():
    f = open("a", "r")
    while True:
        str1 = f.readline()  # 한번씩 띄어쓰기 해줌.
        if str1 == "":
            break
        print(str1)
    f.close()


main3()


def main4():
    with open("a", "r") as f:
        str1 = f.read()
        print(str1)


main4()
'''
# 원본파일명과 타깃 파일명을 입력받아 복사하는 프로그램을 만드시오.
# 강사님 코드
'''
f1_name = input("원본 파일명:")
f2_name = input("복사 파일명:")

f1 = open(f1_name, 'r', encoding="utf-8")
f2 = open(f1_name, 'w', encoding="utf-8")

body = f1.read()
f2.write(body)

f1.close()
f2.close()
'''
'''def write():
    file = open("test.txt", "w", encoding="utf-8")
    message = input("안녕")
    file.write(message)
    file.close()


def read():
    file = open("test.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
    file.close()

write()
read()'''

'''
def read():
    f = open("a", "r", encoding="utf-8")  # open함수로 먼저 파일을 오픈해준다. 파일 이름, r = 이름
    str1 = f.read()
    print(str1)
    f.close()


def write():
    f = open("b.txt", "w", encoding="utf-8")
    msg = input("입력 : ") # 입력 할때마다 초기화된다.
    f.write(msg)

    f.close()


def readB():
    f = open("b.txt", "r", encoding="utf-8")  # open함수로 먼저 파일을 오픈해준다. 파일 이름, r = 이름
    str = f.read()
    print(str)
    f.close()



write()
readB()
'''
# 딕셔너리를 사용해서 3명의 성적표를 만들어라.
# 강사님께서 구현한 코드
# 3명 성적
'''
users = {}  # 모든 학생의 정보로 번호를 키로 사용,
# 각 키에 맵핑되는 값은 그 번호 학생의 정보를 딕셔너리로 갖는다.
keys = ["name", "kor", "eng", "math", "total", "avg"]
for i in range(0, 3):
    s = {}  # 한 학생의 정보를 담는다.
    t = 0  # 총점을 담을 변수
    num = int(input("num :"))  # 번호를 입력 받음, 이 번호는 users의 키로사용한다.
    for j in range(0, 4):  # 위 번호 유저의 name~math를 입력받는다.
        s[keys[j]] = input(keys[j] + ": ")
        if j != 0:
            s[keys[j]] = int(s[keys[j]])
            t += s[keys[j]]  # 총점계산
    s[keys[4]] = t
    s[keys[5]] = t / 3
    users[num] = s  # 위에서 입력받은 키값을 users에 넣는다.

for num in users:
    print("num : {}".format(num), end=" / ")
    s = users[num]
    for i in s:
        print("{}:{}".format(i, s[i]), end=" / ")
    print()
'''
# 내가 구현한 코드
prompt = """1. 추가
2. 전체보기
3. 종료"""
"""
user = {}
# user = {{name: "ddd", kor : "asdf", total:23, avg:26},{},{}}




def add():
    name = input("이름 :")
    kor = int(input("국어 성적 :"))
    eng = int(input("영어 성적 :"))
    math = int(input("수학 성적 :"))
    total = kor + eng + math
    avg = kor + eng + math / 3

    user["이름"] = name
    user["국어"] = kor
    user["영어"] = eng
    user["수학"] = math
    user["총점"] = total
    user["평균"] = avg


def searchAll():
    for key, val in user.items():
        print(key, val)




while True:
    print(prompt)
    number = int(input("숫자 입력 :"))

    if number == 1:
        print("추가")
        add()
    elif number == 2:
        print("전체보기")
        searchAll()
    elif number == 3:
        sys.exit(0)
    else:
        print("다시 선택해주세요.")
"""
# 딕셔너리는 웹에 연동하기 위해서 많이 사용한다.

'''
t3 = (("일", "이", "삼"), ("사", "오"))

# 요소 값
for i in t3:
    for j in i:  # i: (1,2,3),(4,5)
        print(j)
print()
# 방 번호로 접근.
for i in range(0, len(t3)):
    for j in range(0, len(t3[i])):
        print(t3[i][j])
print()
print(t3[0][0])
print(t3[0][1])
print(t3[0][2])
print(t3[1][0])
print(t3[1][1])

prompt = """1. 추가
2. 종료"""


def add():
    print("요소 변경 불가.")
    print("다만, 요소의 리스트를 이용해 우회적으로 추가가능")


while True:
    print(prompt)
    number = int(input("숫자 입력 :"))
    if number == 1:
        add()
    elif number == 2:
        sys.exit(0)
    print()
    print(" 내용 ")
    for i in t3:
        print(t3.index(i))
    print()
'''
"""
list => 변할 수 있다. 요소 : 변할 수 있다.
set => 변할 수 있다. 요소 : 변할 수 없다.
tuple => 변할 수 없다. 요소 : 변할 수 있다.
dictionary => 키와 값 저장. d["name"] = "aaa"
"""
"""
딕셔너리 : 
- 키와 값을 같이 저장
- 요소의 추가, 변경, 삭제가능
- 키는 중복, 변경 안됨. 키는 숫자, 문자열, 튜플만 가능
- 값은 중복, 변경 허용. 값의 타입제한이 없다.

이미 존재하는 키로 추가할 경우, 추가되지 않고 수정이 된다.

"""

# API란? : Application Programing Interface - "(응용 프로그램 프로그래밍 인터페이스)는
# 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다.”

'''정처리 = {
    1: {
        '1번': "설명~",
        '2번': "설명~",
        '3번': "설명~",
        '4번': "설명~",
        '정답': 1
    },
    2: {
        '1번': "설명~",
        '2번': "설명~",
        '3번': "설명~",
        '4번': "설명~",
        '정답': 2
    },
    3: {
        '1번': "설명~",
        '2번': "설명~",
        '3번': "설명~",
        '4번': "설명~",
        '정답': 3
    },
    4: {
        '1번': "설명~",
        '2번': "설명~",
        '3번': "설명~",
        '4번': "설명~",
        '정답': 4
    }
}

print(정처리[1]['정답'])
print(정처리, end="\n")'''
"""
1번 : 문제풀기 (1번부터 20번까지 생성하고 전제 문제를 랜덤으로 돌려서 20문제만 추려낸다.)
 > 문제를 다 풀면 점수가 나온다. 문제당 점수는 5점으로 정한다.
2번 : 문제 전체보기

Manager 으로 로그인 하면 
1번 : 문제 생성
2번 : 문제 수정 
3번 : 문제 삭제
으로 인터페이스가 나올 수 있도록 구현하기. 
"""

# TODO : Test 구현

prompt = """1. 문제 추가
2. 문제 수정
3. 문제 삭제
4. 문제 찾기
5. 문제 전체보기
6. 문제 풀기
7. 종료
"""
'''
Q = {}

number = 1


def addQ():
    global number
    a = input("문제 내용 :")
    # 해당 숫자가 존재하면 + 해서 숫자를 하나씩 늘려간다.
    if number in Q[number]:
        number += 1
    else:

        Q[number] = a


def editQ():
    edit = int(input("수정할 문제의 번호 :"))


def removeQ():
    remove = int(input("삭제할 문제의 번호 :"))


def searchQ():
    searchQ = int(input("찾을 문제 번호 :"))
    print(Q[searchQ])


def searchAllQ():
    for key in Q:
        print("key :{} value: {}".format(key, Q[key]))
    # items() 또한 전체 출력을 할 수 있다.


def testQ():
    print("")


while True:
    print(prompt)
    number = int(input("숫자 입력 :"))
    if number == 1:
        addQ()
    elif number == 2:
        editQ()
    elif number == 3:
        removeQ()
    elif number == 4:
        searchQ()
    elif number == 5:
        searchAllQ()
    elif number == 6:
        testQ()
    elif number == 7:
        sys.exit(0)
'''
# TODO : [복습] 2020년 11월 6일
# [과제]
# 함수를 재정의해서 파라메터값으로 전달해서 주소록 재 구현하기.
# [수업]

# TODO : [복습 리스트]
# 변수 : 값 저장을 위해 메모리 할당

# 연산자
# 산술 : +, - , *, **, /, //, %
# 비교 : ==, !=, < , <= , > , >=
# 논리 : and , or , not
# 대입 : = , += , -=, *= , **=

# 제어문
# 조건문 : 조건 (True,False)을 반환하는 수식
# if 조건 :
#   실행문
# else:
#   실행문

# <조건이 여러개>
# if 조건1:
#   실행문
# elif 조건2:
#   실행문
# else:
#   실행문

# 반복문
# <for문 - 리스트 같은 나열의 길이 만큼 반복>
# for i in [1,2,3,4]: 4번 반복 >> in sthg = sthg 안에서 반복 즉 만큼 반복.
#   print(i)
# for i in "asdfqwer": 8번 반복
#   print(i)
# for i in range() >> range 함수 > range(시작값, 끝값, 간격(기본:1))
# range 함수는 값의 범위를 지정하면 그 범위의 정수를 생성하여 반환

# list = []
# for i in range(10):
#     print(i)
#     list.append(i+1)
#     print(list)

# List[0] = 1
# List[1] = 2
# 위의 예시구현

# [내가 구현한 내용]

# number = int(input("숫자 범위 :"))
# List = []
# for i in range(number):
#     List.append(i + 1)
#     print("List[", i, "] =", List[i])
# print()
#
# # [강사님 구현]
# li = [1, 2, 3, 4, 5]
# for i in li:
#     print(i, end=" ")
#
# print()
# print()
# for i in range(0, len(li)):
#     print("li[", i, "]=", li[i])
# print()
# for idx, i in enumerate(li):
#     print("li[", idx, "]", i)

# <while문 조건에 의해서 반복>
# while 조건 : #조건이 True 일때 까지 반복.

# 아이디 비번 맞으면 로그인 성공 아니면 로그인 실패 메세지 띄우기

# [내가 구현]
# id = "wjdgns"
# pwd = "123123"
#
# id = input("아이디 :")
# qw = input("비밀번호 :")
# while True:
#     if id == "wjdgns" and qw == "123123":
#         print("로그인 성공")
#         break
#     else:
#         print("로그인 실패")
#         break

# [강사님 구현]

# id = "aaa"
# qwd = "111"
# while True:
#     id2 = input("id :")
#     qwd2 = input("qwd :")
#
#     if id == id2 and qwd == qwd2:
#         print("로그인 성공")
#         break
#     else:
#         print("다시입력")
#         continue
#         print("하지마")
# print("메뉴 : 1. 내정보확인 2. 내정보수정 3. 로그아웃")

# 함수 객체 활용 - 룩업 테이블 : 각각의 코드값을 비교해서 함수를 호출해준다. 점프해주는 방식은 좋은 방법이 아니다.
# def error1():
#     print("1번 에러 발생")
#
#
# def error2():
#     print("2번 에러 발생")
#
#
# def error3():
#     print("3번 에러 발생")
#
#
# def error4():
#     print("4번 에러 발생")
#
#
# def error5():
#     print("5번 에러 발생")
#
#
# def main():
#     ec = 2
#     if ec == 1:
#         error1()
#     elif ec == 2:
#         error2()
#     elif ec == 3:
#         error3()
#     elif ec == 4:
#         error4()
#     elif ec == 5:
#         error5()
#
#
# def main2():
#     number = int(input("숫자 :"))
#     ec = number
#     f = [error1, error2, error3, error4, error5]
#     f[ec - 1]()
#
#
# main2()
#
#
# def onEvent(f):
#     print("핸들러가 등록되었습니다.")
#     f()
#     print()
#
#
# def myHanbler1():
#     print("1번 이벤트 핸들러입니다.")
#
#
# def myHanbler2():
#     print("2번 이벤트 핸들러입니다.")
#
#
# def myHanbler3():
#     print("3번 이벤트 핸들러입니다.")
#
#
# def main():
#     onEvent(myHanbler1)
#     onEvent(myHanbler2)
#     onEvent(myHanbler3)
#
#
# main()

# 피보나치 수열 만들기 (1~100)
# 1. 재귀함수, 2. 루프 3. 리스트
# 1. 재귀함수
# 2. 루프
# 3. 리스트
# [내가한 것]
# def fibo(n):
#     if n < 2:
#         return n
#     a = 0
#     b = 1
#     for i in range(n - 1):
#         a = b
#         b = a + b
#     return b
#
# def main():
#     for n in range(1, 101):
#         print(n, fibo(n))
# main()

# [강사님께서 한 것]
# 1 1 2 3 5 8 13...
# 재귀 피보나치
# def fibo1(x):
#     if x <= 2:
#         return 1
#     else:
#         return fibo1(x - 1) + fibo1(x - 2)
#
#
# def main():
#     for i in range(1, 101):
#         print(i, fibo1(i))
#         if i % 10 == 0:
#             print()
#
# main()
# 루프 피보나치
# def fibo2(cnt):
#     # x , y , z
#     x = y = 1
#     print(x, "", y, end=" ")
#     for i in range(3, cnt + 1):  # 3번째 자리 부터 계산하기 위해 3~
#         z = x + y
#         print(z, end=" ")
#         if i % 10 == 0:
#             print()
#         x = y
#         y = z
#     print()
#
#
# def main():
#     fibo2(100)
#
# main()
# 리스트 피보나치

# def count(fiboList):
#     number = [0] * fiboList
#     for i in range(0, len(number)):
#         if i < 2:
#             number[i] = 1
#         else:
#             number[i] = number[i - 1] + number[i - 2]
#     for i in number:
#         print(i, end=",")
#
#     print()
#
#
# # [강사님]
# def fibo3(cnt):
#     nums = [0] * cnt
#     nums[0] = nums[1] = 1
#
#     for i in range(2, cnt):
#         nums[i] = nums[i - 1] + nums[i - 2]
#     print(nums)
#
#
# def main():
#     count(100)
#     fibo3(100)
#
#
# main()

# def fibo(num):

#     if num == 1 or num == 2:
#         return 1
#     else:
#         return fibo(num - 1) + fibo(num - 2)
#
#
# def main():
#     for i in range(1, 51):
#         print(fibo(i), end=",")
#     print()
#
# main()

# factorial 계산하는 함수 만들기
# [내가한 것]

# def num():
#     number = 1
#     for i in range(1, 6):
#         number *= i
#
#     return number
#
#
# print(num())

# [강사님꼐서한 것]
# def func(x):
#     s = 1
#     for i in range(1, x + 1):
#         s *= i
#     return s
#
#
# def f2(x):  # 끝나는 기준을 정확히 기술
#     if x == 1:
#         return 1  # 무한 루프 방지
#     else:
#         return x * f2(x - 1)
#
#
# def main():
#     number = int(input("숫자 입력 :"))
#     print(number, "!:", f2(number))
#
#
# main()

# . 재귀함수 : 되도록이면 지양한다. 이유는 소스를 많이 잡아먹기 때문. 시험으로 간혹 나온다.
# def factorial(num):
#     if num ==1:
#         return 1
#     else:
#         return num*factorial(num-1)

# return
# 1. return : 함수 종료(함수는 return이 없어도 더 이상 실행할 문장이 없으면 종료)
# 2. return 값 : 함수 종료 및 값 반환
# 3. return None : 파이썬은 리턴값이 없는 함수도 None이 반환됨, None은 값이 없음을 나타내는 상수
'''
def printHello():
    print("Hello")


def main():
    result = printHello()
    print("result :", result)
    print("result type :", type(result))
    '''

# 지역 변수
'''''''''main()


def f1(x):
    if x == "windows":
        def win():
            print("윈도우즈 입니다.")
    elif x == "linux":
        def linux():
            print("리눅스 입니다.")
    else:
        def other():
            print("다르 종류의 os 입니다.")

    # win()
    linux()
    # other()





def main():
    f1("linux")

main()'''''''''

# 전역변수와 지역변수
# 전역변수 : 함수 밖에서 정의한 변수로 변수 정의 아래에 있는 모든 함수와 코드에서 사용가능
# 지역변수 : 함수 안에서 정의한 변수로 선언한 함수 안에서만 사용가능
'''
a = 10

def f1(x):
    b = 20
    print("a:", a, "b:", b, "x:", x)


def f2():  # 에러 : b와 x는 f1()의 지역변수 이므로 다른 함수에서 사용 불가.
    print()


# print("a:", a, "b:", b, "x:", x)

def f3():
    a = 100  # a: 지역변수로 만들어짐.
    print("f3()의 지역변수 a:", a)


def f5():
    global a  # a:전역변수 자바는 사실상 전역 변수가 없다...
    a = 200
    print("f5()에서 전역변수 설정 a:", a)


def f4():
    print()


def main():
    f1(30)
    f2()
    f3()
    f5()
    f4()

main()
'''

# 전역변수의 visible
'''def f1():
    print("f1()")
    print("a :", a)
    print("b :", b)
    print("c :", c)


def f2():
    print("f2()")
    print("a :", a)
    print("b :", b)
    print("c :", c)


def f3():
    print("f3()")
    print("a :", a)
    print("b :", b)
    print("c :", c)


a = 10
f1()
b = 20
f2()
c = 30
f3()'''

# 파이썬 함수의 다양한 아규먼트(인자)
# 1. 요구 인자 : 함수에서 일반적으로 사용하는 방법으로 파라메터 개수와 순서를 맞추어 호출
# 2. 키워드 인자 : 파라메터 순서에 맞추지 않아도 됨. 단 이 인자가 어느 파라메터로 전달될지 지정 해야함
'''def f1(age, firstName, lastName):
    print("5년 뒤 나이:", age + 5)
    print("name:", lastName + " " + firstName)


f1(5, "aaa", "bbb")
# f1("aaa", "bbb", 6)  # 이와같이 인자의 순서가 안 맞으면 에러가 발생한다.
f1(lastName="aaa", firstName="bbb", age=6)  # 순서를 지정해주면 에러가 발생하지 않는다.'''
# 3. 디폴트 인자 : 파라메터 기본값을 지정하여 생략가능.
# 4. 가변 인자 : 파라메터의 개수 가변. 인자값을 튜플에 담아 전달
'''def test(*nums):
    print(type(nums))
    for i in nums:
        print(i)
        list.append(i)


list = []


def main():
    test(1, 2, 3)
    test(11, 22, 33, 44, 55, 66, 77, "asd", [1, 2, 3])


main()
print(list)'''

# immutable params test
'''
def paramsTest1(num, msg):  # immutable param test
    print("변경 전")
    print("num:", num, "msg:", msg)
    num = 300
    msg = "함수안"
    print("변경 후")
    print("num:", num, "msg:", msg)


def main():
    n = 10
    m = "main 내부"
    print("함수 호출 전")
    print("n:", n, ",m:", m)
    paramsTest1(n, m)
    print("함수 호출 후")
    print("n:", n, ",m:", m)


main()
print("\n\n\n\n")


# mutable params test

def paramsTest2(list1, list2):  # mutable param test
    print("변경 전")
    print("list1:", list1, "list2:", list2)
    list1 = [100, 200]
    list2[0] = 10
    list2[2] = 30
    print("변경 후")
    print("list1:", list1, "list2:", list2)


def main():
    li1 = [1, 2, 3]
    li2 = [11, 22, 33, 44]
    print("함수 호출 전")
    print("li1:", li1, ",li2:", li2)
    paramsTest2(li1, li2)
    print("함수 호출 후")
    print("li1:", li1, ",li2:", li2)


main()
'''
# TODO : [응용해보기] immutable 인자와 mutable 인자
# a = 10
# print(a)
# a = 20  # 값이 바뀌면 참조 값도 바뀌는데 immutable
# print(a)
#
# b = [1, 2, 3]  # b에는 참조값 100.  b[0]는 1이 아니라. 1의 참조값이 들어가 있는 것이다. b[1]도 2의 참조값을 갖고 있는것.
# print(b)
# b[0] = 30  # b[0]이 1에서 30으로 참조값이 바뀐다. -> mutable 이다.
# print(b)

# def add(a, b):
#     return a + b
#
#
# def main():  # 함수의 다형성
#     print(add(1, 2))
#     print(add("aaa", "bbb"))
#     print(add(1.23, 2.435))
#     print(add([1, 2], [10, 11, 12]))
#
#
# main()

# # class 란? :
# def f1():
#     print("최", end="")
#
#
# def f2():
#     print("정", end="")
#
#
# def f3():
#     print("훈", end="")
#
#
# def f4(x):  # 파라메터로 튜플 받음. 튜플 : immutable 요소로 개수, 값 변경 불가
#     for i in x:
#         print(i, end=" ")
#     print()
#
#
# # params = None -> 디폴트 인자. 호출시 생략 가능.(예외처리)
# # 변수 데코레이터 알아보기.
# def select(f, params=None):  # 함수 포인터 or 함수의 참조값을 받아오는 파라메터. / 핸들러 등록 함수, params : f의 파라메터
#     # 핸들러 등록 함수 , 이벤트가 발생하면 자동으로 호출되서 그 처리를 하는 함수
#     if params == None:
#         f()  # 파라메터 값이 f1이라면 f1()/# 파라메터 값이 f2이라면 f2()/# 파라메터 값이 f3이라면 f3()
#     else:
#         f(params)
#
#
# def main():
#     print("메인 호출")
#     select(f1)
#     select(f2)
#     select(f3)
#     print()
#     select(f4, (1, 2, 3))
#     # f1()#함수를 호출하면 그 함수가 사용할 스택 메모리를 할당
# main()

#
# number = int(input("숫자 :"))
# while number == 4:
#     if number == 1:
#         print(select(f1), end="")
#         print()
#
#     elif number == 2:
#         select(f2)
#         print()
#     elif number == 3:
#         select(f3)
#         print()

# a = select(f1)
# b = select(f2)
# c = select(f3)

# print()
# f1()
# print()
# f2()
# print()
# f3()

# TODO : [복습] 2020년 11월 5일

# [과제]
# 1. 함수를 사용해서 주소록 만들기.
# < 선택 과제 >
# 1. 숫자 넣기
# 빈 리스트를 하나 만들고, 요소에 숫자를 넣기
# 메뉴 : 추가(중복 안됨), 검색, 수정, 삭제, 전체목록, 전체 삭제 ,종료 만들기.
# 2. 주소록 만들기 (함수 사용해서 만들기.)
# 메뉴 : 추가(중복 안됨), 검색, 수정, 삭제, 전체목록, 전체 삭제 ,종료 만들기.
# [[이름,전화,주소],[],[]] 이름을 기준으로 검색, 중복체크, 수정, 삭제하기.

# # [자습]
# def name(num):  # 함수를 정의하고 해당 파라메터값 안에 변수를 생성한다.
#     for i in num:  # 반복문을 변수에 참조하게 만든다.
#         print(i)
#
#
# s = []
# for i in range(5):  #
#     nameInput = input("이름을 입력하세요 :")
#     s.append(nameInput)
#
# name(s)
'''
    # 리스트의 길이를 2로 나눠서 중간 지점을 정해주고 3개의 케이스로 나눈다 같거나 작거나 크거나
    # 첫번쨰가 마지막과 같거나거나 작을때 까지 while문을 돌려줌,, 라스트를 옮겨옴. 첫번째를 뒤로 옮겨감.
    First = 0  # f: 리스트 검색 시작위치
    Last = len(userList) - 1  # -1을 하는 정확한 이유 알아보기. 배열 맨 끝방을 찾기위해 -1 을 한것.  0~9 인 경우는 길이. 합은 10이니까 9를 입력해주기 위해서 -1 을 해준것.

    while First <= Last:  # 시작위치와 끝위치가 역전되지 않는 한 반복 시켜줌, 만약 아닐경우 반복문을 빠져나옴.
        m = (First + Last) // 2  # //은 소수점까지 없애준다. # 리스트 중간 위치 찾기.
        print("First 위치 :", First)
        print("Last 위치 :", Last)
        print("위치 추적:", m)
        if userList[m][m] > searchNum:  # list에 선언된 m이 검색한 숫자보다 더 클경우, 즉 검색된 숫자가 m보다 작을경우
            Last = m - 1  # last를 m보다 앞의 요소를 가르키게 만든다.
        elif userList[m] < searchNum:  # 검색한 숫자가 m보다 클 경우,
            First = m + 1  # First를 m의 한자리 뒤를 가르킬수 있도록 한다.
        else:
            print("번호 찾음: [", userList[m], "](인덱스 번호)")  # middle 값이 해당 요소에 오게되면 멈춤.
            break
    if First > Last:
        print("번호 못 찾음")
'''

# [다른 팀원 과제]
'''
numbers = []

def number_add():
    global numbers

    while True:
        number = int(input('Input number for add : '))

        if number in numbers:
            print(number, 'is already exist.')
        else:
            numbers.append(number)
            print('Add!')
            break

def number_search():
    global numbers

    number = int(input('Input number for search : '))

    if number in numbers:
        print('numbers[{0}] = {1}'.format(numbers.index(number), number))
    else:
        print('Not exist')

def number_modify():
    global numbers

    number = int(input('Input number for modify : '))

    if number in numbers:
        numbers[numbers.index(number)] = int(input('Input new number : '))
        print('Modify!')
    else:
        print('Not exist')

def number_delete():
    global numbers

    number = int(input('Input number for delete : '))

    if number in numbers:
        del numbers[numbers.index(number)]
        print('Delete!')
    else:
        print('Not exist')

def number_print():
    global numbers

    for number in numbers:
        print(number, end=', ')
    print('\b\b')


print('Start number program!')
while True:
    menu = int(input('1.add 2.search 3.modify 4.delete 5.print 0.end : '))

    if menu == 0:
        print('End number program..')
        break
    elif menu == 1:
        number_add()
    elif menu == 2:
        number_search()
    elif menu == 3:
        number_modify()
    elif menu == 4:
        number_delete()
    elif menu == 5:
        number_print()


print()


# 02
data = []

def IsDuplicate(name): # 이름 중복 체크
    global data
    names = [datum[0] for datum in data]

    if name in names:
        idx = names.index(name)
    else:
        idx = None

    return name in names, idx


def add_data():
    while True:
        name = input('Input name for add : ')

        if IsDuplicate(name)[0]:
            print(name, 'is already exist.')
        else:
            tel = input('Input telephone for add : ')
            addr = input('Input address for add : ')
            data.append([name, tel, addr])
            print('Add!')
            break

def search_data():
    global data

    name = input('Input name for search : ')
    isDuplicate, idx = IsDuplicate(name)

    if isDuplicate:
        print('name\ttelephone\taddress')
        for d in data[idx]:
            print(d, end='\t')
        print()
    else:
        print('Not exist')


def modify_data():
    global data

    name = input('Input name for modify : ')
    isDuplicate, idx = IsDuplicate(name)

    if isDuplicate:
        tel = input('Input telephone for modify : ')
        addr = input('Input address for modify : ')
        data[idx] = [name, tel, addr]
        print('Modify!')
    else:
        print('Not exist')

def delete_data():
    global data

    name = input('Input name for delete : ')
    isDuplicate, idx = IsDuplicate(name)

    if isDuplicate:
        del data[idx]
        print('Delete!')
    else:
        print('Not exist')

def print_data():
    global data

    if len(data) != 0:
        print('name\ttelephone\taddress')
        for datum in data:
            for d in datum:
                print(d, end='\t')
            print()
    else:
        print('No data..')

print('Start address book program!')
while True:
    menu = int(input('1.add 2.search 3.modify 4.delete 5.print 0.end : '))

    if menu == 0:
        print('End address book program..')
        break
    elif menu == 1:
        add_data()
    elif menu == 2:
        search_data()
    elif menu == 3:
        modify_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        print_data()
''' \
'''def func_add(li, val):
    if val in li:
        return False
    else:
        li.append(val)
        return True


def func_find(li, val):
    if val in li:
        return li.index(val)
    else:
        return None


def func_set(li, val, newval):
    idx = func_find(li, val)
    if idx is not None:
        li[idx] = newval
        return True
    else:
        return False


def func_del(li, val):
    if val in li:
        li.remove(val)
        return True
    else:
        return False


def func_print(li):
    print("리스트:", li)


nums = []
while True:
    menu = input("메뉴 (1:추가, 2:검색, 3:수정, 4:삭제, 5.전체목록, 6:종료):")
    if not menu.isdigit():
        continue
    menu = int(menu)
    # 추가
    if menu == 1:
        val = int(input("추가:"))
        if not func_add(nums, int(input("추가:"))):
            print("실패")
        func_print(nums)
    # 검색
    if menu == 2:
        val = int(input("검색:"))
        print(func_find(nums, val))
        continue
    # 수정
    if menu == 3:
        val, newval = int(input("수정:")), int(input("값:"))
        if not func_set(nums, val, newval):
            print("실패")
        func_print(nums)
    # 삭제
    if menu == 4:
        val = int(input("삭제:"))
        if not func_del(nums, val):
            print("실패")
        func_print(nums)
    # 전체출력
    if menu == 5:
        func_print(nums)
        continue
    # 종료
    if menu == 6:
        print("종료")
        break'''
# [내 과제]
'''
prompt = """
1. 추가
2. 검색(이름)
3. 수정
4. 삭제
5. 전체 출력
6. 전체 삭제
7. 종료
Enter number :
"""
def add():
    name = input("이름 :")
    phoneNum = int(input("전화번호 :"))
    address = input("주소 :")

    userInfo = [name, phoneNum, address]
    userList.append(userInfo)

def search():
    # 2진 탐색 방법
    searchName = (input("이름:"))
    for i in range(0, len(userList)):
        if userList[i][0] == searchName:
            print("정보 있음 :", userList[i][0], userList[i][1], userList[i][2])
            name, phone, address = userList[i][0], userList[i][1], userList[i][2]
            return
        else:
            print("정보 없음")

def edit():
    searchName = input("이름:")
    for i in range(0, len(userList)):
        if userList[i][0] == searchName:
            print("정보 있음 :", userList[i][0], userList[i][1], userList[i][2])
            quest = input("어떤 정보를 수정하시겠습니까? [이름, 번호, 주소] :")
            if quest == "이름":
                etName = input("수정할 이름 :")
                userList[i][0] = etName
            elif quest == "번호":
                userList[i][1] = input("수정할 번호 :")
            elif quest == "주소":
                userList[i][2] = input("수정할 주소 :")
            else:
                return
        else:
            print("정보 없음")

def remove():
    searchName = input("이름:")
    for i in range(0, len(userList)):
        if userList[i][0] == searchName:
            print("정보 있음 :", userList[i][0], userList[i][1], userList[i][2])
            quest = input("삭제 하시겠습니까? [예, 아니오] :")
            if quest == "예":
                userList.remove(userList[i])
                print("삭제 되었습니다.")
                break
            elif quest == "아니오":
                break
            else:
                return
        else:
            print("정보 없음")

def removeAll():
    quest = input("전체삭제 하시겠습니까? [예, 아니오] :")
    if quest == "예":
        userList.clear()

userList = []
number = 0
while number != 7:
    print(prompt)
    number = int(input())

    if number == 1:
        print("[추가]")
        add()

    if number == 2:
        print("검색")
        search()

    if number == 3:
        print("수정")
        edit()

    if number == 4:
        print("삭제")
        remove()

    if number == 5:
        print("전체 출력")
        print(userList)

    if number == 6:
        print("전체 삭제")
        removeAll()

    if number == 7:
        print("종료")

    if number >= 8:
        print("숫자를 다시 입력해주세요.")
'''
# [수업]

# [7교시]
# 다양한 반환값
# 정수를 반환
'''
def add(a, b):
    return print(a + b)
add(1, 4)
''' \
 \
'''
def add(a, b):
    return a + b


print(add(1, 4))  # 안쪽부터 동작한다.
'''

# 아래 리스트를 파라메터로 받아 합을 반환하는 함수 만들기.
# 평균을 반환하는 함수
# 최대값을 반환하는 함수
# 최소값을 반환하는 함수
'''
def hap(list1):
    s = 0
    for i in list1:
        s += i
    return s


# 평균
def avg(list1):
    s = hap(list1)
    return s / len(list1)


# 최대값
def max_val(list1):
    m = list1[0]
    for i in list1:
        if m < i:
            m = i
    return m


# 최소값
def min_val(list1):
    m = list1[0]
    for i in list1:
        if m > i:
            m = i
    return m


def max_min_val(list1):
    res = [list1[0], list1[0]]
    for i in list1:
        if res[0] < i:
            res[0] = i
        if res[1] > i:
            res[1] = i
    return res


def max_min_val2(list1):
    a = b = list1[0]
    for i in list1:
        if a < i:
            a = i
        if b > i:
            b = i
    return a, b  # 값을 2개 선언 하였으므로 2개를 리턴


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(hap(nums))
print(avg(nums))
print(max_val(nums))
print(min_val(nums))
print(max_min_val(nums))

r = max_min_val(nums)
print("max :", r[0])
print("min :", r[1])

x, y = max_min_val2(nums)  # 값이 2개
print("max :", x)
print("min :", y)
'''
# 나

# 강사님
'''# 합
def hap(list1):
    s = 0
    for i in list1:
        s += i
    return s


# 평균
def avg(list1):
    s = hap(list1)
    return s / len(list1)


# 최대값
def max_val(list1):
    m = list1[0]
    for i in list1:
        if m < i:
            m = i
    return m

# 최소값
def min_val(list1):
    m = list1[0]
    for i in list1:
        if m > i:
            m = i
    return m

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(hap(nums))
print(avg(nums))
print(max_val(nums))
print(min_val(nums))
''' \
 \
'''
# [자습]
def name(num):  # 함수를 정의하고 해당 파라메터값 안에 변수를 생성한다.
    for i in num:  # 반복문을 변수에 참조하게 만든다.
        print(i)


s = []
for i in range(5): #
    nameInput = input("이름을 입력하세요 :")
    s.append(nameInput)

name(s)
''' \
'''
def f4(x):
    for i in x:
        print(i, end=", ")
 

s = [1, 2, 3, 4, 5]  # TODO : [복습]
f4(s)
'''
# [6교시]
'''
# 함수 정의 : 이 함수는 이러하게 동작한다. 함수 수식을 작성
# 함수 호출 : 정의한 함수를 불러서(이름) 그 함수를 실행시킴 => 분기(함수코드)
# 다양한 형태의 함수들
# define에 이름을 지어줘서 지우는 함수, 추가하는 함수, 등등을 사용해서 만듦
# 함수안에 코드를 다 실행하면 함수는 종료한다.
# return 함수종료
def f1():
    print("파라메터 없고 리턴 값도 없다.")
    return  # 리턴을 만나면 강제종료됨.
    print("파라메터 없고 리턴 값도 없다.")
f1()

def f2(num):  # 파라메터의 타입이 고정되지 않기 때문에 어떤 값을 전달해도 받을 수 있음.
    # 하지만 함수 안에서 실행시 에러 발생할 수 있음
    if isinstance(num, int):  # 정수형 인 경우.
        print('num:', num / 3)
    else:  # 문자열일 경우
        if num.isdigit():  # digit = 숫자
            print('num:', int(num) / 3)
        else:
            print("알파벳은 계산 불가")


f2(3)
f2("123")
f2("asd")


def f3(name, choi):  # f3에 name이라는 파라메터를 넣음.
    print("name :", name, "|choi :", choi)
    print(name + choi)
f3("aaa", "asmdl")
f3(3, 2)


def f4(x):
    for i in x:
        print(i, end=", ")


s = [1, 2, 3, 4, 5]  # TODO : [복습]
f4(s)




''' \
'''
# 함수 정의
def f0(num):
    if num % 2 == 0:  # 나머지 값이 0이면 찾음,
        print(str(num), end="찾음")
        return  # 함수 종료 역할을 한다.
    else:
        print(num)


# 함수 호충
for i in range(0, 10):
    f0(i)
'''
# 구구단 출력 함수 정의
'''
def gugudan(dan):
    for i in range(1, 10):
        print(dan, i, dan * i)


# 반복문을 돌면서 범위를 정하고 구구단에 파라메터값 전달해서 넣어주기.
for i in range(2, 10):
    gugudan(i)
''' \
'''
List = []


def gugudanList(dan):
    danList = []
    List.append(danList)
    for i in range(2, 10):
        danList.append(i)
        numList = []
        print("number Of dan")
        print(danList)
        List.append(numList)
        for j in range(1, 10):
            numList.append(j)
            print("number")
            print(numList)





for i in range(2, 10):
    gugudanList(i)
    '''

# 5교시
'''
def gugudan(dan):
    for i in range(1, 10):
        print(dan, ' * ', i, ' = ', dan * i)


def f1(num):  # 약수 구하는 함수
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=', ')
    print()


def f2(num):
    res = []
    for i in range(1, num + 1):
        if num % i == 0:
            res.append(i)
    return res


for i in range(2, 10):
    gugudan(i)

f1(25)
l = f2(6)
print(l)
''' \
'''
def num(n):  # 약수 구하는 함수
    for i in range(1, n + 1):  # 이유: 1부터 파라메터로 받은 숫자까지 니까 길이가 0부터 24라서 +1을 해줌.
        if n % i == 0:
            print(i, end=" ")

def f2(num):  # 약수 구하는 함수
    res = []
    for i in range(1, num + 1):  # 이유: 1부터 파라메터로 받은 숫자까지 니까 길이가 0부터 24라서 +1을 해줌.
        if num % i == 0:
            res.append(i)  # 받은 약수를 리스트에 추가.
        return res

gugudan(3)
num(25)
l = f2(6)
print(l)
'''
# 단수를 파라메터로 받아 그 한단만 출력하는 함수 정의 및 호출하기
'''
def gugudan(dan):
    for i in range(1, 10):
        print(dan, i, dan * i)

for i in range(2,10):
    gugudan(i)
'''

# TODO : [복습] 2020년 11월 4일 - list
# [과제]
# 1. 전체 복습하기.
# 1-1. TODO : 피보나치 정렬 복습

# 1-2. TODO : 버블정렬, 추가정렬, 선택정렬 알고리즘 복습

'''
n = [5, 2, 4, 3, 1, 234, 4, 5, 34, 2, 3, 43, 234, 54, 23, 4, 23, 4, 1]  # 리스트 선언 해줌
print("bubbling sort")
for i in range(0, len(n) - 1):  # 0부터 리스트 n의 길이 까지 반복,
    for j in range(0, len(n) - 1 - i):  # 0부터 리스트 n의 길이 - i 번 까지 반복, 횟수 만큼
        if n[j] > n[j + 1]:
            # 스왑하는 부분
            tmp = n[j]
            n[j] = n[j + 1]
            n[j + 1] = tmp
print(n)

print("inserting sort")

for i in range(i, len(n)):  # for 문으로 리스트의 길이만큼 반복시작. [자기 자릴 찾을 값의 위치]
    tmp = n[i]  # 리스트의 맨 첫째 자리를 tmp 변수에 저장한다. [i 위치의 값이 지워지지 않게 tmp 옮겨놓음]
    j = i - 1  # [j는 i의 앞 위치로 i값의 위치를 찾기위해 비교할 대상의 위치를 선언해 준다.]
    while j >= 0 and n[j] > tmp:  # []
        n[j + 1] = n[j]  # [j 위치의 값을 뒤로 한칸 이동]
        j -= 1  # [j를 한칸 앞으로 이동]
    j += 1
    n[j] = tmp
print(n)

for selectNum in range(0, len(n) - 1):  # 리스트의 크기 만큼 반복해준다.
    minNum = selectNum  # 리스트의 첫번째 값을 minNum 변수에 넣어서 임시 저장해준다.
    for nextNum in range(selectNum + 1, len(n)):  # selectNum 의 반복문보다 1칸 뒤의 값을 시작점으로해서 리스트의 마지막
        if n[nextNum] < n[minNum]:
            minNum = nextNum
        n[selectNum], n[minNum] = n[minNum], n[selectNum]
print(n)

print("selecting sort")
for i in range(0, len(n) - 1):  # i : 정렬할 위치 마지막 부분은 비교할 필요가 없으니까 뺴줌.
    min = i  # min : 최소값의 위치. 초기값으로 i 값 할당
    for j in range(i + 1, len(n)):  # j: 최소값을 찾기 위해 한칸씩 위치 이동할 인덱스로 사용 첫번째 부분은 비교할 필요가 없으니까 뒤로 밀어줌.
        if n[min] > n[j]:  # min 위치의 값, 즉 최소 값보다 더 작은 값을 만나면(j 번째 방에서)
            min = j  # 최소값의 위치를 j로 변경. 이동작을 j가 리스트 끝 까지 도달할 때까지 반복
    if min != i:  # min = i 이 부분에  min에 값을 할당 했기 떄문에 min이 이동이하지 않았다면 i에 최소 값이 있는 경우
        tmp = n[min]  # 위 경우에는 자리 바꿀 필요없음
        n[min] = n[i]  # 그런데 min과 i가 같지 않다면 min이 최소값이 있는 위치로 이동한 것이고 그 최소값이 i 위치의
        n[i] = tmp  # 값으로 들어가야 함 그러므로 min과 i가 같이 않으면 두 위치의 값을 swap 해준다.
print(n)
'''
# 1-3. TODO : 탐색, 2진 탐색, 2차원 리스트 추가 복습
# 2. 아래 등수대로 출력 되도록 만들어오기.
'''
data = [[], [], []]
title = ["name ", "number ", "kor ", "cng ", "math ", "total ", "avg "]
for i in range(0, len(data)):  # data 리스트 길이 만큼 반복.
    for count in range(0, 5):  # 입력
        d = input(title[count] + ": ")  # 입력 받은 변수 d를 data에 넣는다
        if count != 0:  # 입력받은 값이 String 이 아니면,
            d = int(d)  # 정수로 변환
        data[i].append(d)
    data[i].append(data[i][2] + data[i][3] + data[i][4])
    data[i].append(data[i][5] / 3)
for i in title:
    print(i, end='\t')
print()

for i in data:
    for j in i:
        print(j, end="\t\t")
    print()
'''
# [수업]
# list 관련

# [5교시]
# 3명 학생의 이름, 번호, 국, 영, 수, 점수를 입력받아 총점, 평균을 출력하시오.
# [내가 한 것]
'''
inputName = input("이름을 입력하세요:")
inputNum = input("번호을 입력하세요:")
inputScore1 = input("국어 점수를 입력하세요:")
inputScore2 = input("영어 점수를 입력하세요:")
inputScore3 = input("수학 점수를 입력하세요:")

a = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for i in range(0, len(a)):
    a[0][0] = inputName
    a[0][1] = inputNum
    a[0][2] = inputScore1
    a[0][3] = inputScore2
    a[0][4] = inputScore3

print(a)
''' \
'''
for i in range(0, 3):
    a = []
    for j in range(0, 5):
        a.append(inputName)
        a.append(inputNum)
        a.append(inputScore1)
        a.append(inputScore2)
        a.append(inputScore3)
    print(a)
'''

# [강사님께서 구현한 것]
# TODO : [복습][이해]
'''
data = [[], [], []]
title = ["name ", "number ", "kor ", "cng ", "math ", "total ", "avg "]
for i in range(0, len(data)): # data 리스트 길이 만큼 반복.
    for count in range(0, 5): # 입력
        d = input(title[count]+": ") # 입력 받은 변수 d를 data에 넣는다
        if count != 0: # 입력받은 값이 String 이 아니면, 
            d = int(d) #정수로 변환
        data[i].append(d)
    data[i].append(data[i][2]+data[i][3]+data[i][4])
    data[i].append(data[i][5]/3)
for i in title:
    print(i, end='\t')
print()

for i in data:
    for j in i:
        print(j, end="\t\t")
    print()
'''
# 내가 한 것
'''
a = [[0] * 3] * 2
#123456 넣기
for i in a:
    num = 0
    for j in i:
        num += 1
        j += num
        print(a[j])
    i += 1
print(a)
'''

# 강사님 께서 한 것
'''
a = [[0, 0, 0], [0, 0, 0]]

for i in range(0, 2):
    for j in range(0, 3):
        a[i][j] = i * 3 + j + 1
print(a)
'''
# 2차원 리스트
'''
a = [[1, 2, 3], [4, 5, 6]]

for i in a:
    for j in i:
        print(j,end=" ")
    print()
print(a[0][0]) # 큰 > 작 순서로 검색됨
print(a[1][2])

print()
# 리스트는 요소의 타입에 제한이 없다. 정수 문자열 리스트 객체... 다 저장이 된다.
# 리스트 안에 리스트
a = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
     [["asdfc", "casdf", "casdf"], ["casdf", "casdf", "casdf"], ["casdf", "casdf", "casd"]]]

for i in a:  # 반복문 i 를 a에 넣어준다.
    for j in i:  # 반복문 j를 i에 넣어준다.
        for z in j:
            print(z, end=" ")
        print()
    print()
print(a[0][1][0])
'''
# 2진 탐색
'''
print("강사님께서 구현한 코드")
list = [5, 2, 4, 3, 1, 234, 23, 4, 1, 234, 2345, 234, 234, 23, 42, 34, 23, 41, 23, 1, 423, 5, 234, 23, 423, 412, 3, 15,
        325, 3, 6, 3456]  # 리스트 선언 해줌
for i in range(0, len(list) - 1):  # i : 정렬할 위치 마지막 부분은 비교할 필요가 없으니까 뺴줌.
    min = i  # min : 최소값의 위치. 초기값으로 i 값 할당
    for j in range(i + 1, len(list)):  # j: 최소값을 찾기 위해 한칸씩 위치 이동할 인덱스로 사용 첫번째 부분은 비교할 필요가 없으니까 뒤로 밀어줌.
        if list[min] > list[j]:  # min 위치의 값, 즉 최소 값보다 더 작은 값을 만나면(j 번째 방에서)
            min = j  # 최소값의 위치를 j로 변경. 이동작을 j가 리스트 끝 까지 도달할 때까지 반복
    if min != i:  # min = i 이 부분에  min에 값을 할당 했기 떄문에 min이 이동이하지 않았다면 i에 최소 값이 있는 경우
        tmp = list[min]  # 위 경우에는 자리 바꿀 필요없음
        list[min] = list[i]  # 그런데 min과 i가 같지 않다면 min이 최소값이 있는 위치로 이동한 것이고 그 최소값이 i 위치의
        list[i] = tmp  # 값으로 들어가야 함 그러므로 min과 i가 같이 않으면 두 위치의 값을 swap 해준다.
print(list)
searchNum = int(input("찾을 숫자 :"))
# 리스트의 길이를 2로 나눠서 중간 지점을 정해주고 3개의 케이스로 나눈다 같거나 작거나 크거나
# 첫번쨰가 마지막과 같거나거나 작을때 까지 while문을 돌려줌,, 라스트를 옮겨옴. 첫번째를 뒤로 옮겨감.
First = 0  # f: 리스트 검색 시작위치
Last = len(list) - 1  # -1을 하는 정확한 이유 알아보기. 배열 맨 끝방을 찾기위해 -1 을 한것.  0~9 인 경우는 길이. 합은 10이니까 9를 입력해주기 위해서 -1 을 해준것.

while First <= Last:  # 시작위치와 끝위치가 역전되지 않는 한 반복 시켜줌, 만약 아닐경우 반복문을 빠져나옴.
    m = (First + Last) // 2  # //은 소수점까지 없애준다. # 리스트 중간 위치 찾기.
    print("First 위치 :", First)
    print("Last 위치 :", Last)
    print("위치 추적:", m)
    if list[m] > searchNum:  # list에 선언된 m이 검색한 숫자보다 더 클경우, 즉 검색된 숫자가 m보다 작을경우
        Last = m - 1  # last를 m보다 앞의 요소를 가르키게 만든다.
    elif list[m] < searchNum:  # 검색한 숫자가 m보다 클 경우,
        First = m + 1  # First를 m의 한자리 뒤를 가르킬수 있도록 한다.
    else:
        print("번호 찾음: [", m, "](인덱스 번호)")  # middle 값이 해당 요소에 오게되면 멈춤.
        break
if First > Last:
    print("번호 못 찾음")
'''
# 탐색
# [내가 구현한 내용]
'''
n = [6, 3, 6, 7, 4, 4, 3, 5, 6, 2]
print(n)
searchNum = int(input("찾을 숫자 :"))
# 입력 받은 숫자가 for 문 돌면서 몇번 인덱스에 있는지 알아보기.
for i in range(0, len(n)):  # 리스트의 0번 부터 찾는다.
    if searchNum == n[i]:  # n[i] 리스트안에 for문을 돌림. n[]이 안에 for 문인 i 을 넣음.
        print("인덱스 번호 :", i)
        # print(n[i])
# TODO : 중복 번호가 다 찾아지면 안나올 수 있도록,
if searchNum != n[i]:
    print("번호 없음")
'''
# [강사님께서 구현한 내용]
'''
searchNum = int(input("찾을 숫자 :"))
for i in range(0, len(n)):
    if searchNum == n[i]:
        print(i, "번쨰 방에 있음")
        break  # 루프를 빠져나옴
if searchNum != n[i]:
    print("내용 없음")
'''

# [3~4교시]
'''
n = list()  # 리스트를 변수에 넣어서 초기화 해주는 방식. [추가해주면서 만드는 방식]
for i in range(0, 10):
    n.append(int(input("num:")))

for i in n:
    print(i, end=", ")

# 리스트 요소의 합과 평균, 최대값, 최소값 출력
sum = 0
for i in n:
    sum += i  # 합 계산
print()

f = sum / len(n)  # 평균 계산 길이로 나눠줌.

m1 = m2 = n[0]  # m1 : 최대 값 m2 : 최소 값 제일 오른쪽에서 부터 할당해줌.
for i in n:  # >> n을 참조한다.
    if m1 < i:
        m1 = i
    elif m2 > i:
        m2 = i
print("-----------------------")
print("최대 값 :", m1, "최소 값 :", m2, "평균 값 :", f, "총 합 :", sum)
print("-----------------------")

# TODO : [중요][이해][복습] bubble sort 알고리즘
# 숫자 정렬하는 법 TODO : [중요] 정보처리 기사 예제 문제 1월 신청
# 버블 알고리즘 = 두개씩 비교해서 작은 수를 앞으로 바꿔줌,
# a[0] a[1] 두개를 바꿔 줌
# a[0] = a[1] 해주면 0의 자리가 없어짐 그래서 변수를 선언해서 미리 빼어줌 tmp = a[0] << 이런식으로 한다른 a[1] = tmp 방식으로 2중루프를 만들어서 해줌.
print("bubbling sort")
for i in range(0, len(n) - 1):  # 0부터 리스트 n의 길이 까지 반복,
    for j in range(0, len(n) - 1 - i):  # 0부터 리스트 n의 길이 - i 번 까지 반복, 횟수 만큼
        if n[j] > n[j + 1]:
            # 스왑하는 부분
            tmp = n[j]
            n[j] = n[j + 1]
            n[j + 1] = tmp
print(n)
print("-----------------------")
# TODO : [중요][이해][복습] insert sort 알고리즘
# insert 는 앞에꺼랑 만 비교함.
# temp 변수 리스트 하나하나씩 값을 먼저 넣고 숫자가 기존에 있는 넣는 리스트에 값보다 크면, 그 앞에 추가함.
# 값이 입력된 리스트에 [2,3,5,5,3] 맨 처음의 값은 고정 시켜두고 j i 변수를 지정해줘서 temp 변수에 넣어줄 값을 리스트에서 찾아 선언해줌.
# j는 뒤로 밀려나면서 1씩 증가하되 리스트의 크기까지만., 또, 항상 i 변수의 참조되는 리스트 요소의 앞에 참조 되어야함 즉, i-1이 되어야한다.

# insert sort
print("inserting sort")
for i in range(i, len(n)):  # for 문으로 리스트의 길이만큼 반복시작. [자기 자릴 찾을 값의 위치]
    tmp = n[i]  # 리스트의 맨 첫째 자리를 tmp 변수에 저장한다. [i 위치의 값이 지워지지 않게 tmp 옮겨놓음]
    j = i - 1  # [j는 i의 앞 위치로 i값의 위치를 찾기위해 비교할 대상의 위치를 선언해 준다.]
    while j >= 0 and n[j] > tmp:  # []
        n[j + 1] = n[j]  # [j 위치의 값을 뒤로 한칸 이동]
        j -= 1  # [j를 한칸 앞으로 이동]
    j += 1
    n[j] = tmp
print(n)
# TODO : 보드판에 써 가면서 이해 연습하기.
''' \
'''
print("-----------------------")
# 선택정렬은 리스트 안에 있는 모든 값들을 비교해서 가장 작은 값을 가장 맨앞으로 넣어줌.
print("selecting sort")
print("강사님께서 구현한 코드")
list = [5, 2, 4, 3, 1, 234, 23, 4, 1]  # 리스트 선언 해줌
for i in range(0, len(list) - 1):  # i : 정렬할 위치 마지막 부분은 비교할 필요가 없으니까 뺴줌.
    min = i  # min : 최소값의 위치. 초기값으로 i 값 할당
    for j in range(i + 1, len(list)):  # j: 최소값을 찾기 위해 한칸씩 위치 이동할 인덱스로 사용 첫번째 부분은 비교할 필요가 없으니까 뒤로 밀어줌.
        if list[min] > list[j]:  # min 위치의 값, 즉 최소 값보다 더 작은 값을 만나면(j 번째 방에서)
            min = j  # 최소값의 위치를 j로 변경. 이동작을 j가 리스트 끝 까지 도달할 때까지 반복
    if min != i:  # min = i 이 부분에  min에 값을 할당 했기 떄문에 min이 이동이하지 않았다면 i에 최소 값이 있는 경우
        tmp = list[min]  # 위 경우에는 자리 바꿀 필요없음
        list[min] = list[i]  # 그런데 min과 i가 같지 않다면 min이 최소값이 있는 위치로 이동한 것이고 그 최소값이 i 위치의
        list[i] = tmp  # 값으로 들어가야 함 그러므로 min과 i가 같이 않으면 두 위치의 값을 swap 해준다.
print(list)
''' \
'''
print("참고 자료")
list = [5, 2, 4, 3, 1, 234, 23, 4, 1]  # 리스트 선언 해줌
for selectNum in range(0, len(list) - 1):  # 리스트의 크기 만큼 반복해준다.
    minNum = selectNum  # 리스트의 첫번째 값을 minNum 변수에 넣어서 임시 저장해준다.
    for nextNum in range(selectNum + 1, len(list)):  # selectNum 의 반복문보다 1칸 뒤의 값을 시작점으로해서 리스트의 마지막
        if list[nextNum] < list[minNum]:
            minNum = nextNum
        list[selectNum], list[minNum] = list[minNum], list[selectNum]
print(list)
'''

# TODO: 연습하기.
'''
for i in range(0, len(list) - 1):  # i 에 정렬할 위치를 선언해준다.
    min = i
    for j in range(i + 1, len(list)):  # 최소값을 찾기위해 한칸씩 위치 이동할 인덱스로 사용된다.
'''

# 참조 : https://www.daleseo.com/sort-insertion/
'''
arr = [1, 2, 3, 4, 5,23,45,654,24,23,2,3]


def insertion_sort1(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]


def insertion_sort2(arr):
    for end in range(1, len(arr)):
        i = end
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1


def insertion_sort3(arr):
    for end in range(1, len(arr)):
        to_insert = arr[end]
        i = end
        while i > 0 and arr[i - 1] > to_insert:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = to_insert

print(insertion_sort1())
print(insertion_sort2())
print(insertion_sort3())
''' \
'''
temp = n[0]
n[0] = n[1]
n[1] = temp
''' \
'''
while len(n):
    temp = n[0]
    if n[0] < n[1]:
        n[0] = n[1]
    elif n[0] > n[1]:
        continue
''' \
'''
# 첫번쨰 for문 = 리스트의 길이 만큼
for i in n:  #
    temp = n[i]
    if n[i] < n[i + 1]:
        n[i] = n[i + 1]
    elif n[i] > n[i + 1]:
        continue
'''
# [2교시]
'''
# 리스트 초기화
aa = [0] * 10  # 0을 100개로 초기화 해준다
print(aa)
print("-------")
aa[0] = 10
print(aa)
print("-------")
aa = [0] * 10  # 0을 100개로 초기화 해준다
print(aa)
print("-------")
a = "asd"
aa[0] = a  # TODO : 이슈 질문하기.
aa[1] = 10
aa[2] = 12.3
aa[3] = 's'
aa[4] = True
print(type(aa[0]))
print(type(aa[1]))
print(type(aa[2]))
print(type(aa[3]))
print(type(aa[4]))

# 숫자10개를 리스트에 담아서 출력
firstList = []
firstList.append(1)
firstList.append(2)
firstList.append(3)
firstList.append(4)
firstList.append(5)
firstList.append(6)
firstList.append(7)
firstList.append(8)
firstList.append(9)
firstList.append(10)
print(firstList)

secondList = [0] * 10
for i in range(1, 11):
    secondList[0] = i
print(secondList)

nums = [0] * 10  # 먼저 리스트에 0을 10개 넣어줘서 초기화 시켜주는 방식 [인덱스를 바꿔주는 방식]
for i in range(0, 10):
    nums[i] = int(input("num:"))
for i in nums:
    print(i, end=", ")
print()
print("-----------")

n = list()  # 리스트를 변수에 넣어서 초기화 해주는 방식. [추가해주면서 만드는 방식]
for i in range(0, 10):
    n.append(int(input("num:")))

for i in n:
    print(i, end=", ")

# 리스트 요소의 합과 평균, 최대값, 최소값 출력
sum = 0
for i in n:
    sum += i  # 합 계산
print()

f = sum / len(n)  # 평균 계산 길이로 나눠줌.

m1 = m2 = n[0]  # m1 : 최대 값 m2 : 최소 값 제일 오른쪽에서 부터 할당해줌.
for i in n: # >> n을 참조한다.
    if m1 < i:
        m1 = i
    elif m2 > i:
        m2 = i
print("-----------------------")
print("최대 값 :", m1, "최소 값 :", m2, "평균 값 :", f, "총 합 :", sum)

# 숫자 정렬하는 법 TODO : [중요] 정보처리 기사 예제 문제 버블 알고리즘. 3월
# 버블 알고리즘 = 두개씩 비교해서 작은 수를 앞으로 바꿔줌,
# a[0] a[1] 두개를 바꿔 줌
# a[0] = a[1] 해주면 0의 자리가 없어짐 그래서 변수를 선언해서 미리 빼어줌 tmp = a[0] << 이런식으로 한다른 a[1] = tmp 방식으로 2중루프를 만들어서 해줌.
'''

# [1교시]
'''

a1 = [1, 2, 3]
print(a1[0])

a1[0] = 100
print(a1[0])

a2 = []
# a2[0]=10 # >> 방이 비어있으면 에러 발생,
a2.append(10)  # >> 리스트 뒤에 방을 생성하는 메서드인 append를 사용
print(a2[0])

a2[0] = "s"  # >> 문자로 변환 가능
print(a2[0])

print("-----")
x1 = list()  # 빈리스트를 생성해서 반환
x2 = list(a1)  # 다른 리스트를 복해서 생성
print(x1)
print(x2)

print("-----")
# 복사를 해서 사용한 방법이 원래의 리스트에 영향을 주나 시험, 이해 할 것.
x2[0] = 123
print(a1)
print(x2)

# 추가 실험 내용
print("-----")
x3 = x2  # 여기에서 변수로 선언을 해줘서 밑에서 x3[0]을 345로 바꿔주면 x2도 같이 바뀐다.
print(x2)
print(x3)

x3[0] = 345
print(x2)
print(x3)

print("-----")
x4 = list(x3)
x4[0] = 1000
print(x3)
print(x4)

print("-----")
x5 = x4
x5[0] = 1000
print(x4)
print(x5)

# TODO : 위의 list 활용법 알아두기.

# TODO : [중요] 리스트 이름 : 시작주소

# 파이선에서 list 는 타입 상관 없이 넣을 수 있다.
# 관련 주소값으로 찾아갈 수 있도록
# 파이썬에서 list에 입력되는 값은 참조형 이다. 즉 b = ['abc'] 이면 ,, abc는 어딘가에 저장이 되어있고 b는 참조하는 형태를 갖고 있어서
# 문자나 숫자 등 섞여서 저장이 가능 한 것이다.

textList = [1, "안녕하세요", 'a', 3.14]
print(list)
'''

# TODO : [복습] 2020년 11월 3일 - For 문
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
# 1+1=2 1+2=3 이런식으로 배치하면 손쉽게 생각 해 볼 수있다.
# 인덱스를 활용, >> 인덱스로 1+1=2
# 답변수에 2를 추가.
# 첫째와 두번째 변수 생성해서
# 두번째 변수에 답을 넣어줌.
# 답만 넣을 리스트 생성. 2,3,5,8 << 이런식으로 들어갈 수 있도록
# 그 후에 답이 들어있는 리스트에서의 인덱스를 for문으로 돌려서 출력한다.
'''
def fibo(n):
    if n < 2:
        return n
    a = 0
    b = 1
    for i in range(n - 1):
        a = b
        b = a + b
    return b


for n in range(1, 101):
    print(n, fibo(n))
'''

# 바로 앞의 자리의 수와 더해서 값이 또 나올 수 있도록 구현

# TODO: 주소록 구현
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
''' \
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
''' \
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
''' \
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
        ''' \
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

# TODO : [복습] 2020년 11월 2일 - while 문

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
''' \
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
''' \
 \
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
