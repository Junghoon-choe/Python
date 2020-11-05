list1 = list(range(1,11))
print(list1)

print(list1[3:8])
print(list1[3:8:2])
#print(list1[10])  =>에러발생.
list1.append(11)#끝에 방을 추가하고 그 방에 값 저장
print(list1[10])
list1.insert(5, 100)#param1:끼어넣을 위치, param2:값
print(list1)
list1[5]=200    #수정
print(list1)
a=10
print(a)
a=0
print(a)
del a#변수 삭제
#print(a)#에러

del list1[5]    #인덱스가 5인 방의 값을 제거
print(list1)

del list1[5]    #인덱스가 5인 방의 값을 제거
print(list1)

list1.remove(3) #값 3을 찾아서 삭제
print(list1)

#list1.remove(3) #값 3을 찾아서 삭제.없는 값 삭제시 에러
#print(list1)
print(list1.index(7))
print(list1.index(3))#없는 값 찾으면 에러

list1.clear()#모든 항목 삭제
print(list1)