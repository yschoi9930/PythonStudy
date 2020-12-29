# 연습문제 6

hong = str(input('gildong : '))
lee = str(input('monglyong : '))

if hong == 'scissors' and lee == 'rock' or \
    hong == 'rock' and lee == 'scissors' or \
    hong == 'paper' and lee == 'rock':
    print('gildong wins')

elif hong == lee :
    print('draw')

else :
    print('monglyong wins')