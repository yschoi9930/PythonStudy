# 10_if_ex6.py

# 가위 바위보 게임을 컴퓨터와 you로 변경
# 컴퓨터는 랜덤하게 가위바위보를 생성(난수를 이용)
# 1. 가위, 2. 바위, 3. 보

from random import randint

n = randint(1,3)
if n == 1 :
    com = 'scissors'
elif n == 2 :
    com = 'rock'
else :
    com = paper

you = input('input : ')

if  you == 'scissors' and com =='paper' or \
    you == 'rock' and com == 'scissors' or \
    you == 'paper' and com == 'rock' :
    print('you win')

elif you == n :
    print('draw')


else:
    print('you lose')

print('computer was %s' % com)