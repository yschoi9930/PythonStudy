# find_index.py

# find()
# 문자열 내에서 특정 문자열이 존재하는지 여부와 문자열의 시작위치를 반환
# 존재하지 않으면 -1을 반환
# 필요한 문자열만 추출할 수 있도록 필터링 하거나 검사할 때 주로 사용

crawling = 'Data crawling is fun'
print(crawling.find('fun'))
print(crawling.find('f')) # 문자가 문자열에 여러번 나타나면 첫번째 만나는 문자의 위치를 반환 후 바로 종료
print(crawling.find('parsing'))

# index()
# 문자열 내에서 특정 문자열의 시작 위치를 반환
# find() 는 존재하지 않으면 -1을 반환, index()는 존재하지 않으면 에러 발생

print(crawling.index('fun'))
print(crawling.index('f'))


print('-------------------------------')


cities = '인천 대전 광주 울산 대구 부산'

city = input('우리나라 광역시 중 하나를 입력 : ')
if cities.find(city) != -1 : # 존재한다면
    print('정답입니다.')
else :
    print('틀렸습니다.')

# 동일 표현
city = input('우리나라 광역시 중 하나를 입력 : ')
if city in cities :   # 존재한다면
    print('정답입니다.')
else:
    print('틀렸습니다.')