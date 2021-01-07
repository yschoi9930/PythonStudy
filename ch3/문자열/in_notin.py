# in_notin

# 문자열 안에 특정 문자열의 포함여부를 확인해서 T/F 로 결과값을 돌려주는 연산자

string = 'Python programming'

print('Python' in string)
print('Programming' in string)

if 'Python' in string :
    print('there is')
else :
    print('there is no')

# 리스트에서 in 연산자 사용하기

ids = ['sum', 'flower', 'moon', 'sky']

ID = input('id 입력 : ')
if ID in ids :
    print('login success')
else :
    print('login failed')

