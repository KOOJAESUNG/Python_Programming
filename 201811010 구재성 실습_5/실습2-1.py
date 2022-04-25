origin_money=int(input("저축금액 입력: "))
plus_money = origin_money*0.0375
tax=plus_money * 0.15
result = origin_money + plus_money - tax
print("원금:%10d원"%origin_money)
print("이자:%10d원"%plus_money)
print("세금:%10d원"%tax)
print("최종:%10d원"%result)


