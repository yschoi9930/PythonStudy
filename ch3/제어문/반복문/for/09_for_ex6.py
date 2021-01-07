# 숫자 10개를 입력받아서 양, 음, 0의 개수 출력

pos=neg=zero=0

for i in range(1,11) :
    n = int(input('number ' + str(i) + ' input : '))

    if n > 0 :
        pos += 1
    elif n < 0 :
        neg += 1
    else :
        zero += 1

print('-----------------------')
print('positive : ', pos)
print('nagative : ', neg)
print('zero : ', zero)