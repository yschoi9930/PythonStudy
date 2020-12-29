# 점수를 입력 받아서 총점과 평균 출력

a = int(input("국어 점수 입력 : "))
b = int(input("영어 점수 입력 : "))
c = int(input("수학 점수 입력 : "))

sum = a + b + c
avg = (a+b+c)/3
print("총점 : ", sum)
print("평균 : %.2f" % avg)