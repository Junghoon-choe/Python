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