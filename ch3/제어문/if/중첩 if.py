# 중첩 if.py

# if문 안에 다른 if문 포함 되어 있는 구조

# 사용자로부터 사과 상태를 입력받아서 상태가 '신선'이면 아래 조건에 따라 사과를 구매한다.
# 사과가격을 다시 입력받아서 사과 가격이 1000원 미만이면 10개를 산다 출력
# 그렇지 않으면 5개를 산다로 출력
# 사과 상태가 신선이 아니면 사과를 사지 않는다 를 출력

apple_quality = input('apple quality : ')

if apple_quality == 'fresh' :
    apple_price = int(input('input apple price : '))
    if apple_price < 1000 :
        print('buy 10 apples')
    else :
        print('buy 5 apples')
else :
    print("don't buy apple")