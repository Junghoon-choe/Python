# 메모라는 디렉토리가 없으면 생성
# 메뉴 : 1.읽기 2.쓰기 3.삭제. 4.전체삭제
# 읽기 : 파일명 읽어서 파일 내용 보여주기
# 쓰기 : 파일명을 입력받는데 중복되면 안됨, 저장할 내용 입력받음.
# 삭제 : 파일 목록을 보여주고 삭제할 파일 선택 후 삭제
# 전체 삭제 : 메모 디렉토리 삭제
# 파일 있으면 '이어쓰기'
import os

def print_menu():
    print("==== 메뉴 ====")
    print("1. 읽기")
    print("2. 쓰기")
    print("3. 삭제")
    print("4. 전체 삭제")
    print("5. 종료")
    print("=============")

def proc_read():
    filename = input("파일 이름:")
    if not os.path.isfile(filename):
        print("해당 파일이 없습니다.")

    f = open(filename, "r", encoding='utf-8')
    print(f.name)
    print(f.read())
    f.close()

def proc_write():
    filename = input("파일 이름:")
    write_mode = 'w+';
    if os.path.isfile(filename):
        while True:
            i = input("파일이 이미 존재합니다. 이어쓰시겠습니까? (Y/N)")
            if i == "Y" or i == "y":
                write_mode = 'a+'
                break
            elif i == 'N' or i == 'n':
                return

    f = open(filename, write_mode, encoding='utf-8')
    while True:
        print(f.name)
        print(f.read())
        i = input("입력:")
        print("('/stop'으로 입력을 끝낼 수 있습니다.)")
        if i == '/stop':
            break
        f.writelines(i+"\n")
    print(f.read())
    f.close()
    f = open(filename, 'r', encoding='utf-8')
    print(f.read())


def proc_remove():
    for i in os.listdir():
        print(i)
    filename = input("파일 이름:")
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        "해당 파일이 없습니다."

def proc_clear():
    for i in os.listdir():
        os.remove(i)
    os.chdir("../")
    os.rmdir("memo")
    return False

def proc_exit():
    return False

def check_dir():
    if not os.path.isdir("memo"):
        os.mkdir("memo")
    os.chdir("memo")

def main():
    print("현재 디렉토리:", os.getcwd())

    if not os.path.isdir("memo"):
        os.mkdir("memo")
    os.chdir("memo")

    while True:
        print_menu()
        proc = [proc_read,proc_write,proc_remove,proc_clear,proc_exit]
        i = input("선택:");
        if i.isdigit():
            if proc[int(i)-1]() == False:
                break


main()
