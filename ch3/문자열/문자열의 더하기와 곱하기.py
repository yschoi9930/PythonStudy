# 문자열의 더하기와 곱하기

first = '홍'
second = '길동'

full = first + second
print(full)

# 문자열의 * 연산 : 곱해지는 숫자만큼 반복해서 표시

full2 = first * 3
print(full2)

# 문자열의 곱하기 연산은 곱해지는 값이 반드시 정수

for num in range(5,0,-1) :
    print('*'*num)