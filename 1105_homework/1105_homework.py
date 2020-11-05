'''
1번과 2번 중 선택
1. 숫자를 담을 빈 리스트를 하나 만들고, 아래 기능 구현하기
    - 메뉴: 추가, 검색, 수정, 삭제, 전체목록, 종료
    - 추가 시 중복값이면 메세지 띄운 후 다시 입력받기
2. 주소록 만들기
    - 메뉴: 추가, 검색, 수정, 삭제, 전체목록, 종료
    - 빈 리스트에서 시작
    - 기능 함수로 만들기
    - 이름 중복 허용 안함
    - 수정, 삭제, 검색 모두 이름이 기준
'''


def func_add(li, val):
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
        break
