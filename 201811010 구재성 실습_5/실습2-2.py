origin_money=int(input("저축금액 입력: "))
plus_money = origin_money*0.0375
tax=plus_money * 0.15
result = origin_money + plus_money - tax
print("원금:{:10d}원".format(origin_money))
print("이자:{:10.2f}원".format(plus_money))
print("세금:{:10.2f}원".format(tax))
print("최종:{:10.2f}원".format(result))


