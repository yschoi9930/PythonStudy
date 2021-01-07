# 중첩

# for 문장안에 for 문이 포함되어 있는 구조

for y in range(3) : # 0-2 3번의 반복
    for x in range(5) : #0-4번의 반복
        print(x, end=' ') # x와 같이 동작되는 for 문 : 중첩되어 있으므로 15번 반복
    print() # 변수 y와 같이 동작되는 for 문 : 3번 반복 x와 관련된 for문이 종료 된 후에 실행
