# 공백함수.py

# 문자열의 공백 제거 해 주는 함수

# strip()
# 문자열 앞 뒤의 공백 제거
# lstrip()
# 문자열의 왼쪽 공백 제거
# rstrip()
# 문자열의 오른쪽 공백 제거
# 문자열 중간의 스페이스 코드는 상관 없는 함수


s1= '        hello          '

print(s1)
print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())

print('------------------------')

ID = 'sun'

input_id = input('input your id : ')

if input_id.strip() == ID :
    print('success')
else :
    print('failed')