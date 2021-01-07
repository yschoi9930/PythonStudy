# 슬라이싱과 인덱싱

craw = 'Data crawling is fun'
pars = 'Data parsing is also fun'
print(craw)

# 문자열 인덱싱 (문자열은 위치값을 갖게 되고 위치값은 0부터 시작한다.)

print(craw[0]) # 첫번째 문자
print(craw[-1]) # 마지막 문지
n = 3
print(craw[n])

s = craw[n]
print(s)

# craw[n] = 'e' : 문자열의 부분 수정(assignment)는 불가능 하다
print('--------------------')

#문자열 슬라이싱

print(craw[0:4])
print(craw[5:16])
print(craw[17:])
print(craw[19])
print(craw[-1:]) # 마지막부터 끝까지 : 마지막 글자
print(craw[:-1]) # 처음부터 마지막-1(마지막 전글자) 까지
print(craw[16:16+4]) # 16에서부터 4글자 갖고와라

print('--------------------')
print(pars)
print(pars[5:])
print(pars[:15])
print(pars[:]) # 처음부터 끝까지