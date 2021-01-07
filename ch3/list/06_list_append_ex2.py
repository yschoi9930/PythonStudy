student = []
#
# for i in range(5) :
#     scores = int(input('학생' + str(i+1) + 'student score : ')
#     student.append(scores)
# print(sum/len(student))
#

b = input('학생 수 입력 : ')
scores=[]
sum_s = 0
for i in range(int(b)) :
    score = input('학생' + str(i+1) + ' 점수 입력 : ')
    scores.append(score)

for s in scores :
    sum_s += int(s)

avg = sum_s / len(scores)

print("총점 : %d" % sum_s)
print('평균 : %.2f' % avg)