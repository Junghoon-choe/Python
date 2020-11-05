members = []

def make_mem():
    global  members
    n = input('name : ')
    t = input('tel : ')
    a = input('address : ')
    members.append([n, t, a])

'''
# 추가
for i in range(3):
    n = input('name : ')
    t = input('tel : ')
    a = input('address : ')
    members.append([n, t, a])
'''

for i in range(3):
    make_mem()
    print(members)