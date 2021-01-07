# 1부터 100까지의 모든 3의 배수의 합을 계산하여 출력

num = 1
sum = 0

while num <= 100 :
    if num % 3 == 0 :
        sum += num
    num += 1
print('1부터 100까지 모든 3의 배수의 합은 %d입니다' % sum)