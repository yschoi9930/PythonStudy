# is_alpha 관련 함수.py
#
# isalpha()
# 문자 여부 결과 반환
# isdigit()
# 숫자 여부 결과 반환
# isspace()
# 하나의 문자에 대해 공백 여부 결과 반환
# isalum()
# 문자 또는 숫자 여부 결과 반환
#

phone = input('input yout number : ')

if phone.isdigit() :
    pass # 어떤 작업 없이 다음 블럭으로 진행
else :
    print('only digit plz')


print('------------------------------------------')

name = input('input your name : ')
if name.isalpha() :
    pass
else :
    print('only alphabet plz')

print('------------------------------------------')

id = input('id 입력 : ')

if not(id.isalnum()) :
    print('id plz')

print('------------------------------------------')
# 스페이스 여부 확인

print(' '.isspace())
print(' c'.isspace())
print('   '.isspace())