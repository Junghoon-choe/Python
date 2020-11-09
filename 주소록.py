# 내가 구현한 코드
# TODO : 중복검사 하기.

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
userList = []


def add():
    global userList
    userInfo = nameCheck()
    userList.append(userInfo)


def nameCheck():
    while True:
        name = input("이름 :")
        phoneNum = int(input("전화번호 :"))
        address = input("주소 :")
        userInfo = [name, phoneNum, address]

        search(name)
        if name == search(name):
            print('중복된 이름')
        else:
            break
    return userInfo


def search(name):
    for i in range(0, len(userList)):
        if name in userList[i][0]:
            # 변수 in list[] 로 리스트 안에 값이 있는지 확인 할 수있다.
            return name


def searchName():
    searchName = (input("이름:"))
    for i in range(0, len(userList)):
        if userList[i][0] == searchName:
            print("정보 있음 :", userList[i][0], userList[i][1], userList[i][2])
            break
        else:
            print("정보 없음")


def edit():
    searchName = input("이름:")
    for i in range(0, len(userList)):
        if userList[i][0] == searchName:
            print("정보 있음 :", userList[i][0], userList[i][1], userList[i][2])
            quest = input("어떤 정보를 수정하시겠습니까? [이름, 번호, 주소] :")
            if quest == "이름":
                while True:
                    etName = input("수정할 이름 :")
                    if search(etName) == etName:
                        print("중복된 이름 입니다.")
                    else:
                        userList[i][0] = etName
                        break

            elif quest == "번호":
                userList[i][1] = input("수정할 번호 :")

            elif quest == "주소":
                userList[i][2] = input("수정할 주소 :")

            print()
            print("수정되었습니다.")
            break

        elif userList[i][0] != searchName:
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
            print("정보 없음")


def removeAll():
    quest = input("전체삭제 하시겠습니까? [예, 아니오] :")
    if quest == "예":
        userList.clear()


number = 0
while number != 7:
    print(prompt)
    number = int(input())

    if number == 1:
        print("추가")
        add()

    if number == 2:
        print("검색")
        searchName()

    if number == 3:
        print("수정")
        edit()

    if number == 4:
        print("삭제")
        remove()

    if number == 5:
        print("전체 출력")
        userList.sort()
        print(userList)

    if number == 6:
        print("전체 삭제")
        removeAll()

    if number == 7:
        print("종료")

    if number >= 8:
        print("숫자를 다시 입력해주세요.")

# 강사님께서 구현한 코드
# 1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.전체삭제 7.종료

# 1. 숫자

'''datas = []


def add():
    global datas
    num = numCheck()
    datas.append(num)


def editNum():
    global datas
    num = int(input('edit num:'))
    flag = search(num)
    if flag == None:
        print('not found')
    else:
        num = numCheck()
        datas[flag] = num
        print('datas[', flag, '] 가 ', datas[flag], '로 수정됨')


def numCheck():
    while True:
        num = int(input('num:'))
        flag = search(num)
        if flag == None:
            break
        else:
            print('중복된 숫자')
    return num


def search(x):
    if x in datas:
        return datas.index(x)


def printAll():
    for i in datas:
        print(i, end=', ')
    print()


def stop():
    return False


def getNum():
    num = int(input('search num:'))
    flag = search(num)
    if flag == None:
        print('not found')
    else:
        print(flag, ' 방에 있다')


def delNum():
    global datas
    num = int(input('del num:'))
    flag = search(num)
    if flag == None:
        print('not found')
    else:
        del datas[flag]


def clearDatas():
    global datas
    datas.clear()


def main():
    li = [add, getNum, editNum, delNum, printAll, clearDatas, stop]  # 룩업 테이블. 함수 객체 리스트
    flag = True
    while flag:
        menu = int(input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.전체삭제 7.종료'))
        if 1 <= menu <= 6:
            li[menu - 1]()
        elif menu == 7:
            flag = li[menu - 1]()


main()'''
# 2. 주소록
'''members = []


def search(name):
    for idx, i in enumerate(members):
        if i[0] == name:
            return idx


def add():
    global members
    m = ["", "", ""]
    while True:
        name = input("name :")
        flag = search(name)
        if flag == None:
            m[0] = name
            break
        else:
            print("중복된 이름. 다시 입력하세요")
    m[1] = input("tel :")
    m[2] = input("address :")
    members.append(m)


def stop():
    return False


def printAll():
    for i in members:
        for j in i:
            print(j, end="/")
        print()


def main():
    li = [add, None, None, None, printAll, None, stop]  # 룩업 테이블. 함수 객체 리스트
    flag = True
    while flag:
        menu = int(input('1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.전체삭제 7.종료'))
        if 1 <= menu <= 6:
            li[menu - 1]()
        elif menu == 7:
            flag = li[menu - 1]()

main()'''
