bank_name=input("은행명을 입력하시오: ")
way=input("입금 수단을 선택하시오(카드 or 통장): ")
check_money=input("입금하시려는 화폐의 종류를 입력하시오(현금 or 수표: ")

if((bank_name=="파이")and((way=="카드")or(way=="통장"))and(check_money=="현금")):
    print("입금 가능합니다.\n")
else:
    print("입금 불가합니다.\n")

