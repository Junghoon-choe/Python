'''
함수

01. 숫자 리스트
메뉴 : 추가 (중복 x) 검색 (value) 수정 (old, new value) 삭제 (value) 전체 목록

02. 주소록
[[이름, 전화, 주소], [], []]
메뉴 : 추가 (이름 중복 x) 검색 (이름) 수정 (old, new 이름) 삭제 (이름) 전체 목록
'''

# 01
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