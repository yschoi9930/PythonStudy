# 날짜시간출력포맷팅

# 날짜와 시간을 사용하기 위해서는
# datetime 모듈 import

from datetime import date, datetime, timedelta
# 모듈(Module)
# 함수나 변수들을 모아 놓은 파일
# 모듈 안에 있는 함수들을 import 문으로 포함하여 사용 가능

# 오늘 날짜를 반환하는 함수 date.today()

today = date.today()
print(today)

year = today.year # today라는 개체가 갖고 있는 변수 자체를 뜻함
month = today.month
day = today.day

print('오늘 날짜 : {0}' .format(today))
print('오늘 날짜 : %s' % today)

# 현재 시간

c_date = datetime.now()
print(c_date)
c_time = datetime.now().time() # 현재 날짜와 시간에서 시간만 다시 추출
print(c_time)
hour = c_time.hour

# 프로그래밍 언어에서 날짜와 시간의 data는 숫자로 처리
print('현재시간')

# 날짜는 계산이 가능
# 날짜 계산 사용하는 함수 : timedelta() 함수 사용


today = date.today()
print('오늘 : {0}'.format(today))
print('어제 : {0}'.format(today + timedelta(days=-1)))
print('내일 : {0}'.format(today + timedelta(days=1)))
print('일주일 전 : {0}'.format(today + timedelta(days=-7)))
print('일주일 전 : {0}'.format(today + timedelta(days=7)))

print('-------------------시간계산--------------------')

c_time = datetime.now()
print('현재 시간 : {0}'.format(c_time))

# 1시간 전
print('1시간 전 : {0}'.format(c_time + timedelta(hours=-1)))
# 1시간 후
print('1시간 전 : {0}'.format(c_time + timedelta(hours=1)))
# 1일 2시간 후
print('1일 2시간 후 : {0}'.format(c_time + timedelta(hours=2) + timedelta(days=1)))

print('----------------날짜 출력 형식------------------')

