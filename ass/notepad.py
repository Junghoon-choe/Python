'''
메모장
ㄴ 실행시 memo 디렉토리 생성

메뉴
1 - 읽기 (파일 목록 출력 후 파일 이름 입력)
2 - 쓰기 (중복x or 덮어쓰기, 이어쓰기)
3 - 삭제 (파일 목록 출력 후 파일 이름 입력)
4 - 클리어 (디렉토리 전체 삭제)
5 - 종료
'''

import os

def startmemo():
    if not os.path.isdir('./memo'):
        os.mkdir('./memo')
    os.chdir('./memo')

def printdir():
    print(os.listdir(os.getcwd()))

def readmemo():
    printdir()
    fname = input('input file name for read : ')

    if os.path.isfile('./%s' % (fname)):
        with open(fname, 'r', encoding='utf-8') as file:
            print(file.read())
    else:
        print('not exist')

def writememo():
    fname = input('input file name for write : ')

    mode = 'w'

    if os.path.isfile('./%s' % (fname)):
        mode = input('input mode (덮어쓰기 : w, 이어쓰기 : a) : ')

    print('input content (종료 : /exit)')
    with open(fname, mode, encoding='utf-8') as file:
        while True:
            content = input()
            if content == '/exit':
                break
            file.write(content + '\n')

def removememo():
    printdir()
    fname = input('input file name for remove : ')

    if os.path.isfile('./%s' % (fname)):
        os.remove(fname)
    else:
        print('not exist')

def clearmemo():
    for i in os.listdir(os.getcwd()):
        os.remove(i)

def main():
    startmemo()

    while True:
        menu = int(input('1.읽기 2.쓰기 3.삭제 4.클리어 0.종료 : '))

        if menu == 0:   # 종료
            break
        elif menu == 1: # 읽기
            readmemo()
        elif menu == 2: # 쓰기
            writememo()
        elif menu == 3: # 삭제
            removememo()
        elif menu == 4: # 클리어
            clearmemo()

main()