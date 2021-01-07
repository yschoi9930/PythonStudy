# 구구단의 단수를 입력 받아서 해당 구구단을 출력하는 프로그램 작성

num1 = int(input('input number : '))


for x in range(1,10) :
    print('%d * %d = %d' % (num1, x, num1*x))



for x in range(9,0,-1) :
    print('%d * %d = %d' % (num1, x, num1*x))

# 작아지는 range는 -step을 추가해야함