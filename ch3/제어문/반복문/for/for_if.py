# for_if

# 리스트 안에 저장된 점수가 합격인지 불합격인지 판단하는 프로그램
# 점수가 60점 이상이면 합격으로 출력한다. 그외는 불합격 출력
# 1번 90점 합격

scores = [90,57,88,45,78]
num = 0
for score in scores :
    num += 1
    if score >= 60 :
        result = 'pass'
    else :
        result = 'failed'
    print('%d) %d, %s' % (num, score, result) )