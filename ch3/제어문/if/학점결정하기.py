# 학점 결정하기.py
# 사용자로부터 점수를 입력받아 해당 점수의 학점을 결정해서 출력하시오

# 90 이상 A 80 이상 B 70 이상 C 60 이상 D 60 미만 F
# 입력 형식과 출력형식은 임의로 설정할 것

score = float(input('input your score : '))

if score >= 90 :
    grade = 'A'

elif score >= 80 :
    grade = 'B'

elif score >= 70 :
    grade = 'C'

elif score >= 60 :
    grade = 'D'

else :
   grade = 'F'

print('your grade is ' + grade )
