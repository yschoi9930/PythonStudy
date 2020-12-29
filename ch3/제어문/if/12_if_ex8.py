
way = int(input('how to pay(1. 현금, 2. 카드) : '))
if way == 1 or way == 2 :
    payment = int(input('price : '))
    if way == 1 :
        print('sale_percetage : 10% ')
        print("sale_price : %d " % (int(payment*0.1)))
    else :
        print('sale_percetage : 5% ')
        print("sale_price : %d " % (int(payment*0.05)))
else :
    print('wrong input, end')