# 가장 큰 수 출력

# 정수 3개를 입력 받아서 제일 큰 수를 출력하는 프로그램

num1 = int(input('input number1 '))
num2 = int(input('input number2 '))
num3 = int(input('input number3 '))

if num1 > num2 and num1 > num3 : # num1 가장 큰지 확인
    maxnum = num1

elif num2 > num3 : # num1이 가장 큰 수가 아니어서 num2가 가장 큰지 확인
    maxnum = num2

print('biggest num :', maxnum)