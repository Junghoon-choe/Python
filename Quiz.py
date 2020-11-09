import pyrebase
import sys

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

prompt = """1. 회원가입
2. 로그인
3. 종료"""

Login = False

while True:
    print(prompt)
    number = int(input("숫자를 입력주세요 :"))
    # 회원가입
    if number == 1:
        print("회원가입")
        email = input("이메일 :")
        password = input("비밀번호 :")
        passwordCheck = input("비밀번호 확인 :")
        while password == passwordCheck:
            auth.create_user_with_email_and_password(email, password)
            print("회원가입이 되었습니다.")
            break
        else:
            print("비밀번호를 다시 입력해주세요.")

    # 로그인
    elif number == 2:
        print("로그인")
        # Login
        email = input("이메일 :")
        password = input("비밀번호 :")
        try:
            auth.sign_in_with_email_and_password(email, password)
            Login = True
            print("로그인 되었습니다.")
        except:
            print("이메일 또는 비밀번호를 다시 입력해주세요.")
        break
    # 종료
    elif number == 3:
        sys.exit(0)
    else:
        print("숫자를 다시 입력해주세요.")

'''
email = input("이메일 :")
password = input("비밀번호 :")
# Login
try:
    auth.sign_in_with_email_and_password(email, password)
    print("로그인 되었습니다.")
except:
    print("이메일 또는 비밀번호를 다시 입력해주세요.")

# SignUp

    user = auth.create_user_with_email_and_password(email, password)
    print("회원가입 되었습니다.")

    print("이메일 또는 비밀번호를 다시 입력해주세요.")
'''



"""
1. 1 ~ 4번 문제를 2차원 배열을 사용해서 [[1,"문제설명~~","1번 :","2번 :","3번 :","4번 :",4],[],[],[],[],[]]
                              문제번호,문제설명 , 1번문제 설명 , 2, 3, 4 , 정답   
                                
정처리 = {
    1: {
        '1번': "설명~",
        '2번': "설명~",
        '3번': "설명~",
        '4번': "설명~",
        '정답': 4
    },
    2: {
        '1번': "설명~",
        '2번': "설명~",
        '3번': "설명~",
        '4번': "설명~",
        '정답': 4
    },
    3: {
        '1번': "설명~",
        '2번': "설명~",
        '3번': "설명~",
        '4번': "설명~",
        '정답': 4
    },
    4: {
        '1번': "설명~",
        '2번': "설명~",
        '3번': "설명~",
        '4번': "설명~",
        '정답': 4
    }
}
                                 
"""

# 참고
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


