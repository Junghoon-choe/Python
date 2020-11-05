list1 = list(range(1, 11))
print(list1)

print(list1[3:8])
print(list1[3:8:2])

list1.append(11)
print(list[10])

list1.insert(5, 100)
print(list1)

list1[5] = 200
print(list1)

a = 10
print(a)
a = 0
print(a)
del a
# print(a) : NameError : 'a' is not defined

del list1[3]       # 인덱스 제거
print(list1)

list1.remove(3)     # 값 제거
print(list1)

list1.clear()
print(list1)

# 요소 검색
list1 = [1, 2, 3, 4, 5]
if 3 in list1:
    idx = list1.index(3)
    print('[{0}] = {1}'.format(idx, list1[idx]))
else:
    print('X')

# 요소 정렬
list1 = [7, 3, 5, 9, 2, 4, 1]
list1.sort(reverse=True)
print(list1)

# 얕은 복사
a = [1, 2, 3, 4]
b = a # 메모리 공유
print(a, b)
print(id(a), id(b))

# 얕은 복사2 (이중 리스트 메모리 공유)
import copy
b = copy.copy(a)
print(a, b)
print(id(a), id(b))

c = [1, 2, [3, 4, 5]]
d = copy.copy(c)
print(c, d)
print(id(c), id(d))
print(id(c[2]), id(d[2]))

# 깊은 복사
e = [1, 2, [3, 4, 5]]
f = copy.deepcopy(e)
print(id(e), id(f))
print(id(e[2]), id(f[2]))

# 리스트 확장
# 01.
a = [1, 2, 3]
b = [6, 7]
c = a + b
print(c)
# 02.
a.extend(b)
print(a)