# for 1.py

# for 문은 반복의 횟수가 정해져 있을 때 주로 사용
# for 변수 in 리스트 또는 범위 :
#   반복해야할 문장

# 리스트를 사용한 반복 예제
# 리스트 안에 저장되어 있는 이름을 모두 출력하시오
# 리스트 : 여러개의 데이터가 하나의 공간에 저장되는 자료구조 [ 데이터1, 데이터2, ...  ] 기호를 사용해서 리스트 생성

for name in ['홍길동', '이몽룡', '이춘향', '변학도'] :
    print(name)

# 리스트에 0~9까지 저장을 하고 해당 리스트의 값을 모두 출력하시오.
for num in [0,1,2,3,4,5,6,7,8,9] :
    print(num)

# 위에서 작성한 프로그램을 한줄에 내용이 모두 출력되도록 변경하시오.
print('------------------------------------------------')

for num in [0,1,2,3,4,5,6,7,8,9] :
    print(num, end=' ')

# 반복(for) 범위 사용 : range() 함수
# range() 함수
# 특정 범위의 정수 생성
# range(10) : 0 ~ 9가지의 정수( 10개 / 시작은 0) # 초기값 설정을 안 할시 0부터 시작

# range(start, stop)
# start에서 stop-1까지의 정수를 생성
# range(0,10) : 0 ~ 9까지의 정수

# range(start, stop, step)
# start에서 stop-1까지 step 간격으로 정수 생성
# range(0,10,2) : 0에서부터 9까지 2씩 증가하면서 정수 생성 0,2,4,6,8

print('\n------------------------------------------------')

# range(10)을 사용해 범위 생성

for i in range(10) :
    print(i, end=' ')

print('\n------------------------------------------------')

# range(start, stop)을 사용해 범위 생성
for i in range(11, 21) :
    print(i, end=' ')

print('\n------------------------------------------------')

# range(start, stop, step)을 사용해 범위 생성
for i in range(11,21,2) :
    print(i, end=' ')

