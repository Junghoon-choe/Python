#1.추가 2.검색 3.수정 4.삭제 5.전체출력 6.전체삭제 7.종료
datas = []
def add():
    global datas
    while True:
        num = int(input('num:'))
        flag = search(num)
        if flag==None:
            break
        else:
            print('중복된 숫자')
    datas.append(num)

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

def editNum():
    global datas
    num = int(input('edit num:'))
    flag = search(num)
    if flag == None:
        print('not found')
    else:
        num = int(input('new num:'))
        datas[flag] = num
        print('datas[', flag, '] 가 ', datas[flag], '로 수정됨')

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
        if 1<=menu<=6:
            li[menu-1]()
        elif menu==7:
            flag = li[menu-1]()

main()