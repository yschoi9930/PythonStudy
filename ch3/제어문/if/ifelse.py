# ifelse.py


# 예제 1
# 사용자로부터 비밀번호를 입력받아서 해당 비밀번호가 지정된 비밀번호와 같은지 확인 후 결과를
# 출력하는 프로그램

passinput = input('비밀번호를 입력하세요 : ')
passsave = '12345'

if passinput == passsave :
    print('right password')
else :
    print('wrong password')

print('end')

# 예제2
# 사용자가 입력한 비밀번호와 저장된 비밀번호가 일치하지 않으면 불일치라는 문구를
# 출력하고 일치하면 다음 문장을 수행하시오. if~else 구문을 사용할 것

if passinput != passsave:
    print('wrong password')
else:
    pass # 어떤 작업도 수행하지 않고 문장을 종료함 값이 일치해서 else 구문으로 왔을 경우 문장을 종료

print('end')