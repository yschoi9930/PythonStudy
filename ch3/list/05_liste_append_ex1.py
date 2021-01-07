a = input('member name : ')
b = input('member name : ')
c = input('member name : ')

names = [a,b,c]

for i in names :
    print('회원명단 :' + i, end=' ')

print('\n-----------------------------------------')
members=[]
for i in range(3) :
    member = input('회원 입력 : ')
    members.append(member)


print ('회원명단 : ', end= ' ')
for member in members :
    print(member, end=' ')