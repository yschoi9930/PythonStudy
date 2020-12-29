# 랜덤숫자 생성(난수).py
# 파이썬에서 난수(random number) 사용하기 위해서는 모듈(random)을 사용해야 함
# random 모듈의 randint() 함수를 이용해서 난수를 발생시켜 봄
# randint(최소, 최대)
# 최소부터 최대 사이의 임의의 정수 반환해주는 함수
# 모듈을 프로그램 안으로 갖고 와야 함
# from random import randint
# n = randint(1,100) - 1부터 100 사이에서 임의 숫자 하나를 반환

from random import randint
n = randint(1,100)
print(n)
n1 = randint(1,5)
print(n1)