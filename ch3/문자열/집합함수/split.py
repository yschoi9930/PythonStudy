# split.py

# split
# 구분자를 기준으로 문자열을 나눔
# 리스트로 반환
# 구분자 : 기본은 공백
# split('구분자') : '-', ':', '.'

s = 'Python programming'
s_split=s.split()
print(s_split) # 리스트 형태로 변환

names = '홍길동, 이몽룡, 성춘향, 변학도'
names_split=names.split(',')
print(names_split)

colors = 'red:blue:yellow:green'
colors_split=colors.split(':')
print(colors_split)

# 리스트의 각 요소 출력
for c in colors_split :
    print(c)

# 문자열을 반복의 요소로 사용
for c in colors : # 문자열별로 출력
    print(c)