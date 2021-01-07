# replace.py

# 전체 문자열에서 특정 문자열을 찾아 다른 문자열로 변경
# 전체문자열.replace(찾는 문자열, 변경할 문자열)
# 찾는 문자열이 존재하면 변경된 문자열 반환
# 찾는 문자열이 존재하지 않는 경우 변경된 내용이 없기 때문에 원래 문자열 반환

course = 'Java Programming'

# Jave -> Python으로 변경
c_replace = course.replace('Java', 'Python')
print(c_replace) # 문자열 찾음 : 변경해서 반환 없을 시 그대로 반환
print(course)
