# 명단확인
# 사용자로부터 이름을 입력받아서 해당 이름이 명단에 있는지 확인하는 프로그램
# 명단은 리스트로 임의로 구성

names=['홍길동', '이몽룡', '성춘향', '변학도']

search_name = input('input your name : ')

for name in names :
    if search_name == name :
        find = True # 명단에서 이름을 발견했다는 표시
        break # 명단에 이름이 있으므로 더 이상 반복을 진행하지 않는다
    else :
        find = False
if find == True :
    print('in line')
else :
    print('sorry')