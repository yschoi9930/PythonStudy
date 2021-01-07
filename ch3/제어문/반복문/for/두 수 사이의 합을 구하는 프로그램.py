# 두 수 사이의 합을 구하는 프로그램

# 사용자로부터 정수 2개를 입력받아서 두 정수 사이의 합을 구하는 프로그램 작성
# 단, 사용자는 정수만 입력하고 첫번째 수가 두번째 수보다 작다 가정한다.

num1 = int(input('input number1 : '))
num2 = int(input('input number2 : '))

sumx = 0
for x in range(num1,num2+1) :
    sumx += x

print('%d부터 %d 까지의 합 : %d' % (num1, num2, sumx))