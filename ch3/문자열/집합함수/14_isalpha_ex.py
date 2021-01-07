
alphas=digits=spaces=others=0

string =input('문장을 입력하세요 : ')

for c in string :
    if c.isalpha() :
        alphas += 1
    elif c.isdigit() :
        digits += 1
    elif c.isspace() :
        spaces += 1
    else :
        others += 1

print('문자 : %d개' % alphas)
print('숫자 : %d개' % digits)
print('스페이스 : %d개' % spaces)
print('기타 : %d개' % others)