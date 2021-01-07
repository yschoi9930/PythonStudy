def showinfo() :
    print('홍길동')
    print('20')
    print('010-1234-1234')

showinfo()

# 첫번째 방법
def sum(n1,n2) :
    print(input('숫자1 입력 : %d \n숫자2 입력 : %d \n합 : %d ' % (n1, n2, n1+n2) ))

# 두번째 방법
def sum1(n1,n2) :
    print('합 :', n1+n2)

n1 = int(input('숫자1 입력 : '))
n2 = int(input('숫자2 입력 : '))
sum1(n1,n2)

# 세번째 방법
def sum3() :
    n1 = int(input('숫자1 입력 : '))
    n2 = int(input('숫자2 입력 : '))
    return n1+n2

print('두 수의 합 : ', sum3())


def get_area() :
    n1 = int(input('가로길이 입력 : '))
    n2 = int(input('세로길이 입력 : '))
    return n1 * n2

print('사각형의 면적 : ', get_area())