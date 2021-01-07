
# 이메일 주소를 입력받아서 이메일 형식이 아니면 아니라고 출력

email = input('input your email : ')
if (email.find("@") == -1 or email.find(".") == -1 or email.find('.') > email.find('@')
    or email.index('.') - email.index('@') < 2 or email[0] == '@' or email[-1] == '.'
    or email.count('@') >= 2 or email.count(".") > 2 ) :
    print('It is not email')
else :
    print('login success')

