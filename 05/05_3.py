# 구구단 함수
'''
def gugudan(dan):
    for i in range(1, 10):
        print('{0} * {1} = {2}'.format(dan, i, dan * i))

# dan = int(input('dan : '))

for i in range(2, 10):
    gugudan(i)
    print()
'''

# 약수 함수
'''
def measure(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=' ')
    print()

number = int(input('number : '))
measure(number)
'''

