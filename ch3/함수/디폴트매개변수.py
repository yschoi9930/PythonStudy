# 디폴트 매개변수

def clac(n1,n2) : # 2개의 파라미터를 요구하는 함수
    return n1 +n2
    # clac(1) 은 실행이 안됨

# 디폴트 매개변수를 사용할 수 있다.
# 디폴트를 지정해 놓을 시 사용자가 변수를 입력하지 않아도 기본 디폴트 값으로 출력 됨
def greet(name, msg='hello!') :
    print(name + ',' + msg)

greet('kim','hello')
greet('choi')
