# 연습문제 3
# 정수를 입력 받아서 홀수인지 짝수인지 판별하여 출력

a = float(input('정수 입력 : '))

if (a % 2) == 0 :
    print('짝수')
else :
    print('홀수')

if (a % 2) != 0 :
    print('홀수')
else :
    print('짝수')