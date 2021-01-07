# 무한반복 예제1

# 노래방 기계는 1곡에 2000원이고 현재 잔액은 10000원
# whle문을 이용해서 노래를 몇 곡째 부르고 있는지 출력하고
# 잔액이 얼마인지 출력하는 프로그램을 작성하시오
# 단, 잔액이 없으면 종료한다

song = 2000
money = 10000
count = 0

# while True
# while 1 - 파이썬은 0이 아닌 값을 모두 True로 간주
# while money - 변수 money 저장되어 있는 값이 0이면 false로 결정됨
while True :
    count += 1
    money -= song
    print('노래를 ' + str(count) + '곡 불렀습니다')
    if money == 0 : # 잔액이 없는 경우
        print('잔액이 없습니다. 종료합니다')
        break
    else :
        print('현재 ' + str(money) + '원 남았습니다')
