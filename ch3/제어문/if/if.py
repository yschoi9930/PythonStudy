# if 1.py

# if 문
# 조건식이 참이면 주어진 문장 수행
# 조건식이 거짓이면 아무것도 수행하지 않는다
#
# if(조건식) :
#     참일 경우 수행되는 문장
#     들여쓰기는 탭키를 이용
#     위 if문에 걸리는 문장은 8라인부터 10라인까지(들여쓰기 되어 있는)가 실행

# 기본예제
# password = 1235
# if password == 1234 :
#     print(' password is right')

# 기본예제 2
# password = 1234
# if password == 1234 :
#     print(' password is right')
# print('password checking ends') # 조건식이 참이거나 거짓일 때 모두 수행하는 문장

# 예제 1
# 사용자로부터 비밀번호를 입력받아서 해당 비밀번호가 지정된 비밀번호와 같은지 확인 후 결과를
# 출력하는 프로그램

passinput = input('비밀번호를 입력하세요 : ')
passsave = '12345'

if passinput == passsave :
    print('right password')

print('end')