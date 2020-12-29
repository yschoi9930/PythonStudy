# 다음과 같이 무게와 키 값을 입력받아서 BMI 지수를 계산하는 프로그램 작성
# BMI = 몸무게/키의 제곱

a = float(input("몸무게(킬로그램) : "))
b = float(input("키(미터) : "))
BMI = a/(b**2)
print("당신의 BMI : %2f", % BMI)