# split함수_숫자추출.py

# 숫자만 추출해서 총 합계 구하기
str_data = '{a1:20}, {a2:30}, {a3:15}, \
            {a4:50}, {a5:-15}, {a6:80}, \
            {a7:0}, {a8:-110}'
total = 0 # 총 합에 사용

# 쉼표로 구분하여 전체 문자열을 분리
split_str_data = str_data.split(',')
print(split_str_data)
print(len(split_str_data))

print(split_str_data[0].split(':')) # ['{a1', '20}']
print(split_str_data[0].split(':')[1].split('}')[0]) # 20

# 숫자만 추출해서 총 합계 구하기

for i in range(0,len(split_str_data)) :
    str_temp = split_str_data[i].split(':')[1].split('}')[0]
    # : 을 기준으로 분리해서 [1]번째 추출 (오른쪽 데이터 추출 : 숫자_
    # } 을 기준으로 분리해서 [0]번째 추출(왼쪽 데이터 추출 : 숫자만 추출)
    total += int(str_temp) # 추출된 숫자 총합

print(total)
