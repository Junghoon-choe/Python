'''
피보나치 수열 100개
1. 재귀함수
2. 루프
3. 리스트 사용
1   1   2   3   5   8
'''

#재귀함수
def fibo1(x):
    if x<=2:
        return 1
    else:
        return fibo1(x-1)+fibo1(x-2)

def fibo2(cnt):
    #x, y, z
    x=y=1
    print(x, ', ', y, end=', ')
    for i in range(3, cnt+1):
        z=x+y
        print(z, end=', ')
        if i % 10 == 0:
            print()
        x=y
        y=z
    print()

def fibo3(cnt):#생성할 수열의 개수.
    nums = [0]*cnt
    nums[0]=nums[1]=1

    for i in range(2, cnt):
        nums[i]=nums[i-1]+nums[i-2]

    print(nums)

def main():
    '''
    for i in range(1, 101):
        print(fibo1(i), end=',')
        if i%10==0:
            print()
    fibo2(100)
    '''
    fibo3(100)
main()

