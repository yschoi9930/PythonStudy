# join.py
# join()
# 각 문자 사이에 특정 문자(열) 삽입
# a = "aa"
# a.joint("bbb")
# a를 b 사이에 삽입
# 결과 : baabaab

# 문자열 사이에 구분자 사이에 사용
# a = "-"
# print(a.join('abcd')
# 결과 : a-b-c-d

# 리스트에도 적용 가능

names = ['홍길동', '이몽룡', '성춘형']
print(type('-'.join(names)))

numbers =['10','20','30']
numbers2 = [10,20,30]
print(','.join(numbers))
print(','.join(numbers2)) # 숫자데이터에는 적용 불가