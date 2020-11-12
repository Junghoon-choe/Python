# 강사님께서 구현하신 코드 (참고자료) - MVC 패턴

# 1명의 학생을 정의하는 클래스
class Student:  # 한 학생의 정보 및 성적처리 . 캡슐화 (주의할 점~! C언어나, 자바처럼 구현x, 하나라고 생각해야한다.)
    def __init__(self, name, number, kor, eng, math):  # 생성자로 각 멤버변수 생성.
        self.name = name  # 파라메터로 받아서 멤버변수에 저장한다.
        self.number = number
        self.kor = kor
        self.eng = eng
        self.math = math

    def calculrator(self):  # 점수를 계산하는 메서드
        self.total = self.kor + self.eng + self.math
        self.avg = self.total / 3

    def printInfo(self):  # 입력한 정보를 보여주는 메서드
        print("name :", self.name)
        print("number :", self.number)
        print("kor :", self.kor)
        print("eng :", self.eng)
        print("math :", self.math)
        print("total :", self.total)
        print("avg :", self.avg)
        print("---------------------")


# Dao = database access object - 작업 전담 클래스
class Dao:  # 정보를 저장해주는 클래스
    def __init__(self):  # 생성자
        self.datas = []  # 맴버변수를 리스트로 선언해준다.

    def insert(self, sum):  # 파라메터로 sum 을 받아와서 클래서에서 사용할 수 있게 해준다.
        self.datas.append(sum)  # 멤버변수인 리스트에 데이터를 추가, 저장해준다.

    def selectAll(self):  # 맴버변수를 보여줄 메서드 선어
        return self.datas  # 멤버변수에 저장된 리스트를 반환해 준다.


class Service:  # 사용자에게 UI를 보여주는 클래스
    def __init__(self):  # 생성자 선언
        self.dao = Dao()  # 정보를 저장해주는 클래스를 받아와서 맴버변수로 선언해준다.

    def addStudent(self):  # 학생의 정보를 사용자에게 받아와서 Dao 클래스로 넘겨주는 메서드
        name = input("이름 :")
        number = int(input("번호 :"))
        kor = int(input("국어 :"))
        eng = int(input("영어 :"))
        math = int(input("수학 :"))
        s = Student(name, number, kor, eng, math)  # 위의 Student 클래스를 불러와서 지역변수 선언을 해주고 ,
        # 사용자에게 입력받은 값을 저장 시킨다.
        s.calculrator()  # Student 클래스의 계산 메서드를 불러와서 실행시킨다.
        self.dao.insert(s)  # 계산 까지된 값들을 저장 클래스에 넘겨서 저장클래스 insert 메서드를 사용해 리스트에 넣어준다.

    def printAll(self):
        all = self.dao.selectAll()
        for i in all:
            i.printInfo()


def main():
    service = Service()
    service.addStudent()
    service.addStudent()
    for i in range(3):
        service.addStudent()
    service.printAll()

main()

# 내가 구현한 코드
"""
class Student:
    def __init__(self, number, name, kor, eng, math):
        self.number = number
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def printStudent(self):
        print(self.number)
        print(self.name)
        print(self.kor)
        print(self.eng)
        print(self.math)


def main():
    s = Student()
    s.number= input("111")
    s.name = input("aaa")
    s.kor = input("10")
    s.eng = input("20")
    s.math = input("30")

main()
"""
