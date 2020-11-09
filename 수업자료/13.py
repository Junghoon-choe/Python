def func(x):
   s=1
   for i in range(1, x+1):
      s*=i
   return s

def f2(x):#끝나는 기준을 정확히 기술. 5!=5*4*3*2*1
    if x==1:
        return 1
    else:
        return x*f2(x-1)

def main():
    print('5!:', f2(5))

main()
