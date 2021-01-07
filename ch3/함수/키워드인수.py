# 키워드 인수.py

def student_info(name, age,gender) :
    student = {
        'name' : name,
        'age' : age,
        'gender' : gender
    }
    return student

print(student_info('kim','23','여'))
print(student_info(age=23,name='kim', gender ='여'))
print(student_info('lee', gender = '남', age =22))