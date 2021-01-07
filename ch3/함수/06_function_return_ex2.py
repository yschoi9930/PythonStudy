

def order() :
    n1 = int(input('상품 가격 입력 : '))
    n2 = int(input('주문 수량 입력 : '))
    print('--------------------------')
    print('상품 가격 : ', n1)
    print('주문 수량 : ', n2)
    print('주문액 : ', n1 * n2)

order()

# 정의
def order1() :
    n1 = int(input('상품 가격 입력 : '))
    n2 = int(input('주문 수량 입력 : '))
    return n1, n2

# 호출
price, volume = order1()

print('--------------------------')
print('상품 가격 : ', price)
print('주문 수량 : ', volume)
print('주문액 : ', price * volume)

