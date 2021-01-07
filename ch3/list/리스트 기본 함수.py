# 리스트 기본 함수.py

a = [1,2,3,4,5]
# len() : 리스트 전체 데이터의 개수 반환
print(len(a))

# count() : 리스트 내에서 특정 요소(값)의 개수 세기
print(a.count(3))

# append() : 리스트의 끝에 새로운 요소 추가
a.append(5)
print(a)

a.append([6,7]) # 리스트 끝에 하위 리스트로 추가 [1, 2, 3, 4, 5, 5, [6, 7]]
print(a)

# append 함수는 추가는 1개씩(변수 or 리스트)만 가능

# insert(위치, 값) : 특정 위치에 요소 삽입
a.insert(2,300)
print(a)