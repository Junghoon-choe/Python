"""
1. firebase 연동 및 회원 가입 로그인 기능
2. Manager, User UI 다르게 만들기.
3. Manager, User 기능 구현(문제를 풀때에는 마지막 정답:1 이 부분이 안나오게 제어하고, 만약 푼 문제가 틀렸으면 오답노트로 파일을 생성해준다.)
4. 패키징 하기.
5. 추가로 쓰레드 사용 하기.
"""
from random import random

"""
[클래스 관련 내용]
객체를 먼저 판단해서 나눌지 결정하기.
유저, 매니저, 문제,
"""

import pyrebase
import sys
import os

config = {
    "apiKey": "AIzaSyAcJdQ7H6f8RsYItDNK1FYGLNO-ViOGMR8",
    "authDomain": "pythonquiz-ded50.firebaseapp.com",
    "databaseURL": "https://pythonquiz-ded50.firebaseio.com",
    "projectId": "pythonquiz-ded50",
    "storageBucket": "pythonquiz-ded50.appspot.com",
    "messagingSenderId": "727076101887",
    "appId": "1:727076101887:web:1ea8d91ac5572464cb36ca",
    "measurementId": "G-9DEF4Z3P6P"
}

firebase = pyrebase.initialize_app(config)

# db = firebase.database()
# storage = firebase.storage()
auth = firebase.auth()

prompt = """\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1. 로그인
2. 회원가입
3. 종료"""

userPrompt = """\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1. 문제풀기
2. 오답노트
3. 로그아웃
4. 종료"""

managerPrompt = """\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1. 문제 추가
2. 문제 검색 및 수정
3. 문제 삭제
4. 문제 전체 삭제
5. 로그 아웃
6. 시스템 종료"""

question = """1. 예
2. 아니오"""


def loginUser():
    global email
    Login = False
    while True:
        print(prompt)
        try:
            number = int(input("숫자를 입력주세요 :"))
            # 로그인
        except ValueError:
            return

        if number == 1:
            print(
                "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\"뒤로가기\"를 입력하면 이전 페이지로 이동합니다.\n")
            # Login
            while True:
                email = input("이메일 :")
                if email == "뒤로가기":
                    break
                password = input("비밀번호 :")
                if password == "뒤로가기":
                    break

                # tryLogin = 0
                # if tryLogin >= 3:
                #     Check = input("뒤로 돌아가시겠습니까? (1. 네, 2. 아니오) :")
                #     if tryLogin == 1:
                #         break
                try:
                    auth.sign_in_with_email_and_password(email, password)
                    print("로그인 되었습니다.")
                    if not os.path.isdir("../회원파일/{}".format(email)):
                        os.mkdir("../회원파일/{}".format(email))
                    return email


                except:
                    # tryLogin += 1
                    print("\n이메일 또는 비밀번호를 다시 입력해주세요.\n")

        # 회원가입
        elif number == 2:
            print("\n\"뒤로가기\"를 입력하면 이전 페이지로 이동합니다.\n")
            email = input("이메일 :")
            if email == "뒤로가기":
                break
            password = input("비밀번호 :")
            if password == "뒤로가기":
                break
            passwordCheck = input("비밀번호 확인 :")
            if password == "뒤로가기":
                break
            while password == passwordCheck:
                auth.create_user_with_email_and_password(email, password)
                print("회원가입이 되었습니다.")
                if not os.path.isdir("../회원파일/{}".format(email)):
                    os.mkdir("../회원파일/{}".format(email))
                break
            else:
                print("비밀번호를 다시 입력해주세요.")

        # 종료
        elif number == 3:
            sys.exit(0)
        else:
            print("숫자를 다시 입력해주세요.")


class Dao:
    def __init__(self):
        self.prod = []

    def addQ(self):
        arr = []
        file_name = input("\"뒤로가기\"를 입력하면 메뉴창으로 이동합니다\" \n문제 번호 :")
        if os.path.isfile(file_name):
            print("\n\t같은 파일명을 갖고 있는 파일이 존재합니다.\n\t파일명을 바꿔주세요.\n")
            return
        elif file_name == "뒤로가기":
            return

        print("""\n마지막에 \"정답:1\"과 같은식으로 정답을 기입해주세요.\n(작성을 완료 하려면 "/w"을 입력하세요!!)\n""")
        while True:
            string = input()
            if string == "/w":
                break
            arr.append(string + '\n')

        file = open(file_name, "w")
        file.writelines(arr)
        file.close()

    # 수정 로직 = 파일을 불러와서 위에서 보여준다 > 수정 하시겠냐고 물어보면 (수정 , 뒤로가기)를 입력해서
    # 각 입력받은 내용을 전달 받아 if else 제어문으로 UI 조종한다.
    # 수정을 입력하면 새 파일을 만들때 처럼, UI를 만들어 줘서 저장시킨다. 저장할 때는 추가 할때 방법과 같지만 파일이 새로 생기는것이 아닌, 같은 파일에서 새로 저장이 될 수 있도록 구현한다.
    def editQ(self):
        msg = """\n수정 하시겠습니까? (\"네\" 또는 \"아니오\"를 기입해주세요) :"""
        while True:
            # 셔플하는 방법 알아보기.
            print(os.listdir(os.getcwd()), '\n')
            mode = "r"
            file_name = input("\n어떤 파일을 수정 하시겠습니까? :")
            if os.path.isfile(file_name):
                while True:
                    file = open(file_name, mode)
                    print("--------------------------------")
                    print("\n", file.read())
                    print("--------------------------------")
                    try:
                        Q = input(msg)
                    except ValueError:
                        print("다시 입력해주세요.")
                    if Q == "네":
                        # 해당 파일 삭제
                        os.remove(file_name)
                        # 새로운 파일 작성
                        arr = []
                        if os.path.isfile(file_name):
                            print("\n\t같은 파일명을 갖고 있는 파일이 존재합니다.\n\t파일명을 바꿔주세요.\n")
                            return
                        print("""(작성을 완료 하려면 "/w"을 입력하세요!!)\n""")
                        while True:
                            string = input()
                            if string == "/w":
                                break
                            arr.append(string + '\n')
                        file = open(file_name, "w")
                        file.writelines(arr)
                        file.close()
                    elif Q == "아니오":
                        break
                    else:
                        print("다시 입력해주세요.")
                    file.close()
            elif file_name == "뒤로가기":
                break
            else:
                print('\n\t파일명을 다시 확인해주세요!!\n')

    def removeQ(self):

        while True:
            print(os.listdir(os.getcwd()))
            file_name = input("\n어떤 파일을 삭제 하시겠습니까? :")
            if os.path.isfile(file_name):
                os.remove(file_name)
                print('\t', "\"", file_name, "\"파일이 삭제 되엇습니다!\n")
                break
            elif file_name == "뒤로가기":
                break
            else:
                print('\n\t파일명을 다시 확인해주세요!!\n')

    def removeAllQ(self):
        for i in os.listdir(os.getcwd()):
            os.remove(i)

    def exam(self):
        print("exam")

    def myNote(self):
        print("myNote")


def Manager():
    dao = Dao()
    while True:
        print(managerPrompt)
        number = int(input("\n숫자를 입력해주세요.\n"))
        if number == 1:
            dao.addQ()
        elif number == 2:
            dao.editQ()
        elif number == 3:
            dao.removeQ()
        elif number == 4:
            dao.removeAllQ()
        elif number == 5:
            break
        elif number == 6:
            sys.exit(0)
        else:
            print("숫자를 다시 입력해주세요.")


# userPrompt = """1. 문제풀기
# 2. 오답노트
# 3. 로그아웃
# 4. 종료"""

# managerPrompt = """1. 문제 추가
# 2. 문제 수정
# 3. 문제 찾기
# 4. 문제 삭제
# 5. 문제 전체 삭제"""

def User():
    dao = Dao()
    while True:
        print(userPrompt)
        try:
            number = int(input("\n숫자를 입력해주세요.\n"))
            if number == 1:
                dao.exam()
            elif number == 2:
                dao.myNote()
            elif number == 3:
                break
            elif number == 4:
                sys.exit(0)
            else:
                print("숫자를 다시 입력해주세요.")
        except ValueError:
            print("숫자를 기입해주세요.")


def main():
    if not os.path.isdir("./문제파일"):
        os.mkdir("./문제파일")
    os.chdir("./문제파일")
    print("현재 :", os.getcwd())
    while True:
        loginUser()
        try:
            if email == "Manager@naver.com":
                Manager()
            else:
                User()
        except NameError:
            print('다시입력하세요')


main()
