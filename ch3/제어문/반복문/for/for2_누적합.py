# for1_누적합.py

# 1부터 10까지 출력하고 1부터 10까지 더한 결과를 마지막에 출력하시오

# 누적변수 생성
sumx = 0
for x in range(1,11) : # 1 ~ 10
    print(x)
    sumx = sumx +x
print('1부터 10까지의 합 : ', sumx)

# 1부터 100까지 홀수를 출력하고 홀수의 합을 구해서 마지막에 출력하시오.
for x in range(1,100,2) :
    print(x)
    sumx = sumx + x
print('1부터 100까지 홀수의 합 : ', sumx)

