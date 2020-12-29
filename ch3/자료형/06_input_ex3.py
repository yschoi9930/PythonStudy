# 그림과 같이 예금액과 이자율을 입력 받아서
# 예금액, 이자율, 예금이자, 잔액 출력

deposit = int(input("예금액 입력 : "))
int_rate = float(input("이자율 입력(%) : "))
interest = int(deposit * int_rate / 100)
balance = deposit + interest

print("________________")
print("예금액 : %d 원 " % deposit)
print("이자율 : %.2f%% " % int_rate)
print("예금이자 : %d 원 " % interest)
print("잔액 : %d 원 " % balance)